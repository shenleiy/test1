from common import Element
from appium.webdriver.common import mobileby
import random, re, string
import time

by = mobileby.MobileBy()


class login_fail(Element.Element):
    def __init__(self, driver):
        self.driver = driver
        login_fail.get_name(self, '设置')
        login_fail.get_name(self, '退出登录')
        login_fail.get_name(self, '确定')
        login_fail.get_xpath_btn_clear(self, "com.broadlink.auxair:id/phone").click()
        print("-------开始登录失败测试-------")
        print("测试1-未输入手机号登录")
        login_fail.get_id(self, "com.broadlink.auxair:id/btn_next")
        login_fail.find_toast(self, text="请输入手机号")

        count1 = 5
        i = 0
        while i < 10:
            n = 0
            while n < count1:
                phone_head = random.choice([150, 189, 188, 170, 132, 150, 186])
                phone_end = random.randint(0, 99999999)
                phone_ture = '%s%08d\n' % (phone_head, phone_end)
                n += 1
            login_fail.get_xpath_edit(self, "com.broadlink.auxair:id/phone").send_keys(phone_ture)
            login_fail.get_id(self, "com.broadlink.auxair:id/btn_next")
            print("测试2-随机输入正规的手机号和空密码登录", phone_ture, end="")
            login_fail.find_toast(self, text="请输入密码")
            self.driver.implicitly_wait(5)
            login_fail.get_xpath_btn_clear(self, "com.broadlink.auxair:id/phone").click()
            i = i + 1

        count2 = 5
        i = 0
        while i < 10:
            n = 0
            while n < count2:
                phone_head = random.choice([150, 189, 188, 170, 132, 150, 186])
                phone_end = random.randint(0, 99999999)
                phone_ture = '%s%08d\n' % (phone_head, phone_end)
                n += 1
                m = 0
                passwds = []
                while m < count2:
                    a = random.randint(1, 7)
                    password_ture = random.sample(string.ascii_letters + string.digits, a)
                    passwd = ''.join(password_ture)
                    if re.search('[0-9]', passwd) and re.search('[A-Z]', passwd) and re.search('[a-z]', passwd):
                        passwds.append(passwd)
                        m += 1
            login_fail.get_xpath_edit(self, "com.broadlink.auxair:id/phone").send_keys(phone_ture)
            login_fail.get_xpath_edit(self, "com.broadlink.auxair:id/password").send_keys(password_ture)
            login_fail.get_id(self, "com.broadlink.auxair:id/btn_eye")
            time.sleep(3)
            login_fail.get_id(self, "com.broadlink.auxair:id/btn_next")
            print("测试3-随机输入正规的手机号和小于8位的密码登录")
            print('手机号：', phone_ture, end="")
            print('密码：', ''.join(password_ture))
            login_fail.find_toast(self, text="密码不能小于8位")
            self.driver.implicitly_wait(5)
            login_fail.get_xpath_btn_clear(self, "com.broadlink.auxair:id/phone").click()
            login_fail.get_xpath_btn_clear(self, "com.broadlink.auxair:id/password").click()
            i = i + 1

        count3 = 5
        i = 0
        while i < 1:
            n = 0
            while n < count3:
                phone_error = random.randint(0, 9999999999)
                n += 1
            login_fail.get_xpath_edit(self, "com.broadlink.auxair:id/phone").send_keys(phone_error)
            login_fail.get_id(self, "com.broadlink.auxair:id/btn_next")
            print("测试4-随机输入小于11位的手机号和空密码登录", phone_error, end="")
            login_fail.find_toast(self, text="请输入正确的手机号")
            self.driver.implicitly_wait(5)
            login_fail.get_xpath_btn_clear(self, "com.broadlink.auxair:id/phone").click()
            i = i + 1

        count4 = 5
        i = 0
        while i < 10:
            n = 0
            while n < count4:
                phone_head = random.choice([150, 189, 188, 170, 132, 150, 186])
                phone_end = random.randint(0, 99999999)
                phone_ture = '%s%08d\n' % (phone_head, phone_end)
                n += 1
                m = 0
                passwds = []
                while m < count4:
                    a = random.randint(8, 18)
                    password_ture = random.sample(string.ascii_letters + string.digits, a)
                    passwd = ''.join(password_ture)
                    if re.search('[0-9]', passwd) and re.search('[A-Z]', passwd) and re.search('[a-z]', passwd):
                        passwds.append(passwd)
                        m += 1
            login_fail.get_xpath_edit(self, "com.broadlink.auxair:id/phone").send_keys(phone_ture)
            login_fail.get_xpath_edit(self, "com.broadlink.auxair:id/password").send_keys(password_ture)
            login_fail.get_id(self, "com.broadlink.auxair:id/btn_eye")
            self.driver.implicitly_wait(5)
            login_fail.get_id(self, "com.broadlink.auxair:id/btn_next")
            print("测试5-随机输入正规的手机号和密码登录")
            print('手机号：', phone_ture, end="")
            print('密码：', ''.join(password_ture))
            login_fail.find_toast(self, text="用户名或密码错误")
            self.driver.implicitly_wait(5)
            login_fail.get_xpath_btn_clear(self, "com.broadlink.auxair:id/phone").click()
            login_fail.get_xpath_btn_clear(self, "com.broadlink.auxair:id/password").click()
            i = i + 1
            print("-------结束登录失败测试-------")
