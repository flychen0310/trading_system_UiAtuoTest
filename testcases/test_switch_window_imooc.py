#! C:\Users\AdiminiChen\AppData\Local\Programs\Python\Python310
# coding=utf-8
# @Time: 2023/3/5 14:37
# @Author: jackchen

import time
from config.driver_config import DriverConfig
from page.LeftMenuPage import LeftMenuPage
from page.ExternalLinkPage import ExternalLinkPage
from page.LoginPage import LoginPage


class TestSwitchWindowHandle:

    def test_switch_window_2_imooc(self, driver):
        # driver = DriverConfig().driver_config()
        LoginPage().login(driver, 'jay')
        time.sleep(2)
        LeftMenuPage().click_level_one_menu(driver, '外链')
        time.sleep(1)
        title = ExternalLinkPage().go_2_mooc(driver)
        print(title)
        time.sleep(2)
        # driver.close()
