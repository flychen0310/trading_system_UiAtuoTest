#! C:\Users\AdiminiChen\AppData\Local\Programs\Python\Python310
# coding=utf-8
# @Time: 2023/2/27 9:45
# @Author: jackchen
from selenium.webdriver.common.by import By
from base.LoginBase import LoginBase
from base.ObjectMap import ObjectMap
from common.yaml_config import GetConfig


class LoginPage(LoginBase, ObjectMap):

    def login_input_value(self, driver, input_placeholder, input_val):
        """
        登录页输入值
        :param driver:
        :param input_placeholder:
        :param input_val:
        """
        input_xpath = self.login_input(input_placeholder)
        # return driver.find_element_by_xpath(input_xpath).send_keys(input_val)
        return self.element_fill_value(driver, By.XPATH, input_xpath, input_val)

    def login_click(self, driver, button_name):
        """
        点击登录
        :param driver:
        :param button_name:
        :return:
        """
        button_xpath = self.login_button(button_name)
        # return driver.find_element_by_xpath(button_xpath).click()
        return self.element_click(driver, By.XPATH, button_xpath)

    def login(self, driver, user):
        """
        登录
        :param driver:
        :param user:
        """
        self.element_to_url(driver, "/login")
        username, password = GetConfig().get_username_pwd(user)
        self.login_input_value(driver, '用户名', username)
        self.login_input_value(driver, '密码', password)
        self.login_click(driver, '登录')
