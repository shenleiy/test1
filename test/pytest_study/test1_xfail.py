import pytest


class Test_Pytest():

    @pytest.mark.xfail
    # 期望测试用例是失败的，但是不会影响测试用例的的执行。如果测试用例执行失败的则结果是xfail（不会额外显示出错误信息）；
    # 如果测试用例执行成功的则结果是xpass。
    def test_one(self):
        print("test_one方法执行")
        assert 1 == 1

    def test_two(self):
        print("test_two方法执行")
        assert "o" in "love"

    def test_three(self):
        print("test_three方法执行")
        assert 3 - 2 == 1


if __name__ == "__main__":
    pytest.main(['-s', 'test1_xfail.py'])
