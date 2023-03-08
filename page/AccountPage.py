#! C:\Users\AdiminiChen\AppData\Local\Programs\Python\Python310
# coding=utf-8
# @Time: 2023/3/5 15:29
# @Author: jackchen
from selenium.webdriver.common.by import By

from base.AccountBase import AccountBase
from base.ObjectMap import ObjectMap
from common.tools import get_img_path


class AccountPage(ObjectMap, AccountBase):

    def upload_avatar(self, driver, img_name):
        """
        上传个人头像
        :param driver:
        :param img_name:
        :return:
        """
        img_path = get_img_path(img_name)
        upload_xpath = self.basic_info_pic()
        return self.upload(driver, By.XPATH, upload_xpath, img_path)

    def click_basic_info_button(self, driver):
        """
        点击提交按钮
        :param driver:
        :return:
        """
        button_xpath = self.basic_info_button()
        return self.element_click(driver, By.XPATH, button_xpath)


