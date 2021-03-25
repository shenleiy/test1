from common import Element
import time
import random, re, string


class My_Product(Element.Element):
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(50)  # 隐形等待最长50s
        print("-------开始电子说明书测试-------")
        My_Product.get_name(self, "产品指南")
        print("点击产品指南")
        My_Product.get_name(self, "电子说明书")
        print("点击电子说明书")
        modle = ['KF-23GW/AFF600+3', 'KF-26GW/TYC2+3a', 'KFR-25GW/TYF1+3', 'T081', 'YKR-T011']
        Module = random.choice(modle)
        print(Module)
        My_Product.get_name(self, "请输入设备型号")
        time.sleep(1)
        My_Product.get_Name(self, "请输入设备型号").send_keys(Module)
        My_Product.get_id(self, 'com.broadlink.auxair:id/model')
        time.sleep(3)
        My_Product.get_id(self, 'com.broadlink.auxair:id/sLeftIconId')
        My_Product.get_name(self, '取消')
        time.sleep(1)
        My_Product.get_id(self, 'com.broadlink.auxair:id/model')
        time.sleep(3)
        My_Product.get_id(self, 'com.broadlink.auxair:id/sLeftIconId')
        My_Product.get_id(self, 'com.broadlink.auxair:id/iv_search_clear')
        My_Product.get_name(self, '取消')
        My_Product.get_id(self, 'com.broadlink.auxair:id/iv_search_clear')
        My_Product.get_name(self, '确定')
        time.sleep(1)
        My_Product.get_id(self, "com.broadlink.auxair:id/sLeftIconId")
        print("-------结束电子说明书测试-------")
