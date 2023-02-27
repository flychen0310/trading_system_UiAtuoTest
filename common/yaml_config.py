#! C:\Users\AdiminiChen\AppData\Local\Programs\Python\Python310
# coding=utf-8
# @Time: 2023/2/25 20:22
# @Author: jackchen
import yaml
from common.tools import get_project_path, sep


def get_yam():
    """
    获取yaml文件内容
    :return:
    """
    with open(get_project_path() + sep(["config", "environment.yaml"], add_sep_before=True), 'r', encoding='utf-8') as f:
        yaml_file = yaml.load(f, Loader=yaml.FullLoader)
        return yaml_file['username'], yaml_file['password']


if __name__ == '__main__':
    print(get_yam())
