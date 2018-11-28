#coding=utf-8
'''
Created on 2017年8月15日
updated on 2017年8月30日
updated on 2017年9月13日更改进入班级定位方法，新增老师角色是否为班主任的判断
五好导学网-教师web端-班级管理 自动化测试脚本
@author: 房立信
'''

from selenium import webdriver
import sys
#from robotide.widgets import dialog
sys.path.append('\PubModule')
from test_case.PubModule import login
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

class test_banji2(unittest.TestCase):
    '''教师pc端-班级管理模块测试2'''
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
    
    def test_01_cjxz(self):
        '''创建小组'''
        success = True
        wd = self.wd
        print u"开始测试！创建小组"

        #登录
        login.login(self,"17200000091", "1qaz@WSX")
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
        #进入九年级48班
        wd.find_element_by_xpath("//ul[@class='c_createdList']//p[.='九年级48班']/../input").click()
        if not ("九年级48班" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-班级详情页面初始化失败")
        else:
            print(u"PASS-班级详情页面初始化成功")
            
        if wd.find_element_by_xpath("html/body/div[1]/div[3]/article[1]/div[2]/div[2]/div[1]/li/i").is_displayed():
            print(u"PASS-当前老师为班主任老师")
        else:
            print(u"WARNING-当前老师非班主任，转换班主任")
            #退出当前老师
            logout.logout(self)
            #########转换班主任#######################            
            #登录9年级数学老师账号，还原测试数据
            login.login(self,'17200000092', '1qaz@WSX')
            #进入班级管理
            wd.find_element_by_link_text("班级管理").click()
            wd.find_element_by_xpath("html/body/article/div/div[4]/ul/li/input").click()
            #下面任命班主任
            #定位到任课老师头像        
            article = wd.find_element_by_xpath("html/body/div[1]/div[3]/article[1]/div[2]/div[2]/div[2]/ul/li/p[1]/img")  
            #鼠标悬浮在小组名称上方
            ActionChains(wd).move_to_element(article).perform()
            #等待1秒
            time.sleep(1)
            #定位到任命班主任按钮
            mouse = wd.find_element_by_xpath("html/body/div[1]/div[3]/article[1]/div[2]/div[2]/div[2]/ul/li/span[4]")  
            #鼠标移动至任命班主任上方悬浮
            ActionChains(wd).move_to_element(mouse).perform()
            #点击任命班主任
            wd.find_element_by_xpath("html/body/div[1]/div[3]/article[1]/div[2]/div[2]/div[2]/ul/li/span[4]").click()
            time.sleep(1)
            #确定任命班主任
            wd.find_element_by_css_selector("input.m_classAppointBtnYes").click()
            logout.logout(self)
            #重新登录
            login.login(self,"17200000091", "1qaz@WSX")
            #进入班级管理
            wd.find_element_by_xpath(".//*[@id='Header']/header/div/nav/ul/li[7]/a").click()
            #进入九年级48班
            wd.find_element_by_xpath("//ul[@class='c_createdList']//p[.='九年级48班']/../input").click()
            
        #切换小组管理标签
        wd.find_element_by_xpath("//div[@class='c_StudentAreaTab']//button[.='小组管理']").click()
        time.sleep(1)
        if not ("创建小组以便更好的布置分层作业哦！" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-当前的班级存在小组")
        else:
            print(u"PASS-切换小组管理标签成功")

        #点击创建小组
        wd.find_element_by_css_selector("img.c_classImg").click()
        time.sleep(1)
        #小组输入框输入小组名称
        wd.find_element_by_id("gourpName_ipt").click()
        wd.find_element_by_id("gourpName_ipt").clear()
        wd.find_element_by_id("gourpName_ipt").send_keys(u"自动化小组1")
        #点击添加学生
        wd.find_element_by_xpath("//div[@class='c_MainB']//span[.='添加学生']").click()
        if not ("学生名单" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-学生名单展示失败")
        else:
            print(u"PASS-学生名单展示成功")
        #选择5名学生
        wd.find_element_by_xpath("//ul[@class='c_ul']//li[.='房学-9023号']").click()
        wd.find_element_by_xpath("//ul[@class='c_ul']//li[.='房学-9022号']").click()
        wd.find_element_by_xpath("//ul[@class='c_ul']//li[.='房学-9021号']").click()
        wd.find_element_by_xpath("//ul[@class='c_ul']//li[.='房学-9020号']").click()
        wd.find_element_by_xpath("//ul[@class='c_ul']//li[.='房学-9019号']").click()
        #点击确定
        wd.find_element_by_css_selector("button.c_OkBtn").click()
        #点击保存
        wd.find_element_by_css_selector("button.c_SaveGroup").click()
        if not ("自动化小组1" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-创建小组失败")
        else:
            print(u"PASS-创建小组成功")
        
        
        #点击创建小组
        wd.find_element_by_xpath("//div[@class='c_MainAdd']/i").click()
        #小组输入框输入小组名称
        wd.find_element_by_id("gourpName_ipt").click()
        wd.find_element_by_id("gourpName_ipt").clear()
        wd.find_element_by_id("gourpName_ipt").send_keys(u"自动化小组2")
        wd.find_element_by_xpath("//li[@class='c_GrouptManageWrap']/div[2]/div[2]/div/span").click()
        wd.find_element_by_xpath("//ul[@class='c_ul']//li[.='房学-9018号']").click()
        wd.find_element_by_xpath("//ul[@class='c_ul']//li[.='房学-9017号']").click()
        wd.find_element_by_xpath("//ul[@class='c_ul']//li[.='房学-9016号']").click()
        wd.find_element_by_xpath("//ul[@class='c_ul']//li[.='房学-9015号']").click()
        wd.find_element_by_xpath("//ul[@class='c_ul']//li[.='房学-9014号']").click()
        #点击确定
        wd.find_element_by_css_selector("button.c_OkBtn").click()
        #点击取消
        wd.find_element_by_xpath("html/body/div[1]/div[3]/article[2]/div[2]/ul/li[2]/div[2]/div[2]/p/button[2]").click()
        if not ("自动化小组2" in wd.find_element_by_tag_name("html").text):
            print(u"PASS-取消创建小组成功")
        else:
            success = False
            print(u"FAILED-取消创建小组失败")
        
        
        logout.logout(self)
        self.assertTrue(success)

    def test_02_scxzxs(self):
        '''班主任身份删除小组及学生'''
        success = True
        wd = self.wd
        print u"开始测试！班主任删除小组及学生"

        #登录
        login.login(self,"17200000091", "1qaz@WSX")
        #检查是否登录成功
        if not (len(wd.find_elements_by_id("User")) != 0):
            success = False
            print(u"FAILED-登录失败！")
            
        #进入班级管理
        wd.find_element_by_xpath(".//*[@id='Header']/header/div/nav/ul/li[7]/a").click()
        if wd.title != "班级管理":
            success = False
            print(u"FAILED-班级管理列表页初始化失败")

        #进入九年级48班
        wd.find_element_by_xpath("//ul[@class='c_createdList']/li[2]/input").click()
        if not ("九年级48班" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-班级详情页面初始化失败")
        #切换小组管理标签
        wd.find_element_by_xpath("//div[@class='c_StudentAreaTab']//button[.='小组管理']").click()
        time.sleep(1)
        if not ("创建小组以便更好的布置分层作业哦！" in wd.find_element_by_tag_name("html").text):
            print(u"PASS-当前的班级存在小组")
        
        for no_stu in range(5):
        
            #下面删除小组内学生
            #定位到小组内学生        
            article = wd.find_element_by_xpath("//div[1]/div[3]/article[2]/div[2]/ul/li[2]/div[2]/div[1]/ul/li[1]")  
            #鼠标悬浮在小组内学生上方
            ActionChains(wd).move_to_element(article).perform()
            #等待1秒
            time.sleep(1)
            #定位到删除元素
            mouse = wd.find_element_by_xpath("//div[1]/div[3]/article[2]/div[2]/ul/li[2]/div[2]/div[1]/ul/li[1]/i")  
            #鼠标移动至删除元素上方悬浮
            ActionChains(wd).move_to_element(mouse).perform()
            #点击删除
            wd.find_element_by_xpath("//div[1]/div[3]/article[2]/div[2]/ul/li[2]/div[2]/div[1]/ul/li[1]/i").click()
            time.sleep(1)
            no_stu += 1
        #取消删除学生
        wd.find_element_by_css_selector("button.c_CancelGroup").click()
        if not ("房学-9019号" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-取消删除小组内学生失败")
        
        for no_stu in range(3):
            #下面删除小组内学生
            #定位到小组内学生        
            article = wd.find_element_by_xpath("//div[1]/div[3]/article[2]/div[2]/ul/li[2]/div[2]/div[1]/ul/li[1]")  
            #鼠标悬浮在小组内学生上方
            ActionChains(wd).move_to_element(article).perform()
            #等待1秒
            time.sleep(1)
            #定位到删除元素
            mouse = wd.find_element_by_xpath("//div[1]/div[3]/article[2]/div[2]/ul/li[2]/div[2]/div[1]/ul/li[1]/i")  
            #鼠标移动至删除元素上方悬浮
            ActionChains(wd).move_to_element(mouse).perform()
            #点击消息
            wd.find_element_by_xpath("//div[1]/div[3]/article[2]/div[2]/ul/li[2]/div[2]/div[1]/ul/li[1]/i").click()
            time.sleep(1)
            no_stu += 1
        #保存删除学生
        wd.find_element_by_css_selector("button.c_SaveGroup").click()
        if not ("房学-9019号" in wd.find_element_by_tag_name("html").text):
            print(u"PASS-删除小组内学生成功")
        else:
            success = False
            print(u"FAILED-删除小组内学生失败")
    
        #下面删除小组
        #定位到小组名称        
        article = wd.find_element_by_xpath("html/body/div[1]/div[3]/article[2]/div[2]/ul/li[2]/div[2]/div[1]/h3")  
        #鼠标悬浮在小组名称上方
        ActionChains(wd).move_to_element(article).perform()
        #等待1秒
        time.sleep(1)
        #定位到删除元素
        mouse = wd.find_element_by_xpath("html/body/div[1]/div[3]/article[2]/div[2]/ul/li[2]/div[2]/div[1]/i")  
        #鼠标移动至删除元素上方悬浮
        ActionChains(wd).move_to_element(mouse).perform()
        #点击删除
        wd.find_element_by_xpath("html/body/div[1]/div[3]/article[2]/div[2]/ul/li[2]/div[2]/div[1]/i").click()
        time.sleep(1)
        
        #确定删除
        wd.find_element_by_css_selector("input.m_DelGroupBtn").click()
        
        if not ("创建小组以便更好的布置分层作业哦！" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-班主任删除小组失败")
        else:
            print(u"PASS-班主任删除小组成功")
            
        
        logout.logout(self)
        self.assertTrue(success)

    def test_03_zrbzr(self):
        '''班主任转让班级'''
        success = True
        wd = self.wd
        print u"开始测试！转让班主任"

        #登录
        login.login(self,"17200000091", "1qaz@WSX")
        #检查是否登录成功
        if not (len(wd.find_elements_by_id("User")) != 0):
            success = False
            print(u"FAILED-登录失败！")
            
        #进入班级管理
        wd.find_element_by_xpath(".//*[@id='Header']/header/div/nav/ul/li[7]/a").click()
        if wd.title != "班级管理":
            success = False
            print(u"FAILED-班级管理列表页初始化失败")

        #进入九年级48班
        wd.find_element_by_xpath("//ul[@class='c_createdList']/li[2]/input").click()
        if not ("九年级48班" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-班级详情页面初始化失败")
        
        #下面任命班主任
        #定位到任课老师头像        
        article = wd.find_element_by_xpath("html/body/div[1]/div[3]/article[1]/div[2]/div[2]/div[2]/ul/li/p[1]/img")  
        #鼠标悬浮在小组名称上方
        ActionChains(wd).move_to_element(article).perform()
        #等待1秒
        time.sleep(1)
        #定位到任命班主任按钮
        mouse = wd.find_element_by_xpath("html/body/div[1]/div[3]/article[1]/div[2]/div[2]/div[2]/ul/li/span[4]")  
        #鼠标移动至任命班主任上方悬浮
        ActionChains(wd).move_to_element(mouse).perform()
        #点击任命班主任
        wd.find_element_by_xpath("html/body/div[1]/div[3]/article[1]/div[2]/div[2]/div[2]/ul/li/span[4]").click()
        time.sleep(1)
        #确定任命班主任
        wd.find_element_by_css_selector("input.m_classAppointBtnYes").click()
        if not ("设置成功" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-班主任转让班级失败")
        else:
            print(u"PASS-班主任转让班级成功")
        time.sleep(1)
        
        logout.logout(self)
        self.assertTrue(success)

    def test_04_scxzxs(self):
        '''任课老师删除小组和学生'''
        success = True
        wd = self.wd
        print u"开始测试！任课老师删除小组和学生"

        #登录
        login.login(self,"17200000091", "1qaz@WSX")
        #检查是否登录成功
        if not (len(wd.find_elements_by_id("User")) != 0):
            success = False
            print(u"FAILED-登录失败！")
            
        #进入班级管理
        wd.find_element_by_xpath(".//*[@id='Header']/header/div/nav/ul/li[7]/a").click()
        if wd.title != "班级管理":
            success = False
            print(u"FAILED-班级管理列表页初始化失败")

        #进入九年级48班
        wd.find_element_by_xpath("//ul[@class='c_createdList']/li[3]/input").click()
        if not ("九年级48班" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-班级详情页面初始化失败")
        
        #切换小组管理标签
        wd.find_element_by_xpath("//div[@class='c_StudentAreaTab']//button[.='小组管理']").click()
        #创建小组
        wd.find_element_by_css_selector("img.c_classImg").click()
        #输入小组名称
        wd.find_element_by_id("gourpName_ipt").click()
        wd.find_element_by_id("gourpName_ipt").clear()
        wd.find_element_by_id("gourpName_ipt").send_keys(u"自动化任课小组1")
        wd.find_element_by_xpath("//div[@class='c_MainB']//span[.='添加学生']").click()
        #添加小组学生，确定，保存
        wd.find_element_by_xpath("//ul[@class='c_ul']//li[.='房学-9004号']").click()
        wd.find_element_by_xpath("//ul[@class='c_ul']//li[.='房学-9005号']").click()
        wd.find_element_by_xpath("//ul[@class='c_ul']//li[.='房学-9006号']").click()
        wd.find_element_by_css_selector("button.c_OkBtn").click()
        wd.find_element_by_css_selector("button.c_SaveGroup").click()

        for no_stu in range(1):
        
            #下面删除小组内学生
            #定位到小组内学生        
            article = wd.find_element_by_xpath("//div[1]/div[3]/article[2]/div[2]/ul/li[2]/div[2]/div[1]/ul/li[1]")  
            #鼠标悬浮在小组内学生上方
            ActionChains(wd).move_to_element(article).perform()
            #等待1秒
            time.sleep(1)
            #定位到删除元素
            mouse = wd.find_element_by_xpath("//div[1]/div[3]/article[2]/div[2]/ul/li[2]/div[2]/div[1]/ul/li[1]/i")  
            #鼠标移动至删除元素上方悬浮
            ActionChains(wd).move_to_element(mouse).perform()
            #点击消息
            wd.find_element_by_xpath("//div[1]/div[3]/article[2]/div[2]/ul/li[2]/div[2]/div[1]/ul/li[1]/i").click()
            time.sleep(1)
            no_stu += 1
        #取消删除学生
        wd.find_element_by_css_selector("button.c_CancelGroup").click()
        if not ("房学-9004号" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-取消删除小组内学生失败")
        
        for no_stu in range(2):
            #下面删除小组内学生
            #定位到小组内学生        
            article = wd.find_element_by_xpath("//div[1]/div[3]/article[2]/div[2]/ul/li[2]/div[2]/div[1]/ul/li[1]")  
            #鼠标悬浮在小组内学生上方
            ActionChains(wd).move_to_element(article).perform()
            #等待1秒
            time.sleep(1)
            #定位到删除元素
            mouse = wd.find_element_by_xpath("//div[1]/div[3]/article[2]/div[2]/ul/li[2]/div[2]/div[1]/ul/li[1]/i")  
            #鼠标移动至删除元素上方悬浮
            ActionChains(wd).move_to_element(mouse).perform()
            #点击消息
            wd.find_element_by_xpath("//div[1]/div[3]/article[2]/div[2]/ul/li[2]/div[2]/div[1]/ul/li[1]/i").click()
            time.sleep(1)
            no_stu += 1
        #保存删除学生
        wd.find_element_by_css_selector("button.c_SaveGroup").click()
        if not ("房学-9004号" in wd.find_element_by_tag_name("html").text):
            print(u"PASS-删除小组内学生成功")
        else:
            success = False
            print(u"FAILED-删除小组内学生失败")

        #下面删除小组
        #定位到小组名称        
        article = wd.find_element_by_xpath("html/body/div[1]/div[3]/article[2]/div[2]/ul/li[2]/div[2]/div[1]/h3")  
        #鼠标悬浮在小组名称上方
        ActionChains(wd).move_to_element(article).perform()
        #等待1秒
        time.sleep(1)
        #定位到删除元素
        mouse = wd.find_element_by_xpath("html/body/div[1]/div[3]/article[2]/div[2]/ul/li[2]/div[2]/div[1]/i")  
        #鼠标移动至删除元素上方悬浮
        ActionChains(wd).move_to_element(mouse).perform()
        #点击删除
        wd.find_element_by_xpath("html/body/div[1]/div[3]/article[2]/div[2]/ul/li[2]/div[2]/div[1]/i").click()
        time.sleep(1)
        #确定删除        
        wd.find_element_by_xpath("html/body/div[4]/div/p/input[1]").click()
                        
        if not ("创建小组以便更" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-任课老师删除小组失败")
        else:
            print(u"PASS-任课老师删除小组成功")
        
        #退出登录
        logout.logout(self)
        
        #登录9年级数学老师账号，还原测试数据
        login.login(self,'17200000092', '1qaz@WSX')
        #进入班级管理
        wd.find_element_by_link_text("班级管理").click()
        wd.find_element_by_xpath("html/body/article/div/div[4]/ul/li/input").click()
        
        #下面任命班主任
        #定位到任课老师头像        
        article = wd.find_element_by_xpath("html/body/div[1]/div[3]/article[1]/div[2]/div[2]/div[2]/ul/li/p[1]/img")  
        #鼠标悬浮在小组名称上方
        ActionChains(wd).move_to_element(article).perform()
        #等待1秒
        time.sleep(1)
        #定位到任命班主任按钮
        mouse = wd.find_element_by_xpath("html/body/div[1]/div[3]/article[1]/div[2]/div[2]/div[2]/ul/li/span[4]")  
        #鼠标移动至任命班主任上方悬浮
        ActionChains(wd).move_to_element(mouse).perform()
        #点击任命班主任
        wd.find_element_by_xpath("html/body/div[1]/div[3]/article[1]/div[2]/div[2]/div[2]/ul/li/span[4]").click()
        time.sleep(1)
        #确定任命班主任
        wd.find_element_by_css_selector("input.m_classAppointBtnYes").click()
        
        #退出登录
        logout.logout(self)        
        self.assertTrue(success)
    
    def test_05_rklszybg(self):
        '''任课老师作业报告'''
        success = True
        wd = self.wd
        print u"开始测试！任课老师作业报告"

        #登录7年级语文老师，验证任课老师作业报告
        login.login(self,'17200000071', '1qaz@WSX')
        #进入班级管理
        wd.find_element_by_link_text("班级管理").click()
        #进入班级
        wd.find_element_by_xpath("//ul[@class='c_createdList']/li[1]/input").click()
        #进入任课老师作业页面
        wd.find_element_by_xpath("html/body/div[1]/div[3]/article[1]/div[2]/div[2]/div[2]/ul/li[1]/p[1]/img").click()
        if not ("作业提交情况" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-报告页面初始化失败")
        else:
            print(u"PASS-报告页面初始化成功")
        
        #wd.find_element_by_id("c_HomeName").click()
        #wd.find_element_by_id("cf13cc1c1f1b43cc890a152879114859").click()
        #wd.find_element_by_xpath("//div[@class='c_noSubmitNames']/i").click()
        #wd.find_element_by_xpath("//div[@class='c_noSubmitNames']/i").click()
        try:
            wd.find_element_by_id("c_HomeSelectName").click()
        except Exception:
            if (wd.find_element_by_xpath("//article/div/div[3]/div/div[2]/div[4]/div/img").is_displayed()):
                print(u"PASS-任课老师测试报告暂无数据")
            else:
                success = False
                print(u"FAILED-任课老师测试报告筛选失败")
        else:
            wd.find_element_by_xpath("//article/div/div[3]/div/div[2]/div[2]/ul/li[1]").click()
            if (wd.find_element_by_xpath("//article/div/div[3]/div/div[2]/div[4]/div/img").is_displayed()):
                print(u"PASS-任课老师测试报告暂无数据")
            else:
                if not ("平均分" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print(u"FAILED-任课老师测试报告展示失败")
                else:
                    print(u"PASS-任课老师测试报告展示成功")
        
        #退出登录
        logout.logout(self)
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
