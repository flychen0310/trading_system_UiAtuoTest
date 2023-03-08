#! C:\Users\AdiminiChen\AppData\Local\Programs\Python\Python310
# coding=utf-8
# @Time: 2023/3/5 15:12
# @Author: jackchen
import time

import pytest

from config.driver_config import DriverConfig
from page.LeftMenuPage import LeftMenuPage
from page.OrderPage import OrderPage
from page.LoginPage import LoginPage

tab_list = ['全部', '待付款', '待发货', '运输中', '待确认', '待评价']


class TestOrderTab:

    @pytest.mark.parametrize("tab", tab_list)
    def test_order_tab(self, driver, tab):
        # driver = DriverConfig().driver_config()
        LoginPage().login(driver, 'william')
        LeftMenuPage().click_level_one_menu(driver, '我的订单')
        time.sleep(2)
        LeftMenuPage().click_level_two_menu(driver, '已买到的宝贝')
        time.sleep(1)
        # tab_list = ['全部', '待付款', '待发货', '运输中', '待确认', '待评价']
        # for tab in tab_list:
        OrderPage().click_order_tab(driver, tab)
        time.sleep(1.5)
        # driver.close()
