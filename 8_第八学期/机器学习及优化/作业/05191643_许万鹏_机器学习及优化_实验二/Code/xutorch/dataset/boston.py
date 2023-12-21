import os
import torch
import pandas as pd
from torch.utils.data import Dataset


class BOSTON(Dataset):
    data_url = "http://lib.stat.cmu.edu/datasets/boston"
    current_dir = os.path.dirname(os.path.abspath(__file__))

    def __init__(self, download=True, path=os.path.join(current_dir, 'data', 'boston.txt'), train=True, transform=True, test_ratio=0.25):
        if download:
            path = self.data_url
        column_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
        raw_df = pd.read_csv(path, sep="\s+", skiprows=22, header=None)
        # 取出每一行的全部数据（11列特征）和其下一行的前3列数据（2列特征和1列目标）
        left = raw_df.iloc[::2, :].reset_index(drop=True)
        right = raw_df.iloc[1::2, :3].reset_index(drop=True)

        df = pd.concat([left, right], axis=1)
        df.columns = column_names

        data = df.drop('MEDV', axis=1)
        targets = df['MEDV']

        # 不建议对全集归一化
        # mean = np.mean(data, axis=0)
        # std = np.std(data, axis=0)

        pivot = int(100 * (1 - test_ratio))
        if train:
            indices = [i for i in range(len(data)) if i % 100 < pivot]
        else:
            indices = [i for i in range(len(data)) if i % 100 >= pivot]

        self.data = torch.FloatTensor(data.iloc[indices].values)
        self.targets = torch.FloatTensor(targets.iloc[indices].values)

        if transform:
            # 对train或dev集合分别进行归一化
            self.data = (self.data - self.data.mean(dim=0, keepdim=True)) / self.data.std(dim=0, keepdim=True)

        self.dim = self.data.shape[1]

        print('Finished reading the {} set of BOSTON Dataset ({} samples found, each dim = {})'.format(
            'train' if train else 'val', len(self.data), self.dim))

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.data[index], self.targets[index]
