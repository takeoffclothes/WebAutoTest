# -*- coding: utf-8 -*-
'''
Created on 2018年2月6日
updated on 2018年8月31日   8月30号班级升级优化班级名称
五好导学网-教师web端-班级管理 自动化测试脚本
此脚本执行：
01:创建班级
02：解散班级
03：学生申请加入班级
04：拒绝学生加入班级
05：学生端验证是否拒绝成功
06：允许学生加入班级
07：学生端验证加入班级成功
08：老师删除学生
09：学生撤销申请
@author: 阎恩明
'''
from test_case.PubModule import login,logout
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

class test_ClassManage01(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)
        self.wd.get(LOGIN_URL)
    #创建班级
    def test_01CreatClass(self):
        success = True
        wd = self.wd
        #登录
        login.login(self,"14200080001", "123456")
        #检查是否登录成功
        if not (len(wd.find_elements_by_id("User")) != 0):
            success = False
            print(u"FAILED-登录失败！")
        #创建班级
        time.sleep(2)
        print (u"开始测试！创建班级")
        wd.find_element_by_link_text("班级管理").click()
        time.sleep(1)
        #当前状态没有班级，点击创建班级
        if not ("八年级2班" in wd.find_element_by_tag_name("html").text):
            wd.find_element_by_xpath(".//*[@id='main']/div[1]/div/span[1]").click()
            time.sleep(2)
            if not ("当前还可创建" in wd.find_element_by_class_name("c_cue").text):
                success = False
                print(u"FAILED-打开创建班级页面失败")
            else:
                print(u"PASS-打开创建班级页面成功！")
                time.sleep(1)
                #点击八年级
                wd.find_element_by_xpath(".//*[@id='main']/div/ul[1]/li[2]").click()
                time.sleep(2)
                #点击2班
                wd.find_element_by_xpath(".//*[@id='c_classes']/li[2]").click()
                time.sleep(1)
                #点击下一步
                wd.find_element_by_xpath(".//*[@id='test_tree_list_dummy']").click()
                time.sleep(1)
                #选择年份
                print("选择班级年份2016")
                time.sleep(1)
                wd.find_elements_by_css_selector(".dw-bf>div")[1].click()
                wd.find_elements_by_css_selector(".dw-bf>div")[2].click()
                wd.find_elements_by_css_selector(".dw-bf>div")[3].click()
                time.sleep(1)
                wd.find_element_by_css_selector(".dwb-s>span").click()
                time.sleep(4)
                print("创建完了")
                if not ("八年级2班" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print(u"FAILED-创建班级失败")
                else:
                    print(u"PASS-八年级2班创建成功！")
                logout.logout(self)
        else:
            print("已创建过八年级2班，执行下一步解散班级")
            logout.logout(self)
        self.assertTrue(success)

    #解散班级
    def test_02DissolveClass(self):
        success = True
        wd = self.wd
        login.login(self, "14200080001", "123456")
        # 检查是否登录成功
        if not (len(wd.find_elements_by_id("User")) != 0):
            success = False
            print(u"FAILED-登录失败！")
        print(u"开始测试解散班级")
        #点击导航的班级管理
        time.sleep(1)
        wd.find_element_by_link_text("班级管理").click()
        time.sleep(1)
        #点击进入班级
        wd.find_element_by_xpath(".//*[@id='main']/div[1]/ul/li").click()
        time.sleep(1)
        #鼠标移动到更多
        mouse=wd.find_element_by_xpath(".//*[@id='info']/div[1]/div/div[1]/span[3]")
        ActionChains(wd).move_to_element(mouse).perform()
        time.sleep(1)
        #点击解散班级
        wd.find_element_by_xpath(".//*[@id='info']/div[1]/div/div[1]/span[3]/div/ul/li[2]").click()
        time.sleep(2)
        print("输入解散班级登录密码")
        wd.find_element_by_xpath(".//*[@id='info']/div[3]/div/div/input").click()
        wd.find_element_by_xpath(".//*[@id='info']/div[3]/div/div/input").clear()
        wd.find_element_by_xpath(".//*[@id='info']/div[3]/div/div/input").send_keys("123456")
        time.sleep(3)
        wd.find_element_by_xpath(".//*[@id='info']/div[3]/div/p[2]/button[1]").click()
        time.sleep(2)
        if not ("八年级2班" in wd.find_element_by_tag_name("html").text):
            print(u"PASS-解散班级成功！")
        else:
            success = False
            print(u"FAILED-解散班级失败")
        time.sleep(2)
        logout.logout(self)
        self.assertTrue(success)

    #学生申请加入班级
    def test_03JoinClass_student(self):
        success = True
        wd = self.wd
        print("开始测试学生申请加入班级")
        #登录
        login.login(self,"19100080001", "123456")
        #检查是否登录成功
        if not (len(wd.find_elements_by_id("User")) != 0):
            success = False
            print(u"FAILED-登录失败！")
        #进入个人中心
        mouse=wd.find_element_by_xpath("html/body/div[1]/div/div/div[1]/div[2]/img")
        ActionChains(wd).move_to_element(mouse).perform()
        time.sleep(2)
        wd.find_element_by_xpath("html/body/div[1]/div/div/div[1]/ul/li[2]/a").click()
        if not ("个人中心" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-打开个人中心失败")
        else:
            print(u"PASS-打开个人中心成功！")
            time.sleep(1)
        if not ("加入班级" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"你已加入班级")
            logout.logout_s(self)
            return
        else:
            time.sleep(1)
        #点击加入班级
            wd.find_element_by_id("m_JoinClass").click()
            time.sleep(1)
            wd.find_element_by_id("m_SeacherInput").click()
            wd.find_element_by_id("m_SeacherInput").clear()
            wd.find_element_by_id("m_SeacherInput").send_keys("000502")
            time.sleep(1)
            wd.find_element_by_id("m_SeacherBtn").click()
            time.sleep(1)
            if not ("11班" in wd.find_element_by_tag_name("html").text):
                success = False
                print(u"FAILED-未查到要加入的班级")
            else:
                print(u"PASS-查到要加入的班级！")
                wd.find_element_by_class_name("applyJoinBtn").click()
                if not ("我的班级" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print(u"FAILED-申请加入失败")
                else:
                    print(u"PASS-申请加入成功！")
        logout.logout_s(self)
        self.assertTrue(success)

    #拒绝学生加入班级
    def test_04DeclineJoin_student(self):
        success = True
        wd = self.wd
        print("开始测试老师拒绝学生加入班级")
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
        #点击第一行的“拒绝”按钮
        wd.find_element_by_xpath(".//*[@id='message']/ul/li[1]/span[5]").click()
        time.sleep(2)
        print("已拒绝，请去学生端验证")
        #老师退出
        logout.logout(self)
        self.assertTrue(success)

    #去学生端验证是否拒绝成功
    def test_05VerifyDecline_student(self):
        success = True
        wd = self.wd
        print("开始测试学生加入班级")
        #登录
        login.login(self,"19100080001", "123456")
        #检查是否登录成功
        if not (len(wd.find_elements_by_id("User")) != 0):
            success = False
            print(u"FAILED-登录失败！")
        #进入个人中心
        mouse=wd.find_element_by_xpath("html/body/div[1]/div/div/div[1]/div[2]/img")
        ActionChains(wd).move_to_element(mouse).perform()
        time.sleep(2)
        wd.find_element_by_xpath("html/body/div[1]/div/div/div[1]/ul/li[2]/a").click()
        if not ("个人中心" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-打开个人中心失败")
        else:
            print(u"PASS-打开个人中心成功！")
            time.sleep(1)
        if not ("加入班级" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-老师拒绝加入班级失败")
        else:
            print(u"PASS-老师拒绝加入班级成功！")
        logout.logout_s(self)
        self.assertTrue(success)

    #允许学生加入班级
    def test_06AllowJoin_student(self):
        #先引用学生申请加入班级
        test_ClassManage01.test_03JoinClass_student(self)
        success = True
        wd = self.wd
        print("开始测试老师允许学生加入班级")
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
        print("已允许，请去学生端验证")
        #老师退出
        logout.logout(self)
        self.assertTrue(success)

    #去学生端验证加入班级成功
    def test_07VerifyAllow_student(self):
        success = True
        wd = self.wd
        print("开始验证学生加入班级成功")
        #登录
        login.login(self,"19100080001", "123456")
        #检查是否登录成功
        if not (len(wd.find_elements_by_id("User")) != 0):
            success = False
            print(u"FAILED-登录失败！")
        #进入个人中心
        mouse=wd.find_element_by_xpath("html/body/div[1]/div/div/div[1]/div[2]/img")
        ActionChains(wd).move_to_element(mouse).perform()
        time.sleep(2)
        wd.find_element_by_xpath("html/body/div[1]/div/div/div[1]/ul/li[2]/a").click()
        if not ("个人中心" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-打开个人中心失败")
        else:
            print(u"PASS-打开个人中心成功！")
            time.sleep(1)
        wd.find_element_by_xpath(".//*[@id='m_JoinClass']").click()
        time.sleep(1)
        if not ("000502" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-老师允许加入班级失败")
        else:
            print(u"PASS-老师允许加入班级成功！")
        time.sleep(2)
        logout.logout_s(self)
        self.assertTrue(success)

    #老师删除学生
    def test_08DeleteStudent(self):
        #下面是老师删除学生
        success = True
        wd = self.wd
        print("开始执行老师删除学生")
        #登录
        login.login(self,"14200080002", "123456")
        #检查是否登录成功
        if not (len(wd.find_elements_by_id("User")) != 0):
            success = False
            print(u"FAILED-登录失败！")
        #点击导航班级管理
        time.sleep(1)
        wd.find_element_by_link_text("班级管理").click()
        if not ("九年级11班" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-打开班级列表页失败")
        else:
            print(u"PASS-打开班级列表页成功！")
        #点击进入班级
        time.sleep(1)
        wd.find_element_by_xpath(".//*[@id='main']/div[1]/ul/li").click()
        if not ("学生成员" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-打开详情页失败")
        else:
            print(u"PASS-打开班级详情页成功！")
        #点击删除成员
        time.sleep(1)
        #鼠标移上更多
        mouse=wd.find_element_by_xpath(".//*[@id='info']/div[1]/div/div[1]/span[3]")
        ActionChains(wd).move_to_element(mouse).perform()
        #点击删除成员
        wd.find_element_by_xpath(".//*[@id='info']/div[1]/div/div[1]/span[3]/div/ul/li[2]").click()
        print("打开删除成员弹窗")
        time.sleep(1)
        # 选择要删除的学生
        wd.find_element_by_xpath(".//*[@id='info']/div[4]/div/div/ul[2]/li").click()
        #点击确定
        wd.find_element_by_xpath(".//*[@id='info']/div[4]/div/p[2]/button[1]").click()
        time.sleep(1)
        if not ("8小一" in wd.find_element_by_tag_name("html").text):
            print(u"PASS-删除学生成功")
        else:
            success = False
            print(u"FAILED-删除学生失败！")
        logout.logout(self)
        self.assertTrue(success)

    #学生撤销申请
    def test_09JoinClass_student(self):
        success = True
        wd = self.wd
        print("开始测试学生撤销申请")
        #登录
        login.login(self,"19100080001", "123456")
        #检查是否登录成功
        if not (len(wd.find_elements_by_id("User")) != 0):
            success = False
            print(u"FAILED-登录失败！")
        #进入个人中心
        mouse=wd.find_element_by_xpath("html/body/div[1]/div/div/div[1]/div[2]/img")
        ActionChains(wd).move_to_element(mouse).perform()
        time.sleep(2)
        wd.find_element_by_xpath("html/body/div[1]/div/div/div[1]/ul/li[2]/a").click()
        if not ("个人中心" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-打开个人中心失败")
        else:
            print(u"PASS-打开个人中心成功！")
            time.sleep(1)
        if not ("加入班级" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"你已加入班级")
            logout.logout_s(self)
            return
        else:
            time.sleep(1)
        #点击加入班级
            wd.find_element_by_id("m_JoinClass").click()
            time.sleep(1)
            wd.find_element_by_id("m_SeacherInput").click()
            wd.find_element_by_id("m_SeacherInput").clear()
            wd.find_element_by_id("m_SeacherInput").send_keys("000502")
            time.sleep(1)
            wd.find_element_by_id("m_SeacherBtn").click()
            time.sleep(1)
            if not ("11班" in wd.find_element_by_tag_name("html").text):
                success = False
                print(u"FAILED-未查到要加入的班级")
            else:
                print(u"PASS-查到要加入的班级！")
                wd.find_element_by_class_name("applyJoinBtn").click()
                if not ("我的班级" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print(u"FAILED-申请加入失败")
                else:
                    print(u"PASS-申请加入成功！")
                    #点击我的班级
                    wd.find_element_by_xpath(".//*[@id='m_JoinClass']").click()
                    time.sleep(2)
                    #点击撤销申请
                    wd.find_element_by_class_name("revokeApplyBtn").click()
                    time.sleep(1)
                    if not ("加入班级" in wd.find_element_by_tag_name("html").text):
                        success = False
                        print(u"撤销申请失败")
        logout.logout_s(self)
        self.assertTrue(success)

    def tearDown(self):
        self.wd.quit()
if __name__ == '__main__':
    unittest.main()
