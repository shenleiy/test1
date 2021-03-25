# coding:utf-8
import unittest
from config import driver_configure1
from pages.My_Network import My_network
import time
from pages import Boot
from appium import webdriver  # 导入driver的对象


class Test_network(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # self.driver = driver_configure.driver_configure().get_driver()
        # self.Boot = Boot.Boot(self.driver)  # 引导页
        print("-------开始配网测试用例-------")

    @classmethod
    def tearDownClass(self):
        # self.driver.quit()
        print("-------结束配网测试用例-------")

    def setUp(self):
        print("=======Test Start=======")

    def tearDown(self):
        print("=======Test End=======")

    def test_1(self):
        # runTimes = input("请输入您要执行的次数：")
        runTimes = 1
        i = 0
        while i < int(runTimes):
            self.driver = driver_configure1.driver_configure().get_driver()
            self.network = My_network.My_network(self.driver)  # 个人页面测试用例
            self.driver.quit()
            i = i + 1
            now = time.time()
            now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(now))  # 当前时间
            print('\033[4;34m配网执行第%d次\033[0m' % i, now_time)


Test_network()
# if __name__ == '__main__':
# unittest.main()
