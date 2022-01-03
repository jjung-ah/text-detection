import glob
from pathlib import Path
import cv2


def load_image(img_path: str, type='RGB'):   # type: str
    image = cv2.imread(img_path)
    if type == 'RGB':
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    elif type == 'L':
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    return image


def save_image(image, img_path: str):
    cv2.imwrite(img_path, image)


def make_file_list(root_path: str, ext_list: list) -> list:
    p = str(Path(root_path).resolve())
    file_list = []
    for ext in ext_list:
        file_list += glob.glob(f'{p}/{ext}', recursive=True)   # iterator 형식으로 받으려면 glob.iglob 사용

    return file_list


def get_file_list(root_path: str):
    img_ext = ['**/*.jpg', '**/*.jpeg', '**/*.png']
    json_ext = ['**/*.json']
    img_file_list = make_file_list(root_path, json_ext)  # iterator 형식으로 받으려면 glob.iglob 사용
    json_file_list = make_file_list(root_path, img_ext)

    return sorted(img_file_list), sorted(json_file_list)


def make_data_list(root_path: str) -> list:
    img_list, text_list = get_file_list(root_path)

    samples = []
    for img_dir, text_dir in zip(img_list, text_list):
        samples.append((img_dir, text_dir))

    return samples


def make_train_test(samples: list, train_ratio: float):
    split_index = int(len(samples) * train_ratio)

    train_list = samples[:split_index]
    test_list = samples[split_index:]

    return train_list, test_list



# def get_file_list(root_path: str):
#     p = str(Path(root_path).resolve())
#     img_ext = ['**/*.jpg', '**/*.jpeg', '**/*.png']
#     json_ext = '**/*.json'
#     json_file_list, img_file_list = [], []
#     json_file_list += glob.glob(f'{p}/{json_ext}', recursive=True)
#     for ext in img_ext:
#         img_file_list += glob.glob(f'{p}/{ext}', recursive=True)  # iterator 형식으로 받으려면 glob.iglob 사용
#
#     return sorted(img_file_list), sorted(json_file_list)


# def img2label_paths(img_paths):
#     # Define label paths as a function of image paths
#     sa, sb = os.sep + 'images' + os.sep, os.sep + 'labels' + os.sep  # /images/, /labels/ substrings
#     return [sb.join(x.rsplit(sa, 1)).rsplit('.', 1)[0] + '.txt' for x in img_paths]





'''

"""이 부분을 어디에 두어야 할지..."""

def load_yaml(path: str) -> yaml:
    """
    load yaml file
        : param path: config file path from argparse
    :return: yaml (dict)
    """
    with open(path, encoding="UTF8") as file:
        configs = yaml.load(file, Loader=yaml.FullLoader)
    return configs



def count_files(data: dict):
    """
        : param data:
    :return: counts #
    """
    counts = 0
    for name, paths in data.items():
        counts += len(paths)
    return counts


def is_dir(path: dict):
    """
        :param path: folder path
    :return:
    """
    PAth(path).mkdir(exist_ok=True, parents=True)


def convert_float_to_int(points: list):
    return [lost(map(int, point)) for point in points]
    

def crop_image(image, polygons: np.array):
    points = convert_polygons_to_xywh(polygons)
    crop_image - image[points.y:points.y+points.h, points.x:points.x+points.w]
    return crop_image

def load_json(path: str):
    with open(path) as file:
        data = json.load(file)
    return data


'''
