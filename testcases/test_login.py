#! C:\Users\AdiminiChen\AppData\Local\Programs\Python\Python310
# coding=utf-8
# @Time: 2023/2/27 9:51
# @Author: jackchen
import time

import allure
import pytest

from page.LoginPage import LoginPage
from config.driver_config import DriverConfig
from common.report_add_img import add_img_2_report


class TestLogin:
    @pytest.mark.login
    @allure.feature("登录")
    @allure.description("d登录")
    def test_login(self, driver):
        """使用错误账号登录"""
        # driver = DriverConfig().driver_config()
        with allure.step("登录"):
            LoginPage().login(driver, 'll')
            time.sleep(3)
            add_img_2_report(driver, "登录")
        # driver.close()
