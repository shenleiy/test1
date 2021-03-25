# coding:utf-8
import unittest

from config import driver_configure
from pages.Device import device_list, device_test
from pages import Boot


class Test_device(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = driver_configure.driver_configure().get_driver()
        #self.Boot = Boot.Boot(self.driver)  # 引导页
        print("\033[4;33m-------开始设备列表测试用例-------")

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        print("\033[4;33m-------结束设备列表测试用例-------")

    def setUp(self):
        print("=======Test Start=======")

    def tearDown(self):
        print("=======Test End=======")

    def test_1(self):
        runTimes = input('\033[31m请输入您要执行的次数：')
        i = 0
        while i < int(runTimes):
            self.device = device_test.device_list(self.driver)  # 设备列表测试用例
            i = i + 1
            print('\033[4;34m设备列表--挂机设备测试第%d次' % i)


if __name__ == '__main__':
    unittest.main()
