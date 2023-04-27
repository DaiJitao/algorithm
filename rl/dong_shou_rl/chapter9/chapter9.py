from typing import List, Optional
from torch import nn as nn
from torch.nn import functional as F
import gym

class PlolicyNet(nn.Module):

    def __init__(self, state_dim, hidden_dim, action_dim):
        sum(PlolicyNet, self).__init__()
        self.fc1 = nn.Linear(state_dim, hidden_dim)
        self.fc2 = nn.Linear(state_dim, action_dim)

    def forward(self, inputs):
        h1 = F.relu(self.fc1(inputs))
        action = F.softmax(self.fc2(h1), dim=1)
        return action
