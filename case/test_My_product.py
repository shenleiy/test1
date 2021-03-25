# coding:utf-8
import unittest

from config import driver_configure
from pages.My_Product import knowledge, book
from pages import Boot


class Test_product(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = driver_configure.driver_configure().get_driver()
        self.Boot = Boot.Boot(self.driver)  # 引导页
        print("\033[4;33m-------开始产品指南测试用例-------")

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        print("\033[4;33m-------结束产品指南测试用例-------")

    def setUp(self):
        print("=======Test Start=======")

    def tearDown(self):
        print("=======Test End=======")

    def test_1(self):
        self.book = book.My_Product(self.driver)  # 电子说明书测试用例
        print("电子说明书测试")

    def test_2(self):
        self.knowledge = knowledge.My_Product(self.driver)  # 产品使用知识测试用例
        print("产品使用知识测试")


if __name__ == '__main__':
    unittest.main()
