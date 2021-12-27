from torchvision import transforms


def _train_transforms():
    return transforms.Compose([
        transforms.ToTensor(),
        transforms.Resize((,)),
        transforms.RandomVerticalFlip(p=0.5)
    ])


def _val_transforms():
    return transforms.Compose([
        transforms.ToTensor(),
        transforms.Resize((,))
    ])

