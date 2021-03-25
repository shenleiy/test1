# coding=utf-8
"""
Created on 2021-2-25
@author:Shenlei
Project:token接口
"""
from common import Yaml_Data
import sys
from common.Request import RequestsHandler
from common import Assert
from common.Logs import Log
import os
from Conf.conf import *
from common.Retrun_Response import dict_style
from common import Consts

file = os.path.basename(sys.argv[0])
log = Log(file)
logger = log.Logger


class Token:
    @staticmethod
    def tokenGet():
        handle_yaml = Yaml_Data.HandleYaml()
        yaml_dict = handle_yaml.file_load()
        def_name = sys._getframe().f_code.co_name
        test_assert = Assert.Assertions(def_name)
        logger.info("开始执行脚本%s:\n", def_name)
        opera_url = server_ip('uat1') + yaml_dict['test_config_token']['token_url']
        # print(opera_url)

        """ 测试http://10.88.2.23:12342/app/access_token接口 """
        opera_result = RequestsHandler().post_Req(url=opera_url, json=yaml_dict['test_config_token']['token_headers'],
                                                  data=yaml_dict['test_config_token']['token_params'])
        sting_response = opera_result.content.decode()  # 返回的请求结果
        json_response = dict_style(sting_response)  # 请求结果转换为json格式
        value = (json_response['data']['accessToken'])  # 获取请求结果中的token值
        token = 'bearer ' + value
        handle_yaml.file_dump(name='headers', key='Authorization', value=token)  # 写入组合后的token值
        test_assert.assert_code(json_response['code'], yaml_dict['code'])  # 断言请求的code值
        test_assert.assert_body(json_response, 'message', yaml_dict['message'])  # 断言请求的message值
        Consts.RESULT_LIST.append('pass')  # 接口执行结果为pass


Token.tokenGet()
