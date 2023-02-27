#! C:\Users\AdiminiChen\AppData\Local\Programs\Python\Python310
# coding=utf-8
# @Time: 2023/2/27 9:45
# @Author: jackchen
from base.LoginBase import LoginBase


class LoginPage(LoginBase):

    def login_input_value(self, driver, input_placeholder, input_val):
        """
        :param driver:
        :param input_placeholder:
        :param input_val:
        """
        input_xpath = self.login_input(input_placeholder)
        return driver.find_element_by_xpath(input_xpath).send_keys(input_val)

    def login_click(self,driver,button_name):
        """

        :param driver:
        :param button_name:
        :return:
        """
        button_xpath = self.login_button(button_name)
        return driver.find_element_by_xpath(button_xpath).click()



