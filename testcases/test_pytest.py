#! C:\Users\AdiminiChen\AppData\Local\Programs\Python\Python310
# coding=utf-8
# @Time: 2023/3/6 20:44
# @Author: jackchen
import time

import pytest

from config.driver_config import DriverConfig


class TestPytestMclass:

    @pytest.fixture(scope="class")
    def scope_class(self):
        print("我是class级别，在所有用例之前只 执行一次")

    @pytest.fixture(scope="function")  # 测试套件 scope="function" 在每个测试用例之前都会执行
    def driver(self):
        get_driver = DriverConfig().driver_config()
        return get_driver

    @pytest.mark.baidu  # mark 起别名 --可以在终端来直接 pytest -m baidu来执行
    def test_open_baidu(self, driver, scope_class):
        driver.get("https://www.baidu.com")
        time.sleep(1)
        driver.close()

    @pytest.mark.bing
    def test_open_bing(self, driver, scope_class):
        driver.get("https://cn.bing.com")
        time.sleep(1)
        driver.close()
