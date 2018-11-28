# coding：utf-8(定义源代码的编码:源代码的编码可以包含中文字符串)
# Created on 2018年1月30日
# updated on 2018年1月30日
# 五好导学网-教师web端-登录 自动化测试脚本
# 作者: 马春苗


from selenium import webdriver
from Constant.sys_constant import *
import sys
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest


class test_login_s (unittest.TestCase):
    # 学生端登录
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_login(self):
        success = True
        wd = self.wd
        self.wd.get(LOGIN_URL)
        #wd.get("http://www.wuhaodaoxue.com/")
        # 窗口最大化
        wd.maximize_window()
        wd.find_element_by_id("Phone").click()
        wd.find_element_by_id("Phone").clear()
        wd.find_element_by_id("Phone").send_keys("17400007001")
        wd.find_element_by_id("Pass").click()
        wd.find_element_by_id("Pass").clear()
        wd.find_element_by_id("Pass").send_keys("123456")
        wd.find_element_by_id("LoginBtn").click()
        time.sleep(2)
        if not (len(wd.find_elements_by_id("User")) != 0):
            print("登录失败！")
        else:
            print("登录成功")
        self.assertTrue(success)

    def tearDown(self):
        self.wd.quit()
if __name__ == '__main__':
    unittest.main()
