# coding:utf-8
import unittest

from config import driver_configure
from pages.My_Help import My_help
from pages import Boot


class Test_help(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = driver_configure.driver_configure().get_driver()
        self.Boot = Boot.Boot(self.driver)  # 引导页
        print("\033[4;33m-------开始帮助与反馈测试用例-------")

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        print("\033[4;33m-------结束帮助与反馈测试用例-------")

    def setUp(self):
        print("=======Test Start=======")

    def tearDown(self):
        print("=======Test End=======")

    def test_1(self):
        self.help = My_help.My_help(self.driver)  # 账号问题测试用例


if __name__ == '__main__':
    unittest.main()
