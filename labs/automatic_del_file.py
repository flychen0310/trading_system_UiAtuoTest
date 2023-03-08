#! C:\Users\AdiminiChen\AppData\Local\Programs\Python\Python310
# coding=utf-8
# @Time: 2023/3/1 21:42
# @Author: jackchen
import os
import time


def clean_image_files(path, days, threshold):
    # 获取硬盘使用率
    statvfs = os.statvfs('/')
    disk_size = statvfs.f_frsize * statvfs.f_blocks
    disk_used = statvfs.f_frsize * (statvfs.f_blocks - statvfs.f_bfree)
    disk_percent = disk_used / disk_size

    # 如果使用率超过阈值，则开始清理文件
    if disk_percent > threshold:
        # 获取当前时间
        now = time.time()
        # 遍历目录下的所有文件
        for file in os.listdir(path):
            filepath = os.path.join(path, file)
            # 如果文件是图片文件，并且存储时间超过了指定天数
            if os.path.isfile(filepath) and file.endswith('.jpg') and (now - os.path.getmtime(filepath)) > days * 86400:
                os.remove(filepath)
                print('Removed file:', filepath)
