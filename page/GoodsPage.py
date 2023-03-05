#! C:\Users\AdiminiChen\AppData\Local\Programs\Python\Python310
# coding=utf-8
# @Time: 2023/3/4 16:07
# @Author: jackchen
import time

from selenium.webdriver.common.by import By

from base.GoodsBase import GoodsBase
from base.ObjectMap import ObjectMap
from common.tools import get_img_path


class GoodsPage(GoodsBase, ObjectMap):
    """商品上传页方法"""

    def input_goods_title(self, driver, input_value):
        """
        输入商品标题
        :param driver:
        :param input_value:
        """
        goods_title_xpath = self.goods_title()
        return self.element_fill_value(driver, By.XPATH, goods_title_xpath, input_value)

    def input_goods_details(self, driver, input_value):
        """
        输入商品详情
        :param driver:
        :param input_value:
        """
        goods_details_xpath = self.goods_details()
        return self.element_fill_value(driver, By.XPATH, goods_details_xpath, input_value)

    def input_goods_number(self, driver, input_value, nums=1, flag=True):
        """
        输入商品数量或点击数量
        :param nums:默认点击一次
        :param flag:默认执行输入
        :return:
        :param driver:
        :param input_value:
        """
        if flag:
            goods_num_xpath = self.goods_number(plus=False)
            return self.element_fill_value(driver, By.XPATH, goods_num_xpath, input_value)
        else:
            click_goods_num_xpath = self.goods_number()
            for i in range(nums):
                self.element_click(driver, By.XPATH, click_goods_num_xpath)
                time.sleep(0.5)

    def upload_goods_img(self, driver, img_name):
        """
        上传商品图片
        :param driver:
        :param img_name:
        """
        # get img path
        img_path = get_img_path(img_name)
        upload_goods_img_xpath = self.goods_picture()
        return self.upload(driver, By.XPATH, upload_goods_img_xpath, img_path)

    def goods_prices(self, driver, input_value):
        """
        商品单价
        :param driver:
        :param input_value:
        """
        goods_price_xpath = self.goods_price()
        return self.element_fill_value(driver, By.XPATH, goods_price_xpath, input_value)

    def select_goods_status(self, driver, select_status_name):
        """
        商品选择
        :param select_status_name:
        :param driver:
        """
        select_goods_xpath = self.goods_status()
        self.element_click(driver, By.XPATH, select_goods_xpath)
        time.sleep(1)
        select_goods_status_name_xpath = self.goods_select_name(select_status_name)
        return self.element_click(driver, By.XPATH, select_goods_status_name_xpath)

    def click_goods_submit(self, driver, select_button):
        """
        提交
        :param driver:
        :param select_button:
        """
        goods_button_xpath = self.goods_submit(select_button)
        return self.element_click(driver, By.XPATH, goods_button_xpath)

    def add_goods_process(self, driver, goods_title, goods_details, goods_num, goods_pic_list, goods_price,
                          goods_status, button):
        """
        添加商品的流程
        :param driver:
        :param goods_title:商品标题
        :param goods_details:商品描述
        :param goods_num:商品数量
        :param goods_pic_list:商品图片名字  --列表
        :param goods_price:商品单价
        :param goods_status:商品状态
        :param button:提交
        """
        self.input_goods_title(driver, goods_title)
        time.sleep(1)
        self.input_goods_details(driver, goods_details)
        time.sleep(1)
        self.input_goods_number(driver, goods_num, flag=False)
        time.sleep(1)
        for goods_pic in goods_pic_list:
            self.upload_goods_img(driver, goods_pic)
            time.sleep(3)
        time.sleep(1)
        self.goods_prices(driver, goods_price)
        time.sleep(1)
        self.select_goods_status(driver, goods_status)
        time.sleep(1)
        self.click_goods_submit(driver, button)
        time.sleep(1)
        return True
