from pathlib import Path
import os


def check_format(self, root):
    """data format check"""
    # json이면 COCO
    # xml이면 PASCAL VOC
    # 아니면 LABELME
    # 아니고.. yaml로 checking
    return format


def check_suffix(file='1st.yaml', suffix=('.yaml', '.py',), msg=''):
    # Check file for acceptable suffix
    if file and suffix:
        if isinstance(suffix, str):
            suffix = [suffix]
        for f in file if isinstance(file, (list, tuple)) else [file]:
            s = Path(f).suffix.lower()   # file suffix
            if len(s):
                assert s in suffix, f"{msg}{f} acceptable suffix is {suffix}"


def check_yaml(file, suffix=('.yaml', '.yml')):
    """ Search YAML file (if necessary) and return path, checking suffix """
    return check_file(file, suffix)

'''
# 다음과 같은 방법으로 사용
with open(check_yaml(yaml_path), errors='ignore') as f:
    data = yaml.safe_load(f)  # data dict
'''


def check_file(file, suffix=''):
    """ Search file (if necessary) and return path """
    check_suffix(file, suffix)   # optional
    file = str(file)   # convert to str()
    # if Path(file).is_file() or file == '':   # exist
    if Path(file).is_file():  # exist
        return file
    else:
        assert Path(file).exists(), f'File not exist: {file}'  # check
        # pass


def check_dataset(file_list):
    file_list = [Path(x).resolve() for x in (file_list if isinstance(file_list, list) else [file_list])]
    if not all(x.exists() for x in file_list):
        print('\nWarning:  Dataset not found, nonexistent paths: %s' % [str(x) for x in file_list if not x.exists()])


        

# def check_file(img_list, json_list):
#     if len(img_list) == len(json_list):
#         return img_list, json_list


# def check_dataset(self):
#     """data 존재여부 체크"""
#     print("Image Folder : {}".format(os.path.join(self.root, self.IMAGE_FOLDER)))
#     print("Label Folder : {}".format(os.path.join(self.root, self.LABEL_FOLDER)))
#
#     return os.path.exists(os.path.join(self.root, self.IMAGE_FOLDER)) and \
#             os.path.exists(os.path.join(self.root, self.LABEL_FOLDER))


# 데이터 비율 확인
# 데이터 polygon
# 동일한 자료형인지 체크 -> int, float
# label -> string


# Test 
# p1 = 'D:\\PycharmProjects\\research-pytorch-text-detection-baek-v2\\data\\datasets\\utils.py'
# p = 'D:\\PycharmProjects\\research-pytorch-text-detection-baek-v2\\data\\datasets\\config.yaml'
# file_list = [p, p1]
# print(check_file(p1))
# # print(check_yaml(p1))
# print(check_dataset(file_list))
# print(check_suffix(p, '.yaml'))


'''
def cvtData(self):

    result = []
    voc = cvtVOC()

    yolo = cvtYOLO(os.path.abspath(self.class_path))
    flag, self.dict_data =voc.parse(os.path.join(self.root, self.LABEL_FOLDER))

    try:

        if flag:
            flag, data =yolo.generate(self.dict_data)

            keys = list(data.keys())
            keys = sorted(keys, key=lambda key: int(key.split("_")[-1]))

            for key in keys:
                contents = list(filter(None, data[key].split("\n")))
                target = []
                for i in range(len(contents)):
                    tmp = contents[i]
                    tmp = tmp.split(" ")
                    for j in range(len(tmp)):
                        tmp[j] = float(tmp[j])
                    target.append(tmp)

                result.append({os.path.join(self.root, self.IMAGE_FOLDER, "".join([key, self.IMG_EXTENSIONS])) : target})

            return result

    except Exception as e:
        raise RuntimeError("Error : {}".format(e))
'''


