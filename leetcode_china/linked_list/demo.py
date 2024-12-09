from typing import List, Optional

#
# from torch.optim import optimizer
# import torch
# from torch import nn
# class LinearNet(nn.Module):
#     def __init__(self, n_feature, in_feature, outch, kernel_size, padding):
#         super(LinearNet, self).__init__()
#         self.conv = nn.Conv2d(in_channels=in_feature, out_channels=outch, kernel_size=kernel_size, padding=padding)
#         self.conv = nn.Conv2d(in_channels=in_feature, out_channels=outch, kernel_size=kernel_size, padding=padding)
#         self.linear = nn.Linear(n_feature, 1)
#
#
#     def forward(self, x):
#         y = self.conv(x)
#         y = self.conv(y)
#         y = self.linear(y)
#         y = self.linear(y)
#         return y
#
# models = LinearNet(n_feature=3, outch=3, kernel_size=3, padding=0)
# # # 打印网络结构
# # print(net)
# optimizer = optimizer.Adam(models.parameters(), lr=0.0001)
#
# loss_f = nn.MSELoss()
# input = torch.randn([16, 3, 256, 256])
# label = torch.randn([16, 3])
# models.train()
# for epoch in range(10):
#     y_pred = models(input)
#     loss = loss_f(y_pred, label)
#     models.zero_grad()
#     loss.backward()
#     optimizer.step()
#     # for param in models.parameters():
#     #     param.data -= param.grad.data * learning_rate

import numpy as np
t = [np.exp(i) for i in [0.01, 1, 8, 10]]
_sum = sum(t)
for i in t:
    print(i/_sum)