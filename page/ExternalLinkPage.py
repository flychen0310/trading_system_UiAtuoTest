#! C:\Users\AdiminiChen\AppData\Local\Programs\Python\Python310
# coding=utf-8
# @Time: 2023/3/5 14:35
# @Author: jackchen
from base.ObjectMap import ObjectMap


class ExternalLinkPage(ObjectMap):

    def go_2_mooc(self, driver):
        """
        切换至imooc网站
        :param driver:
        :return:
        """
        self.switch_window_to_handle(driver)
        return driver.title
