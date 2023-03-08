#! C:\Users\AdiminiChen\AppData\Local\Programs\Python\Python310
# coding=utf-8
# @Time: 2023/2/27 19:48
# @Author: jackchen
import time
from selenium.common.exceptions import ElementNotVisibleException, WebDriverException, NoSuchElementException, \
    StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from common.yaml_config import GetConfig


class ObjectMap:
    # 获取url地址
    url = GetConfig().get_url()

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
        等待页面加载时间
        :param driver:
        :param timeout:设置的超时时间
        """
        # 开始时间
        start_ms = time.time() * 1000
        # 结束时间
        stop_ms = start_ms + (timeout * 1000)
        for x in range(int(timeout * 10)):
            try:
                # 获取页面的状态
                ready_state = driver.execute_script("return document.readyState")
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

    def element_disappear(self, driver, locate_type, locate_expression, timeout=30):
        """
        等待页面元素消失
        :param driver:
        :param locate_type:
        :param locate_expression:
        :param timeout:
        """
        # 如果定位方式存在
        if locate_type:
            start_ms = time.time() * 1000
            stop_ms = start_ms + timeout * 1000
            for x in range(int(timeout * 10)):
                try:
                    el = driver.find_element(by=locate_type, value=locate_expression)
                    if el.is_displayed():
                        now_ms = time.time() * 1000
                        if now_ms >= stop_ms:
                            break
                        time.sleep(0.1)

                except Exception:
                    return True
            raise Exception("元素定位没有消失，定位方式：{}，定位表达式：{}".format(locate_type, locate_expression))
        else:
            pass

    def element_appear(self, driver, locate_type, locator_expression, timeout=30):
        """
        等待页面元素出现
        :param driver:
        :param locate_type:
        :param locator_expression:
        :param timeout:
        """
        if locate_type:
            start_ms = time.time() * 1000
            stop_ms = start_ms + timeout * 1000
            for x in range(int(timeout * 10)):
                try:
                    el = driver.find_element(by=locate_type, value=locator_expression)
                    if el.is_displayed():
                        return el
                    else:
                        raise Exception()
                except Exception:
                    now_ms = time.time() * 1000
                    if now_ms >= stop_ms:
                        break
                    time.sleep(0.1)
            raise ElementNotVisibleException("元素没有出现，定位方式：{}，定位表达式：{}".format(locate_type, locator_expression))
        else:
            pass

    def element_to_url(self, driver, url, locate_type_disappear=None, locator_expression_disappear=None,
                       locate_type_appear=None, locator_expression_appear=None):
        """
        跳转地址
        :param driver:
        :param url: 跳转的地址
        :param locate_type_disappear: 等待页面元素消失的定位方式
        :param locator_expression_disappear: 等待页面元素消失的定位表达方式
        :param locate_type_appear: 等待页面元素出现的定位方式
        :param locator_expression_appear: 等待页面元素出现的定位表达方式
        """
        try:
            driver.get(self.url + url)
            # 等待页面元素都加载完成
            self.wait_for_ready_state_complete(driver)
            # 跳转地址后等待页面元素消失
            self.element_disappear(driver=driver, locate_type=locate_type_disappear,
                                   locate_expression=locator_expression_disappear)
            # 跳转后等待页面元素出现
            self.element_appear(driver=driver, locate_type=locate_type_appear,
                                locator_expression=locator_expression_appear)
        except Exception as e:
            print("跳转地址出现异常：", e)
            return False
        return True

    def element_is_display(self, driver, locate_type, locate_expression):
        """
        元素是否显示
        :param driver:
        :param locate_type:
        :param locate_expression:
        """
        try:
            driver.find_element(by=locate_type, value=locate_expression)
            return True
        except NoSuchElementException:
            # 发生了NoSuchElementException异常，说明页面中未找到元素，返回false
            return False

    def element_fill_value(self, driver, locate_type, locator_expression, fill_value, timeout=30):
        """
        元素填值操作
        :param driver:
        :param locate_type:
        :param locator_expression:
        :param fill_value: 填入的值
        :param timeout:
        """
        # 元素必须先出现
        el = self.element_appear(driver=driver, locate_type=locate_type, locator_expression=locator_expression,
                                 timeout=timeout)
        try:
            # 先清除元素中的原有值
            el.clear()
        # 页面元素没有刷新，就对元素进行异常捕获
        except StaleElementReferenceException:
            # 等待页面加载完成
            self.wait_for_ready_state_complete(driver)
            time.sleep(0.06)
            # 等元素出现
            el = self.element_appear(driver=driver, locate_type=locate_type, locator_expression=locator_expression,
                                     timeout=timeout)
            try:
                el.clear()
            except Exception:
                pass
        except Exception:
            pass
        # 填入值转成字符串
        if type(fill_value) is int or type(fill_value) is float:
            fill_value = str(fill_value)
        try:
            # 不是以\n 结尾 直接填值
            if not fill_value.endswith("\n"):
                el.send_keys(fill_value)
                # 填完值后等待元素加载完成
                self.wait_for_ready_state_complete(driver=driver)
            else:
                # 有\n结尾 要截去\n 123\n ---> 123
                fill_value = fill_value[:-1]
                el.send_keys(fill_value)
                # 进行回车
                el.send_keys(Keys.RETURN)
                self.wait_for_ready_state_complete(driver=driver)
        except StaleElementReferenceException:
            # 等待页面加载完成
            self.wait_for_ready_state_complete(driver=driver)
            time.sleep(0.06)
            el = self.element_appear(driver=driver, locate_type=locate_type, locator_expression=locator_expression,
                                     timeout=timeout)
            el.clear()
            # 不是以\n 结尾 直接填值
            if not fill_value.endswith("\n"):
                el.send_keys(fill_value)
                # 填完值后等待元素加载完成
                self.wait_for_ready_state_complete(driver=driver)
            else:
                # 有\n结尾 要截去\n 123\n ---> 123
                fill_value = fill_value[:-1]
                el.send_keys(fill_value)
                # 进行回车
                el.send_keys(Keys.RETURN)
                self.wait_for_ready_state_complete(driver=driver)
        except Exception:
            raise Exception("元素填值失败")
        # 填写成功后return True
        return True

    def element_click(self, driver, locate_type, locator_expression, locate_type_disappear=None,
                      locator_expression_disappear=None,
                      locate_type_appear=None,
                      locator_expression_appear=None, timeout=30):
        """
        元素的点击
        :param driver:
        :param locate_type:定位方式
        :param locator_expression:定位表达式
        :param locate_type_disappear:等待页面元素消失的定位方式
        :param locator_expression_disappear:等待页面元素消失的定位表达式
        :param locate_type_appear:等待页面元素出现的定位方式
        :param locator_expression_appear:等待页面元素出现的定位表达式
        :param timeout:
        """
        # 元素要可见
        el = self.element_appear(driver=driver, locate_type=locate_type, locator_expression=locator_expression,
                                 timeout=timeout)
        try:
            # 点击元素
            el.click()
        except StaleElementReferenceException:
            self.wait_for_ready_state_complete(driver=driver)
            el = self.element_appear(driver=driver, locate_type=locate_type, locator_expression=locator_expression,
                                     timeout=timeout)
            el.click()

        except Exception as e:
            print("页面元素出现异常，不可点击", e)
            return False

        try:
            # 点击元素后的元素出现
            self.element_appear(driver, locate_type_appear, locator_expression_appear)
            # 等待页面元素的消失
            self.element_disappear(driver, locate_type_disappear, locator_expression_disappear)
        except Exception as e:
            print("页面元素消失或出现异常", e)
            return False
        return True

    def upload(self, driver, locate_type, locator_expression, file_path):
        """
        文件上传
        :param file_path:
        :param driver:
        :param locate_type:
        :param locator_expression:
        """
        el = self.element_get(driver, locate_type, locator_expression)
        return el.send_keys(file_path)

    def switch_window_to_handle(self, driver):
        """
        窗口的切换
        :param driver:
        """
        # 获取窗口权柄
        window_handle = driver.window_handles
        # 传入最后一个窗口的权柄
        driver.switch_to.window(window_handle[-1])

    def switch_into_iframe(self, drive, locate_iframe_type, locator_iframe_expression):
        """
        iframe切换
        :param drive:
        :param locate_iframe_type:
        :param locator_iframe_expression:
        :return:
        """
        iframe = self.element_get(drive, locate_iframe_type, locator_iframe_expression)
        drive.switch_to.frame(iframe)

    def switch_from_iframe_to_content(self, driver):
        """
        从iframe切换到主页面
        :param driver:
        :return:
        """
        driver.switch_to.parent_frame()
