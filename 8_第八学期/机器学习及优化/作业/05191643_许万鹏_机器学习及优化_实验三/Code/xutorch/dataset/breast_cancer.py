import os
import torch
from torch.utils.data import Dataset
import pandas as pd


class BreastCancer(Dataset):
    data_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data"
    current_dir = os.path.dirname(os.path.abspath(__file__))

    def __init__(self, download=True, path=os.path.join(current_dir, 'data', 'wdbc.data'), train=True, transform=True, test_ratio=0.25):
        if download:
            path = self.data_url

        column_names = ["ID", "Diagnosis", "Mean_Radius", "Mean_Texture", "Mean_Perimeter", "Mean_Area",
                        "Mean_Smoothness", "Mean_Compactness", "Mean_Concavity", "Mean_Concave_Points", "Mean_Symmetry",
                        "Mean_Fractal_Dimension", "SE_Radius", "SE_Texture", "SE_Perimeter", "SE_Area", "SE_Smoothness",
                        "SE_Compactness", "SE_Concavity", "SE_Concave_Points", "SE_Symmetry", "SE_Fractal_Dimension",
                        "Worst_Radius", "Worst_Texture", "Worst_Perimeter", "Worst_Area", "Worst_Smoothness",
                        "Worst_Compactness", "Worst_Concavity", "Worst_Concave_Points", "Worst_Symmetry",
                        "Worst_Fractal_Dimension"]
        df = pd.read_csv(path, names=column_names)
        df = df.drop("ID", axis=1)

        data = df.drop("Diagnosis", axis=1)
        targets = df["Diagnosis"].replace({'M': 1, 'B': -1})    # -1和1符合SVM表述

        pivot = int(100 * (1 - test_ratio))
        if train:
            indices = [i for i in range(len(data)) if i % 100 < pivot]
        else:
            indices = [i for i in range(len(data)) if i % 100 >= pivot]

        self.data = torch.FloatTensor(data.iloc[indices].values)
        self.target = torch.FloatTensor(targets.iloc[indices].values)

        if transform:
            # 对train或dev集合分别进行归一化
            self.data = (self.data - self.data.mean(dim=0, keepdim=True)) / self.data.std(dim=0, keepdim=True)

        self.dim = self.data.shape[1]

        print('Finished reading the {} set of BreastCancer Dataset ({} samples found, each dim = {})'.format(
            'train' if train else 'val', len(self.data), self.dim))

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.data[index], self.target[index]
