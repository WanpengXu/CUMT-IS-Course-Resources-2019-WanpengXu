import torch
import torch.nn as nn


class EmulatedSVM(nn.Module):
    def __init__(self, kernel_func, input_dim=30, output_dim=1):
        super(EmulatedSVM, self).__init__()
        self.kernel_func = None
        self.kernel_funcs = {
            'linear': self.linear_kernel,
            'poly': self.polynomial_kernel,
            'rbf': self.rbf_kernel,
            'sigmoid': self.sigmoid_kernel,
            'gaussian': self.gaussian_kernel
        }
        if isinstance(kernel_func, str):
            # 根据简称获取核函数
            if kernel_func in self.kernel_funcs:
                self.kernel_func = self.kernel_funcs[kernel_func]
            # 根据全称获取核函数
            elif hasattr(self, kernel_func):
                self.kernel_func = getattr(self, kernel_func)
            else:
                raise ValueError("Invalid kernel function: {}".format(kernel_func))
        elif callable(kernel_func):
            self.kernel_func = kernel_func

        self.fc = nn.Linear(input_dim, output_dim)

    def forward(self, x):
        x = self.kernel_func(x)
        x = self.fc(x)
        return x.squeeze(1)

    # 核函数方法
    def linear_kernel(self, x):
        return x

    def polynomial_kernel(self, x, degree=2):
        return torch.pow(x + 1, degree)

    def gaussian_kernel(self, x, sigma=1.0):
        return torch.exp(-torch.pow(x, 2) / (2 * sigma ** 2))

    def rbf_kernel(self, x, gamma=1.0):
        return torch.exp(-gamma * torch.pow(x, 2))

    def sigmoid_kernel(self, x):
        return torch.sigmoid(x)
