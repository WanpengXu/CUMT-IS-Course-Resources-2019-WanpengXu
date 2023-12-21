import torch.nn as nn


class EmbeddingMLP(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(EmbeddingMLP, self).__init__()
        self.fc1 = nn.Embedding(input_dim, hidden_dim)
        self.relu1 = nn.ReLU()
        self.fc2 = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu1(x)
        x = self.fc2(x)
        return x.squeeze(1)
