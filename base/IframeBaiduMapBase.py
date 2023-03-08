#! C:\Users\AdiminiChen\AppData\Local\Programs\Python\Python310
# coding=utf-8
# @Time: 2023/3/5 16:16
# @Author: jackchen
class IframeBaiduMapBase:

    def search_button(self):
        """
        搜索
        :return:
        """
        return "//button[@data-title='搜索']"

    def baidu_iframe(self):
        """
        定位iframe元素
        :return:
        """
        return "//iframe[@src='https://map.baidu.com/']"
