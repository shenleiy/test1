from common import Element
import time


class device_list(Element.Element):
    def __init__(self, driver):
        self.driver = driver
        device_list.get_name(self, '奥克斯空调')
        n = 0
        while n < 300:
            time.sleep(3)
            device_list.get_name(self, '制冷')
            time.sleep(3)
            device_list.get_name(self, '上下摆风')
            device_list.get_name(self, '开关')
            print('开关机')
            n += 1
            print(n)
