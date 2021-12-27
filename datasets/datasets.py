import torch
from torch.utils.data import Dataset
from torch.utils.data import DataLoader


def get_label(img_path_list):
    label_list = []
    for p in img_path_list:
        label_list.append()
    return label_list


class BasicDataset(Dataset):
    def __init__(self, img_path_list, transform=None):
        self.img_path_list = img_path_list
        self.transform = transform
        self.label = get_label(img_path_list)
    

    def __len__(self):
        return len(self.img_path_list)

    
    def __getitem__(self, idx):
        data = {}  # 이거 어떻게 만들지 함수 만드는게 가장 큰 일!!
        key = list(self.data[idx].keys())[0]
        img = Image.open(key).convert('RGB')   # imread 해야하나.. ㅜㅜ & 'RGB' 이거나 'L'이거나 선택하는 함수만들어 넣기
        current_shape = img.size
        img = img.resize(self.resize_factor, self.resize_factor)
        label = self.data[idx][key]

        if self.transform is not None:
            img = self.transform(img)

        return data


    # @staticmethod
    # def collate_fn(batch):
    #     img, label, path, shapes = zip(*batch)  # transposed
    #     for i, l in enumerate(label):
    #         l[:, 0] = i  # add target image index for build_targets()
    #     return torch.stack(img, 0), torch.cat(label, 0), path, shapes