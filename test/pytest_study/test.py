#!/usr/bin/env python
# -*-coding:utf-8 -*-
import pytest
import requests
import time
import logging


def test_get_page_baidu(url='http://www.baidu.com/'):
    r = requests.get(url=url)
    assert r.status_code == 200


def test_get_page_taobao(url='http://www.taobao.com/'):
    r = requests.get(url=url)
    assert r.status_code == 200


def test_get_page_qq(url='http://www.qq.com/'):
    r = requests.get(url=url)
    assert r.status_code == 200


@pytest.mark.login
def test_login_001():
    log = logging.getLogger('test_1')
    time.sleep(1)
    log.debug('after 1 sec')
    time.sleep(1)
    log.debug('after 2 sec')
    time.sleep(1)
    log.debug('after 3 sec')
    assert 1, 'should pass'


@pytest.mark.login
def test_login_002():
    log = logging.getLogger('test_2')
    time.sleep(1)
    log.debug('after 1 sec')
    time.sleep(1)
    log.debug('after 2 sec')
    time.sleep(1)
    log.debug('after 3 sec')
    assert 0, 'failing for demo purposes'


@pytest.mark.skip(reason='忽略执行该测试用例')
def test_login_003():
    pass
