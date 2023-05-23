import json
import tensorflow as tf
import numpy as np
from torch import nn


def save_to_excel(inf: str, data: dict):
    import pandas as pd
    dataFrame = pd.DataFrame(data)
    writer = pd.ExcelWriter(inf)
    dataFrame.to_excel(writer, index=False)
    writer.save()


# inf = r'C:\Users\daijitao\Desktop\base_result.txt'
# with open(inf, encoding='utf-8') as fp:
#     data = json.loads(fp.read())
#     titles = []
#     predict1 = []
#     predict2 = []
#     predict3 = []
#     contents = []
#     for obj in data:
#         titles.append(obj['title'])
#         contents.append(obj['content'])
#         predict1.append(obj['predict1'])
#         predict2.append(obj['predict2'])
#         predict3.append(obj['predict3'])
#
#     res = {'原文标题': titles, 'GPT生成的标题1': predict1, 'GPT生成的标题2': predict2, 'GPT生成的标题3': predict3, "政策原文": contents}
#     save_to_excel('GPT2文本写作效果.xls', res)
import torch
from torch.nn import Parameter
import torch.nn.functional as F
import math



class MyMultiheadAttention(nn.Module):

    def __init__(self, embed_dim, num_heads, dropout=0., bias=True):
        """

        :param embed_dim: 词嵌入的维度，比如512， 768
        :param num_heads: 头的个数
        :param dropout: 0.5
        :param bias:
        """
        self.embed_dim = embed_dim  # 前面的d_model参数
        self.head_dim = embed_dim // num_heads  # head_dim 指的就是d_k,d_v
        self.kdim = self.head_dim
        self.vdim = self.head_dim
        self.num_heads = num_heads  # 多头个数
        self.dropout = dropout

        assert self.num_heads * self.head_dim == self.embed_dim
        self.q_proj_weight = Parameter(torch.Tensor(embed_dim, embed_dim))  # embed_dim = kdim * num_heads
        # 这里第二个维度之所以是embed_dim，实际上这里是同时初始化了num_heads个W_q堆叠起来的, 也就是num_heads个头
        self.k_proj_weight = Parameter(torch.Tensor(embed_dim, embed_dim))  # W_k,  embed_dim = kdim * num_heads
        self.v_proj_weight = Parameter(torch.Tensor(embed_dim, embed_dim))  # W_v,  embed_dim = vdim * num_heads
        self.out_proj = nn.Linear(embed_dim, embed_dim, bias=bias)
        # 最后将所有的Z组合起来的时候，也是一次性完成， embed_dim = vdim * num_heads

    def multi_head_attention_forward(self):
        Q = F.linear()





if __name__ == '__main__':
    transformer_model = nn.Transformer(nhead=16, num_encoder_layers=12)
    src = torch.rand((10, 32, 512))
    tgt = torch.rand((20, 32, 512))
    out = transformer_model(src, tgt)
    print(out)


