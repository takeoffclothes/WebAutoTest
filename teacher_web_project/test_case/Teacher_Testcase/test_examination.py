#作者：王帅 功能：可以进入五年真题、三年模拟页面
#未完善：判断是否下载功能
# 2018.08.30 优化教师导航栏导致的问题
# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest,os,sys
import random
from Constant.sys_constant import *
def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_examination(unittest.TestCase):
    def setUp(self):

        self.wd = WebDriver()
        #profile = WebDriver.firefox_profile("C:\\Users\\Administrator\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\8jbk8dci.default")
        #self.wd = WebDriver.firefox(profile)
        self.wd.implicitly_wait(60)
        wd = self.wd
        wd.get(LOGIN_URL)

    def test_01_fiveyears(self):
        success = True
        wd = self.wd
        #登录账号、密码
        wd.find_element_by_id("Phone").click()
        wd.find_element_by_id("Phone").clear()
        wd.find_element_by_id("Phone").send_keys("14600000071")
        wd.find_element_by_id("Pass").click()
        wd.find_element_by_id("Pass").clear()
        wd.find_element_by_id("Pass").send_keys("123456")
        wd.find_element_by_id("LoginBtn").click()
        time.sleep(2)
        #鼠标悬停操作
        preview = wd.find_element_by_class_name("c_Nav ")
        preview1 = preview.find_elements_by_class_name("totalnav")
        ActionChains(wd).move_to_element(preview1[1]).perform()
        time.sleep(1)
        preview2 = preview1[1].find_elements_by_class_name("menuId")
        preview2[0].click()
        time.sleep(2)
        #判断是否进入五年真题页面
        if ("五年" in wd.find_element_by_class_name("Com_Crumbs").text):
            print("进入五年真题页面成功！")
        else:
            print("进入五年真题页面失败！")
        test = wd.find_elements_by_class_name("three_test_paper_evey")
        ActionChains(wd).move_to_element(test[0]).perform()
        time.sleep(2)
        test[0].find_element_by_class_name("three_test_paper_evey_download").click()
        time.sleep(2)
        self.assertTrue(success)

    def test_02_threeyears(self):
        success = True
        wd = self.wd
        #登录账号、密码
        wd.find_element_by_id("Phone").click()
        wd.find_element_by_id("Phone").clear()
        wd.find_element_by_id("Phone").send_keys("14600000071")
        wd.find_element_by_id("Pass").click()
        wd.find_element_by_id("Pass").clear()
        wd.find_element_by_id("Pass").send_keys("123456")
        wd.find_element_by_id("LoginBtn").click()
        time.sleep(2)
        #鼠标悬停操作
        preview = wd.find_element_by_class_name("c_Nav ")
        preview1 = preview.find_elements_by_class_name("totalnav")
        ActionChains(wd).move_to_element(preview1[1]).perform()
        time.sleep(1)
        preview2 = preview1[1].find_elements_by_class_name("menuId")
        preview2[1].click()
        time.sleep(2)
        #判断是否进入三年真题页面
        if ("三年" in wd.find_element_by_class_name("Com_Crumbs").text):
            print("进入三年真题页面成功！")
        else:
            print("进入三年真题页面失败！")
        test = wd.find_elements_by_class_name("three_test_paper_evey")
        ActionChains(wd).move_to_element(test[0]).perform()
        time.sleep(2)
        test[0].find_element_by_class_name("three_test_paper_evey_download").click()
        time.sleep(2)
        self.assertTrue(success)

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()