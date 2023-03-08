#! C:\Users\AdiminiChen\AppData\Local\Programs\Python\Python310
# coding=utf-8
# @Time: 2023/3/5 16:18
# @Author: jackchen
from selenium.webdriver.common.by import By
from base.IframeBaiduMapBase import IframeBaiduMapBase
from base.ObjectMap import ObjectMap


class IframeBaiduMapPage(ObjectMap, IframeBaiduMapBase):

    def switch_2_baidu_iframe(self, driver):
        """
        切换到百度iframe
        :param driver:
        :return:
        """
        iframe_xpath = self.baidu_iframe()
        return self.switch_into_iframe(driver, By.XPATH, iframe_xpath)

    def iframe_out(self, driver):
        """
        从百度切换到网页
        :param driver:
        :return:
        """
        return self.switch_from_iframe_to_content(driver)

    def get_baidu_map_baidu_button(self, driver):
        """
        获取百度搜索按钮
        :param driver:
        :return:
        """
        button_xpath = self.search_button()
        return self.element_click(driver, By.XPATH, button_xpath)
