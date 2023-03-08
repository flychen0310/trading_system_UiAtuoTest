#! C:\Users\AdiminiChen\AppData\Local\Programs\Python\Python310
# coding=utf-8
# @Time: 2023/3/5 15:08
# @Author: jackchen
from selenium.webdriver.common.by import By

from base.ObjectMap import ObjectMap
from base.OrderBase import OrderBase


class OrderPage(OrderBase, ObjectMap):

    def click_order_tab(self, driver, tab_name):
        """
        点击已买到的各个标签
        :param driver:
        :param tab_name:
        :return:
        """
        tab_xpath = self.my_order_by_goods(tab_name)
        return self.element_click(driver, By.XPATH, tab_xpath)
