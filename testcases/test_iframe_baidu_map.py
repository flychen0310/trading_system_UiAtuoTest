#! C:\Users\AdiminiChen\AppData\Local\Programs\Python\Python310
# coding=utf-8
# @Time: 2023/3/5 16:20
# @Author: jackchen

import time

from config.driver_config import DriverConfig
from page.LoginPage import LoginPage
from page.LeftMenuPage import LeftMenuPage
from page.IframeBaiduMapPage import IframeBaiduMapPage


class TestBaiduMap:

    def test_baidu_map(self, driver):
        # driver = DriverConfig().driver_config()
        LoginPage().login(driver, 'jay')
        time.sleep(1)

        LeftMenuPage().click_level_one_menu(driver, 'iframe测试')
        time.sleep(1)
        IframeBaiduMapPage().switch_2_baidu_iframe(driver)
        IframeBaiduMapPage().get_baidu_map_baidu_button(driver)
        time.sleep(1)
        IframeBaiduMapPage().iframe_out(driver)
        LeftMenuPage().click_level_one_menu(driver,"首页")
        time.sleep(1)
        # driver.close()
