# -*- coding: utf-8 -*-
# @Time    : 2018/7/19 下午5:23
# @Author  : Danny
# @File    : Yaml_Data.py

from ruamel import yaml
import os
import sys


# curPath = os.path.dirname(os.path.abspath('..'))
# yamlPath = os.path.join(curPath + '\\A+6.0 Interface Api\\test_data', "test_data.yaml")
# print(yamlPath)
class HandleYaml:
    def __init__(self, file_path=None):
        if file_path:
            self.file_path = file_path
        else:
            curPath = os.path.dirname(os.path.abspath('..'))
            # os.path.abspath('.')表示获取当前文件所在目录；os.path.dirname表示获取文件所在父目录；所以整个就是项目的所在路径
            print('........................', curPath, '..........................')
            self.file_path = curPath + '\\A+6.0 Interface Api\\test_data\\test_yaml_data.yaml'  # 获取文件所在的相对路径(相对整个项目)
            # Xiaoniu_Api_Rili\\
            # self.data = self.get_data()

    def file_load(self):
        fp = open(self.file_path, 'r', encoding='utf-8')
        file_data = fp.read()
        fp.close()
        data = yaml.safe_load_all(file_data)
        for a in data:
            return a

    def file_dump(self, name, key, value):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            # data = list(yaml.safe_load_all(fp))
            # print(data)
            # data[name][key] = value
            doc = yaml.round_trip_load(f)
        doc[name][key] = value
        with open(self.file_path, 'w', encoding="utf-8") as f:
            yaml.round_trip_dump(doc, f, allow_unicode=True, default_flow_style=True)
            f.close()


if __name__ == '__main__':
    HandleYaml()
    # HandleYaml().file_dump(name='loginBySms_params_success', key='code', value=1)
