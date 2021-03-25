# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver  # 导入driver的对象
from test.study.device import MY_GUI

PlatformName = MY_GUI.text()


class driver_configure:
    def __init__(self):
        desired_caps = {'platformName': 'Android',
                        'platformVersion': '9',
                        'deviceName': '736a2c56̉',
                        'appPackage': 'com.broadlink.auxair',
                        'appActivity': 'com.auxgroup.smarthome.activity.appstart.SplashActivity',
                        'unicodeKeyboard': 'true',  # 是否支持unicode的键盘。如果需要输入中文，要设置为“true”
                        'resetKeyboard': 'true',  # 是否在测试结束后将键盘重轩为系统默认的输入法。
                        'noReset': 'true'}  # true:不重新安装APP，false:重新安装app

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)  # 隐形等待最长5s

    def get_driver(self):
        return self.driver


driver_configure()
# if __name__ == '__main__':
# driver_configure().get_driver()
