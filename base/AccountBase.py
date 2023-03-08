#! C:\Users\AdiminiChen\AppData\Local\Programs\Python\Python310
# coding=utf-8
# @Time: 2023/3/5 15:25
# @Author: jackchen
class AccountBase:

    def basic_info_pic(self):
        """
        基本资料-个人头像
        """
        return "//input[@type='file']"


    def basic_info_button(self):
        """
        基本资料-保存按钮
        :return:
        """
        return "//span[text()='保存']/parent::button"


