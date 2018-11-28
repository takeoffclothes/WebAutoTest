# -*- coding: utf-8 -*-
'''
Created on 2018年2月7日
updated on 2018年8月31日  8月30号班级升级优化班级名称
五好导学网-教师web端-班级管理 自动化测试脚本
此脚本执行：
01：老师申请加入班级
02：班主任允许老师加入
03：删除老师
04：老师自己退出班级
05：转让班主任
06：分层管理模块：包括创建分层、添加层员、删除层员、解散分层
@author: 阎恩明
'''
from test_case.PubModule import login,logout,is_ele_exist
from Constant.sys_constant import *
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_ClassManage02(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)
        self.wd.get(LOGIN_URL)

    #老师申请加入班级
    def test_01JoinClass_teacher(self):
        success = True
        wd = self.wd
        print("开始测试老师加入班级")
        #登录
        login.login(self,"14200080006", "123456")
        #检查是否登录成功
        if not (len(wd.find_elements_by_id("User")) != 0):
            success = False
            print(u"FAILED-登录失败！")
        wd.find_element_by_link_text("班级管理").click()
        time.sleep(3)
        #点击加入班级
        wd.find_element_by_xpath(".//*[@id='main']/div[1]/div/span[2]").click()
        time.sleep(1)
        wd.find_element_by_css_selector("input.c_input").click()
        wd.find_element_by_css_selector("input.c_input").clear()
        wd.find_element_by_css_selector("input.c_input").send_keys("000502")
        time.sleep(1)
        wd.find_element_by_xpath(".//*[@id='main']/div[2]/div/p[2]/i").click()
        time.sleep(1)
        wd.find_element_by_class_name("c_joinBtn").click()
        time.sleep(1)
        if not ("九年级11班" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-申请加入班级失败")
        else:
            print(u"PASS-申请加入班级成功！")
        logout.logout(self)
        self.assertTrue(success)

    #班主任允许老师加入
    def test_02AllowJoin_teacher(self):
        success = True
        wd = self.wd
        print("开始测试班主任允许老师加入班级")
        #登录
        login.login(self,"14200080002", "123456")
        #检查是否登录成功
        if not (len(wd.find_elements_by_id("User")) != 0):
            success = False
            print(u"FAILED-登录失败！")
        #点击头像下拉菜单-消息
        mouse = wd.find_element_by_xpath("html/body/article/div[1]/div[1]/header/div/div/div[2]/img")
        ActionChains(wd).move_to_element(mouse).perform()
        time.sleep(2)
        wd.find_element_by_xpath("html/body/article/div[1]/div[1]/header/div/div/nav/ul/li[1]/a").click()
        if not ("消息" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-打开消息列表页失败")
        else:
            print(u"PASS-打开消息列表页成功！")
        time.sleep(2)
        #点击“申请列表”按钮
        wd.find_element_by_class_name("message_select_play").click()
        time.sleep(2)
        #点击第一行的“允许”按钮
        wd.find_element_by_xpath(".//*[@id='message']/ul/li[1]/span[4]").click()
        time.sleep(2)
        logout.logout(self)
        self.assertTrue(success)

    #删除老师
    def test_03DeleteTeacher(self):
        success = True
        wd = self.wd
        print("开始测试删除老师")
        #登录
        login.login(self,"14200080002", "123456")
        #检查是否登录成功
        if not (len(wd.find_elements_by_id("User")) != 0):
            success = False
            print(u"FAILED-登录失败！")
        #点击班级管理
        wd.find_element_by_link_text("班级管理").click()
        time.sleep(1)
        #点击进入班级按钮
        wd.find_element_by_xpath(".//*[@id='main']/div[1]/ul/li").click()
        if not ("8生物闫" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"8生物闫老师没有在此班")
        else:
            print(u"开始执行删除老师的操作")
            # 点击删除成员
            time.sleep(1)
            # 鼠标移上更多
            mouse = wd.find_element_by_xpath(".//*[@id='info']/div[1]/div/div[1]/span[3]")
            ActionChains(wd).move_to_element(mouse).perform()
            # 点击删除成员
            wd.find_element_by_xpath(".//*[@id='info']/div[1]/div/div[1]/span[3]/div/ul/li[2]").click()
            print("打开删除成员弹窗")
            time.sleep(1)
            # 选择要删除的老师
            wd.find_element_by_xpath(".//*[@id='info']/div[4]/div/div/ul[1]/li").click()
            # 点击确定
            wd.find_element_by_xpath(".//*[@id='info']/div[4]/div/p[2]/button[1]").click()
            time.sleep(2)
            if not ("8生物闫" in wd.find_element_by_tag_name("html").text):
                print(u"PASS-删除老师成功")
            else:
                success = False
                print(u"FAILED-删除老师失败！")
        logout.logout(self)
        self.assertTrue(success)

    #老师自己退出班级
    def test_04ExitClass_teacher(self):
        success = True
        wd = self.wd
        print("开始测试老师退出班级")
        #登录
        login.login(self,"14200080006", "123456")
        #检查是否登录成功
        if not (len(wd.find_elements_by_id("User")) != 0):
            success = False
            print(u"FAILED-登录失败！")
        wd.find_element_by_link_text("班级管理").click()
        time.sleep(1)
        if ("九年级11班" in wd.find_element_by_tag_name("html").text):
            print(u"已加入九年级11班，开始执行退出班级")
            #点击进入班级按钮
            wd.find_element_by_xpath(".//*[@id='main']/div[1]/ul/li").click()
            time.sleep(2)
            # 鼠标移上更多
            mouse = wd.find_element_by_xpath(".//*[@id='info']/div[1]/div/div[1]/span[3]")
            ActionChains(wd).move_to_element(mouse).perform()
            #点击退出班级
            wd.find_element_by_xpath(".//*[@id='info']/div[1]/div/div[1]/span[3]/div/ul/li").click()
            time.sleep(5)
            if ("九年级11班" in wd.find_element_by_tag_name("html").text):
                success = False
                print(u"FAILED_退出班级失败")
            else:
                print(u"PASS-退出班级成功")
        else:
            print(u"还没有加入班级，先执行申请加入班级和允许加入操作")
            print(u"第一步：先申请加入班级")
            #点击加入班级
            wd.find_element_by_xpath(".//*[@id='main']/div[1]/div/span[2]").click()
            time.sleep(1)
            wd.find_element_by_css_selector("input.c_input").click()
            wd.find_element_by_css_selector("input.c_input").clear()
            wd.find_element_by_css_selector("input.c_input").send_keys("000502")
            time.sleep(1)
            wd.find_element_by_xpath(".//*[@id='main']/div[2]/div/p[2]/i").click()
            time.sleep(1)
            wd.find_element_by_class_name("c_joinBtn").click()
            time.sleep(1)
            if not ("九年级11班" in wd.find_element_by_tag_name("html").text):
                success = False
                print(u"FAILED-申请加入班级失败")
                logout.logout(self)
            else:
                print(u"PASS-申请加入班级成功！")
                logout.logout(self)
            #调用班主任允许加入的操作
            print(u"第二步：调用班主任允许加入班级函数")
            test_ClassManage02.test_02AllowJoin_teacher(self)

            #第三步执行退出班级
            print(u"第三步：执行老师退出班级")
            login.login(self,"14200080006", "123456")
            # 检查是否登录成功
            if not (len(wd.find_elements_by_id("User")) != 0):
                success = False
                print(u"FAILED-登录失败！")
            #点击导航班级管理
            wd.find_element_by_link_text("班级管理").click()
            #点击进入班级按钮
            wd.find_element_by_xpath(".//*[@id='main']/div[1]/ul/li").click()
            time.sleep(2)
            # 鼠标移上更多
            mouse = wd.find_element_by_xpath(".//*[@id='info']/div[1]/div/div[1]/span[3]")
            ActionChains(wd).move_to_element(mouse).perform()
            #点击退出班级
            wd.find_element_by_xpath(".//*[@id='info']/div[1]/div/div[1]/span[3]/div/ul/li").click()
            time.sleep(5)
            if ("九年级11班" in wd.find_element_by_tag_name("html").text):
                success = False
                print(u"FAILED-退出班级失败")
            else:
                print(u"PASS-退出班级成功")
        logout.logout(self)
        self.assertTrue(success)

    #转让班主任
    def test_05MakeOverClassManager(self):
        success = True
        wd = self.wd
        print("开始测试转让班主任")
        login.login(self,"14200080003","123456")
        #检查是否登录成功
        if not (len(wd.find_elements_by_id("User")) != 0):
            success = False
            print(u"FAILED-登录失败！")
        # 点击导航班级管理
        wd.find_element_by_link_text("班级管理").click()
        time.sleep(3)
        #通过判断班级管理列表的班级有没有“班主任”标签，判断当前用户是否是班主任，如果是，执行转让，如果不是，执行还原数据，让原来的任课老师把权限转让回来
        tag = is_ele_exist.isElementCssExist(self,".c_isSir")
        print(tag)
        if( tag ):
            print(u"当前账号是班主任，可以转让班主任")
            # 点击进入班级按钮
            wd.find_element_by_xpath(".//*[@id='main']/div[1]/ul/li").click()
            #鼠标移上更多
            mouse=wd.find_element_by_xpath(".//*[@id='info']/div[1]/div/div[1]/span[3]")
            ActionChains(wd).move_to_element(mouse).perform()
            #点击转让班级
            time.sleep(1)
            wd.find_element_by_xpath(".//*[@id='info']/div[1]/div/div[1]/span[3]/div/ul/li[3]").click()
            time.sleep(2)
            #点击弹窗上的老师,点击确定
            wd.find_element_by_xpath(".//*[@id='info']/div[4]/div/div/ul/li").click()
            time.sleep(1)
            wd.find_element_by_xpath(".//*[@id='info']/div[4]/div/p[2]/button[1]").click()
            time.sleep(1)
            #点击班级管理，返回列表页
            wd.find_element_by_link_text("班级管理").click()
        else:
            print(u"当前账号不是班主任，没有权限")
            print(u"开始执行数据还原，新班主任把权限转让给原班主任")
            #当前账号退出登录
            logout.logout(self)
            #新班主任账号重新登录
            login.login(self,"14200080004","123456")
            #新班主任把权限转让给原班主任
            # 点击导航班级管理
            wd.find_element_by_link_text("班级管理").click()
            # 点击进入班级按钮
            wd.find_element_by_xpath(".//*[@id='main']/div[1]/ul/li").click()
            #鼠标移上更多
            mouse=wd.find_element_by_xpath(".//*[@id='info']/div[1]/div/div[1]/span[3]")
            ActionChains(wd).move_to_element(mouse).perform()
            #点击转让班级
            time.sleep(1)
            wd.find_element_by_xpath(".//*[@id='info']/div[1]/div/div[1]/span[3]/div/ul/li[3]").click()
            time.sleep(2)
            #点击弹窗上的老师,点击确定
            wd.find_element_by_xpath(".//*[@id='info']/div[4]/div/div/ul/li").click()
            time.sleep(1)
            wd.find_element_by_xpath(".//*[@id='info']/div[4]/div/p[2]/button[1]").click()
            time.sleep(1)
            #点击班级管理，返回列表页
            wd.find_element_by_link_text("班级管理").click()
            time.sleep(1)
        logout.logout(self)
        self.assertTrue(success)

    '''
        分层管理模块
        老师账号：14200080007
    '''
    #分层管理模块
    def test_06GroupManage(self):
        success = True
        wd = self.wd
        #浏览器窗口最大化
        self.wd.maximize_window()
        print("开始测试分层管理")
        login.login(self, "14200080007", "123456")
        #检查是否登录成功
        if not (len(wd.find_elements_by_id("User")) != 0):
            success = False
            print(u"FAILED-登录失败！")
        # 点击导航班级管理
        wd.find_element_by_link_text("班级管理").click()
        if not ("九年级50班" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-班级管理列表页初始化失败")
        else:
            print(u"PASS-班级管理列表页初始化成功")
        time.sleep(2)
        #点击进入班级
        wd.find_element_by_xpath(".//*[@id='main']/div[1]/ul/li").click()
        if not ("九年级50班" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-班级详情页初始化失败")
        else:
            print(u"PASS-班级详情页初始化成功")
        time.sleep(2)
        #点击分层管理
        wd.find_element_by_xpath(".//*[@id='info']/div[1]/div/div[3]/p/span[2]").click()
        time.sleep(2)
        print(u"开始测试创建分层")
        #点击创建分层
        wd.find_element_by_xpath(".//*[@id='layers']/div[1]/button").click()
        time.sleep(2)
        #输入分层名称
        wd.find_element_by_xpath(".//*[@id='create']/div[1]/input").send_keys("group1")
        time.sleep(1)
        #点击学生
        wd.find_element_by_xpath(".//*[@id='create']/div[1]/ul/li[1]").click()
        time.sleep(1)
        #点击确定按钮
        wd.find_element_by_xpath(".//*[@id='create']/div[1]/div/button").click()
        time.sleep(1)
        #点击弹窗的“知道了”
        wd.find_element_by_xpath(".//*[@id='create']/div[2]/div/div/button").click()
        time.sleep(1)

        #删除层员
        print(u"开始测试删除层员")
        #点击删除层员按钮
        wd.find_element_by_xpath(".//*[@id='layers']/div[1]/div/div[1]/ul/li[3]/p[1]").click()
        time.sleep(2)
        #点击要删除的学生
        wd.find_element_by_xpath(".//*[@id='layers']/div[3]/div/ul/li/p").click()
        #点击确定
        wd.find_element_by_xpath(".//*[@id='layers']/div[3]/div/p[2]/button[1]").click()
        time.sleep(2)

        #增加层员
        print(u"开始测试增加层员")
        #点击增加层员按钮
        wd.find_element_by_xpath(".//*[@id='layers']/div[1]/div/div[1]/ul/li[1]/p[1]").click()
        time.sleep(2)
        #点击要增加的学生
        wd.find_element_by_xpath(".//*[@id='layers']/div[3]/div/ul/li/p").click()
        #点击确定
        wd.find_element_by_xpath(".//*[@id='layers']/div[3]/div/p[2]/button[1]").click()
        time.sleep(2)

        #解散分层
        print(u"开始测试解散分层")
        #点击解散分层按钮
        wd.find_element_by_xpath(".//*[@id='layers']/div[1]/div/div[1]/p/span[2]").click()
        time.sleep(1)
        #点击弹窗的“确定”按钮
        wd.find_element_by_xpath(".//*[@id='layers']/div[2]/div/p[2]/button[1]").click()
        #退出登录
        logout.logout(self)
        self.assertTrue(success)

    def tearDown(self):
        self.wd.quit()
if __name__ == '__main__':
    unittest.main()
