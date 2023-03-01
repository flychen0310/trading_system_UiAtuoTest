#! C:\Users\AdiminiChen\AppData\Local\Programs\Python\Python310
# coding=utf-8
# @Time: 2023/2/27 9:51
# @Author: jackchen
import time

from page.LoginPage import LoginPage
from config.driver_config import DriverConfig


class TestLogin:

    def test_login(self):
        driver = DriverConfig().driver_config()
        LoginPage().login(driver, 'william')
        time.sleep(3)
        driver.close()
