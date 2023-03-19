#! C:\Users\AdiminiChen\AppData\Local\Programs\Python\Python310
# coding=utf-8
# @Time: 2023/3/19 19:36
# @Author: jackchen
import logging
import os
import time

from common.tools import get_project_path, sep


def get_log(log_name):
    logger = logging.getLogger(log_name)
    logger.setLevel(logging.INFO)
    # 获取当前时间
    rq = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
    # 获取日志路径
    all_log_path = get_project_path() + sep(['logs', 'all_logs'], add_sep_before=True, add_sep_after=True)
    if not os.path.exists(all_log_path):
        os.makedirs(all_log_path)
    all_log_name = all_log_path + rq + '.log'
    # 创建handler
    # 创建一个handler写入所有日志
    fh = logging.FileHandler(all_log_name)
    fh.setLevel(logging.INFO)

    # 定义日志输出格式
    all_log_formatter = logging.Formatter(
        "%(asctime)s - %(filename)s - %(module)s - %(funcName)s - %(lineno)d - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S")
    # 将定义好的输出形式添加到handler
    fh.setFormatter(all_log_formatter)

    # 给logger添加handler
    logger.addHandler(fh)
    return logger


log = get_log("自动化测试")

if __name__ == '__main__':
    log.info("i`m info")
