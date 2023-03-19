#! C:\Users\AdiminiChen\AppData\Local\Programs\Python\Python310
# coding=utf-8
# @Time: 2023/3/7 20:43
# @Author: jackchen
import pytest

from config.driver_config import DriverConfig
from common.report_add_img import add_img_2_report


@pytest.fixture()
def driver():
    global get_driver
    get_driver = DriverConfig().driver_config()
    yield get_driver
    get_driver.quit()


# 内置钩子函数 如果执行用例中失败，立即把截图加入测试报告
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # 获取钩子方法的调用结果
    out = yield
    # 从out里获取测试报告
    report = out.get_result()
    report.description = str(item.function.__doc__)  # 获取执行过程中的注释

    if report.when == "call":
        if report.failed:
            # 失败就截图
            add_img_2_report(get_driver, "失败截图", need_sleep=False)

