import torch


class MSE(torch.nn.Module):
    def __init__(self):
        super(MSE, self).__init__()

    def forward(self, inputs, targets):
        return torch.mean((inputs - targets) ** 2)
