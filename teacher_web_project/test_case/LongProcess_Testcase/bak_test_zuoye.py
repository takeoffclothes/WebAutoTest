#coding=utf-8
'''
Created on 2017年9月5-7日
五好导学网-长流程-作业 自动化测试脚本
@author: 房立信
'''

from selenium import webdriver
import sys
sys.path.append('\PubModule')
from test_case.PubModule import login
from test_case.PubModule import logout
from test_case.PubModule import topmenu_t
#from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest,os
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

class test_zuoye(unittest.TestCase):
    '''长流程测试-作业'''
    ASSIGN_TIME = "hallo"
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
    
    def test_zuoye_01_bzzy(self):
        '''作业长流程-布置作业'''
        print u"开始测试！作业长流程-布置作业"
        wd = self.wd
        success = True
        #登录
        login.login(self,"17200000083", "1qaz@WSX")
        #检查是否登录成功
        if not (len(wd.find_elements_by_id("User")) != 0):
            success = False
            print(u"FAILED-教师登录失败！")
        else:
            print(u"PASS-教师登录成功！")
        
        time.sleep(0.5)
        #进入布置作业
        topmenu_t.top_menu_bzzy(self)
        #切换章节目录
        wd.find_element_by_xpath("//article/div/div[3]/div/div[1]/dl[1]/dd/ul/li[2]").click()
        wd.find_element_by_xpath("//article/div/div[3]/div/div[1]/dl[2]/dd/ul/li[2]").click()
        wd.find_element_by_xpath("//article/div/div[3]/div/div[1]/dl[3]/dd/ul/li[2]").click()
        #点击课时练
        wd.find_element_by_xpath("//div[@class='h_Type_ul']/div/div[1]/a/img").click()
        if not ("Unit 2 Section B (2a-2e)" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-课时练初始化失败！")
        else:
            print(u"PASS-课时练初始化成功！")

        #定位到题目元素        
        article = wd.find_element_by_xpath("html/body/article/div/div[4]/div/div[2]/ul/li[2]/ul/li[1]/div[1]")  
        #鼠标悬浮在题目位置
        ActionChains(wd).move_to_element(article).perform()
        #等待1秒
        time.sleep(1)
        #定位到查看解析
        mouse = wd.find_element_by_xpath("html/body/article/div/div[4]/div/div[2]/ul/li[2]/ul/li[1]/div[1]/div/span")  
        #鼠标移动至查看解析上方悬浮
        ActionChains(wd).move_to_element(mouse).perform()
        
        #查看解析展开/收起
        wd.find_element_by_xpath("html/body/article/div/div[4]/div/div[2]/ul/li[2]/ul/li[1]/div[1]/div/span").click()
        if not ("收回解析" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-查看解析失败！")
        else:
            print(u"PASS-查看解析成功！")
        #收回解析
        wd.find_element_by_css_selector("span.options_analysis.on").click()
        if  ("收回解析" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-收回解析失败！")
        else:
            print(u"PASS-收回解析成功！")

        #点击打印
        wd.find_element_by_id("w_PrintBtn").click()
        #普通打印
        wd.find_element_by_css_selector("div.print_btn.normal").click()
        time.sleep(0.5)
        #调用autoit程序。
        os.system("D:\\selenium_upfile\\print_cancel.exe")
        #带解析打印
        wd.find_element_by_css_selector("div.print_btn.withAnalyze").click()
        time.sleep(1)
        try:
            #调用autoit程序。
            os.system("D:\\selenium_upfile\\print_cancel.exe")
        except Exception:
            print u"FAILED-打印功能出错"
        else:
            print u"PASS-打印功能正常"
        #关闭打印对话框
        wd.find_element_by_xpath("//div[@class='print_in']/i").click()
        
        #点击编辑
        wd.find_element_by_xpath("html/body/article/div/div[3]/div/a[1]").click()
        #定位到题目元素        
        article = wd.find_element_by_xpath("html/body/article/div/div[4]/div/div[2]/ul/li[2]/ul/li[1]/div[1]")  
        #鼠标悬浮在题目位置
        ActionChains(wd).move_to_element(article).perform()
        #等待1秒
        time.sleep(1)
        #定位到查看解析
        mouse = wd.find_element_by_xpath("html/body/article/div/div[4]/div/div[2]/ul/li[2]/ul/li[1]/div[1]/div/span[1]")  
        #鼠标移动至查看解析上方悬浮
        ActionChains(wd).move_to_element(mouse).perform()
        
        #查看解析-展开/收起
        wd.find_element_by_xpath("html/body/article/div/div[4]/div/div[2]/ul/li[2]/ul/li[1]/div[1]/div/span[1]").click()
        if not ("收回解析" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-查看解析失败！")
        else:
            print(u"PASS-查看解析成功！")
        time.sleep(0.5)
        wd.find_element_by_css_selector("span.options_analysis.on").click()
        if  ("收回解析" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-收回解析失败！")
        else:
            print(u"PASS-收回解析成功！")
        time.sleep(0.5)
        #点击编辑
        #wd.find_element_by_xpath("html/body/article/div/div[3]/div/a[1]").click()
        #定位到题目元素        
        article = wd.find_element_by_xpath("html/body/article/div/div[4]/div/div[2]/ul/li[2]/ul/li[1]/div[1]")  
        #鼠标悬浮在题目位置
        ActionChains(wd).move_to_element(article).perform()
        #等待1秒
        time.sleep(1)
        #定位到删除
        mouse = wd.find_element_by_xpath("html/body/article/div/div[4]/div/div[2]/ul/li[2]/ul/li[1]/div[1]/div/span[2]")  
        #鼠标移动至删除上方悬浮
        ActionChains(wd).move_to_element(mouse).perform()
        #删除试题
        wd.find_element_by_xpath("html/body/article/div/div[4]/div/div[2]/ul/li[2]/ul/li[1]/div[1]/div/span[2]").click()
        if  ("it was very late, he didn’t go to bed" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-题目删除失败！")
        else:
            print(u"PASS-题目删除成功！")
        
        #完成时间修改
        wd.find_element_by_css_selector("input.t_time").click()
        wd.find_element_by_css_selector("input.t_time").clear()
        wd.find_element_by_css_selector("input.t_time").send_keys("50")
        
        #点击添加题目
        wd.find_element_by_css_selector("i.line_addQuestion").click()
        time.sleep(3)
        #定位到题目元素        
        article = wd.find_element_by_xpath("html/body/div[1]/div/div[2]/div[1]/ul/li[1]/div[1]")  
        #鼠标悬浮在题目位置
        ActionChains(wd).move_to_element(article).perform()
        #等待1秒
        time.sleep(1)
        #定位到查看解析
        mouse = wd.find_element_by_xpath("html/body/div[1]/div/div[2]/div[1]/ul/li[1]/div[1]/div/span[1]")  
        #鼠标移动至查看解析上方悬浮
        ActionChains(wd).move_to_element(mouse).perform()
        #查看解析
        wd.find_element_by_xpath("//div[@class='addLineQuestion_middle_questions']//span[.='查看解析']").click()
        if not ("收回解析" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-查看解析失败！")
        else:
            print(u"PASS-查看解析成功！")
        #点击选入
        wd.find_element_by_xpath("html/body/div[1]/div/div[2]/div[1]/ul/li[1]/div[1]/div/span[3]").click()
        #点击报错
        wd.find_element_by_xpath("html/body/div[1]/div/div[2]/div[1]/ul/li[1]/div[1]/div/span[2]").click()
        wd.find_element_by_id("02").click()
        wd.find_element_by_id("errorReason").click()
        wd.find_element_by_id("errorReason").clear()
        wd.find_element_by_id("errorReason").send_keys(u"自动化测试数据请忽略")
        wd.find_element_by_css_selector("input.m_submitErrorsSure").click()
        if not ("报错成功" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-报错失败！")
        else:
            print(u"PASS-报错成功！")
        #收起解析
        wd.find_element_by_css_selector("span.options_analysis.on").click()
        if  ("收回解析" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-收回解析失败！")
        else:
            print(u"PASS-收回解析成功！")
        wd.find_element_by_link_text("完成").click()
        #print wd.find_element_by_xpath("html/body/article/div/div[4]/div/div[2]/ul/li[2]/ul/li[5]").get_attribute("class")
        if not ("question new" in wd.find_element_by_xpath("html/body/article/div/div[4]/div/div[2]/ul/li[2]/ul/li[5]").get_attribute("class")):
            success = False
            print(u"FAILED-添加题目失败！")
        else:
            print(u"PASS-添加题目成功！")
            
        #调整题型
        wd.find_element_by_css_selector("input.exercise_btn_setline").click()
        #调用autoit执行拖动操作
        os.system("D:\\selenium_upfile\\tiaozhengtixing.exe")
        #调整题型完成
        wd.find_element_by_css_selector("span.setLine_btn_done").click()
        #编辑作业完成
        wd.find_element_by_css_selector("input.exercise_btn_done").click()
        if not ("I. 用方框中所给词的" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-题目顺序调整失败！")
        else:
            print(u"PASS-题目顺序调整成功！")
        #点击布置
        wd.find_element_by_link_text("布置").click()
        time.sleep(1)
        wd.find_element_by_xpath("//div[@class='publish_box']//li[.='八年级38班']").click()
        time.sleep(1)
        wd.find_element_by_link_text("确定").click()
        now_time = time.strftime('%Y-%m-%d %H:%M',time.localtime(time.time()))
        if not (now_time in wd.find_element_by_xpath("html/body/article/div/div[3]/div/div[3]/dl/dd/table/tbody/tr[2]/td[4]").text):
            success = False
            print(u"FAILED-布置作业失败！")
        else:
            print(u"PASS-布置作业成功！")
        #将布置时间保存到全局变量中，以备下面作业报告中判断是否生成报告
        global ASSIGN_TIME
        ASSIGN_TIME = now_time
        topmenu_t.top_menu_pgzy(self)
        wd.find_element_by_xpath("//article/div/div[3]/ul/li[1]/ul/li[5]/span").click()
        wd.find_element_by_xpath("//article/div/div[3]/ul/li[1]/ul/li[6]").click()
        if not ("暂无学生提交" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-批改判断失败！")
        else:
            print(u"PASS-批改判断成功！")
        
        logout.logout(self)
        self.assertTrue(success)
        return(now_time)
    
    def test_zuoye_02_xzy_s(self):
        '''作业长流程-学生写作业'''
        print u"开始测试！作业长流程-学生写作业"
        wd = self.wd
        success = True
        #登录
        login.login(self,"17200008071", "1qaz@WSX")
        #检查是否登录成功
        if not (len(wd.find_elements_by_id("User")) != 0):
            success = False
            print(u"FAILED-学生登录失败！")
        else:
            print(u"PASS-学生登录成功！")

        topmenu_t.top_menu_xzy_s(self)
        if not ("写作业" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-写作业列表初始化失败！")
        else:
            print(u"PASS-写作业列表初始化成功！")
        #点击去完成
        wd.find_element_by_xpath("//div[3]/div[1]/ul/li[2]/ul[1]/li[6]/span[2]").click()
        if not ("1.选择题请在电脑上做答，提交后将由系统批改。" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-答题页面初始化失败！")
        else:
            print(u"PASS-答题页面初始化成功！")
        #点击打印
        wd.find_element_by_css_selector("span.task_print").click()
        time.sleep(1)
        #调用autoit3
        os.system("D:\\selenium_upfile\\print_cancel.exe")
        time.sleep(0.5)
        wd.find_element_by_xpath("//div[@class='task_strogepaper']//p[.='B. How often']").click()
        time.sleep(0.5)
        wd.find_element_by_xpath("//div[@class='task_strogepaper']//p[.='A. Although; but']").click()
        time.sleep(0.5)
        wd.find_element_by_xpath("//div[@class='task_strogepaper']//p[.='A. of']").click()
        time.sleep(0.5)
        wd.find_element_by_xpath("//div[@class='task_strogepaper']//p[.='A. In']").click()
        time.sleep(0.5)
        wd.find_element_by_xpath("//div[@class='task_strogepaper']//div[.='B. are']").click()
        time.sleep(0.5)
        wd.find_element_by_xpath("//div[@class='task_strogepaper']//div[.='T']").click()
        time.sleep(0.5)
        wd.find_element_by_xpath("//div[@class='task_strogepaper']/div[7]/div[2]/div/div[3]/div/div[2]/div[2]").click()
        time.sleep(0.5)
        wd.find_element_by_xpath("//div[@class='task_strogepaper']/div[7]/div[2]/div/div[4]/div/div[2]/div[1]").click()
        time.sleep(0.5)
        wd.find_element_by_xpath("//div[@class='task_strogepaper']/div[7]/div[2]/div/div[5]/div/div[2]/div[2]").click()
        time.sleep(0.5)
        wd.find_element_by_xpath("//div[@class='task_strogepaper']/div[7]/div[2]/div/div[6]/div/div[2]/div[1]").click()
        time.sleep(0.5)
        wd.find_element_by_xpath("//div[@class='task_up']//span[.='上传']").click()
        wd.find_element_by_id("inputImage").click()
        #调用autoit上传图片
        os.system("D:\\selenium_upfile\\upfile.exe")
        wd.find_element_by_id("GetImgUrl").click()
        time.sleep(0.5)
        #点击提交
        wd.find_element_by_xpath("html/body/div[4]/div[1]/div[2]/div[3]/div/div[6]").click()
        time.sleep(1)
        wd.find_element_by_css_selector("div.r_personal.clearfix").click()
        if not ("客观题正确数" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-提交作业失败！")
        else:
            print(u"PASS-提交作业成功！")
        if not ("等待批改" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-提交作业失败！")

        topmenu_t.top_menu_xx_s(self)
        if not ("消息" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-进入消息失败！")
        else:
            print(u"PASS-进入消息成功！")
        if not ("房学-8071号,不要错过交作业的末班车哟，赶快提交吧。" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-老师催作业消息发送失败！")
        else:
            print(u"PASS-老师催作业消息发送成功！")
            
        logout.logout_s(self)
        self.assertTrue(success)
    
    def test_zuoye_03_pgzy(self):
        '''作业长流程-教师批改作业'''
        print u"开始测试！作业长流程-教师批改作业'"
        wd = self.wd
        success = True
        #登录
        login.login(self,"17200000083", "1qaz@WSX")
        #检查是否登录成功
        if not (len(wd.find_elements_by_id("User")) != 0):
            success = False
            print(u"FAILED-教师登录失败！")
        else:
            print(u"PASS-教师登录成功！")
        
        topmenu_t.top_menu_pgzy(self)        
        if not ("批改作业" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-批改作业列表展示失败！")
        else:
            print(u"PASS-批改作业列表展示成功！")
        #点击批改，进入批改页面
        wd.find_element_by_xpath("//article/div/div[3]/ul/li[1]/ul/li[6]").click()
        time.sleep(0.5)
        wd.find_element_by_css_selector("span.analytical_span").click()
        if not ("【答案】" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-查看答案失败！")
        else:
            print(u"PASS-查看答案成功！")
        #关闭答案
        wd.find_element_by_css_selector("span.close_span").click()
        #批改题目
        wd.find_element_by_xpath("//article/div/div[3]/div/div[2]/div[2]/ul[1]/ul[2]/li[2]/span[2]").click()
        wd.find_element_by_xpath("//article/div/div[3]/div/div[2]/div[2]/ul[1]/ul[3]/li[2]/span[3]").click()
        wd.find_element_by_xpath("//article/div/div[3]/div/div[2]/div[2]/ul[1]/ul[3]/li[3]/span[3]").click()
        wd.find_element_by_xpath("//article/div/div[3]/div/div[2]/div[2]/ul[1]/ul[3]/li[4]/span[2]").click()
        wd.find_element_by_xpath("//article/div/div[3]/div/div[2]/div[2]/ul[1]/ul[3]/li[5]/span[3]").click()
        wd.find_element_by_xpath("//article/div/div[3]/div/div[2]/div[2]/ul[1]/ul[3]/li[6]/span[2]").click()
        #JS控制滚动条
        js='document.getElementsByClassName("paperList")[0].scrollTop=550' 
        wd.execute_script(js)
        time.sleep(0.5)
        wd.find_element_by_xpath("//article/div/div[3]/div/div[2]/div[2]/ul[1]/ul[5]/li[2]/span[3]").click()
        wd.find_element_by_xpath("//article/div/div[3]/div/div[2]/div[2]/ul[1]/ul[5]/li[3]/span[2]").click()
        wd.find_element_by_xpath("//article/div/div[3]/div/div[2]/div[2]/ul[1]/ul[5]/li[4]/span[3]").click()
        wd.find_element_by_xpath("//article/div/div[3]/div/div[2]/div[2]/ul[1]/ul[5]/li[5]/span[2]").click()
        wd.find_element_by_xpath("//article/div/div[3]/div/div[2]/div[2]/ul[1]/ul[5]/li[6]/span[4]").click()
        time.sleep(0.5)
        
        #定位到添加备注输入框
        mouse = wd.find_element_by_xpath("//article/div/div[3]/div/div[2]/div[1]/textarea") 
        #鼠标移动至添加备注悬浮
        ActionChains(wd).move_to_element(mouse).perform()
        time.sleep(0.5)
        wd.find_element_by_xpath("//article/div/div[3]/div/div[2]/div[1]/textarea").click()
        wd.find_element_by_xpath("//article/div/div[3]/div/div[2]/div[1]/textarea").clear()
        wd.find_element_by_xpath("//article/div/div[3]/div/div[2]/div[1]/textarea").send_keys(u"自动化测试批改作业。")
        time.sleep(0.5)
        #点击画笔
        wd.find_element_by_xpath("html/body/article/div/div[3]/div/div[2]/div[2]/ul[2]/li[1]/span[1]").click()
        #开始进行画笔操作
        os.system("D:\\selenium_upfile\\huabipigai.exe")
        wd.find_element_by_id("nextStu").click()
        
        time.sleep(3)
        topmenu_t.top_menu_zybg(self)
        global ASSIGN_TIME
        if not ( ASSIGN_TIME in wd.find_elements_by_xpath("//article/div/div[3]/div/div[1]/ul[2]/li[1]/p[1]")[0].text):
            success = False
            print(u"FAILED-批改失败！")
        else:
            print(u"PASS-批改成功！")
               
        time.sleep(0.5)
        logout.logout(self)
        self.assertTrue(success)
    
    def test_zuoye_04_zybg(self):
        '''作业长流程-教师作业报告'''
        print u"开始测试！作业长流程-教师作业报告'"
        wd = self.wd
        success = True
        #登录
        login.login(self,"17200000083", "1qaz@WSX")
        #检查是否登录成功
        if not (len(wd.find_elements_by_id("User")) != 0):
            success = False
            print(u"FAILED-教师登录失败！")
        else:
            print(u"PASS-教师登录成功！")
 
        topmenu_t.top_menu_zybg(self)
        #点击查看按钮
        wd.find_element_by_xpath("//article/div/div[3]/div/div[1]/ul[2]/li[1]/p[4]/a[2]").click()
        #声明全局变量
        global ASSIGN_TIME
        #ASSIGN_TIME = '2017-09-07'
        if not (ASSIGN_TIME in wd.find_element_by_xpath("//article/div/div[3]/div/h1[2]").text):
            success = False
            print(u"FAILED-作业报告展示失败！")
        else:
            print(u"PASS-作业报告展示成功！")
        time.sleep(1.5)
        #记录老窗口句柄，准备切换窗口    
        home_page = wd.current_window_handle
        #点击查看详情，打开新窗口
        wd.find_element_by_xpath("//article/div/div[3]/div/div[2]/div/ul[2]/li[1]/p[4]/a[1]").click()
        time.sleep(1)
        #获取当前的所有窗口句柄
        all_handles = wd.window_handles
        for handle in all_handles:
            if handle !=  home_page:
                wd.switch_to_window(handle)
                if not ("房学-8071号" in wd.find_element_by_xpath("//article/div/div[2]/div[1]/div[2]/ul/li").text):
                    success = False
                    print(u"FAILED-学生确认失败！")
                else:
                    print(u"PASS-学生确认成功！")
                if not ("学生答案" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print(u"FAILED-学生报告查看失败！")
                else:
                    print(u"PASS-学生报告查看成功！")
                wd.close()
                wd.switch_to_window(home_page)
        #点击题目详情
        wd.find_element_by_xpath("html/body/article/div/div[3]/div/ul/li[2]").click()
        
        old_id = wd.find_element_by_xpath("//article/div/div[3]/div/div[3]/div[1]/ul[2]/li[1]/p[1]").text
        wd.find_element_by_id("Num_Sort").click()
        if not (old_id == wd.find_element_by_xpath("//article/div/div[3]/div/div[3]/div[1]/ul[2]/li[1]/p[1]").text):
            print(u"PASS-按题号排序成功！")
        else:
            success = False
            print(u"FAILED-按题号排序失败！")
        wd.find_element_by_id("Num_Sort").click()

        old_error_rate = wd.find_element_by_xpath("//article/div/div[3]/div/div[3]/div[1]/ul[2]/li[1]/p[2]").text
        wd.find_element_by_id("Error_Rate").click()
        if not (old_error_rate == wd.find_element_by_xpath("//article/div/div[3]/div/div[3]/div[1]/ul[2]/li[1]/p[2]").text):
            print(u"PASS-按错误率排序成功！")
        else:
            success = False
            print(u"FAILED-按错误率排序失败！")
        wd.find_element_by_id("Error_Rate").click()
        wd.find_element_by_id("Num_Sort").click()
        
        #记录老窗口句柄，准备切换窗口    
        home_page = wd.current_window_handle
        #点击打印
        wd.find_element_by_id("w_PrintBtn0").click()
        #获取当前的所有窗口句柄
        all_handles = wd.window_handles
        for handle in all_handles:
            if handle !=  home_page:
                wd.switch_to_window(handle)
                if not (wd.find_element_by_xpath(".//*[@id='w_PrintBtn']").is_displayed()):
                    success = False
                    print(u"FAILED-打印页面跳转失败！")
                else:
                    print(u"PASS-打印页面跳转成功！")
                #将滚动条移动到页面的顶部
                js="var q=document.documentElement.scrollTop=0"
                wd.execute_script(js)
                time.sleep(1)
                wd.find_element_by_xpath(".//*[@id='w_PrintBtn']").click()
                #try:
                #    wd.find_element_by_xpath(".//*[@id='w_PrintBtn']").click()
                #except Exception,msg:
                #    print msg
                #else:
                #    print u"PASS-点击确认打印成功"
                time.sleep(2)
                #调用autoit取消打印
                os.system("D:\\selenium_upfile\\print_cancel.exe")
                time.sleep(1)
                wd.close()
                wd.switch_to_window(home_page)
        time.sleep(0.5)
        #点击第16题的查看
        wd.find_element_by_xpath("//li[@id='16']/p[3]/span[1]").click()
        time.sleep(0.5)
        
        #点击第16题的解析
        wd.find_element_by_xpath("//article/div/div[3]/div/div[3]/div[2]/ul/li[16]/div[2]/input").click()
        if not ("【答案】Although" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-查看答案失败！")
        else:
            print(u"PASS-查看答案成功！")
        #收起解析
        wd.find_element_by_css_selector("input.w_Analysis1").click()
        #点击返回顶部
        wd.find_element_by_xpath("//article/i").click()
        #点击综合分析
        wd.find_element_by_xpath("//ul[@class='w_OtherTab']//li[.='综合分析']").click()
        if not ("正确率" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-综合分析查看失败！")
        else:
            print(u"PASS-综合分析查看成功！")
            
        logout.logout(self)
        self.assertTrue(success)

    def test_zuoye_05_zybg_s(self):
        '''作业长流程-学生作业报告'''
        print u"开始测试！作业长流程-学生作业报告'"
        wd = self.wd
        success = True
        #登录
        login.login(self,"17200008071", "1qaz@WSX")
        #检查是否登录成功
        if not (len(wd.find_elements_by_id("User")) != 0):
            success = False
            print(u"FAILED-学生登录失败！")
        else:
            print(u"PASS-学生登录成功！")
        
        time.sleep(1)
        
        topmenu_t.top_menu_kbg_s(self)
        if not ("作业报告" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-作业报告列表展示失败！")
        else:
            print(u"PASS-作业报告列表展示成功！")
        #点击查看
        wd.find_element_by_xpath("//div[3]/div/div[2]/div[1]/ul[1]/li[6]/span").click()
        if not ("数据分析" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-报告详情页展示失败！")
        else:
            print(u"PASS-报告详情页展示成功！")
        #点击班级目标
        wd.find_element_by_css_selector("div.r_classtarget").click()
        if not ("班级目标" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-班级目标展示失败！")
        else:
            print(u"PASS-班级目标展示成功！")
        #点击关闭按钮
        wd.find_element_by_css_selector("i.iconfont.classDelete").click()
        if not ("教师批注 : 自动化测试批改作业。" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-作业报告信息错误！")
        else:
            print(u"PASS-作业报告信息暂未发现错误！")

        logout.logout_s(self)
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
