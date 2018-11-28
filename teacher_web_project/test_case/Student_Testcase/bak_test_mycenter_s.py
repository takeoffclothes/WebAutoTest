#coding=utf-8
'''
Created on 2017年8月21日
updated on 2017年8月31日
五好导学网-教师web端-班级管理 自动化测试脚本
@author: 房立信
'''

from selenium import webdriver
import sys
import os
sys.path.append('\PubModule')
from test_case.PubModule import login
from test_case.PubModule import logout
from test_case.PubModule import topmenu_t
#from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

class test_mycenter_s(unittest.TestCase):
    '''学生pc端-个人中心'''
    def setUp(self):
        #定义浏览器下载配置
        profile = webdriver.FirefoxProfile("C:\\Users\\Administrator\\Application Data\\Mozilla\\Firefox\\Profiles\\nce5v0dx.default")
        #定义浏览器，打开测试网站
        self.wd=webdriver.Firefox(profile)
        #self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.wd.get("http://www.wuhaodaoxue.com")
        #脚本运行时，错误的信息将被打印到这个列表中。
        self.verificationErrors = []
        #是否继续接受下一下警告
        self.accept_next_alert = True
        wd = self.wd
        #登录
        login.login(self,"17200007072", "1qaz@WSX")
        #检查是否登录成功
        if not (len(wd.find_elements_by_id("User")) != 0):
            print(u"FAILED-登录失败！")
        time.sleep(0.5)    
        #进入个人中心
        topmenu_t.top_menu_grzx_s(self)
    
    def test_01_ggtx_s(self):
        '''个人中心-更改头像'''
        print u"开始测试！个人中心-更改头像"
        wd = self.wd
        success = True

        if not ("个人中心" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-个人中心初始化失败")
        else:
            print(u"PASS-个人中心初始化成功")
        
        #这里更改头像写的比较变态，页面结构有三层，两层隐藏的元素
        #定位到第一层元素        
        article = wd.find_element_by_xpath(".//*[@id='m_Photo']")  
        #鼠标悬浮在第一层位置
        ActionChains(wd).move_to_element(article).perform()
        #定位到第二层隐藏元素        
        article = wd.find_element_by_xpath(".//*[@id='m_ChangePhoto']")  
        #鼠标悬浮在第二层位置
        ActionChains(wd).move_to_element(article).perform()
        #等待1秒
        time.sleep(1)
        #定位到改头像
        mouse = wd.find_element_by_xpath(".//*[@id='m_ChangePhoto']/i[1]")  
        #鼠标移动至改头像上方悬浮
        ActionChains(wd).move_to_element(mouse).perform()
        #更改头像
        try:
            wd.find_element_by_xpath(".//*[@id='m_ChangePhoto']/i[1]").click()
        except Exception,msg:
            print msg
        #点击选择文件
        wd.find_element_by_xpath(".//*[@id='inputImage']").click()
        #调用 upfile.exe 上传程序上传图片
        os.system("D:\\selenium_upfile\\upfile.exe")
        #点击保存头像
        wd.find_element_by_id("GetImgUrl").click()
        time.sleep(0.5)
        if not ("保存成功" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-头像更改失败")
        else:
            print(u"PASS-头像更改成功")
        
        
        self.assertTrue(success)

    def test_02_grzl_s(self):
        '''个人资料'''
        print u"开始测试！个人资料"
        wd = self.wd
        success = True
         
        #定位到个人资料上一层元素        
        article = wd.find_element_by_xpath("html/body/div[3]/div/div/div[3]")  
        #鼠标悬浮在个人资料上一层位置
        ActionChains(wd).move_to_element(article).perform()
        #等待1秒
        time.sleep(1)
        #定位到个人资料
        mouse = wd.find_element_by_xpath("html/body/div[3]/div/div/div[3]/a")  
        #鼠标移动至个人上方悬浮
        ActionChains(wd).move_to_element(mouse).perform()
        #点击个人资料
            #wd.find_element_by_link_text("个人资料").click()
        wd.find_element_by_xpath("html/body/div[3]/div/div/div[3]/a").click()
        if not ("基本资料" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-个人资料初始化失败")
        else:
            print(u"PASS-个人资料初始化成功")
        #编辑
        wd.find_element_by_id("m_Editxt").click()
        wd.find_element_by_id("m_UserName1").click()
        wd.find_element_by_id("m_UserName1").clear()
        wd.find_element_by_id("m_UserName1").send_keys(u"房学-7072号-自动化测试")
        wd.find_element_by_id("ChangeInfo").click()
        wd.find_element_by_css_selector("span.ArrowsFont.m_Downico").click()
        wd.find_element_by_xpath("//ul[@id='GradeList']//li[.='八年级']").click()
        time.sleep(1)
        #将页面滚动条拖到底部
        js="var q=document.documentElement.scrollTop=100000"
        wd.execute_script(js)
        #点击确认
        wd.find_element_by_id("m_InfoBtn0").click()
        if not ("修改成功" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-修改资料失败")
        else:
            print(u"PASS-修改资料成功")

        time.sleep(5)
        #重新登录
        #login.login(self,"17200007072", "1qaz@WSX")
        #进入个人中心
        topmenu_t.top_menu_grzx_s(self)
        #定位到个人资料上一层元素        
        article = wd.find_element_by_xpath("html/body/div[3]/div/div/div[3]")  
        #鼠标悬浮在个人资料上一层位置
        ActionChains(wd).move_to_element(article).perform()
        #等待1秒
        time.sleep(1)
        #定位到个人资料
        mouse = wd.find_element_by_xpath("html/body/div[3]/div/div/div[3]/a")  
        #鼠标移动至个人上方悬浮
        ActionChains(wd).move_to_element(mouse).perform()
        #点击个人资料
        wd.find_element_by_link_text("个人资料").click()
        wd.find_element_by_id("m_Editxt").click()
        wd.find_element_by_id("m_UserName1").click()
        wd.find_element_by_id("m_UserName1").clear()
        wd.find_element_by_id("m_UserName1").send_keys(u"房学-7072号")
        wd.find_element_by_id("Grade").click()
        wd.find_element_by_xpath("//ul[@id='GradeList']//li[.='七年级']").click()
        time.sleep(1)
        wd.find_element_by_id("m_InfoBtn0").click()
        time.sleep(5)
        
        self.assertTrue(success)

    def test_03_jrbj_s(self):
        '''加入班级'''
        print u"开始测试！加入班级"
        wd = self.wd
        success = True
         
        #定位到个人资料上一层元素        
        article = wd.find_element_by_xpath("html/body/div[3]/div/div/div[3]")  
        #鼠标悬浮在个人资料上一层位置
        ActionChains(wd).move_to_element(article).perform()
        #等待1秒
        time.sleep(1)
        #定位到个人资料
        mouse = wd.find_element_by_xpath("html/body/div[3]/div/div/div[3]/a")  
        #鼠标移动至个人上方悬浮
        ActionChains(wd).move_to_element(mouse).perform()
        #点击加入班级
        #wd.find_element_by_link_text("加入班级").click()
        wd.find_element_by_id("m_JoinClass").click()
        wd.find_element_by_id("m_SeacherInput").click()
        wd.find_element_by_id("m_SeacherInput").clear()
        wd.find_element_by_id("m_SeacherInput").send_keys("000743")
        wd.find_element_by_id("m_SeacherBtn").click()
        wd.find_element_by_id("m_JoinClassBtn0").click()
        time.sleep(0.5)
        if not ("申请已提交" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-申请加入班级失败")
        else:
            print(u"PASS-申请加入班级成功")

        #退出班级
        logout.logout_s(self)
        
        #老师登录
        login.login(self,"17200000071", "1qaz@WSX")
        #进入消息页面
        topmenu_t.top_menu_xx(self)
        time.sleep(2)
        #点击申请列表
        wd.find_element_by_id("m_Btnbg2").click()
        time.sleep(0.5)
        wd.find_element_by_css_selector("p.m_OptionYes0.EntryOperate").click()
        if not ("m_OptionicoYes.png" in wd.find_element_by_xpath("//article/div[1]/div[3]/ul[2]/li[1]/div[2]/img").get_attribute('src')):
            success = False
            print(u"FAILED-同意入班申请失败")
        else:
            print(u"PASS-同意入班申请成功！")
        #退出被申请班级老师账号
        logout.logout(self)

        #学生登录
        login.login(self,"17200007072", "1qaz@WSX")
        #进入个人中心
        topmenu_t.top_menu_grzx_s(self)
        #定位到个人资料上一层元素        
        article = wd.find_element_by_xpath("html/body/div[3]/div/div/div[3]")  
        #鼠标悬浮在个人资料上一层位置
        ActionChains(wd).move_to_element(article).perform()
        #等待1秒
        time.sleep(1)
        #定位到班级
        mouse = wd.find_element_by_xpath("html/body/div[3]/div/div/div[3]/a")  
        #鼠标移动至班级
        ActionChains(wd).move_to_element(mouse).perform()
        #点击进入班级
        wd.find_element_by_id("m_JoinClass").click()
        time.sleep(1)
        #点击退出班级
        wd.find_element_by_xpath(".//*[@id='m_QuitClassBtn']").click()
        time.sleep(1)
        #确认退出班级，页面按钮放在了隐藏元素内，捕捉不到，只能用JS方法去点击
        button=wd.find_element_by_xpath("//div[4]/div/p[2]")
        wd.execute_script("$(arguments[0]).click()",button)
        time.sleep(5)
        if not ("加入班级" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-退出班级失败")
        else:
            print(u"PASS-退出班级成功")
        
        self.assertTrue(success)

    def test_04_jb_s(self):
        '''金币'''
        print u"开始测试！金币"
        wd = self.wd
        success = True
        
        #找到按钮上层
        article = wd.find_element_by_xpath(".//*[@id='GoWealth']")  
        #鼠标移动过去
        ActionChains(wd).move_to_element(article).perform()
        #悬浮1秒钟
        time.sleep(1)
        #找到金币元素
        mouse = wd.find_element_by_xpath(".//*[@id='m_GoldIco']")  
        #鼠标移动至个人上方悬浮
        ActionChains(wd).move_to_element(mouse).perform()
        #悬停1秒
        time.sleep(1)
        #点击金币
        wd.find_element_by_id("m_GoldIco").click()
        if not ("金币记录" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-金币记录展示失败")
        else:
            print(u"PASS-金币记录展示成功")

        self.assertTrue(success)

    def test_05_tg_s(self):
        '''投稿'''
        print u"开始测试！投稿"
        wd = self.wd
        success = True
        
        #开始测试投稿
        #找到投稿上层
        article = wd.find_element_by_xpath(".//*[@id='GoWealth']")  
        #鼠标移动过去
        ActionChains(wd).move_to_element(article).perform()
        #悬浮1秒钟
        time.sleep(1)
        #找到投稿元素
        mouse = wd.find_element_by_xpath("html/body/div[3]/ul/li[2]/a")  
        #鼠标移动至投稿上方悬浮
        ActionChains(wd).move_to_element(mouse).perform()
        #悬停1秒
        time.sleep(1)
        #点击投稿
        wd.find_element_by_xpath("html/body/div[3]/ul/li[2]/a") .click()
        #点击知识总结的上传
        wd.find_element_by_xpath("html/body/div[3]/ul/li[2]/p").click()
        if not ("投稿" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-知识总结投稿页面初始化失败")
        else:
            print(u"PASS-知识总结投稿页面初始化成功")
        wd.find_element_by_id("file").click()
        #调用文件上传
        os.system("D:\\selenium_upfile\\upfile_tougao.exe")
        
        wd.find_element_by_id("Sub").click()
        wd.find_element_by_xpath("//ul[@id='m_SubList']//li[.='英语']").click()
        wd.find_element_by_id("m_FileTitle").click()
        wd.find_element_by_id("m_FileTitle").clear()
        wd.find_element_by_id("m_FileTitle").send_keys(u"自动化测试数据")
        wd.find_element_by_id("m_FileTitle").click()
        wd.find_element_by_id("m_FileTitle").clear()
        wd.find_element_by_id("m_FileTitle").send_keys(u"自动化测试数据")
        wd.find_element_by_id("m_Intro").click()
        wd.find_element_by_id("m_Intro").clear()
        wd.find_element_by_id("m_Intro").send_keys(u"自动化测试数据")
        #点击提交
        wd.find_element_by_id("m_SubMitBtn").click()
        
        if not ("上传成功" or "上传中" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-投稿失败")
        else:
            print(u"PASS-投稿成功")
       
        time.sleep(4)
        #点击学习方法的上传
        wd.find_element_by_xpath("html/body/div[3]/ul/li[1]/p").click()
        if not ("投稿" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-学习方法投稿页面初始化失败")
        else:
            print(u"PASS-学习方法投稿页面初始化成功")
        time.sleep(1)
        wd.find_element_by_id("file").click()
        #调用文件上传
        os.system("D:\\selenium_upfile\\upfile_tougao.exe")

        wd.find_element_by_css_selector("span.ArrowsFont.m_Downico").click()
        wd.find_element_by_xpath("//ul[@id='m_SubList']//li[.='数学']").click()
        wd.find_element_by_id("m_FileTitle").click()
        wd.find_element_by_id("m_FileTitle").clear()
        wd.find_element_by_id("m_FileTitle").send_keys(u"自动化测试数据2")
        wd.find_element_by_id("m_Intro").click()
        wd.find_element_by_id("m_Intro").clear()
        wd.find_element_by_id("m_Intro").send_keys(u"自动化测试数据22")
        wd.find_element_by_id("m_SubMitBtn").click()
        time.sleep(1)
        if not ("上传成功" or "上传中" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-投稿失败")
        else:
            print(u"PASS-投稿成功")
        
        #点击上传列表
        wd.find_element_by_xpath("html/body/div[3]/div[1]/a").click()
        if not ("自动化测试数据" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-上传列表展示失败")
        else:
            print(u"PASS-上传列表展示成功")

        self.assertTrue(success)
    
    def test_06_ctb_s(self):
        '''错题本'''
        print u"开始测试！错题本"
        wd = self.wd
        success = True
        
        #退出当前学生账号
        logout.logout_s(self)
        
        #登录第二个学生账号
        login.login(self,"17200007001", "1qaz@WSX")
        #进入个人中心
        topmenu_t.top_menu_grzx_s(self)
        
        time.sleep(1)
        #定位第一层隐藏元素
        article = wd.find_element_by_xpath("//div[3]/ul/li[1]")  
        #鼠标悬浮第一层隐藏
        ActionChains(wd).move_to_element(article).perform()
        #定位错题本元素
        article2 = wd.find_element_by_xpath("//div[3]/ul/li[1]/ul")  
        #鼠标悬浮错题本
        ActionChains(wd).move_to_element(article2).perform()
        time.sleep(0.5)
        if not ("语文" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-错题本悬浮后展示学科信息失败")
        #等待一秒钟
        time.sleep(1)
        #定位语文元素
        mouse = wd.find_element_by_xpath("//div[3]/ul/li[1]/ul/li[1]")  
        #悬浮语文元素
        ActionChains(wd).move_to_element(mouse).perform()
        #点击语文链接
        wd.find_element_by_xpath("//div[3]/ul/li[1]/ul/li[1]").click()
        if not ("错题本" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-语文错题本展示失败")
        else:
            print(u"PASS-语文错题本展示成功")
        time.sleep(1)
        wd.find_element_by_xpath("//ul[@id='m_UnitList']//li[.='第二单元']").click()
        if not (len(wd.find_elements_by_xpath("//div[@id='m_Nolist']/img")) != 0):
            success = False
            print(u"FAILED-错题本章节目录展示失败")
        else:
            print(u"PASS-错题本章节目录展示成功")
        wd.find_element_by_xpath("//ul[@id='m_UnitList']//li[.='第一单元']").click()
        #获取原有窗口句柄
        oldpage_handle = wd.current_window_handle
        #点击“查看”按钮，查看错题详情
        wd.find_element_by_xpath(".//*[@id='m_WrongTest']/li[1]/div[2]/a").click()
        time.sleep(1)
        all_handles = wd.window_handles
        for handle in all_handles:
            if handle != oldpage_handle:
                wd.switch_to_window(handle)
                #输入错题分析
                try:
                    wd.find_element_by_xpath(".//*[@id='m_Intro']").click()
                except Exception:
                    #print msg
                    wd.find_element_by_xpath(".//*[@id='m_Editxt']").click()
                    wd.find_element_by_xpath(".//*[@id='m_Intro']").click()
                time.sleep(0.5)
                wd.find_element_by_xpath(".//*[@id='m_Intro']").clear()
                wd.find_element_by_xpath(".//*[@id='m_Intro']").send_keys(u"自动化测试数据2")
                #保存错题分析
                wd.find_element_by_xpath(".//*[@id='m_SaveBtn']").click()
                if not ("成功" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print(u"FAILED-错题分析保存失败")
                else:
                    print(u"PASS-错题分析保存成功")

                wd.close()
                wd.switch_to_window(oldpage_handle)
        #点击打印                
        wd.find_element_by_id("m_PrintBtn").click()
        if not (len(wd.find_elements_by_xpath("//ul[@id='m_UnitSelectList']/li[2]/img")) != 0):
            success = False
            print(u"FAILED-打印弹框失败")
        else:
            print(u"PASS-打印弹框成功")
        #勾选第一单元
        wd.find_element_by_xpath("//ul[@id='m_UnitSelectList']/li[2]/img").click()
        
        #这里确定按钮上上层有一个隐藏元素
        #定位到隐藏元素        
        article = wd.find_element_by_xpath("//div[5]")  
        #鼠标悬浮在隐藏元素位置
        ActionChains(wd).move_to_element(article).perform()
        #定位到第二层隐藏元素        
        article2 = wd.find_element_by_xpath("//div[5]/div")  
        #鼠标悬浮在第二层位置
        ActionChains(wd).move_to_element(article2).perform()
        #等待1秒
        time.sleep(1)
        #定位到确定按钮
        mouse = wd.find_element_by_xpath("//div[5]/div/p[2]")  
        #鼠标移动至确定按钮上方悬浮
        ActionChains(wd).move_to_element(mouse).perform()        
        
        #点击确定按钮，页面新打开打印预览页
        wd.find_element_by_id("m_UnitSelectEnsure").click()
        time.sleep(0.5)
        all_handles = wd.window_handles
        for handle in all_handles:
            if handle != oldpage_handle:
                wd.switch_to_window(handle)
                if not ("第一单元" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print(u"FAILED-打印预览失败")
                else:
                    print(u"PASS-打印预览成功")
                #点击确定打印
                wd.find_element_by_xpath(".//*[@id='m_PrintBtn']").click()
                #调用autoit处理对话框
                os.system("D:\\selenium_upfile\\print_cancel.exe")
                wd.close()
                wd.switch_to_window(oldpage_handle)
        
        #关闭打印对话框
        #这里确定按钮上上层有一个隐藏元素
        #定位到隐藏元素        
        article = wd.find_element_by_xpath("//div[5]")  
        #鼠标悬浮在隐藏元素位置
        ActionChains(wd).move_to_element(article).perform()
        #定位到第二层隐藏元素        
        article2 = wd.find_element_by_xpath("//div[5]/div")  
        #鼠标悬浮在第二层位置
        ActionChains(wd).move_to_element(article2).perform()
        #等待1秒
        time.sleep(1)
        #定位到关闭按钮
        mouse = wd.find_element_by_xpath("//div[5]/div/img")  
        #鼠标移动至关闭按钮上方悬浮
        ActionChains(wd).move_to_element(mouse).perform()        
        #点击关闭打印对话框
        wd.find_element_by_xpath("//div[5]/div/img").click()
        
        self.assertTrue(success)
    
    def test_07_bjmb_s(self):
        '''班级目标'''
        print u"开始测试！班级目标"
        wd = self.wd
        success = True
        
        #退出当前学生账号
        logout.logout_s(self)
        
        #登录第二个学生账号
        login.login(self,"17200007001", "1qaz@WSX")
        #进入个人中心
        topmenu_t.top_menu_grzx_s(self)
       
        #开始测试班级目标
        #定位班级目标
        article2 = wd.find_element_by_xpath(".//*[@id='GoTarget']")  
        #鼠标悬浮班级目标
        ActionChains(wd).move_to_element(article2).perform()
        #等待一秒钟
        time.sleep(1)
        #定位班级目标
        mouse = wd.find_element_by_xpath(".//*[@id='GoTarget']/p[1]/span")  
        #悬浮班级目标
        ActionChains(wd).move_to_element(mouse).perform()
        #点击班级目标
        wd.find_element_by_xpath(".//*[@id='GoTarget']/p[1]/span").click()
        if not ("班级目标" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-班级目标初始化失败")
        else:
            print(u"PASS-班级目标初始化成功")
        wd.find_element_by_link_text("记录").click()
        time.sleep(1.5)
        if  "班级目标记录" == wd.title:
            print(u"PASS-PK记录页面跳转成功")
        else:
            print(u"FAILED-PK记录页面跳转失败")
        wd.find_element_by_xpath("//div[@class='m_LogUser']/i").click()
        wd.find_element_by_xpath("//div[@class='m_LogUser']/i").click()
        #点击返回班级目标
        wd.find_element_by_id("GoTarget").click()
        
        #测试更换班级目标   //div[3]/div[3]/div[1]/div/div[2]/div[1]/p[2]     //div[3]/div[3]/div[1]/div/div[2]/div[1]      //div[3]/div[3]
        #定位班级目标
        article = wd.find_element_by_xpath("//div[3]/div[3]")  
        #鼠标悬浮班级目标
        ActionChains(wd).move_to_element(article).perform()
        #等待一秒钟
        time.sleep(1)
        #定位班级目标
        article = wd.find_element_by_xpath("//div[3]/div[3]/div[1]/div/div[2]/div[1]")  
        #鼠标悬浮班级目标
        ActionChains(wd).move_to_element(article).perform()
        #等待一秒钟
        time.sleep(1)
        #定位班级目标
        mouse = wd.find_element_by_xpath("//div[3]/div[3]/div[1]/div/div[2]/div[1]/p[2]")  
        #悬浮班级目标
        ActionChains(wd).move_to_element(mouse).perform()
        #更换对手-需要细化
        wd.find_element_by_xpath("//div[3]/div[3]/div[1]/div/div[2]/div[1]/p[2]").click()

        wd.find_element_by_xpath("//ul[@id='m_TargetList']//span[.='房学-7023号']").click()
        wd.find_element_by_xpath("//ul[@id='m_TargetList']//span[.='房学-7003号']").click()

        if not ("选择班级目标" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-切换点击班级目标失败")
        else:
            print(u"PASS-切换点击班级目标成功")
        print (u"需要添加更换班级目标的脚本。涉及数据库数据还原，暂未确定保存，最后一块整理。")
        wd.find_element_by_id("m_SeacherClose").click()
        
        #退出
        self.assertTrue(success)
    
    def tearDown(self):
        logout.logout_s(self)
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
