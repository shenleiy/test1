from common import Element
import time


class device_list(Element.Element):
    def __init__(self, driver):
        self.driver = driver
        device_list.get_name(self, '设备')
        if device_list.find_name(self, '暂无设备，去添加'):
            print('设备列表无设备')
        elif device_list.find_name(self, '离线'):
            print('设备离线')
            device_list.get_name(self, '离线')
            device_list.find_name(self, '已离线')
            device_list.get_id(self, 'com.broadlink.auxair:id/sLeftIconId')
            print('返回设备列表页面')
        else:
            print('无离线设备')
            if device_list.find_name(self, '关机'):
                print('设备在线关机')
                device_list.get_name(self, '关机')
                device_list.find_name(self, '已关机')
                device_list.get_name(self, '清洁')
                device_list.get_name(self, '防霉')
                print('开启清洁、防霉功能')
                device_list.get_id(self, 'com.broadlink.auxair:id/sLeftIconId')
                print('返回设备列表页面')
                device_list.get_id(self, 'com.broadlink.auxair:id/pane_ofoff')
            elif device_list.find_name(self, '℃'):
                print('设备在线开机')
                device_list.get_id(self, 'com.broadlink.auxair:id/modeName')
                device_list.find_name(self, '模式')
                device_list.get_name(self, '模式')
                time.sleep(1)
                if device_list.find_name(self, '制热'):
                    device_list.get_name(self, '制热')
                    device_list.get_id(self, 'com.broadlink.auxair:id/sLeftIconId')
                    print('返回设备列表页面--制热模式')
                    device_list.find_name(self, '制热')
                    device_list.get_id(self, 'com.broadlink.auxair:id/pane_add')
                    print('升高温度')
                    time.sleep(1)
                    device_list.get_id(self, 'com.broadlink.auxair:id/pane_minus')
                    print('降低温度')
                    device_list.get_id(self, 'com.broadlink.auxair:id/modeName')
                    device_list.get_name(self, '模式')
                else:
                    print('\033[4;34m单冷机型')
                device_list.get_name(self, '制冷')
                device_list.get_id(self, 'com.broadlink.auxair:id/sLeftIconId')
                print('返回设备列表页面--制冷模式')
                device_list.find_name(self, '制冷')
                device_list.get_id(self, 'com.broadlink.auxair:id/pane_add')
                print('升高温度')
                device_list.get_id(self, 'com.broadlink.auxair:id/pane_minus')
                print('降低温度')

                device_list.get_id(self, 'com.broadlink.auxair:id/modeName')
                device_list.get_name(self, '模式')
                device_list.get_name(self, '除湿')
                device_list.get_id(self, 'com.broadlink.auxair:id/sLeftIconId')
                print('返回设备列表页面--除湿模式')
                device_list.find_name(self, '除湿')
                device_list.get_id(self, 'com.broadlink.auxair:id/pane_add')
                print('升高温度')
                device_list.get_id(self, 'com.broadlink.auxair:id/pane_minus')
                print('降低温度')

                device_list.get_id(self, 'com.broadlink.auxair:id/modeName')
                device_list.get_name(self, '模式')
                device_list.get_name(self, '送风')
                device_list.get_id(self, 'com.broadlink.auxair:id/sLeftIconId')
                print('返回设备列表页面--送风模式')
                device_list.find_name(self, '送风')
                device_list.get_id(self, 'com.broadlink.auxair:id/pane_add')
                device_list.find_toast(self, '送风模式不能设置温度')
                time.sleep(3)
                device_list.get_id(self, 'com.broadlink.auxair:id/pane_minus')
                device_list.find_toast(self, '送风模式不能设置温度')

                device_list.get_id(self, 'com.broadlink.auxair:id/modeName')
                device_list.get_name(self, '模式')
                device_list.get_name(self, '自动')
                device_list.get_id(self, 'com.broadlink.auxair:id/sLeftIconId')
                print('返回设备列表页面--自动模式')
                device_list.find_name(self, '自动')
                device_list.get_id(self, 'com.broadlink.auxair:id/pane_add')
                device_list.find_toast(self, '自动模式不能设置温度')
                time.sleep(3)
                device_list.get_id(self, 'com.broadlink.auxair:id/pane_minus')
                device_list.find_toast(self, '自动模式不能设置温度')
            else:
                print('无在线设备')


