import torch.nn as nn


class Linear(nn.Module):
    def __init__(self, input_dim):
        super(Linear, self).__init__()

        # 线性回归模型
        self.fc = nn.Linear(input_dim, 1)

    def forward(self, x):
        return self.fc(x).squeeze(1)