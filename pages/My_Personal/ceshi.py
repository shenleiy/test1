# coding:utf-8
import unittest
from common import Element
import time

class My_virtual(Element.Element):
    def __init__(self, driver):
        self.driver = driver
        print("-------开始虚拟体验测试-------")
        My_virtual.get_name(self, '我的')
        print("我的页面")
        My_virtual.get_name(self, '虚拟体验')
        print("点击虚拟体验")
        i = 0
        while i < 20:
            My_virtual.get_id(self, "com.broadlink.auxair:id/addBtn")
            time.sleep(1)
            if My_virtual.get_Id(self,'com.broadlink.auxair:id/tv_temp') != 33:
                i=i+1
                if My_virtual.find_toast(self, text='已是最高温度'):
                    break

