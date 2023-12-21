from xutorch.dataset.boston import BOSTON
from xutorch.dataset.breast_cancer import BreastCancer
from xutorch.dataset.sentiment import Sentiment
from torch.utils.data import DataLoader


def prep_dataloader(dataset_name, download, train, batch_size, num_workers=0, test_ratio=0.25, **kwargs):
    dataset = None
    if dataset_name == 'BOSTON':
        dataset = BOSTON(download=download, train=train, test_ratio=test_ratio, **kwargs)
    elif dataset_name == 'BreastCancer':
        dataset = BreastCancer(download=download, train=train, test_ratio=test_ratio, **kwargs)
    elif dataset_name == 'Sentiment':
        dataset = Sentiment(download=download, train=train, test_ratio=test_ratio, **kwargs)

    dataloader = DataLoader(dataset, batch_size, shuffle=train, drop_last=False, num_workers=num_workers, pin_memory=True)
    return dataloader, dataset
