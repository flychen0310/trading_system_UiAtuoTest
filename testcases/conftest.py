#! C:\Users\AdiminiChen\AppData\Local\Programs\Python\Python310
# coding=utf-8
# @Time: 2023/3/7 20:43
# @Author: jackchen
import pytest

from config.driver_config import DriverConfig


@pytest.fixture()
def driver(self):
    get_driver = DriverConfig().driver_config()
    yield get_driver
    get_driver.quit()
