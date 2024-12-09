from typing import List, Optional
import torch
from torch import nn


class ManualLinearRegression(nn.Module):
    def __init__(self):
        super().__init__()
        # To make "b" and "w" real parameters of the model,
        # we need to wrap them with nn.Parameter
        self.b = nn.Parameter(torch.randn(1,
                                          requires_grad=True,
                                          dtype=torch.float))

        self.w = nn.Parameter(torch.randn(1,
                                          requires_grad=True,
                                          dtype=torch.float))

        self.dense = nn.Linear()

    def forward(self, x):
        # Computes the outputs / predictions
        return self.b + self.w * x

if __name__ == '__main__':
    from transformers import DistilBertForSequenceClassification, BertForSequenceClassification
    torch.manual_seed(42)
    # bert_cls = DistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased', num_labels=2)
    model = BertForSequenceClassification.from_pretrained("bert-base-cased", _fast_init=False)
    print(model)

if __name__ == '__main__1':
    model = ManualLinearRegression()
    i = 0
    print(model.state_dict())
    for layer in model.parameters():
        i += 1
        print(i, layer)


