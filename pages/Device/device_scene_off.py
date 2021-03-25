from os.path import join

from common import Element
import random, re, string
import time


class device_scene(Element.Element):
    def __init__(self, driver):
        self.driver = driver
        xing = '赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜'
        X = random.choice(xing)
        a = random.randint(1, 20)
        device_scene.get_name(self, '场景')
        scene = ['回家（手动）', '离家（手动）']
        Scene = random.choice(scene)
        print(Scene)
        device_scene.get_name(self, Scene)
        print('场景未添加设备')
        device_scene.get_name(self, '确定')
        device_scene.find_toast(self, '请选择有效设备')
        device_scene.get_name(self, '选择设备')
        time.sleep(1)
        device_scene.get_id(self, 'com.broadlink.auxair:id/recyclerview')
        device_scene.get_name(self, '确定')
        print('关机场景')
        time.sleep(1)
        device_scene.get_name(self, '确定')
        device_scene.get_id(self, 'com.broadlink.auxair:id/iv_delete')
        print('输入超20位的场景名称')
        device_scene.get_Id(self, 'com.broadlink.auxair:id/tv_input').send_keys('1234567890qwertyuiop!')
        device_scene.find_toast(self, '场景名称不能超过20位')
        device_scene.get_id(self, 'com.broadlink.auxair:id/iv_delete')
        name = random.sample(string.ascii_letters + string.digits + X, a)
        Name = ''.join(name)
        print('随机输入20位以内的场景名称:', Name)
        device_scene.get_Id(self, 'com.broadlink.auxair:id/tv_input').send_keys(name)
        device_scene.get_name(self, '完成')
        device_scene.find_toast(self, '保存成功')
        device_scene.find_name(self, Name)
        device_scene.get_name(self, '执行')
        device_scene.get_id(self, 'com.broadlink.auxair:id/scene_log')
        device_scene.find_name(self, Name + '执行成功')
        device_scene.get_id(self, 'com.broadlink.auxair:id/sLeftIconId')
        device_scene.get_name(self, '推荐')
        device_scene.get_name(self, '设备')
        device_scene.find_name(self, '关机')
