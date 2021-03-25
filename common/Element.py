# coding=utf-8
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Element:
    def __init__(self, driver):
        self.driver = driver
    """
    封装Appium中关于元素对象的方法
    """

    def get_Id(self, Id):
        self.driver.implicitly_wait(3)
        element = self.driver.find_element_by_id(Id)
        return element

    def get_id(self, id):
        self.driver.implicitly_wait(3)
        element = self.driver.find_element_by_id(id).click()
        return element

    # id定位

    def get_Name(self, Name):
        self.driver.implicitly_wait(3)
        element = self.driver.find_element(by=By.XPATH, value="//*[@text='%s']" % Name)
        return element

    def get_name(self, name):
        self.driver.implicitly_wait(3)
        element = self.driver.find_element(by=By.XPATH, value="//*[@text='%s']" % name).click()
        return element

    # name定位

    def get_class(self, classname):
        element = self.driver.find_element_by_class_name(classname).click()
        return element

    # classname定位

    def get_xpath_edit(self, id):
        element = self.driver.find_element(by=By.XPATH,
                                           value="//*[@resource-id='%s']/android.view.ViewGroup/android.widget.EditText" % id)
        return element

    def get_xpath_btn_clear(self, id):
        element = self.driver.find_element(by=By.XPATH,
                                           value="//*[@resource-id='%s']/android.widget.ImageView" % id)
        return element

    # xpath_id定位登录页面

    def over(self):
        element = self.driver.quit()
        return element

    def back(self):
        self.driver.keyevent(4)

    def get_screen(self, path):
        self.driver.get_screenshot_as_file(path)

    def get_size(self):
        size = self.driver.get_window_size()
        return size

    def swipe_to_up(self):
        self.driver.implicitly_wait(3)
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, 2000)

    # 上滑

    def swipe_to_down(self):
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width / 2, height / 4, width / 2, height * 3 / 4, 2000)

    # 下滑

    def swipe_to_left(self):
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width / 4, height / 2, width * 3 / 4, height / 2, 2000)

    # 左滑

    def swipe_to_right(self):
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width * 9 / 10, height / 2, width / 20, height / 2, 2000)

    # 右滑

    def swipe_up(self, name):
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        i = 0
        while i < 5:
            try:
                self.driver.implicitly_wait(1)
                self.driver.find_element(by=By.XPATH, value="//*[@text='%s']" % name).click()  # 尝试点击元素
                return
            except Exception as e:
                self.driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, 2000)
                print("未搜索到元素:", name, ",页面上滑")
                i = i + 1

    def swipe_down(self, name):
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.implicitly_wait(1)
        i = 0
        while i < 5:
            try:
                self.driver.find_element_by_xpath("//*[@text='%s']" % name).click()  # 尝试点击元素
                break
            except Exception as e:
                self.driver.swipe(width / 2, height * 3 / 4, width / 2, height * 19 / 20, 2000)
                print("未搜索到元素:", name, ",页面下滑")
                i = i + 1

    # 当前页面元素判定

    def find_toast(self, text):
        try:
            toast_loc = (By.XPATH, "//*[contains(@text,'" + text + "')]")
            ele = WebDriverWait(self.driver, 10, 0.1).until(EC.presence_of_element_located(toast_loc))
            return ele.text
        except:
            print("\033[4;31m页面未搜索到判定词：", "FAIL")
            return "Toast not found"

    # toast提示框判定

    def find_name(self, name):
        self.driver.implicitly_wait(10)  # 隐形等待最长10
        try:
            element = self.driver.find_element(by=By.XPATH, value="//*[@text='%s']" % name)
            print('\033[4;32m页面搜索到判定词：', name, "PASS")
            return element
        except Exception:
            print("\033[4;31m页面未搜索到判定词：", name, "FAIL")
            return

    # 页面文字判定

    def find_success(self, name):
        self.driver.implicitly_wait(60)  # 隐形等待最长60
        try:
            element = self.driver.find_element(by=By.XPATH, value="//*[@text='%s']" % name)
            print('\033[4;32m页面搜索到判定词：', name, "PASS")
            return element
        except Exception:
            print("\033[4;31m页面未搜索到判定词：", name, "FAIL")
            return

    # 配网是否成功判定

    def check_cancelBtoon(self, id):
        print("检查取消按钮")
        try:
            cancelBtoon = self.driver.find_element_by_id(id)
        except  Exception:
            print("没有取消按钮")
        else:
            cancelBtoon.click()

    # 取消按钮框判定

    def check_skipBtoon(self, id):
        print("检查跳过按钮")
        try:
            skipBtoon = self.driver.find_element_by_id(id)
        except Exception:
            print("没有跳过按钮")
        else:
            skipBtoon.click()
    # 跳过按钮框判定
