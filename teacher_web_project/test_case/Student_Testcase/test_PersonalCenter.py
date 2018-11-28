'''
Created on 2018年1月29日
updated on 2018年2月2日
五好导学网-学生web端-个人中心 自动化测试脚本
@author: 闫双双
2018年2月25日 学生-个人中心-错题本--修改错题本切换单元方式
              学生-个人中心---修改登录调用
2018年5月17日 学生-个人中心  所有功能脚本在判断后面添加success = False语句
              学生-个人中心  修改删除题目方式
2018年7月20日 学生-个人中心  所有功能修改v1.4版本个人中心页面改版问题
              学生-个人中心  修改个人资料增加性别生日和教材问题
              学生-个人中心  修改加入班级流程问题
2018年11月19日 学生-个人中心-金币功能去掉
'''

# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest
import sys, os
from Constant.sys_constant import *
from test_case.PubModule import login,topmenu_t

def is_alert_present(wd):
    try:
        wd.switch_to.alert().text
        return True
    except:
        return False


class test_PersonalCenter(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        success = True
        wd = self.wd
        # 登录测试环境
        wd.get(LOGIN_URL)
        # self.wd.get("http://preprod-whdx.bcbook.cn")
        wd.maximize_window()

    #个人中心-上传个人头像
    def test_01PerCen_UploadPicture(self):
        print("开始测试个人中心-上传头像")
        success = True
        wd = self.wd
        # 调用login()函数登录
        login.login(self, "19600000701", "123456")
        # 判断登录是否成功
        if not ("首页" in wd.find_element_by_xpath(".//*[@id='Com_NavMain']/li[1]/a").text):
            print("FAILED-登录失败！")
            success = False
        else:
            print("SUCCESS-登录成功！")
        # 定位首页头像并点击个人中心菜单
        topmenu_t.top_menu_grzx(self)
        # 判断是否进入个人中心页面
        if not ("个人资料" in wd.find_element_by_xpath("html/body/div[3]/div/div/div[3]/a").text):
            print("FAILED-进入个人中心失败！")
            success = False
        else:
            print("SUCCESS-进入个人中心成功！")
        # 点击头像上传
        B = wd.find_element_by_id("m_UserPhoto")
        ActionChains(wd).move_to_element(B).perform()
        time.sleep(2)
        wd.find_element_by_xpath(".//*[@id='m_ChangePhoto']/i[1]").click()
        time.sleep(2)
        # 点击选择文件
        wd.find_element_by_xpath(".//*[@id='inputImage']").click()
        # 利用autoit工具上传图片
        os.system(autoitfile_path + "uploadpicture.exe")
        time.sleep(4)
        # 点击保存
        wd.find_element_by_xpath(".//*[@id='GetImgUrl']").click()
        time.sleep(1)
        # 判断保存是否成功
        if not ("保存成功" in wd.find_element_by_xpath(".//*[@id='c_ErrorMsg']").text):
            print("FAILED-头像上传失败！")
            success = False
        else:
            print("SUCCESS-头像上传成功")
        time.sleep(2)
        self.assertTrue(success)

    #个人中心-个人资料修改
    def test_02PerCen_PesonalData(self):
        print("开始测试个人中心-个人资料修改")
        success = True
        wd = self.wd
        # 调用login()函数登录
        login.login(self, "19600000701", "123456")
        # 判断登录是否成功
        if not ("首页" in wd.find_element_by_xpath(".//*[@id='Com_NavMain']/li[1]/a").text):
            print("FAILED-登录失败！")
            success = False
        else:
            print("SUCCESS-登录成功！")
        # 定位首页头像并点击个人中心菜单
        topmenu_t.top_menu_grzx(self)
        # 定位并点击个人资料
        B = wd.find_element_by_xpath("html/body/div[3]/div/div/div[3]/a")
        ActionChains(wd).move_to_element(B).perform()
        time.sleep(2)
        wd.find_element_by_xpath("html/body/div[3]/div/div/div[3]/a").click()
        # 判断是否正常进入个人资料页面
        if not ("基本资料" in wd.find_element_by_xpath("html/body/div[3]/div[1]/div[2]/span").text):
            print("FAILED-进入个人资料页面失败！")
            success = False
        else:
            print("SUCCESS-进入个人资料页面成功！")
            time.sleep(1)
        # 点击编辑
        wd.find_element_by_xpath(".//*[@id='m_Editxt']").click()
        time.sleep(2)
        # 编辑
        # 点击修改性别
        wd.find_element_by_xpath(".//*[@id='ChangeInfo']/div[1]/div").click()
        wd.find_element_by_xpath(".//*[@id='sexList']/li[2]").click()
        # 点击修改生日
        wd.find_element_by_xpath(".//*[@id='selectDate']").click()
        # 点击选择年
        wd.find_element_by_xpath(".//*[@id='ui-datepicker-div']/div/div/select[1]").click()
        wd.find_elements_by_css_selector(".ui-datepicker-year>option")[0].click()
        # 点击选择月
        wd.find_element_by_xpath(".//*[@id='ui-datepicker-div']/div/div/select[2]").click()
        wd.find_elements_by_css_selector(".ui-datepicker-month>option")[0].click()
        # 点击选择日
        wd.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[1]/td[1]/a").click()
        # 点击切换教材
        wd.find_element_by_xpath(".//*[@id='m_UserSubMat1']/li[1]/div").click()
        wd.find_element_by_xpath(".//*[@id='m_UserSubMat1']/li[1]/div/ul/li[4]").click()
        time.sleep(1)
        wd.find_element_by_xpath(".//*[@id='m_UserSubMat1']/li[2]/div").click()
        wd.find_element_by_xpath(".//*[@id='m_UserSubMat1']/li[2]/div/ul/li[9]").click()
        time.sleep(1)
        # 点击确定
        wd.find_element_by_xpath(".//*[@id='m_InfoBtn0']").click()
        time.sleep(1)
        # 判断是否编辑成功
        if not ("女" in wd.find_element_by_xpath(".//*[@id='m_UserSex0']").text):
            print("FAILED-编辑个人资料失败！")
            success = False
        else:
            print("SUCCESS-编辑个人资料成功！")
        time.sleep(3)
        self.assertTrue(success)

    '''个人中心-金币

    def test_03PerCen_GoldCoins(self):
        print("开始测试个人中心-金币")
        success = True
        wd = self.wd
        # 调用login()函数登录
        login.login(self, "19600000701", "123456")
        # 判断登录是否成功
        if not ("首页" in wd.find_element_by_xpath(".//*[@id='Com_NavMain']/li[1]/a").text):
            print("FAILED-登录失败！")
            success = False
        else:
            print("SUCCESS-登录成功！")
        # 定位并点击进入个人中心
        A = wd.find_element_by_xpath(".//*[@id='UserHeadImg']")
        ActionChains(wd).move_to_element(A).perform()
        time.sleep(3)
        wd.find_element_by_xpath(".//*[@id='Com_SignBox']/ul/li[2]/a").click()
        time.sleep(1)
        # 点击金币
        wd.find_element_by_xpath(".//*[@id='GoWealth']").click()
        time.sleep(3)
        # 判断是否进入金币页面
        if not ("金币记录" in wd.find_element_by_class_name("m_ConListTitle").text):
            print("FAILED-金币页面展示不成功！")
            success = False
        else:
            print("SUCCESS-金币页面展示成功！")
        time.sleep(3)
        self.assertTrue(success)
        '''
    '''个人中心-投稿'''

    def test_04PerCen_Contribute(self):
        print("开始测试个人中心-投稿")
        success = True
        wd = self.wd
        # 调用login()函数登录
        login.login(self, "19600000701", "123456")
        # 判断登录是否成功
        if not ("首页" in wd.find_element_by_xpath(".//*[@id='Com_NavMain']/li[1]/a").text):
            print("FAILED-登录失败！")
            success = False
        else:
            print("SUCCESS-登录成功！")
        # 定位并点击个人中心
        topmenu_t.top_menu_grzx(self)
        # 点击投稿
        wd.find_element_by_xpath("html/body/div[3]/ul/li[2]/a/img").click()
        # 点击课堂笔记上传按钮
        wd.find_element_by_xpath("html/body/div[3]/ul/li[1]/p").click()
        # 点击选择文件
        wd.find_element_by_xpath(".//*[@id='file']").click()
        # 调用文件上传
        os.system(autoitfile_path + "Classnotes.exe")
        # 点击学科
        wd.find_element_by_id("Sub").click()
        time.sleep(0.2)
        # 选择数学学科
        wd.find_element_by_xpath("//ul[@id='m_SubList']//li[.='数学']").click()
        # 点击教材
        wd.find_element_by_id("Material").click()
        # 点击人教版数学七年级上册
        wd.find_element_by_css_selector("li.m_MaterialOption").click()
        # wd.find_element_by_xpath(".//*[@id='MaterialList']/li[3]").click()
        # 点击标题并输入
        wd.find_element_by_id("m_FileTitle").click()
        wd.find_element_by_id("m_FileTitle").clear()
        wd.find_element_by_id("m_FileTitle").send_keys("测试自动化投稿")
        # 点击简介并输入
        wd.find_element_by_id("m_Intro").click()
        wd.find_element_by_id("m_Intro").clear()
        wd.find_element_by_id("m_Intro").send_keys("测试自动化投稿")
        # 点击提交按钮
        wd.find_element_by_id("m_SubMitBtn").click()
        time.sleep(1)
        # 判断是否上传成功
        if not ("上传成功" in wd.find_element_by_xpath(".//*[@id='c_ErrorMsg']").text):
            print("FAILED-上传课堂笔记失败！")
            success = False
        else:
            print("SUCCESS-上传课堂笔记成功！")
        time.sleep(3)
        # 点击知识总结上传按钮
        wd.find_element_by_xpath("html/body/div[3]/ul/li[2]/p").click()
        # 点击选择文件
        wd.find_element_by_xpath(".//*[@id='file']").click()
        # 调用文件上传
        os.system(autoitfile_path + "Knowledgesummary.exe")
        # 点击学科
        wd.find_element_by_id("Sub").click()
        # 选择数学学科
        wd.find_element_by_xpath("//ul[@id='m_SubList']//li[.='数学']").click()
        # 点击教材
        wd.find_element_by_id("Material").click()
        # 点击人教版数学七年级上册
        wd.find_element_by_css_selector("li.m_MaterialOption").click()
        # 点击标题并输入
        wd.find_element_by_id("m_FileTitle").click()
        wd.find_element_by_id("m_FileTitle").clear()
        wd.find_element_by_id("m_FileTitle").send_keys("测试自动化投稿知识总结")
        # 点击简介并输入
        wd.find_element_by_id("m_Intro").click()
        wd.find_element_by_id("m_Intro").clear()
        wd.find_element_by_id("m_Intro").send_keys("测试自动化投稿知识总结")
        # 点击提交按钮
        wd.find_element_by_id("m_SubMitBtn").click()
        time.sleep(1)
        # 判断是否上传成功
        if not ("上传成功" in wd.find_element_by_xpath(".//*[@id='c_ErrorMsg']").text):
            print("FAILED-上传知识总结失败！原因："+wd.find_element_by_xpath(".//*[@id='c_ErrorMsg']").text)

            success = False
        else:
            print("SUCCESS-上传知识总结成功！")
        time.sleep(2)
        # 点击上传列表
        wd.find_element_by_link_text("上传列表").click()

        self.assertTrue(success)

    '''个人中心-错题本'''

    def test_05PerCen_WrongTopic(self):
        print("开始测试个人中心-错题本")
        success = True
        wd = self.wd
        # 调用login()函数登录
        login.login(self, "19600000701", "123456")
        # 判断登录是否成功
        if not ("首页" in wd.find_element_by_xpath(".//*[@id='Com_NavMain']/li[1]/a").text):
            print("FAILED-登录失败！")
            success = False
        else:
            print("SUCCESS-登录成功！")
        # 定位并点击个人中心
        time.sleep(1)
        topmenu_t.top_menu_grzx(self)
        # 定位到错题本（用控制台定位到上一级ID）
        B = wd.find_element_by_id("m_WrongText")
        ActionChains(wd).move_to_element(B).perform()
        time.sleep(3)
        # 点击语文错题本
        wd.find_element_by_xpath(".//*[@id='m_UserWrong']/li[1]").click()
        time.sleep(2)
        # 判断是否正常进入语文错题本页面
        # if not("错题本"in wd.find_element_by_xpath("html/body/div[3]/div/span").text):
        # print(u"FAILED-进入语文错题本页面失败！")
        # else:
        # print("SUCCESS-进入语文错题本页面成功！")
        # 判断语文科目中是否有错题
        if ("暂无教材" in wd.find_element_by_id("Material").text):
            print("错题本中暂无数据！")
        else:
            print("错题本中有错题数据！")

            # 点击切换教材
            wd.find_element_by_id("Material").click()
            wd.find_elements_by_class_name("m_MaterialOption")[0].click()
            time.sleep(2)
            # 点击切换单元
            wd.find_element_by_xpath(".//*[@id='m_UnitList']/li[2]").click()
            time.sleep(1)
            wd.find_element_by_xpath(".//*[@id='m_UnitList']/li[3]").click()
            time.sleep(1)
            wd.find_element_by_xpath(".//*[@id='m_UnitList']/li[4]").click()
            time.sleep(1)
            wd.find_element_by_xpath(".//*[@id='m_UnitList']/li[5]").click()
            time.sleep(1)
            wd.find_element_by_xpath(".//*[@id='m_UnitList']/li[6]").click()
            time.sleep(1)
            wd.find_element_by_xpath(".//*[@id='m_UnitList']/li[7]").click()
            time.sleep(1)
            wd.find_element_by_xpath(".//*[@id='m_UnitList']/li[1]").click()
            time.sleep(2)
            # 点击第一个错题查看
            check = wd.find_elements_by_class_name("m_WrongOpBtn0")
            check[0].click()
            time.sleep(1)

            # 获取跳转到错题详情页面窗口句柄
            all_handles = wd.window_handles
            wd.switch_to.window(all_handles[1])
            # 加入try，该页面中是否存在“编辑”按钮，如果有，先点编辑，如果没有，直接继续
            try:
                wd.find_element_by_xpath(".//*[@id='m_Editxt']").click()
            except Exception:
                print("没有编辑按钮，直接点击输入框。")
            # 输入错题分析
            wd.find_element_by_xpath(".//*[@id='m_Intro']").click()
            wd.find_element_by_xpath(".//*[@id='m_Intro']").clear()
            wd.find_element_by_xpath(".//*[@id='m_Intro']").send_keys("自动化输入错题分析")
            # 点击保存
            wd.find_element_by_xpath(".//*[@id='m_SaveBtn']").click()
            time.sleep(1)
            # 判断错题分析是否保存成功
            if not ("保存成功" in wd.find_element_by_xpath(".//*[@id='c_ErrorMsg']").text):
                print("FAILED-错题分析保存失败！")
                success = False
            else:
                print("SUCCESS-错题分析保存成功！")
                time.sleep(2)
            # 刷新页面后才会出现编辑按钮
            # wd.refresh()
            # time.sleep(3)
            # 点击错题分析编辑
            wd.find_element_by_xpath(".//*[@id='m_Editxt']").click()
            # 编辑错题分析
            wd.find_element_by_xpath(".//*[@id='m_Intro']").click()
            wd.find_element_by_xpath(".//*[@id='m_Intro']").send_keys("自动化编辑错题分析")
            # 点击保存
            wd.find_element_by_xpath(".//*[@id='m_SaveBtn']").click()
            time.sleep(1)
            # 判断错题分析编辑是否保存成功
            if not ("保存成功" in wd.find_element_by_xpath(".//*[@id='c_ErrorMsg']").text):
                print("FAILED-错题分析编辑保存失败！")
                success = False
            else:
                print("SUCCESS-错题分析编辑保存成功！")
            time.sleep(2)
            # 关闭当前页面并跳转到错题本页面
            wd.close()
            wd.switch_to.window(all_handles[0])
            time.sleep(2)
            wd.maximize_window()
            # 点击全部
            wd.find_element_by_xpath(".//*[@id='Unit']").click()
            time.sleep(2)
            # 悬浮在某一题目上方
            # C = wd.find_element_by_xpath(".//*[@id='m_WrongTest']/div/div/div[1]/div/div")
            # ActionChains(wd).move_to_element(C).perform()
            # time.sleep(2)
            # 点击第一个错题删除按钮
            check = wd.find_elements_by_class_name("m_WrongOpBtn1")
            check[0].click()
            time.sleep(2)
            # 判断删除是否成功
            if not ("删除成功" in wd.find_element_by_xpath(".//*[@id='c_ErrorMsg']").text):
                print("FAILED-删除失败！")
                success = False
            else:
                print("SUCCESS-删除成功！")
            time.sleep(2)
            # 点击打印按钮
            wd.find_element_by_xpath(".//*[@id='m_PrintBtn']").click()
            time.sleep(2)
            # 点击弹出弹窗中的全部
            wd.find_element_by_xpath(".//*[@id='IsAll']").click()
            time.sleep(2)
            # 点击确定按钮
            wd.find_element_by_xpath(".//*[@id='m_UnitSelectEnsure']").click()
            time.sleep(2)
            # 获取跳转到打印预览页面窗口句柄
            all_handles = wd.window_handles
            # a = wd.current_window_handle
            # wd.switch_to.window(a)
            wd.switch_to.window(all_handles[1])
            # 判断是否成功进入打印预览页面
            if not ("确认打印" in wd.find_element_by_xpath(".//*[@id='m_PrintBtn']").text):
                print("FAILED-进入打印预览页面失败！")
                success = False
            else:
                print("SUCCESS-进入打印预览页面成功！")
            time.sleep(2)
            # 点击打印预览
            wd.find_element_by_xpath(".//*[@id='m_PrintBtn']").click()
            time.sleep(2)
            # 调用autoit处理弹窗
            os.system(autoitfile_path + "cancel.exe")
            time.sleep(2)
            wd.close()
            wd.switch_to.window(all_handles[0])

        self.assertTrue(success)

    '''个人中心-加入班级'''

    def test_06PerCen_JoinClass(self):
        print("开始测试个人中心-加入班级")
        success = True
        wd = self.wd
        wd.maximize_window()
        # 调用login()函数登录
        login.login(self, "19600000701", "123456")
        # 判断登录是否成功
        if not ("首页" in wd.find_element_by_xpath(".//*[@id='Com_NavMain']/li[1]/a").text):
            print("FAILED-登录失败！")
            success = False
        else:
            print("SUCCESS-登录成功！")
        # 定位并点击个人中心
        topmenu_t.top_menu_grzx(self)
        # 判断学生是否已经加入班级
        if not ("加入班级" in wd.find_element_by_xpath(".//*[@id='m_JoinClass']").text):
            print(u"学生已经加入班级，无需重复加入！")
            time.sleep(2)
            '''# 点击我的班级按钮
            wd.find_element_by_xpath(".//*[@id='m_JoinClass']").click()
            # 判断是否已经成功加入班级还是在申请中状态
            if not ("任课老师" in wd.find_element_by_xpath("html/body/div[3]/div[2]/div/p").text):
                print("学生还在申请中状态，执行撤销申请操作！")
                # 执行学生撤销申请操作
                # 点击撤销申请按钮
                wd.find_element_by_xpath("html/body/div[3]/div[4]/div/p[2]/a").click()
                time.sleep(2)
            else:
                print("学生已经加入班级，执行班主任删除该学生成员操作！")
                # 学生退出登录
                B = wd.find_element_by_xpath(".//*[@id='UserHeadImg']")
                ActionChains(wd).move_to_element(B).perform()
                time.sleep(3)
                wd.find_element_by_xpath(".//*[@id='Quit']").click()
                # 登录老师端删除该学生成员
                # 班主任登录
                # 调用login()函数登录
                login.login(self, "19600000071", "123456")
                # 判断登录是否成功
                if not ("首页" in wd.find_element_by_xpath(".//*[@id='Header']/header/div/nav/ul/li[1]/a").text):
                    print("FAILED-登录失败！")
                    success = False
                else:
                    print("SUCCESS-登录成功！")
                # 点击班级管理菜单
                wd.find_element_by_link_text("班级管理").click()
                time.sleep(2)
                # 点击七年级1班，进入班级详情页面
                wd.find_element_by_xpath(".//*[@id='main']/div[1]/ul/li[1]").click()
                time.sleep(1)
                # 悬浮定位更多按钮并点击删除成员
                C = wd.find_element_by_xpath(".//*[@id='info']/div[1]/div/div[1]/span[3]")
                ActionChains(wd).move_to_element(C).perform()
                time.sleep(2)
                wd.find_element_by_xpath(".//*[@id='info']/div[1]/div/div[1]/span[3]/div/ul/li[2]").click()
                # 选中学生
                wd.find_element_by_xpath(".//*[@id='info']/div[4]/div/div/ul[2]/li[1]/p[1]/img").click()
                # 点击确定按钮
                wd.find_element_by_xpath(".//*[@id='info']/div[4]/div/p[2]/button[1]").click()
                time.sleep(0.5)
                # 判断是否删除成功
                if not ("删除成功" in wd.find_element_by_xpath(".//*[@id='c_ErrorMsg']").text):
                    print("FAILED-删除学生成员失败！")
                    success = False
                else:
                    print("SUCCESS-删除学生成员成功！")
                time.sleep(2)
                # 班主任退出登录
                D = wd.find_element_by_xpath(".//*[@id='UserHeadImg']")
                ActionChains(wd).move_to_element(D).perform()
                time.sleep(3)
                wd.find_element_by_xpath(".//*[@id='menav']/li[3]/a").click()
                # 登录学生端
                # 调用login()函数登录
                login.login(self, "19600000701", "123456")
                # 判断登录是否成功
                if not ("首页" in wd.find_element_by_xpath(".//*[@id='Com_NavMain']/li[1]/a").text):
                    print("FAILED-登录失败！")
                    success = False
                else:
                    print("SUCCESS-登录成功！")
                time.sleep(2)
                # 定位并点击个人中心
                E = wd.find_element_by_xpath(".//*[@id='UserHeadImg']")
                ActionChains(wd).move_to_element(E).perform()
                time.sleep(3)
                wd.find_element_by_xpath(".//*[@id='Com_SignBox']/ul/li[2]/a").click()
                time.sleep(2)'''
        else:
            print(u"学生还未加入班级，执行加入班级操作！")
            time.sleep(2)
            # 点击加入班级按钮
            wd.find_element_by_xpath(".//*[@id='m_JoinClass']").click()
            time.sleep(2)
            # 输入六位班级码
            wd.find_element_by_xpath(".//*[@id='m_SeacherInput']").click()
            wd.find_element_by_xpath(".//*[@id='m_SeacherInput']").clear()
            wd.find_element_by_xpath(".//*[@id='m_SeacherInput']").send_keys("001896")
            # 点击搜索按钮
            wd.find_element_by_xpath(".//*[@id='m_SeacherBtn']").click()
            time.sleep(2)
            # 点击申请加入按钮
            wd.find_element_by_xpath(".//*[@id='m_Seacher']/p[2]/a").click()
            time.sleep(2)
            # 判断点击加入班级按钮是否成功
            if not ("我的班级" in wd.find_element_by_xpath(".//*[@id='m_JoinClass']").text):
                print(u"FAILED-点击加入班级按钮失败！")
                success = False
            else:
                print(u"SUCCESS-点击加入班级按钮成功！")
            time.sleep(2)

            # 学生退出登录
            F = wd.find_element_by_xpath(".//*[@id='UserHeadImg']")
            ActionChains(wd).move_to_element(F).perform()
            time.sleep(3)
            wd.find_element_by_xpath(".//*[@id='Quit']").click()

            # 班主任登录
            # 调用login()函数登录
            login.login(self, "19600000071", "123456")
            # 判断登录是否成功
            if not ("首页" in wd.find_element_by_xpath(".//*[@id='Header']/header/div/nav/ul/li[1]/a").text):
                print("FAILED-登录失败！")
                success = False
            else:
                print("SUCCESS-登录成功！")
            # 定位并点击消息
            G = wd.find_element_by_xpath(".//*[@id='UserHeadImg']")
            ActionChains(wd).move_to_element(G).perform()
            time.sleep(3)
            wd.find_element_by_xpath(".//*[@id='menav']/li[1]/a").click()
            wd.refresh()
            time.sleep(3)
            # 点击申请列表
            wd.find_element_by_xpath(".//*[@id='message']/div/span[2]").click()
            time.sleep(3)
            # 点击允许加入班级
            wd.find_element_by_xpath(".//*[@id='message']/ul/li[1]/span[4]").click()
            time.sleep(3)
            # 班主任退出登录
            H = wd.find_element_by_xpath(".//*[@id='UserHeadImg']")
            ActionChains(wd).move_to_element(H).perform()
            time.sleep(3)
            wd.find_element_by_xpath(".//*[@id='menav']/li[3]/a").click()
            # 学生登录
            # 调用login()函数登录
            login.login(self, "19600000701", "123456")
            # 判断登录是否成功
            if not ("首页" in wd.find_element_by_xpath(".//*[@id='Com_NavMain']/li[1]/a").text):
                print("FAILED-登录失败！")
                success = False
            else:
                print("SUCCESS-登录成功！")
            # 定位并点击个人中心
            I = wd.find_element_by_xpath(".//*[@id='UserHeadImg']")
            ActionChains(wd).move_to_element(I).perform()
            time.sleep(3)
            wd.find_element_by_xpath(".//*[@id='Com_SignBox']/ul/li[2]/a").click()
            # 判断是否加入班级成功
            wd.find_element_by_xpath(".//*[@id='m_JoinClass']").click()
            time.sleep(2)
            if not ("任课老师" in wd.find_element_by_xpath("html/body/div[3]/div[2]/div/p").text):
                print(u"FAILED-加入班级失败！")
                success = False
            else:
                print(u"SUCCESS-加入班级成功！")
            time.sleep(2)
        self.assertTrue(success)

    '''个人中心-班级目标'''

    def test_07PerCen_ClassGoal(self):
        print("开始测试个人中心-班级目标")
        success = True
        wd = self.wd
        # 调用login()函数登录
        login.login(self, "19600000701", "123456")
        # 判断登录是否成功
        if not ("首页" in wd.find_element_by_xpath(".//*[@id='Com_NavMain']/li[1]/a").text):
            print("FAILED-登录失败！")
            success = False
        else:
            print("SUCCESS-登录成功！")
        # 定位头像并点击个人中心
        topmenu_t.top_menu_grzx(self)
        # 点击班级目标
        wd.find_element_by_xpath(".//*[@id='GoTarget']/img").click()
        time.sleep(3)
        # 判断是否成功进入班级目标页面
        if not ("记录" in wd.find_element_by_xpath("html/body/div[3]/div[1]/a").text):
            print(u"FAILED-进入班级目标页面失败！")
            success = False
        else:
            print(u"SUCCESS-进入班级目标页面成功！")
        time.sleep(3)
        # 判断是否当月已经设定班级目标
        if (wd.find_element_by_xpath(".//*[@id='m_ClickHere']").is_displayed()):
            print(u"目前暂未设置pk目标，现在开始设置！")
            # 点击点击此处
            wd.find_element_by_xpath(".//*[@id='m_ClickHere']").click()
            time.sleep(3)
            # 点击选择班级目标
            wd.find_element_by_xpath(".//*[@id='m_TargetList']/li[2]").click()
            time.sleep(3)
            # 点击确定
            wd.find_element_by_xpath(".//*[@id='m_ChoiceBtn']").click()
            time.sleep(1)
            # 判断是否设置目标成功
            if not ("操作成功" in wd.find_element_by_xpath(".//*[@id='c_ErrorMsg']").text):
                print(u"FAILED-设置班级目标失败！")
                success = False
            else:
                print(u"SUCCESS-设置班级目标成功！")
            time.sleep(3)
        else:
            print(u"目前已有pk目标，当月不可再设置！")
        # 鼠标悬浮到对手头像
        B = wd.find_element_by_xpath(".//*[@id='PKImg']")
        ActionChains(wd).move_to_element(B).perform()
        time.sleep(2)
        # 点击更换目标
        wd.find_element_by_xpath(".//*[@id='m_ChangePkBtn']").click()
        time.sleep(2)
        # 判断本月是否可以更换或取消目标
        if not ("本月不可再次更换班级目标" in wd.find_element_by_xpath(".//*[@id='m_Surplus']/span").text):
            print(u"FAILED-本月可以更换班级目标！")
        else:
            print(u"SUCCESS-本月不可更换班级目标！")
        time.sleep(3)
        # 点击X号关闭弹窗
        wd.find_element_by_xpath(".//*[@id='m_SeacherClose']").click()
        time.sleep(2)
        # 点击记录
        wd.find_element_by_xpath("html/body/div[3]/div[1]/a").click()
        time.sleep(2)
        # 判断是否成功进入记录页面
        if not ("记录" in wd.find_element_by_xpath("html/body/div[2]/div/span").text):
            print(u"FAILED-进入记录页面失败！")
            success = False
        else:
            print(u"SUCCESS-进入记录页面成功！")
        time.sleep(3)
        # 判断是否有pk记录
        try:
            wd.find_element_by_class_name("m_VsIco").is_displayed()
            # print(wd.find_element_by_xpath(".//*[@id='m_LogBox']/div[1]/div/div[2]/img"))
            print(u"pk记录展示正常！")
        except:
            print(u"没有pk记录！")

        time.sleep(3)
        self.assertTrue(success)

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
