from torch.utils.data import DataLoader
from datasets import BasicDataset

from datasets.utils import make_train_test
from transform.transform import _train_transforms, _test_transforms
from transform.augmentation import Augmentation

from hydra import compose, initialize
from omegaconf import OmegaConf

initialize(congig_path="conf", job_name="test_app")  # 이 부분 수정
cfg = compose(config_name="config", overrides=["data.image_dir", "data.label_dir", "data.train_ratio=0.6"])
print(OmegaConf.to_yaml(cfg))


def build_dataset(cfg):
    TRAIN_LIST, TEST_LIST = make_train_test(
        image_dir=cfg.data.root_dir,   # data에 대한 hydra yaml파일 만들어야함
        train_ratio=cfg.data.train_ratio,
        shuffle=cfg.data.shuffle
    )

    if cfg.data.augmentation:
        TRAIN_LIST, TEST_LIST = Augmentation(
            train_set=TRAIN_LIST, val_set=TEST_LIST, data_dir=cfg.data.image_dir
        )

    train_datasets = BasicDataset(TRAIN_LIST, transform=_train_transforms())
    test_datasets = BasicDataset(TEST_LIST, transform=_test_transforms())

    train_loader = DataLoader(train_datasets, batch_size=cfg.train.batch_size, drop_last=cfg.data.drop_last)
    test_loader = DataLoader(test_datasets, batch_size=1, drop_last=cfg.data.drop_last)

    return train_loader, test_loader
