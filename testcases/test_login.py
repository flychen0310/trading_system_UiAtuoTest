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
        driver.get('http://192.168.61.144')
        LoginPage().login_input_value(driver, '用户名', '周杰伦')
        time.sleep(1)
        LoginPage().login_input_value(driver, '密码', '123456')
        time.sleep(1)
        LoginPage().login_click(driver, '登录')
        time.sleep(1)
        driver.close()
