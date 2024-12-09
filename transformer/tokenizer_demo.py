from typing import List, Optional

from transformers import BertTokenizer

tokenizer = BertTokenizer.from_pretrained("bert-base-cased")

"""
1 将给定的文本拆分为称为Token（词或标记）的单词（或部分单词、标点符号等）。
2 将这些Token转换为数字编码，以便构建张量并将其提供给模型。
3 添加模型正常工作所需的任何输入数据。例如特殊字符[CLS]，[SEP]等
"""

# Transformer's tokenizer - input_ids
sequence = "A Titan RTX has 24GB of VRAM"
print("Original sequence: ", sequence)
tokenized_sequence = tokenizer.tokenize(sequence)
print("Tokenized sequence: ", tokenized_sequence)
encodings = tokenizer(sequence)
encoded_sequence = encodings['input_ids']
print("Encoded sequence: ", encoded_sequence)
decoded_encodings = tokenizer.decode(encoded_sequence)
print("Decoded sequence: ", decoded_encodings)

tokenizer.encode()
tokenizer.batch_decode()
