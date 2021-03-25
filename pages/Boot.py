from common import Element
from appium.webdriver.common import mobileby
from config import driver_configure1

by = mobileby.MobileBy()


class Boot(Element.Element):
    def boot(self, driver):
        self.driver = driver
        driver_configure1.driver_configure().get_driver()
        print("-------开始引导页测试-------")
        Boot.swipe_to_right(self)
        Boot.swipe_to_right(self)
        Boot.get_id(self, "com.broadlink.auxair:id/btnok")  # 点击立即体验
        # Boot.get_id(self, "android:id/button1")
        Boot.get_id(self, "com.broadlink.auxair:id/btn2")  # 点击同意
        print("-------结束引导页测试-------")
        Boot.get_name(self, '我的')
        # Boot.get_name(self, '密码登录')
        # Boot.get_Name(self, '请输入手机号').send_keys("15888504457")
        # Boot.get_Name(self, '请输入密码').send_keys("Aa123456")
        Boot.get_xpath_edit(self, "com.broadlink.auxair:id/phone").send_keys("15888504457")
        Boot.get_xpath_edit(self, "com.broadlink.auxair:id/password").send_keys("Aa123456")

        Boot.get_id(self, "com.broadlink.auxair:id/btn_eye")
        self.driver.implicitly_wait(3)
        # Boot.get_name(self, '登录')
        Boot.get_id(self, "com.broadlink.auxair:id/btn_next")
        Boot.find_toast(self, text="登录成功")


Boot().boot()
