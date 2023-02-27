#! C:\Users\AdiminiChen\AppData\Local\Programs\Python\Python310
# coding=utf-8
# @Time: 2023/2/27 10:36
# @Author: jackchen


import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from common.tools import get_project_path, sep


class DriverConfig:

    def driver_config(self):
        """
        driver
        """
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

        url = "https://registry.npmmirror.com/-/binary/chromedriver"
        latest_release_url = "https://registry.npmmirror.com/-/binary/chromedriver/LATEST_RELEASE"
        # 自动管理最新的驱动
        driver = webdriver.Chrome(
            ChromeDriverManager(url=url, latest_release_url=latest_release_url, cache_valid_range=365).install(),
            options=options)
        driver.delete_all_cookies()

        return driver
