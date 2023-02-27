#! C:\Users\AdiminiChen\AppData\Local\Programs\Python\Python310
# coding=utf-8
# @Time: 2023/2/26 10:00
# @Author: jackchen
import os
from selenium import webdriver


def get_project_path():
    """获取绝对路径"""
    project_file_name = "trading_system_autotest"
    file_path = os.path.dirname(__file__)
    x = file_path.find(project_file_name)
    return file_path[:x + len(project_file_name)]


def sep(path, add_sep_before=False, add_sep_after=False):
    """
    :param path: 传入元组路径
    :param add_sep_before: 前面+分割符
    :param add_sep_after: 后面 + 分割符
    :return:
    """
    all_path = os.sep.join(path)
    if add_sep_before:
        all_path = os.sep + all_path
    if add_sep_after:
        all_path = all_path + os.sep
    return all_path


def get_driver(host):
    driver = webdriver.Chrome()
    driver.get(host)
    driver.maximize_window()
    return driver


if __name__ == '__main__':
    # print(get_project_path())
    print(sep(['test', 'config.py'], add_sep_after=True))