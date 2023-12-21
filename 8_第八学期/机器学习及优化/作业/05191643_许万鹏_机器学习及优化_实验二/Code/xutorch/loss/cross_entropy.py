import torch.nn as nn


class CrossEntropy(nn.Module):
    def __init__(self):
        super(CrossEntropy, self).__init__()

    def forward(self, outputs, targets):
        log_softmax = nn.LogSoftmax(dim=1)
        log_probs = log_softmax(outputs)
        loss = nn.NLLLoss()(log_probs, targets)
        return loss
