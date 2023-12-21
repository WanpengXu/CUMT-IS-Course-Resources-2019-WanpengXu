import os
import torch
from torch.utils.data import Dataset
import pandas as pd


# 基于特征的文本处理方法
class Sentiment(Dataset):
    data_url = None
    current_dir = os.path.dirname(os.path.abspath(__file__))

    def __init__(self, download=False, path=os.path.join(current_dir, 'data', 'huangguo_mountain.csv'), train=True, test_ratio=0.25, min_df=5, num_sentence_word = 100, stopword_path=os.path.join(current_dir, 'data', 'stopwords.txt')):
        if download:
            path = self.data_url

        df = pd.read_csv(path, encoding='UTF-8')
        df = df.dropna()

        data = df['content']
        labels = df['label']

        with open(stopword_path, 'r', encoding='utf-8') as f:
            stop_words = [stop_word.strip() for stop_word in f.readlines()]

        self.word_counts = {}
        for sentence in data:
            words = sentence.split()
            for word in words:
                if word not in stop_words and len(word) > 1:
                    self.word_counts[word.lower()] = self.word_counts.get(word.lower(), 0) + 1

        self.num_sentence_word = num_sentence_word

        self.word_to_idx = {word: idx + 1 for idx, (word, count) in enumerate(self.word_counts.items()) if count >= min_df}
        self.word_to_idx['<PAD>'] = 0

        pivot = int(100 * (1 - test_ratio))
        if train:
            indices = [i for i in range(len(data)) if i % 100 < pivot]
        else:
            indices = [i for i in range(len(data)) if i % 100 >= pivot]

        self.data = data.iloc[indices].values
        self.labels= labels.iloc[indices].values

        self.dim = len(self.word_to_idx)

        print('Finished reading the {} set of Text Dataset ({} samples found), each dim = {}'.format(
            'train' if train else 'val', len(self.data), self.dim))

    def __len__(self):
        return len(self.data)

    # NLP任务数据量大，取出时再进行处理
    def __getitem__(self, index):
        content = self.data[index]
        label = int(self.labels[index])
        return self.convert_to_tensor(content), torch.tensor(label)

    def convert_to_tensor(self, sentence):
        content_idx = [self.word_to_idx[word.lower()] for word in sentence.split() if word.lower() in self.word_to_idx]
        if len(content_idx) >= self.num_sentence_word:
            content_idx = content_idx[:self.num_sentence_word]
        else:
            content_idx[len(content_idx):self.num_sentence_word] = [0] * (self.num_sentence_word - len(content_idx))
        return torch.FloatTensor(content_idx)
        # return torch.LongTensor(content_idx)      # EmbeddingMLP