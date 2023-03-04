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


if __name__ == '__main__':
    print(LoginBase().login_button('test'))
