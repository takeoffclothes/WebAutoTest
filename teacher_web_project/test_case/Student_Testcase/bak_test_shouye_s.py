#coding=utf-8
'''
Created on 2017年8月23日
updated on 2017年9月04日
五好导学网-教师web端-班级管理 自动化测试脚本
@author: 房立信
'''

from selenium import webdriver
import sys
sys.path.append('\PubModule')
from test_case.PubModule import login
from test_case.PubModule import logout
#from selenium.webdriver.firefox.webdriver import WebDriver
#from selenium.webdriver.common.action_chains import ActionChains
import time, unittest,os
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

class test_shouye_s(unittest.TestCase):
    '''学生pc端-首页'''
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
    
    def test_01_banner(self):
        '''banner-期末复习专题'''
        print u"开始测试！banner-期末复习专题"
        wd = self.wd
        success = True
        
        if not ("瞄准薄弱点，哪里不会点哪里" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-首页初始化失败")
        else:
            print(u"PASS-首页初始化成功")
         
        #点击首页banner
        try:
            wd.find_element_by_xpath("//div[@id='in_swiper']/div[1]/a").click()
        except Exception,msg:
            print msg
            
        if not ("复习测试" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-期末复习专题页面初始化失败")
        else:
            print(u"PASS-期末复习专题页面初始化成功")
        wd.find_element_by_id("7").click()
        if not ("人教版七年级" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-年级切换失败")
        else:
            print(u"PASS-年级切换成功")
        wd.find_element_by_xpath("//ul[@class='R_kwonsub']//li[.='数学']").click()
        if not ("平行线的判定" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-数学学科切换失败")
        else:
            print(u"PASS-数学学科切换成功")
        wd.find_element_by_xpath("//ul[@class='R_kwonsub']//li[.='英语']").click()
        if not ("情态动词" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-英语学科切换失败")
        else:
            print(u"PASS-英语学科切换成功")
        wd.find_element_by_id("8").click()
        wd.find_element_by_xpath("//ul[@class='R_kwonsub']//li[.='数学']").click()
        wd.find_element_by_xpath("//ul[@class='R_kwonsub']//li[.='物理']").click()
        wd.find_element_by_xpath("//div[@class='R_fc']//li[.='典例讲解']").click()
        
        time.sleep(2)
        #隐性等待30秒
        wd.implicitly_wait(30)
        wd.find_element_by_css_selector("div.R_Download").click()
        wd.find_element_by_xpath("//div[@class='R_fc']//span[.='专题二：力与运动']").click()
        wd.find_element_by_xpath("//div[@class='R_fc']/div[2]/ul/li[3]").click()
        time.sleep(2)
        #隐性等待30秒
        wd.implicitly_wait(30)
        wd.find_element_by_css_selector("div.R_Download").click()
        print(u"WARNING！！！-文件下载完成了，暂时人工去下载目录查看结果，后期需要添加下载文件查询及目录切换校验。")
        
        self.assertTrue(success)

    def test_02_xzykbg(self):
        '''写作业、看报告'''
        print u"开始测试！首页-写作业、看报告"
        wd = self.wd
        success = True
         
        homepage_handle = wd.current_window_handle
        #点击写作业链接
        wd.find_element_by_css_selector("span.i_bcue").click()
        all_handles = wd.window_handles
        for handle in all_handles:
            if handle != homepage_handle:
                wd.switch_to_window(handle)
                if not ("写作业" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print(u"FAILED-写作业跳转失败！")
                else:
                    print(u"PASS-写作业跳转成功！")
                wd.close()
                wd.switch_to_window(homepage_handle)
                
        if not ("1500万师生检验的好作业" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-返回首页失败！")
        
        #点击看报告链接
        wd.find_element_by_xpath("//li[@class='seaThePresentation']//span[.='看报告']").click()
        time.sleep(1)
        all_handles = wd.window_handles
        for handle in all_handles:
            if handle != homepage_handle:
                wd.switch_to_window(handle)
                if not ("看报告" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print(u"FAILED-看报告跳转失败！")
                else:
                    print(u"PASS-看报告跳转成功！")
                wd.close()
                wd.switch_to_window(homepage_handle)
                
        if not ("1500万师生检验的好作业" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-返回首页失败！")
        
        self.assertTrue(success)
    
    def test_03_sp(self):
        '''首页-视频'''
        print u"开始测试！首页-视频"
        wd = self.wd
        success = True
        
        homepage_handle = wd.current_window_handle
        wd.find_element_by_xpath("html/body/div[2]/div[3]/div[1]/ul/li[1]").click()
        #进入视频播放页面
        wd.find_element_by_xpath("html/body/div[2]/div[3]/div[2]/ul/li[4]/img[1]").click()
        time.sleep(0.5)
        all_handles = wd.window_handles
        for handle in all_handles:
            if handle != homepage_handle:
                wd.switch_to_window(handle)
                if not ("视频播放" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print(u"FAILED-视频播放页初始化失败！")
                else:
                    print(u"PASS-视频播放页初始化成功！")
                wd.close()
                wd.switch_to_window(homepage_handle)
        if not ("国家级研究课题，助力翻转课堂" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-返回首页失败！")
        else:
            print(u"PASS-返回首页成功！")
        wd.find_element_by_xpath("html/body/div[2]/div[3]/div[1]/ul/li[2]").click()
        if not ("皮孩子追数学之正数和负数" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-数学视频切换失败！")
        else:
            print(u"PASS-数学视频切换成功！")
        wd.find_element_by_xpath("html/body/div[2]/div[3]/div[2]/ul/li[1]/img[3]").click()
        time.sleep(0.5)
        all_handles = wd.window_handles
        for handle in all_handles:
            if handle != homepage_handle:
                wd.switch_to_window(handle)
                if not ("视频播放" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print(u"FAILED-视频播放页初始化失败！")
                else:
                    print(u"PASS-视频播放页初始化成功！")
                wd.close()
                wd.switch_to_window(homepage_handle)
        time.sleep(0.5)

        if not ("国家级研究课题，助力翻转课堂" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-返回首页失败！")
        
        #切换英语视频
        wd.find_element_by_xpath("//ul[@class='subject_ul']//li[.='英语']").click()
        time.sleep(0.5)
        wd.find_element_by_xpath("html/body/div[2]/div[3]/div[2]/ul/li[4]/img[1]").click()
        time.sleep(0.5)
        all_handles = wd.window_handles
        for handle in all_handles:
            if handle != homepage_handle:
                wd.switch_to_window(handle)
                if not ("视频播放" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print(u"FAILED-视频播放页初始化失败！")
                wd.close()
                wd.switch_to_window(homepage_handle)
        #点击更多精彩
        wd.find_element_by_xpath("html/body/div[2]/div[3]/div[1]/a").click()
        time.sleep(0.5)
        all_handles = wd.window_handles
        for handle in all_handles:
            if handle != homepage_handle:
                wd.switch_to_window(handle)
                if not ("看视频" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print(u"FAILED-视频列表页初始化失败！")
                else:
                    print(u"PASS-视频列表页初始化成功！")
                wd.close()
                wd.switch_to_window(homepage_handle)
        time.sleep(0.5)
        
        self.assertTrue(success)
    
    def test_04_hxsy(self):
        '''首页-核心素养'''
        print u"开始测试！首页-核心素养"
        wd = self.wd
        success = True
        
        homepage_handle = wd.current_window_handle
        wd.find_element_by_link_text("难兄难弟").click()
        time.sleep(1)
        all_handles = wd.window_handles
        for handle in all_handles:
            if handle != homepage_handle:
                wd.switch_to_window(handle)
                if not ("难兄难弟" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print(u"FAILED-美文详情页初始化失败！")
                else:
                    print(u"PASS-美文详情页初始化成功！")
                wd.close()
                wd.switch_to_window(homepage_handle)
        time.sleep(0.5)
        
        #将滚动条移动到页面的中部
        #js="var q=document.documentElement.scrollTop=1000"
        #self.wd.execute_script(js)
        wd.find_element_by_xpath("//ul[@class='across_subject_ul']//li[.='数学']").click()
        time.sleep(0.5)
        if not ("来这学数学，简单还有趣" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-数学文章切换失败！")
        else:
            print(u"PASS-数学文章切换成功！")
        wd.find_element_by_xpath("html/body/div[2]/div[4]/div[2]/ul/li[6]/a").click()
        time.sleep(0.5)
        all_handles = wd.window_handles
        for handle in all_handles:
            if handle != homepage_handle:
                wd.switch_to_window(handle)
                if not ("线段的条数与角的个数的确定技巧" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print(u"FAILED-数学文章页初始化失败！")
                else:
                    print(u"PASS-数学文章页初始化成功！")
                wd.close()
                wd.switch_to_window(homepage_handle)
        time.sleep(0.5)
        wd.find_element_by_xpath("//ul[@class='across_subject_ul']//li[.='英语']").click()
        time.sleep(0.5)
        if not ("和英语相知，让阅读更容易" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-英语文章切换失败！")
        else:
            print(u"PASS-英语文章切换成功！")
        time.sleep(0.5)
        wd.find_element_by_xpath("html/body/div[2]/div[4]/div[2]/ul/li[6]/a").click()
        time.sleep(1)
        all_handles = wd.window_handles
        for handle in all_handles:
            if handle != homepage_handle:
                wd.switch_to_window(handle)
                if not ("The Choice of Companion" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print(u"FAILED-英语文章页初始化失败！")
                else:
                    print(u"PASS-英语文章页初始化成功！")
                wd.close()
                wd.switch_to_window(homepage_handle)
        #点击英语更多精彩
        wd.find_element_by_xpath("//div[@class='i_main']/div[4]/div[1]/a").click()
        all_handles = wd.window_handles
        for handle in all_handles:
            if handle != homepage_handle:
                wd.switch_to_window(handle)
                if not ("走遍英美" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print(u"FAILED-走遍英美页面初始化失败！")
                else:
                    print(u"PASS-走遍英美页面初始化成功！")
                wd.close()
                wd.switch_to_window(homepage_handle)
        
        self.assertTrue(success)
    
    def test_05_bst(self):
        '''首页-必刷题'''
        print u"开始测试！首页-必刷题"
        wd = self.wd
        success = True
  
        #点击必刷题-数学
        wd.find_element_by_css_selector("li.mu_Sub02").click()
        if not ("必刷题" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-数学必刷题页面初始化失败")
        else:
            print(u"PASS-数学必刷题页面初始化成功")
            
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

        self.assertTrue(success)
    
    def tearDown(self):
        #将滚动条移动到页面的顶部
        js="var q=document.documentElement.scrollTop=0"
        self.wd.execute_script(js)
        
        logout.logout_s(self)
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
