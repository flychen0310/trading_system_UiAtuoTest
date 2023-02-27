#! C:\Users\AdiminiChen\AppData\Local\Programs\Python\Python310
# coding=utf-8
# @Time: 2023/2/27 10:14
# @Author: jackchen
import time
from selenium import webdriver
from common.tools import get_project_path, sep

options = webdriver.ChromeOptions()
options.add_argument("window_size=1920,1080")
# 去除提示
options.add_experimental_option("excludeSwitches", ["enable-automation"])
# 解决无法访问https问题
options.add_argument("--ignore-certificate-errors")
options.add_argument("--allow-insecure-localhost")
# 设置无痕模式
options.add_argument("--incognito")
# 设置为无头模式
# options.add_argument("--headless")
# 解决卡顿
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(
    executable_path=get_project_path() + sep(['driver_files', 'chromedriver.exe'], add_sep_before=True),
    options=options)
driver.get('https://www.baidu.com')
time.sleep(3)
driver.close()
