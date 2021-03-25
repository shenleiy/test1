from common import Element
import random, re, string
import time


class My_network(Element.Element):
    def __init__(self, driver):
        self.driver = driver
        print("-------开始配网测试-------")
        xing = '赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜'
        X = random.choice(xing)
        a = random.randint(1, 20)
        My_network.get_name(self, '设备')
        My_network.get_id(self, 'com.broadlink.auxair:id/tb_moreBtn')
        print("点击添加设备")
        My_network.get_name(self, '手动选择型号')
        print('选择型号页面')
        # My_Network.get_name(self,'柜机')
        type = ['KFR-35GW/BpBYA700(A1)', 'KFR-26GW/BpAYA800(A1)', 'KFR-35GW/BpR3TYC2+1', 'KFR-26GW/BpR3TYC3+1',
                'KFR-26GW/BpR3AYC600(A1)', 'KFR-26GW/BpR3PYA2+2']
        Type = random.choice(type)
        print(Type)
        My_network.get_name(self, Type)
        print('选择全网通一键配网机型')
        # My_Network.get_id(self,'com.broadlink.auxair:id/btn_clear')
        # print('清除密码')
        My_network.get_Id(self, 'com.broadlink.auxair:id/edit1').send_keys('1234567890qwertyuiopQWERTYUIOP!@')
        print('输入密码')
        My_network.get_id(self, 'com.broadlink.auxair:id/btn_eye')
        print("点击明码显示")
        My_network.get_name(self, '下一步')
        My_network.get_id(self, 'com.broadlink.auxair:id/iv_check')
        print('点击完成上述步骤')
        My_network.get_name(self, '下一步')
        if My_network.find_success(self, name="已成功添加设备"):
            name = random.sample(string.ascii_letters + string.digits + X, a)
            Name = ''.join(name)
            print('空调设备名称为:', Name)
            My_network.get_Id(self, 'com.broadlink.auxair:id/deviceName').send_keys(name)
            My_network.get_name(self, '确定')
            My_network.get_id(self, 'com.broadlink.auxair:id/name')
            My_network.get_name(self, '开关')
            My_network.get_name(self, '制冷')
            time.sleep(1)
            My_network.get_name(self, '风速')
            speed = ['静音', '低档', '中档', '高档', '强力', '自动']
            Speed = random.choice(speed)
            print(Speed)
            My_network.get_name(self, Speed)
        else:
            print('\033[4;31m配网失败')
