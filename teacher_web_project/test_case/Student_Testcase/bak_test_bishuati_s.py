#coding=utf-8
'''
Created on 2017年8月18日
updated on 2017年8月31日
五好导学网-学生web端-天天刷题 自动化测试脚本
@author: 房立信
'''


from selenium import webdriver
import sys
sys.path.append('\PubModule')
from test_case.PubModule import login
from test_case.PubModule import logout
from test_case.PubModule import topmenu_t
#from selenium.webdriver.firefox.webdriver import WebDriver
#from selenium.webdriver.common.action_chains import ActionChains
import unittest,os
import time
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

class test_bishuati(unittest.TestCase):
    '''学生pc端-天天刷题'''
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

    def test_01_bht(self):
        '''天天刷题-必会题'''
        print u"开始测试！天天刷题-必会题"
        wd = self.wd
        success = True
        #进入必会题页面
        topmenu_t.top_menu_bht_s(self)
        
        if not ("必会题" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-必会题初始化失败")
        else:
            print(u"PASS-必会题初始化成功")
        
        wd.find_element_by_id("5e78b446069b4953b72b7ce9fd15b64a").click()
        if not ("第1课时 单项式" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-必会题目录筛选失败")
        else:
            print(u"PASS-必会题目录筛选成功")
        wd.find_element_by_id("6b5cda1e9bc542cd8adcc854b7951390").click()
        if not ("第1课时一元一次方程" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-必会题目录切换失败")
        else:
            print(u"PASS-必会题目录切换成功")
        wd.find_element_by_id("c514971d0cfb44dd9c1b69b494e607d8").click()
        if not ("【类型】解一元一次方程——合并同类项" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-必会题目录切换失败2")
        else:
            print(u"PASS-必会题目录切换成功2")
            
        self.assertTrue(success)

    def test_02_bst(self):
        '''天天刷题-必刷题'''
        print u"开始测试！天天刷题-必刷题"
        wd = self.wd
        success = True
        
        #进入必刷题页面
        topmenu_t.top_menu_bst_s(self)
        if not ("必刷题" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-必刷题页面初始化失败")
        else:
            print(u"PASS-必刷题页面初始化成功")
        #进入数学拓扑图页面
        wd.find_element_by_xpath(".//*[@id='mu_SubMain']/li[2]").click()
           
        #调用autoit程序
        os.system("D:\\selenium_upfile\\bishuati.exe")
        
        if not ("m_vsico.png" in wd.find_element_by_xpath(".//*[@id='QuestionBox']/div/div[2]/div[2]/img").get_attribute("src")):
            success = False
            print(u"FAILED-拓扑图点击拖动验证失败")
        else:
            print(u"PASS-拓扑图点击拖动验证成功！")
        
        #开始答题1，如果有题答题，没题弹出提示
        try:
            wd.find_element_by_xpath(".//*[@id='Question']/div[3]/p").click()
        except Exception,msg:
            print msg
        #开始答题2，如果有题答题，没题弹出提示
        try:
            wd.find_element_by_xpath(".//*[@id='Question']/div[3]/p").click()
        except Exception,msg:
            print msg
        #开始答题3，如果有题答题，没题弹出提示
        try:
            wd.find_element_by_xpath(".//*[@id='Question']/div[3]/p").click()
        except Exception,msg:
            print msg
        #开始答题4，如果有题答题，没题弹出提示
        try:
            wd.find_element_by_xpath(".//*[@id='Question']/div[3]/p").click()
        except Exception,msg:
            print msg
        #开始答题5，如果有题答题，没题弹出提示
        try:
            wd.find_element_by_xpath(".//*[@id='Question']/div[3]/p").click()
        except Exception,msg:
            print msg
        #开始答题6，如果有题答题，没题弹出提示
        try:
            wd.find_element_by_xpath(".//*[@id='Question']/div[3]/p").click()
        except Exception,msg:
            print msg
        #开始答题7，如果有题答题，没题弹出提示
        try:
            wd.find_element_by_xpath(".//*[@id='Question']/div[3]/p").click()
        except Exception,msg:
            print msg
        #开始答题8，如果有题答题，没题弹出提示
        try:
            wd.find_element_by_xpath(".//*[@id='Question']/div[3]/p").click()
        except Exception,msg:
            print msg
        #开始答题9，如果有题答题，没题弹出提示
        try:
            wd.find_element_by_xpath(".//*[@id='Question']/div[3]/p").click()
        except Exception,msg:
            print msg
        #开始答题10，如果有题答题，没题弹出提示
        try:
            wd.find_element_by_xpath(".//*[@id='Question']/div[3]/p").click()
        except Exception,msg:
            print msg

        if not (len(wd.find_elements_by_xpath("//p[@class='m_VsBox0']/img")) != 0):
            success = False
            print(u"FAILED-答题失败")
        else:
            print(u"PASS-答题成功！")
        
        #将滚动条移动到页面的顶部  
        js="var q=document.documentElement.scrollTop=0"  
        wd.execute_script(js)  
        time.sleep(3)  
        
        self.assertTrue(success)
    
    def tearDown(self):
        logout.logout_s(self)
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
