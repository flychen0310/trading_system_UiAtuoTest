#! C:\Users\AdiminiChen\AppData\Local\Programs\Python\Python310
# coding=utf-8
# @Time: 2023/2/27 9:33
# @Author: jackchen
class LoginBase:
    """登录页定位方法"""

    def login_input(self, placeholder):
        """

        :param placeholder:
        :return:
        """
        return "//input[@placeholder='{}']".format(placeholder)

    def login_button(self, button_name):
        """

        :param button_name:
        """
        return "//span[text()='{}']/parent::button".format(button_name)

    def login_success(self):
        return "//p[text()='登录成功']"

    def need_captcha(self):
        """
        是否需要验证码的单选框
        :return:
        """
        return "//span[contains(text(),'是否需要验证码')]/preceding-sibling::span/span"

    def captcha(self):
        """
        验证码
        :return:
        """
        return "//div[@class='el-image']"

    def input_captcha(self):
        """
        输入验证码的输入框
        :return:
        """
        return "//input[@placeholder='请输入验证码']"


if __name__ == '__main__':
    print(LoginBase().login_button('test'))
