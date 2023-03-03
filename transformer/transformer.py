import tensorflow as tf
import numpy as np
from tensorflow.keras.layers import Layer
import tensorflow.keras as keras
from tensorflow.keras.layers import Embedding, Dense, Dropout
'''参考地址：https://zhuanlan.zhihu.com/p/603243890
'''

np.set_printoptions(suppress=True)


def scaled_dot_product_attention(q, k: tf.Tensor, v, mask):
    '''
    实现self-attention
    :param q:
    :param k:
    :param v:
    :param mask:
    :return:
    '''
    matmul_qk = tf.matmul(q, k, transpose_b=True)

    dk = tf.cast(tf.shape(k)[-1], tf.float32)
    scaled_attention_logits = matmul_qk / tf.sqrt(dk)
    if mask is not None:
        scaled_attention_logits += (mask * -1e9)

    attention_weights = tf.nn.softmax(scaled_attention_logits, axis=-1)
    outputs = tf.matmul(attention_weights, v)
    return outputs, attention_weights


'''Multi-Head Attention是由多个Self-Attention组合形成的
'''


class MutilHeadAttention(Layer):
    def __init__(self, d_model, num_heads):
        super(MutilHeadAttention, self).__init__()
        self.num_heads = num_heads
        self.d_model = d_model

        # d_model 必须可以正确分为各个头
        assert d_model % num_heads == 0
        # 分头后的维度
        self.depth = d_model // num_heads
        self.wq = keras.layers.Dense(d_model)
        self.wk = keras.layers.Dense(d_model)
        self.wv = keras.layers.Dense(d_model)

        self.dense = keras.layers.Dense(d_model)

    def split_heads(self, x, batch_size):
        # 分头, 将头个数的维度 放到 seq_len 前面
        x = tf.reshape(x, (batch_size, -1, self.num_heads, self.depth))
        return tf.transpose(x, perm=[0, 2, 1, 3])

    def call(self, v, k, q, mask):
        batch_size = tf.shape(q)[0]

        # 分头前的前向网络，获取q、k、v语义
        q = self.wq(q)  # (batch_size, seq_len, d_model)
        k = self.wk(k)
        v = self.wv(v)

        # 分头
        q = self.split_heads(q, batch_size)  # (batch_size, num_heads, seq_len_q, depth)
        k = self.split_heads(k, batch_size)
        v = self.split_heads(v, batch_size)
        # scaled_attention.shape == (batch_size, num_heads, seq_len_v, depth)
        # attention_weights.shape == (batch_size, num_heads, seq_len_q, seq_len_k)

        # 通过缩放点积注意力层
        scaled_attention, attention_weights = scaled_dot_product_attention(q, k, v, mask)
        # 把多头维度后移
        scaled_attention = tf.transpose(scaled_attention, [0, 2, 1, 3])  # (batch_size, seq_len_v, num_heads, depth)

        # 合并多头
        concat_attention = tf.reshape(scaled_attention, (batch_size, -1, self.d_model))

        # 全连接重塑
        output = self.dense(concat_attention)
        return output, attention_weights


class LayerNormalization(Layer):
    def __init__(self, epsilon=1e-6, **kwargs):
        self.eps = epsilon
        super(LayerNormalization, self).__init__(**kwargs)

    def build(self, input_shape):
        self.gamma = self.add_weight(name='gamma', shape=input_shape[-1:],
                                     initializer=tf.ones_initializer(), trainable=True)
        self.beta = self.add_weight(name='beta', shape=input_shape[-1:],
                                    initializer=tf.zeros_initializer(), trainable=True)
        super(LayerNormalization, self).build(input_shape)

    def call(self, x, **kwargs):
        mean = keras.backend.mean(x, axis=-1, keepdims=True)
        std = tf.keras.backend.std(x, axis=-1, keepdims=True)
        return self.gamma * (x - mean) / (std + self.eps) + self.beta

    def compute_output_shape(self, input_shape):
        return input_shape


class EncoderLayer(Layer):
    def __init__(self, d_model, n_heads, ddf, dropout_rate=0.1):
        super(EncoderLayer, self).__init__()

        self.mha = MutilHeadAttention(d_model, n_heads)
        self.feed_forward = point_wise_feed_forward_network(d_model, ddf)

        self.layernorm1 = LayerNormalization(epsilon=1e-6)
        self.layernorm2 = LayerNormalization(epsilon=1e-6)

        self.dropout1 = tf.keras.layers.Dropout(dropout_rate)
        self.dropout2 = tf.keras.layers.Dropout(dropout_rate)

    def call(self, inputs, training, mask):
        # 多头注意力网络
        att_output, _ = self.mha(inputs, inputs, inputs, mask)
        att_output = self.dropout1(att_output, training=training)
        out1 = self.layernorm1(inputs + att_output)  # (batch_size, input_seq_len, d_model)
        # 前向网络
        ffn_output = self.feed_forward(out1)
        ffn_output = self.dropout2(ffn_output, training=training)
        out2 = self.layernorm2(out1 + ffn_output)  # (batch_size, input_seq_len, d_model)
        return out2


def point_wise_feed_forward_network(d_model, diff):
    '''
    feed forward层
    :param d_model:
    :param diff:
    :return:
    '''
    return tf.keras.Sequential([
        tf.keras.layers.Dense(diff, activation='relu'),
        tf.keras.layers.Dense(d_model)
    ])


def get_angles(pos, i, d_model):
    # 这里的i等价与上面公式中的2i和2i+1
    angle_rates = 1 / np.power(10000, (2 * (i // 2)) / np.float32(d_model))
    return pos * angle_rates


def positional_encoding(position, d_model):
    angle_rads = get_angles(np.arange(position)[:, np.newaxis],
                            np.arange(d_model)[np.newaxis, :],
                            d_model)
    # 第2i项使用sin
    sines = np.sin(angle_rads[:, 0::2])
    # 第2i+1项使用cos
    cones = np.cos(angle_rads[:, 1::2])
    pos_encoding = np.concatenate([sines, cones], axis=-1)
    pos_encoding = pos_encoding[np.newaxis, ...]

    return tf.cast(pos_encoding, dtype=tf.float32)


class Encoder(Layer):
    def __init__(self, n_layers, d_model, n_heads, ddf, input_vocab_size, max_seq_len, drop_rate=0.1):
        super(Encoder, self).__init__()
        self.n_layer = n_layers
        self.d_model = d_model
        self.ebedding = Embedding(input_vocab_size, d_model)
        self.pos_embedding = positional_encoding(max_seq_len, d_model)
        self.encode_layers = [EncoderLayer(d_model, n_heads, ddf, drop_rate) for _ in range(n_layers)]

        self.dropout = Dropout(drop_rate)

    def call(self, inputs, **kwargs):
        sequence_len = inputs.shape[-1] # 获取序列的长度
        word_emb = self.embedding(inputs)
        word_emb *= tf.sqrt(tf.cast(self.d_model, tf.float32)) # 开方


if __name__ == '__main__':
    # 测试多头注意力机制
    temp_mha = MutilHeadAttention(d_model=512, num_heads=8)
    y = tf.random.uniform((1, 60, 512))
    output, att = temp_mha(y, k=y, q=y, mask=None)
    print(output.shape, att.shape)
    # encoder层测试
    sample_encoder_layer = EncoderLayer(d_model=512, n_heads=8, ddf=2048)
    sample_encoder_layer_output = sample_encoder_layer(
        tf.random.uniform((64, 43, 512)), False, None)

    sample_encoder_layer_output.shape


def print_out(q, k, v):
    temp_out, temp_att = scaled_dot_product_attention(
        q, k, v, None)
    print('attention weight:')
    print(temp_att)
    print('output:')
    print(temp_out)


temp_k = tf.constant([[10, 0, 0],
                      [0, 10, 0],
                      [0, 0, 10],
                      [0, 0, 10]], dtype=tf.float32)  # (4, 3)

temp_v = tf.constant([[1, 0],
                      [10, 0],
                      [100, 5],
                      [1000, 6]], dtype=tf.float32)  # (4, 3)
temp_q = tf.constant([[0, 0, 10], [0, 10, 0], [10, 10, 0]], dtype=tf.float32)  # (3, 3)
print_out(temp_q, temp_k, temp_v)
