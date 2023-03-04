#! C:\Users\AdiminiChen\AppData\Local\Programs\Python\Python310
# coding=utf-8
# @Time: 2023/3/4 15:01
# @Author: jackchen
class GoodsBase:
    """新增二手商品页面的定位方法"""

    def goods_title(self):
        """商品标题"""
        return "//form[@class= 'el-form']//textarea[@placeholder='请输入商品标题']"

    def goods_details(self):
        """商品详情"""
        return "//form[@class= 'el-form']//textarea[@placeholder='请输入商品详情']"

    def goods_number(self, plus=True):
        """商品数量"""
        if plus:
            # 用加减号
            return "//label[@for='product_stock']/following-sibling::div//i[@class='el-icon-plus']/parent::span"
        else:
            # 输入值
            return "//form[@class= 'el-form']//input[@placeholder='商品数量']"

    def goods_picture(self):
        """图片"""
        return "//input[@name='file']"

    def goods_price(self):
        """商品单价"""
        return "//form[@class='el-form']//input[@placeholder='请输入商品单价']"

    def goods_status(self):
        """商品状态"""
        return "//form[@class='el-form']//input[@placeholder='请选择商品状态']"

    def goods_select_name(self, select_name):
        """商品状态名字"""
        return "//span[text()='{}']/parent::li".format(select_name)

    def goods_submit(self, select_button):
        """商品提交或重置"""
        return "//span[text()='{}']/parent::button".format(select_button)
