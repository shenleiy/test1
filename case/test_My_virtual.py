# coding:utf-8
import unittest

from config import driver_configure
from pages.My_Virtual import My_virtual
from pages import Boot


class Test_virtual(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = driver_configure.driver_configure().get_driver()
        self.Boot = Boot.Boot(self.driver)#引导页
        print("\033[4;33m-------开始虚拟体验测试用例-------")

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        print("\033[4;33m-------结束虚拟体验测试用例-------")

    def setUp(self):
        print("=======Test Start=======")

    def tearDown(self):
        print("=======Test End=======")

    def test_1(self):
        self.virtual = My_virtual.My_virtual(self.driver)  # 虚拟体验测试用例