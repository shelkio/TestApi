import time
import unittest
import sys

class Demo_API(unittest.TestCase):
    """接口测试"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_th1(self):
        "1213123123"
        print("******* 正在执行用例 ->{0} *********".format("123"))

if __name__=='__main__':
    Demo_API.test_th1()