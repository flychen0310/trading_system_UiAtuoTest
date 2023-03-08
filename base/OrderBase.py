#! C:\Users\AdiminiChen\AppData\Local\Programs\Python\Python310
# coding=utf-8
# @Time: 2023/3/5 15:06
# @Author: jackchen

class OrderBase:

    def my_order_by_goods(self, tab_name):
        """
        我的订单下的已买到的宝贝
        :param tab_name:
        :return:
        """
        return "//div[@role='tab' and text()='{}']".format(tab_name)
