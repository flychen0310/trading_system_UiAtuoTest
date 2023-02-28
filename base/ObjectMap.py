#! C:\Users\AdiminiChen\AppData\Local\Programs\Python\Python310
# coding=utf-8
# @Time: 2023/2/27 19:48
# @Author: jackchen
import time
from selenium.common.exceptions import ElementNotVisibleException, WebDriverException


class ObjectMap:

    def element_get(self, driver, locate_type, locator_expression, timeout=10, must_visible=False):
        """
        单个元素获取
        :param driver: 驱动
        :param locate_type:定位方法 css xpath
        :param locator_expression:定位表达式
        :param timeout:设置的超时时间
        :param must_visible:判断元素是否为可见，默认不可见
        :return:返回元素
        """
        # 开始时间
        start_ms = time.time() * 1000
        # 设置结束时间
        stop_ms = start_ms + (timeout * 1000)
        # 循环找元素 100次
        for x in range(int(timeout * 10)):  #
            # 查找元素
            try:
                el = driver.find_element(by=locate_type, value=locator_expression)
                # 如果元素不是必须可见，就直接返回元素
                if not must_visible:
                    return el
                # 如果元素必须是可见的 ，则先判断元素是否可见
                else:
                    if el.is_displayed():
                        return el
                    else:
                        raise Exception()

            except Exception:
                now_ms = time.time() * 1000
                # 如果超时直接跳出整个循环
                if now_ms >= stop_ms:
                    break
            time.sleep(0.1)
        raise ElementNotVisibleException("元素定位失败，定位方式：{}，定位表达式：{}".format(locate_type, locator_expression))

    def wait_for_ready_state_complete(self, driver, timeout=30):
        """
        等等待页面加载时间
        :param driver:
        :param timeout:设置的超时时间
        """
        # 开始时间
        start_ms = time.time() * 1000
        # 结束时间
        stop_ms = start_ms + timeout * 1000
        for x in range(int(timeout) * 10):
            try:
                # 获取页面的状态
                ready_state = driver.execute_script("document.readyState")
            except WebDriverException:
                # driver执行失败 直接跳过
                time.sleep(0.03)
                return True
            # 如果页面全部加载完成 返回True
            if ready_state == 'complete':
                time.sleep(0.01)
                return True
            else:
                now_ms = time.time() * 1000
                # 如果当前时间大于超时时间结束
                if now_ms >= stop_ms:
                    break
                time.sleep(0.1)
        raise Exception("打开网页时，页面元素在{}秒后没有加载完成".format(timeout))
