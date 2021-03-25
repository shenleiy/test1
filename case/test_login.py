# coding:utf-8
import unittest

from config import driver_configure
from pages.Login import login_fail, login_success
from pages import Boot


class Test_login(unittest.TestCase):

    def setUp(self):
        self.driver = driver_configure.driver_configure().get_driver()
        self.Boot = Boot.Boot(self.driver)  # 引导页
        print("\033[4;33m-------开始登录测试用例-------")

    def tearDown(self):
        self.driver.quit()
        print("\033[4;33m-------结束登录测试用例-------")

    def test_1(self):
        #runTimes = input("\033[31m请输入您要执行的次数：")
        runTimes = 1
        i = 0
        while i < int(runTimes):
            self.login = login_success.login_success(self.driver)  # 登录成功用例
            i = i + 1
            print('\033[4;32m成功登录第%d次' % i)

    def test_2(self):
        self.login = login_fail.login_fail(self.driver)  # 登录失败用例


if __name__ == '__main__':
    unittest.main()
