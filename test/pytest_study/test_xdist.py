# 并行，多线程测试
import pytest
import time


@pytest.mark.parametrize('x', list(range(10)))
# 每秒执行一个线程，共计10个
def test_somethins(x):
    time.sleep(1)

# pytest -v -s -n 5 test_xdist.py
# 5个线程同时执行
