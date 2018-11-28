#coding=utf-8
'''
Created on 2017年8月14日
updated on 2017年8月29日
五好导学网-教师web端-班级管理 自动化测试脚本
@author: 房立信
'''

from selenium import webdriver
import sys
#from genericpath import exists
#from robotide.widgets import dialog
sys.path.append('\PubModule')
from test_case.PubModule import login, topmenu_t
from test_case.PubModule import logout
#from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_banji1(unittest.TestCase):
    '''教师pc端-班级管理模块测试1'''
    def setUp(self):
        #定义浏览器，打开测试网站
        self.wd=webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.wd.get("http://www.wuhaodaoxue.com")
        #脚本运行时，错误的信息将被打印到这个列表中。
        self.verificationErrors = []
        #是否继续接受下一下警告
        self.accept_next_alert = True
        self.wd.maximize_window()

    
    def test_01_cjbj(self):
        '''创建班级'''
        success = True
        wd = self.wd
        print u"开始测试！创建班级"

        #登录
        login.login(self,"17200000071", "1qaz@WSX")
        #检查是否登录成功
        if not (len(wd.find_elements_by_id("User")) != 0):
            success = False
            print(u"FAILED-登录失败！")
        
        #此脚本暂时只测试有班级的情况，没有班级的情况后续脚本添加
        #进入班级管理
        wd.find_element_by_xpath(".//*[@id='Header']/header/div/nav/ul/li[7]/a").click()
        if wd.title != "班级管理":
            success = False
            print(u"FAILED-班级管理列表页初始化失败")
        else:
            print(u"PASS-班级管理列表页初始化成功！")
        #创建班级
        wd.find_element_by_xpath("html/body/article/div/div[4]/div/input[2]").click()
        if not ("7年级" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-打开创建班级对话框失败")
        else:
            print(u"PASS-打开创建班级对话框成功！")
        #勾选7班
        wd.find_element_by_xpath(".//*[@id='c_tabCon']/li[7]/i").click()
        #点击确定
        wd.find_element_by_xpath("html/body/article/div/div[6]/div[2]/input[1]").click()
        time.sleep(1)
        if not ("七年级7班" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-创建班级失败")
        else:
            print(u"PASS-创建班级成功！")
        
        logout.logout(self)
        self.assertTrue(success)

    def test_02_jsbj(self):
        '''解散班级'''
        success = True
        wd = self.wd
        print u"开始测试！解散班级"

        #登录
        login.login(self,"17200000071", "1qaz@WSX")
        #检查是否登录成功
        if not (len(wd.find_elements_by_id("User")) != 0):
            success = False
            print(u"FAILED-登录失败！")
            
        #进入班级管理
        wd.find_element_by_xpath(".//*[@id='Header']/header/div/nav/ul/li[7]/a").click()
        if wd.title != "班级管理":
            success = False
            print(u"FAILED-班级管理列表页初始化失败")

        #进入7年级7班
        wd.find_element_by_xpath("html/body/article/div/div[4]/ul/li[1]/input").click()
        if not ("七年级7班" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-班级详情页面初始化失败")
        else:
            print(u"PASS-班级详情页面初始化成功！")

        time.sleep(0.5)
        #点击更多，解散班级
        try:
            wd.find_element_by_xpath("html/body/div[1]/div[3]/article[1]/div[2]/div[1]/div").click()
        except Exception,msg:
                print msg
        time.sleep(1)
        wd.find_element_by_xpath("html/body/div[1]/div[3]/article[1]/div[2]/div[1]/div/ul/li[2]").click()
        wd.find_element_by_xpath("html/body/div[6]/div/div[1]/input").send_keys("1qaz@WSX")
        wd.find_element_by_xpath("html/body/div[6]/div/div[2]/input[1]").click()
        if not ("解散成功" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-解散班级失败")
        else:
            print(u"PASS-解散班级成功！")
        
        logout.logout(self)
        self.assertTrue(success)

    def test_03_jrbj(self):
        '''申请加入班级'''
        success = True
        wd = self.wd
        print u"开始测试！加入班级"

        #登录
        login.login(self,"17200000071", "1qaz@WSX")
        #检查是否登录成功
        if not (len(wd.find_elements_by_id("User")) != 0):
            success = False
            print(u"FAILED-登录失败！")
            
        #进入班级管理
        wd.find_element_by_xpath(".//*[@id='Header']/header/div/nav/ul/li[7]/a").click()
        if wd.title != "班级管理":
            success = False
            print(u"FAILED-班级管理列表页初始化失败")

        #加入班级
        wd.find_element_by_xpath("html/body/article/div/div[4]/div/input[1]").click()
        wd.find_element_by_xpath("html/body/article/div/div[5]/div[2]/input").send_keys("000844")
        wd.find_element_by_xpath("html/body/article/div/div[5]/div[2]/p/i").click()
        if not ("八年级44班" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-查询班级失败")
        else:
            print(u"PASS-查询班级成功！")
        time.sleep(2)
        wd.find_element_by_xpath(".//*[@id='9fb256ed52c741b2b199c608fde29b8a']").click()
        if not ("申请成功，等待通过" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-申请加入班级失败")
        else:
            print(u"PASS-申请加入班级成功！")
        
        #用户退出
        logout.logout(self)
        self.assertTrue(success)

    def test_04_tyjr(self):
        '''同意加入班级'''
        success = True
        wd = self.wd
        print u"开始测试！同意加入班级"
        
        #被申请班级班主任登录
        login.login(self,"17200000081", "1qaz@WSX")
        #检查是否登录成功
        if not (len(wd.find_elements_by_id("User")) != 0):
            success = False
            print(u"FAILED-登录失败！")
        
        #进入消息页面
        topmenu_t.top_menu_xx(self)       
        time.sleep(1)
        #点击申请列表
        wd.find_element_by_id("m_Btnbg2").click()
        if not ("申请加入44班" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-消息页面初始化失败")
        else:
            print(u"PASS-消息页面初始化成功！")
        time.sleep(1)
        wd.find_element_by_css_selector("p.m_OptionYes0.EntryOperate").click()
        if not ("m_OptionicoYes.png" in wd.find_element_by_xpath("//article/div[1]/div[3]/ul[2]/li[1]/div[2]/img").get_attribute('src')):
            success = False
            print(u"FAILED-同意入班申请失败")
        else:
            print(u"PASS-同意入班申请成功！")
            
        #退出被申请班级老师账号
        logout.logout(self)
        self.assertTrue(success)

    def test_05_tcbj(self):
        '''退出班级'''
        success = True
        wd = self.wd
        print u"开始测试！退出班级"
        
        #申请老师账号登录
        login.login(self,"17200000071", "1qaz@WSX")
        #检查是否登录成功
        if not (len(wd.find_elements_by_id("User")) != 0):
            success = False
            print(u"FAILED-登录失败！")
        
        #进入班级管理
        wd.find_element_by_xpath(".//*[@id='Header']/header/div/nav/ul/li[7]/a").click()
        if wd.title != "班级管理":
            success = False
            print(u"FAILED-班级管理列表页初始化失败")
        #进入8年级44班
        wd.find_element_by_xpath("html/body/article/div/div[4]/ul/li[4]/input").click()
        #退出班级
        wd.find_element_by_xpath("html/body/div[1]/div[3]/article[1]/div[2]/div[1]/button[1]").click()
        wd.find_element_by_xpath("html/body/div[2]/div/p/input[1]").click()
        #判断页面中是否还存在8年级44班
        if wd.title != "班级管理":
            success = False
            print (u"PASS-退出班级成功")
        else:
            print (u"FAILED-退出班级失败")
        
        #s = wd.find_element_by_xpath("html/body/article/div/div[4]/ul/li[4]/input").is_displayed()
        #if s == False:
        #    print (u"PASS-退出班级成功")
        #else:
        #    print (u"FAILED-退出班级失败")
        
        #退出被申请班级老师账号
        logout.logout(self)
        self.assertTrue(success)

    def test_06_scjsxs(self):
        '''删除教师和学生'''
        success = True
        wd = self.wd
        print u"开始测试！删除教师和学生"
        
        #申请老师账号登录
        login.login(self,"17200000071", "1qaz@WSX")
        #检查是否登录成功
        if not (len(wd.find_elements_by_id("User")) != 0):
            success = False
            print(u"FAILED-申请老师登录失败！")
        
        #进入班级管理
        wd.find_element_by_xpath(".//*[@id='Header']/header/div/nav/ul/li[7]/a").click()
        if wd.title != "班级管理":
            success = False
            print(u"FAILED-班级管理列表页初始化失败")
        
        #开始重新申请加入班级，准备测试班主任删除老师和学生
        #加入班级
        wd.find_element_by_xpath("html/body/article/div/div[4]/div/input[1]").click()
        wd.find_element_by_xpath("html/body/article/div/div[5]/div[2]/input").send_keys("000844")
        wd.find_element_by_xpath("html/body/article/div/div[5]/div[2]/p/i").click()
        time.sleep(2)
        wd.find_element_by_xpath(".//*[@id='9fb256ed52c741b2b199c608fde29b8a']").click()
        
        #用户退出
        logout.logout(self)

        #申请学生账号登录
        login.login(self,"17200008051", "1qaz@WSX")
        #检查是否登录成功
        if not (len(wd.find_elements_by_id("User")) != 0):
            success = False
            print(u"FAILED-申请学生登录失败！")
        
        #进入个人中心
        topmenu_t.top_menu_grzx_s(self)
        #加入班级
        wd.find_element_by_xpath(".//*[@id='m_JoinClass']").click()
        time.sleep(1)
        #输入班级码
        wd.find_element_by_xpath(".//*[@id='m_SeacherInput']").send_keys("000844")
        #等待2秒钟
        time.sleep(1)
        #点击搜索
        wd.find_element_by_xpath(".//*[@id='m_SeacherBtn']").click()
        #等待1秒钟
        time.sleep(1)
        #点击加入班级
        wd.find_element_by_xpath(".//*[@id='m_JoinClassBtn0']").click()
        #学生账号退出
        logout.logout_s(self)

        #被申请班级班主任登录
        login.login(self,"17200000081", "1qaz@WSX")
        #检查是否登录成功
        if not (len(wd.find_elements_by_id("User")) != 0):
            success = False
            print(u"FAILED-被申请老师登录失败！")
        
        #点击消息
        topmenu_t.top_menu_xx(self)
        time.sleep(2)
        #点击申请列表
        wd.find_element_by_id("m_Btnbg2").click()
        if not ("递交了入班申请" in wd.find_element_by_tag_name("html").text):
            success = False
            print("verifyTextPresent 学生申请消息 failed")
        wd.find_element_by_xpath(".//*[@id='EntryLIst']/li[1]/div[2]/p[1]").click()
        if not ("申请加入44班" in wd.find_element_by_tag_name("html").text):
            success = False
            print("verifyTextPresent 老师申请消息 failed")
        wd.find_element_by_xpath(".//*[@id='EntryLIst']/li[2]/div[2]/p[1]").click()
        #进入班级管理
        wd.find_element_by_xpath(".//*[@id='Header']/header/div/nav/ul/li[7]/a").click()
        #进入班级
        wd.find_element_by_xpath("html/body/article/div/div[4]/ul/li[1]/input").click()
        #定位到任课老师头像        
        article = wd.find_element_by_xpath("html/body/div[1]/div[3]/article[1]/div[2]/div[2]/div[2]/ul/li[2]/p[1]/img")  
        #鼠标悬浮再任课老师头像      
        ActionChains(wd).move_to_element(article).perform()
        #等待3秒
        time.sleep(1)
        #定位到删除元素
        mouse = wd.find_element_by_xpath("html/body/div[1]/div[3]/article[1]/div[2]/div[2]/div[2]/ul/li[2]/span[5]")  
        #鼠标移动至删除上方悬浮
        ActionChains(wd).move_to_element(mouse).perform()
        #点击删除任课老师
        wd.find_element_by_xpath("html/body/div[1]/div[3]/article[1]/div[2]/div[2]/div[2]/ul/li[2]/span[5]").click()
        time.sleep(1)
        wd.find_element_by_xpath("html/body/div[9]/div/div[2]/input[1]").click()
        if not ("删除成功" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-删除教师失败")
        else:
            print(u"PASS-删除教师成功！")
        
        
        #定位到学生信息        
        article = wd.find_element_by_xpath("html/body/div[1]/div[3]/article[2]/div[2]/ul/li[1]/ul/li[4]")  
        #鼠标悬浮在学生信息       
        ActionChains(wd).move_to_element(article).perform()
        #等待1秒
        time.sleep(1)
        #定位到删除元素
        mouse = wd.find_element_by_xpath("html/body/div[1]/div[3]/article[2]/div[2]/ul/li[1]/ul/li[4]/i")  
        #鼠标移动至删除上方悬浮
        ActionChains(wd).move_to_element(mouse).perform()
        #等待1秒
        time.sleep(1)
        #找到学生、删除
        wd.find_element_by_xpath("//div[1]/div[3]/article[2]/div[2]/ul/li[1]/ul/li[4]/i").click()
        time.sleep(0.5)
        wd.find_element_by_xpath("//input[@class='m_DelBtn']").click()
        time.sleep(0.5)
        if not("房学-8055号" in wd.find_element_by_tag_name("html").text):
            print(u"PASS-删除学生成功！")
        else:
            success = False
            print(u"FAILED-删除学生失败")

        #退出被申请班级老师账号
        logout.logout(self)
        self.assertTrue(success)
    '''
    def test_07_yqjrbj(self):
        ''''''邀请加入班级''''''
        success = True
        wd = self.wd
        print u"开始测试！邀请加入班级"
        
        #申请老师账号登录
        login.login(self,"17200000071", "1qaz@WSX")
        #检查是否登录成功
        if not (len(wd.find_elements_by_id("User")) != 0):
            success = False
            print(u"FAILED-登录失败！")
        
        #进入班级管理
        wd.find_element_by_xpath(".//*[@id='Header']/header/div/nav/ul/li[7]/a").click()
        if wd.title != "班级管理":
            success = False
            print(u"FAILED-班级管理列表页初始化失败")
        
        
        #开始测试邀请
        #进入7年级41班
        wd.find_element_by_xpath("html/body/article/div/div[4]/ul/li[1]/input").click()
        time.sleep(0.5)
        #点击邀请
        wd.find_element_by_xpath("html/body/div[1]/div[3]/article[1]/div[2]/div[1]/button[2]").click()
        time.sleep(0.5)
        
        #鼠标悬浮
        #定位到第一层隐藏元素        
        article = wd.find_element_by_xpath(".//div[11]")  
        #鼠标悬浮在第一层隐藏元素上方
        ActionChains(wd).move_to_element(article).perform()
        #等待1秒
        time.sleep(1)
        #定位到第二层隐藏元素        
        article2 = wd.find_element_by_xpath(".//div[11]/object")  
        #鼠标悬浮在第二层隐藏元素上方
        ActionChains(wd).move_to_element(article2).perform()
        #等待1秒
        time.sleep(1)
#！！！邀请这里应该加入确认邀请信息是否正确的用例。后续补充。
        #定位到复制元素
        mouse = wd.find_element_by_xpath(".//div[11]/object/embed")  
        #鼠标移动至复制元素上方悬浮
        ActionChains(wd).move_to_element(mouse).perform()
        #点击复制
        wd.find_element_by_xpath("//object[@id='global-zeroclipboard-flash-bridge']/embed").click()
        
        if not ("复制成功" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-复制邀请失败")
        else:
            print(u"PASS-复制邀请成功！")
        
        #退出登录账号
        logout.logout(self)
        self.assertTrue(success)
    '''
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
