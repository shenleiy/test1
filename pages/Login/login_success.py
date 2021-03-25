from common import Element


class login_success(Element.Element):
    def __init__(self, driver):
        self.driver = driver
        print("-------开始登录成功测试-------")
        login_success.get_name(self, '设置')
        login_success.get_name(self, '退出登录')
        login_success.get_name(self, '确定')
        login_success.get_name(self, '密码登录')
        self.driver.implicitly_wait(5)
        login_success.get_id(self, 'com.broadlink.auxair:id/yi_input_phone')
        login_success.get_id(self, 'com.broadlink.auxair:id/btn_clear')
        login_success.get_Name(self, '请输入手机号').send_keys("13456140816")
        print("输入手机号13456140816")
        login_success.get_Name(self, '请输入密码').send_keys("Aa123456")
        print("输入密码Aa123456")
        login_success.get_id(self, "com.broadlink.auxair:id/btn_eye")
        print("点击明码显示")
        login_success.get_name(self, '登录')
        print("点击登录")
        login_success.find_toast(self, text="登录功")
        login_success.get_name(self, '我的')
        print("我的页面")
        print("-------结束登录成功测试-------")
