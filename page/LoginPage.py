#! C:\Users\AdiminiChen\AppData\Local\Programs\Python\Python310
# coding=utf-8
# @Time: 2023/2/27 9:45
# @Author: jackchen
from selenium.webdriver.common.by import By
from base.LoginBase import LoginBase
from base.ObjectMap import ObjectMap
from common.yaml_config import GetConfig
from logs.log import log


class LoginPage(LoginBase, ObjectMap):

    def login_input_value(self, driver, input_placeholder, input_val):
        """
        登录页输入值
        :param driver:
        :param input_placeholder:
        :param input_val:
        """
        log.info("输入{}为{}".format(input_placeholder, input_val))
        input_xpath = self.login_input(input_placeholder)
        return self.element_fill_value(driver, By.XPATH, input_xpath, input_val)

    def login_click(self, driver, button_name):
        """
        点击登录
        :param driver:
        :param button_name:
        :return:
        """
        log.info("点击登录")
        button_xpath = self.login_button(button_name)
        # return driver.find_element_by_xpath(button_xpath).click()
        return self.element_click(driver, By.XPATH, button_xpath)

    def assert_login_success(self, driver):
        """
        断言登录成功
        :param driver:
        :return:
        """
        s_xpath = self.login_success()
        self.element_appear(driver, By.XPATH, s_xpath, timeout=2)

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
        self.assert_login_success(driver)

    def login_assert(self, driver, img_name):
        """
        登录后判断头像
        :param driver:
        :param img_name:
        :return:
        """
        return self.find_img_in_source(driver, img_name)
