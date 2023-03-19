#! C:\Users\AdiminiChen\AppData\Local\Programs\Python\Python310
# coding=utf-8
# @Time: 2023/3/12 14:35
# @Author: jackchen
import pytest
from page.LoginPage import LoginPage
import time


class TestLoginImgAssert:
    @pytest.mark.login
    def test_login_assert(self, driver):
        """
        登录后断言图片
        :param driver:
        :return:
        """
        LoginPage().login(driver, "william")
        time.sleep(3)
        assert LoginPage().login_assert(driver, "head_img.png") > 0.9
