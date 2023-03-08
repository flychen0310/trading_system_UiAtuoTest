#! C:\Users\AdiminiChen\AppData\Local\Programs\Python\Python310
# coding=utf-8
# @Time: 2023/3/4 16:36
# @Author: jackchen

import time

import pytest

from config.driver_config import DriverConfig
from page.LoginPage import LoginPage
from page.LeftMenuPage import LeftMenuPage
from page.GoodsPage import GoodsPage

"""
goods_title:商品标题
goods_details:商品描述
goods_num:商品数量
goods_pic_list:商品图片名字  --列表
goods_price:商品单价
goods_status:商品状态
button:提交
"""
goods_info_list = [
    {"goods_title": "商品1",
     "goods_details": "商品1的描述",
     "goods_num": 5,
     "goods_pic_list": ["pic1.img"],
     "goods_price": 233,
     "goods_status": "上架",
     "button": "提交"
     },
    {"goods_title": "商品2",
     "goods_details": "商品2的描述",
     "goods_num": 3,
     "goods_pic_list": ["pic2.img"],
     "goods_price": 2330,
     "goods_status": "上架",
     "button": "提交"
     }
]


class TestAddGoods:

    # @pytest.fixture()
    # def driver(self):
    #     get_driver = DriverConfig().driver_config()
    #     yield get_driver
    #     get_driver.quit()
    @pytest.mark.parametrize("goods_info", goods_info_list)  # 参数化
    def test_add_goods_01(self, driver, goods_info):
        # get_driver = DriverConfig().driver_config()
        LoginPage().login(driver, "jay")
        LeftMenuPage().click_level_one_menu(driver, '产品')
        time.sleep(1)
        LeftMenuPage().click_level_two_menu(driver, '新增二手商品')
        time.sleep(2)
        GoodsPage().add_goods_process(driver, goods_info["goods_title"], goods_info["goods_details"],
                                      goods_info["goods_num"],
                                      goods_info["goods_pic_list"], goods_info["goods_price"],
                                      goods_info["goods_status"], goods_info['button'])
        time.sleep(3)
