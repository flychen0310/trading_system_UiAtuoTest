#! C:\Users\AdiminiChen\AppData\Local\Programs\Python\Python310
# coding=utf-8
# @Time: 2023/2/27 13:27
# @Author: jackchen
class HomeBase:

    def wallet_switch(self):
        """
        首页钱包的开关
        :return:
        """
        return "//span[contains(@class,'switch')]"

    def logo(self):
        """
        左上角的logo
        """
        return "//div[contains(text(),'二手')]"

    def welcome_index(self):
        """
        首页欢迎回来
        :return:
        """
        return "//span[starts-with(text(),'欢迎您回来')]"

    def show_data(self):
        """
        首页日历
        :return:
        """
        # following-sibling:: +某个标签，代表定位同级元素的下一个元素
        return "//div[text()='我的日历']/following-sibling::div"

    def my_head_pic(self):
        """
        首页大头图像
        :return:
        """
        # /parent::div 定位到上一级元素，preceding-sibling::+标签，代表定位同级元素的上一个元素
        # 定位祖先级元素，定位到的元素/ancestor::要定位的祖先元素
        return "//span[contains(text(),'欢迎您回来')]/parent::div/preceding-sibling::div//img"

