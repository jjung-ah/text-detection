from torch.utils.data import DataLoader
from datasets import BasicDataset

from datasets.utils import make_train_test
from transform.transform import _train_transforms, _test_transforms
from transform.augmentation import Augmentation

from hydra import compose, initialize
from omegaconf import DictConfig
# from omegaconf import OmegaConf
# from .checker import check_file

initialize(congig_path="configs", config_name="config")  # 이 부분 수정
cfg = compose(config_name="config", overrides=["data.root_dir", "data.train_ratio=0.6"])   # 여기도 밑에 더 쓰이고 있는 drop_last 등 추가할 부분 확인
# print(OmegaConf.to_yaml(cfg))


def build_dataset(cfg: DictConfig):
    train_list, test_list = make_train_test(
        image_dir=cfg.data.root_dir,   # data에 대한 hydra yaml파일 만들어야함
        train_ratio=cfg.data.train_ratio,
        shuffle=cfg.data.shuffle
    )

    if cfg.data.augmentation:
        train_list, test_list = Augmentation(
            train_set=train_list, val_set=test_list, data_dir=cfg.data.image_dir   # image_dir 인지 root_dir 인지 다시 한번 확인 필요
        )

    # TRAIN_LIST, TEST_LIST = check_file(TRAIN_LIST, TEST_LIST)
    train_datasets = BasicDataset(train_list, transform=_train_transforms())
    test_datasets = BasicDataset(test_list, transform=_test_transforms())

    train_loader = DataLoader(train_datasets, batch_size=cfg.train.batch_size, drop_last=cfg.data.drop_last)
    test_loader = DataLoader(test_datasets, batch_size=1, drop_last=cfg.data.drop_last)

    return train_loader, test_loader
