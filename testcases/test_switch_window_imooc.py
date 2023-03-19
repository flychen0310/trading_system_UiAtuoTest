#! C:\Users\AdiminiChen\AppData\Local\Programs\Python\Python310
# coding=utf-8
# @Time: 2023/3/5 14:37
# @Author: jackchen
import allure
import time
from config.driver_config import DriverConfig
from page.LeftMenuPage import LeftMenuPage
from page.ExternalLinkPage import ExternalLinkPage
from page.LoginPage import LoginPage
from common.report_add_img import add_img_2_report


class TestSwitchWindowHandle:

    @allure.description("窗口句柄")
    def test_switch_window_2_imooc(self, driver):
        # driver = DriverConfig().driver_config()
        with allure.step("login step"):
            LoginPage().login(driver, 'jay')
            time.sleep(2)
            add_img_2_report(driver, "login")

        with allure.step("click leftmenu step"):
            LeftMenuPage().click_level_one_menu(driver, '外链')
            time.sleep(1)

        with allure.step("assert title step"):
            title = ExternalLinkPage().go_2_mooc(driver)
            print(title)
            assert title == "慕课网-程序员的梦工厂"
        # driver.close()
