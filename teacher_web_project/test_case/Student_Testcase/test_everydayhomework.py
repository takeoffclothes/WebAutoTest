#作者：王帅 功能：天天刷题下的必会题和必刷题页面的进入，判断
#由于必刷题用的是插件，目前未做刷题功能
# 2018.08.30 优化学生端去掉必会题导致的问题
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


class test_everyhomework(unittest.TestCase):
    def setUp(self):

        self.wd = WebDriver()
        #profile = WebDriver.firefox_profile("C:\\Users\\Administrator\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\8jbk8dci.default")
        #self.wd = WebDriver.firefox(profile)
        self.wd.implicitly_wait(60)
        wd = self.wd
        wd.get(LOGIN_URL)

    # def test_01_mustdo(self):
    #     success = True
    #     wd = self.wd
    #     #登录账号、密码
    #     wd.find_element_by_id("Phone").click()
    #     wd.find_element_by_id("Phone").clear()
    #     wd.find_element_by_id("Phone").send_keys("14600000701")
    #     wd.find_element_by_id("Pass").click()
    #     wd.find_element_by_id("Pass").clear()
    #     wd.find_element_by_id("Pass").send_keys("123456")
    #     wd.find_element_by_id("LoginBtn").click()
    #     time.sleep(2)
    #     #鼠标悬停
    #     preview = wd.find_element_by_class_name("Com_NavMain")
    #     preview1 = preview.find_elements_by_class_name("Com_Li")
    #     ActionChains(wd).move_to_element(preview1[4]).perform()
    #     time.sleep(1)
    #     preview2 = preview1[4].find_elements_by_tag_name("li")
    #     preview2[0].click()
    #     time.sleep(2)
    #     #判断进入必会题、必刷题页面是否成功
    #     if ("必会题" in wd.find_element_by_class_name("Com_Crumbs").text):
    #         print("进入必会题页面成功！")
    #     else:
    #         success = False
    #         print("进入必会题页面失败！")
    #     self.assertTrue(success)

    def test_02_mustshua(self):
        success = True
        wd = self.wd
        #登录账号、密码
        wd.find_element_by_id("Phone").click()
        wd.find_element_by_id("Phone").clear()
        wd.find_element_by_id("Phone").send_keys("14600000701")
        wd.find_element_by_id("Pass").click()
        wd.find_element_by_id("Pass").clear()
        wd.find_element_by_id("Pass").send_keys("123456")
        wd.find_element_by_id("LoginBtn").click()
        time.sleep(2)
        wd.maximize_window()
        #鼠标悬停
        preview = wd.find_element_by_class_name("Com_NavMain")
        preview1 = preview.find_elements_by_class_name("Com_Li")
        preview1[4].click()
        # ActionChains(wd).move_to_element(preview1[4]).perform()
        # time.sleep(1)
        # preview2 = preview1[4].find_elements_by_tag_name("li")
        # preview2[1].click()
        # time.sleep(2)
        #判断进入必刷题、必做题页面是否成功
        if ("必刷题" in wd.find_element_by_class_name("Com_Crumbs").text):
            print("进入必刷题页面成功！")
        else:
            success = False
            print("进入必刷题页面失败！")
        subject = wd.find_element_by_class_name("GraphBc")
        subject1 =subject.find_elements_by_class_name("sub")
        subject1[1].click()
        time.sleep(2)
        if ("数学" in wd.find_element_by_class_name("Com_Crumbs").text):
            print("进入数学学科页面成功！")
        else:
            success = False
            print("进入数学学科页面失败！")
        os.system(autoitfile_path+"bishuati.exe")
        '''
        #zuoti = wd.find_element_by_class_name("GraphSubject")
        canvas = wd.find_element_by_class_name("GraphSubject")
        ActionChains(wd).move_by_offset(212, 672).click(canvas).release().perform()
        time.sleep(5)
        '''
        self.assertTrue(success)

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()