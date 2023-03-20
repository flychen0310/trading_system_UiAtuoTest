#! C:\Users\AdiminiChen\AppData\Local\Programs\Python\Python310
# coding=utf-8
# @Time: 2023/2/27 9:45
# @Author: jackchen
import time

from selenium.webdriver.common.by import By
from base.LoginBase import LoginBase
from base.ObjectMap import ObjectMap
from common.ocr_identify import OcrIdentify
from common.report_add_img import add_img_path_2_report
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

    def login(self, driver, user, need_captcha=False):
        """
        登录
        :param driver:
        :param user:
        """
        log.info("跳转登录页")
        self.element_to_url(driver, "/login")
        if need_captcha:
            time.sleep(3)
            log.info("需要验证码")
            # 点击勾选验证码
            self.select_need_captcha(driver)
            captcha_xpath = self.captcha()  # 获取图片验证码的元素
            ele_img_path = self.element_screenshot(driver, By.XPATH, captcha_xpath)  # 截取图片
            add_img_path_2_report(ele_img_path, "图像验证码")  # 将图片保存
            identify = OcrIdentify().identify(ele_img_path)  # 识别验证码并返回验证码数字
            log.info("验证码为" + str(identify))
            input_captcha_xpath = self.input_captcha()  # 填写验证码的元素
            log.info("填入验证码")
            self.element_fill_value(driver, By.XPATH, input_captcha_xpath, identify)
            time.sleep(3)
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

    def select_need_captcha(self, driver):
        """
        点击勾选是否需要验证码
        :param driver:
        :return:
        """
        log.info("点击勾选是否需要验证码")
        select_xpath = self.need_captcha()
        return self.element_click(driver, By.XPATH, select_xpath)
