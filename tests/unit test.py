import unittest
import time
import os
from unittest import defaultTestLoader
from common import HTMLTestRunner_PY2

project_path = os.path.join("D:/Python/PyCharm Community Edition 2019.2.3/自动化测试")  # 项目路径
print(project_path)


def run():
    case_path = os.path.join(project_path, 'case')  # 测试用例路径
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py")  # 加载测试用例
    report = os.path.join(project_path, 'report')  # 测试报告文件夹路径
    if not os.path.isdir(report):  # 判定测试报告文件夹是否存在
        os.makedirs(report)  # 创建测试报告文件夹
    now = time.time()
    now_time = time.strftime("%Y-%m-%d-%H.%M", time.localtime(now))  # 当前时间
    report_name = "result_" + now_time + ".html"  # 测试报告名称
    report_path = os.path.join(project_path, 'report', report_name)  # 测试报告路径
    f = open(report_path, "wb")
    runner = HTMLTestRunner_PY2.HTMLTestRunner(stream=f, verbosity=2, title='奥克斯A+自动化测试报告', description='执行人：xx')
    runner.run(discover)
    f.close()


def getTestCaseNames(self, testCaseClass):
    test_names = super().getTestCaseNames(testCaseClass)
    testcase_methods = list(testCaseClass.__dict__.keys())
    test_names.sort(key=testcase_methods.index)
    return test_names


if __name__ == '__main__':
    run()
