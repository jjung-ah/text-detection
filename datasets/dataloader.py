from torch.utils.data import DataLoader
from torchvision import transforms
from jjung.datasets import BasicDataset

from jjung.datasets.utils import make_train_val
from jjung.transform.augmentation import Augmentation

from hydra import compose, initialize
from omegaconf import OmegaConf

initialize(config_path="conf", job_name="test_app")
cfg = compose(config_name="config", overrides=["db=mysql", "db.user=me"])
print(OmegaConf.to_yaml(cfg))


def build_train_dataset(cfg):
    TRAIN_LIST, VAL_LIST = make_train_val(
        image_dir = cfg.data.image_dir,  # data에 대한 hydra yaml파일 만들어야함
        label_dir = cfg.data.label_dir,
        train_ratio = cfg.data.train_ratio,
        shuffle = cfg.data.shuffle
    )

    if cfg.data.augmentation:
        TRAIN_LSIT, VAL_LIST = augmentation(
            train_set = TRAIN_LIST, val_set = VAL_LIST, data_dir = cfg.data.image_dir
        )
      
    train_datasets = BasicDataset(TRAIN_LIST, transform=_train_trainsforms())
    val_datasets = BasicDataset(VAL_LIST, transform=_val_transforms())

    train_loader = DataLoader(train_datasets, batch_size=cfg.train.batch_size, drop_last = cfg.data.drop_last)
    val_loader = DataLoader(val_datasets, batch_size=1, drop_last = cfg.data.drop_last)

    return train_loader, val_loader