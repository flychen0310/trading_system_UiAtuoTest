#! C:\Users\AdiminiChen\AppData\Local\Programs\Python\Python310
# coding=utf-8
# @Time: 2023/3/5 15:38
# @Author: jackchen
import time

from config.driver_config import DriverConfig
from page.LoginPage import LoginPage
from page.LeftMenuPage import LeftMenuPage
from page.AccountPage import AccountPage


class TestBasicInfo:

    def test_basic_info(self, driver):
        # driver = DriverConfig().driver_config()
        LoginPage().login(driver, 'william')
        time.sleep(1)
        LeftMenuPage().click_level_one_menu(driver, '账户设置')
        time.sleep(1)
        LeftMenuPage().click_level_two_menu(driver, "个人资料")
        time.sleep(1)
        AccountPage().upload_avatar(driver, 'img1.jpg')
        time.sleep(1)
        AccountPage().click_basic_info_button(driver)
        time.sleep(2)
        # driver.close()
