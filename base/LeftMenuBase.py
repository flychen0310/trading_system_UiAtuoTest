#! C:\Users\AdiminiChen\AppData\Local\Programs\Python\Python310
# coding=utf-8
# @Time: 2023/2/27 14:03
# @Author: jackchen
class LeftMenuBase:
    """左侧菜单栏定位方法"""

    def level_one_menu(self, menu_name):
        """
        一级菜单栏定位
        """
        return "//aside[@class='el-aside']//span[text()='{}']/ancestor::li".format(menu_name)

    def level_two_menu(self, menu_name):
        """
        二级菜单
        :param menu_name:
        :return:
        """
        return "//aside[@class='el-aside']//span[text()='{}']/parent::li".format(menu_name)


if __name__ == '__main__':
    print(LeftMenuBase().level_one_menu('hhh'))
