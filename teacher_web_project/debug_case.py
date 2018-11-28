# -*- coding: utf-8 -*-
'''
Created on 2018年01月29日
自动化测试——调试用例文件
@author: 房立信
'''

import unittest
from Function.sys_function import *

# 用例
class Case_02(unittest.TestCase):
    u'''哇塞好玩'''
    def setUp(self):
        pass

    def test_zzk(self):
        u'''输入哇塞好玩后点击找找看'''
        search("哇塞好玩")
        print('打印方法名：test_zzk')

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()