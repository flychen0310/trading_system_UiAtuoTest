#! C:\Users\AdiminiChen\AppData\Local\Programs\Python\Python310
# coding=utf-8
# @Time: 2023/3/4 16:36
# @Author: jackchen

import time
from config.driver_config import DriverConfig
from page.LoginPage import LoginPage
from page.LeftMenuPage import LeftMenuPage
from page.GoodsPage import GoodsPage


class TestAddGoods:
    def test_add_goods_01(self):
        driver = DriverConfig().driver_config()
        LoginPage().login(driver, "jay")
        LeftMenuPage().click_level_one_menu(driver, '产品')
        time.sleep(1)
        LeftMenuPage().click_level_two_menu(driver, '新增二手商品')
        time.sleep(2)
        GoodsPage().add_goods_process(driver, '洗衣液', 'None details', 10, ['goods_one.png'], 100, '上架', '提交')
        time.sleep(3)
        driver.close()
