#coding=utf-8
'''
Created on 2017年8月7日
updated on 2017年8月30日
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
import time, unittest
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

class test_shouye(unittest.TestCase):
    '''教师pc端-首页测试'''
    def setUp(self):
        #定义浏览器下载配置
        profile = webdriver.FirefoxProfile("C:\\Users\\Administrator\\Application Data\\Mozilla\\Firefox\\Profiles\\nce5v0dx.default")
        #定义浏览器，打开测试网站        
        self.wd=webdriver.Firefox(profile)
        self.wd.implicitly_wait(30)
        self.wd.get("http://www.wuhaodaoxue.com")
        #脚本运行时，错误的信息将被打印到这个列表中。
        self.verificationErrors = []
        #是否继续接受下一下警告
        self.accept_next_alert = True

        wd = self.wd
        #登录
        login.login(self,"17200000071", "1qaz@WSX")
        #检查是否登录成功
        if not (len(wd.find_elements_by_id("User")) != 0):
            print(u"FAILED-登录失败！")

    def test_01_banner(self):
        '''期末复习-banner'''
        print u"开始测试！期末复习-banner"
        wd = self.wd
        success = True
        #判断期末复习专题：<a href="http://www.wuhaodaoxue.com/model/Review/Review_index.html"/>
        if not (len(wd.find_elements_by_xpath("//article/div/div[2]/div[1]/div/div[1]/div[1]/a")) != 0):
            success = False
            print(u"FAILED-首页初始化失败")
        else:
            print(u"PASS-首页初始化成功")
        time.sleep(5)       
        wd.find_element_by_xpath("//article/div/div[2]/div[1]/div/div[1]/div[2]/a").click()
        time.sleep(3)       
        if not ("期末复习" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-期末复习专题页面初始化失败")
        else:
            print(u"PASS-期末复习专题页面初始化成功")
        
        wd.find_element_by_xpath("//div[@class='R_fc']//li[.='知识梳理']").click()
        wd.find_element_by_xpath("//div[@class='R_fc']//li[.='专题训练']").click()
        wd.find_element_by_xpath("//div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]").click()
        wd.find_element_by_xpath("//div[@class='R_fc']/div[2]/ul/li[2]").click()
        wd.find_element_by_css_selector("div.R_Look").click()
        wd.find_element_by_css_selector("body").click()
        wd.find_element_by_css_selector("div.R_Look.addword").click()
        time.sleep(0.5)       
        wd.find_element_by_css_selector("div.R_Download").click()
        print(u"WARNING！！！-文件下载完成了，暂时人工去下载目录查看结果，后期需要添加下载文件查询及目录切换校验。")
        #wd.find_element_by_css_selector("body").click()
        #将滚动条移动到页面的顶部
        js="var q=document.documentElement.scrollTop=0"
        wd.execute_script(js)
        
        self.assertTrue(success)

    def test_02_sykj(self):
        '''首页-课件'''
        print u"开始测试！首页-课件"
        wd = self.wd
        success = True
         
        if not (len(wd.find_elements_by_id("User")) != 0):
            print(u"FAILED-登录失败！")
           
        if not ("您讲课比赛的坚实后援" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-进入首页失败！")

        #下面是首页-课件部分
        #获得当前窗口句柄
        homepage_window = wd.current_window_handle
        #点击第一个课件
        wd.find_element_by_xpath("html/body/article/div/div[2]/div[2]/div[1]/div[2]/div/div[1]/a/img").click()
        time.sleep(2) 
        #获得当前所有打开的窗口的句柄
        all_handles = wd.window_handles
        #进入课件窗口
        for handle in all_handles:
            if handle != homepage_window:
#                print wd.title
                wd.switch_to_window(handle)
                #print 'now kejian page!'
                #print wd.title
                if not ("课件播放" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print(u"FAILED-进入课件详情页失败！")
                else:
                    print(u"PASS-进入课件详情页成功！")
#                wd.find_element_by_xpath(".//*[@id='ButtonFastFwd-Small14']").click()
                #print wd.window_handles
                wd.close()
                #print wd.window_handles
                wd.switch_to_window(homepage_window)
                #print wd.window_handles
                #print wd.title
        #点击更多                       
        wd.find_element_by_xpath("//a[@id='sort9']").click()
        if not ("第一单元" or "第二单元" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-更多课件失败！")
        else:
            print(u"PASS-更多课件成功！")
        
#        wd.find_element_by_xpath(".//*[@id='336e343ba36c4133b0d0e68e4159839a']/a/p").click()
#        if not ("2  济南的冬天" in wd.find_element_by_tag_name("html").text):
#            success = False
#            print("verifyTextPresent17 failed")
#        wd.find_element_by_link_text("1 春（1）").click()
#        wd.switch_to_frame()

#分享
#        wd.find_element_by_id("ShareClose").click()
        #下载课件
#        wd.find_element_by_xpath("//article/div/div[3]/article/div[2]/button").click()
        self.assertTrue(success)

    def test_03_syzybg(self):
        '''首页-作业报告'''
        print u"开始测试！首页-作业报告"
        wd = self.wd
        success = True
         
        if not (len(wd.find_elements_by_id("User")) != 0):
            print(u"FAILED-登录失败！")
           
        if not ("1500万师生检验的好作业" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-进入首页失败！")
        #进入布置作业页面
        wd.find_element_by_xpath("//a[@id='sort21']/div/img").click()
        time.sleep(0.5)
        if not ("布置作业" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-布置作业页面初始化失败！")
        else:
            print(u"PASS-布置作业页面初始化成功！")
           
        wd.find_element_by_css_selector("a.fl").click()
        time.sleep(0.5)
        #进入批改作业页面
        wd.find_element_by_xpath("//a[@id='sort23']/div/img").click()
        if not ("批改作业" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-批改作业页面初始化失败！")
        else:
            print(u"PASS-批改作业页面初始化成功！")
        time.sleep(0.5)
        wd.find_element_by_css_selector("a.fl").click()
        #进入作业报告页面
        time.sleep(0.5)
        wd.find_element_by_xpath("//a[@id='sort25']/div/img").click()
        if not ("作业报告" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-作业报告页面初始化失败！")
        else:
            print(u"PASS-作业报告页面初始化成功！")

        self.assertTrue(success)

    def test_04_sysp(self):
        '''首页-视频'''
        print u"开始测试！首页-视频"
        wd = self.wd
        success = True
         
        if not (len(wd.find_elements_by_id("User")) != 0):
            print(u"FAILED-登录失败！")
        
        if not ("国家级研究课题，助力翻转课堂" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-进入首页失败！")
        #点击首页视频大图
        wd.find_element_by_xpath("//div[@class='i_Video_max_wrap']/img").click()
        time.sleep(0.5)
        homepage_window = wd.current_window_handle
        #获得当前所有打开的窗口的句柄
        all_handles = wd.window_handles
        #进入视频窗口
        for handle in all_handles:
            if handle != homepage_window:
#                print wd.title
                wd.switch_to_window(handle)
                #print 'now shipin page!'
                #print wd.title
                if not ("视频播放" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print(u"FAILED-进入视频详情页失败！")
                else:
                    print(u"PASS-进入视频详情页成功！")
#                wd.find_element_by_xpath(".//*[@id='ButtonFastFwd-Small14']").click()
                #print wd.window_handles
                wd.close()
                #print wd.window_handles
                wd.switch_to_window(homepage_window)
                #print wd.window_handles
                #print wd.title
        #点击更多                
        wd.find_element_by_id("sort5").click()
        url = wd.current_url
        if not ("model/prepare/prepare_video.html" in url ):
            success = False
            print(u"FAILED-更多视频失败！")
        else:
            print(u"PASS-更多视频成功！")
        
        '''
        #切换至第一单元第三课
        wd.find_element_by_xpath(".//*[@id='60054a669f5d4835bab14c763b0f1f17']").click()
        if not ("3 雨的四季" in wd.find_element_by_tag_name("html").text):
            success = False
            print("verifyTextPresent failed")

#        wd.find_element_by_xpath("//div[@class='videoBox']/div[1]/div[2]/ul/li/a/div/p[1]/img").click()
        wd.find_element_by_xpath("html/body/article/div/div[2]/div[3]/div[1]/div[2]/ul/li/a/div/p[2]").click()

        if not ("视频播放" in wd.find_element_by_tag_name("html").text):
            success = False
            print("verifyTextPresent8 failed")
        #点赞
        wd.find_element_by_xpath("//div[@class='functions']/span[3]").click()
        #分享
        wd.find_element_by_xpath("//div[@class='functions']/span[5]").click()
        #分享到QQ好友
        wd.find_element_by_css_selector("a.bds_sqq").click()
        wd.find_element_by_id("ShareClose").click()
        #推荐
        wd.find_element_by_id("recommend").click()
        wd.find_element_by_xpath("//ul[@id='c_ReferrerClass']//span[.='七年级43班']").click()
        wd.find_element_by_id("c_Remark").click()
        wd.find_element_by_id("c_Remark").clear()
        wd.find_element_by_id("c_Remark").send_keys("fanggeceshi")
        wd.find_element_by_id("c_RefBtn0").click()
        wd.find_element_by_id("recommend").click()
#        if not ("七年级43班fef771fe72ab416387bf34e1ff81ac16yes七年级43班" in wd.find_element_by_tag_name("html").text):
#            success = False
#            print("verifyTextPresent7 failed")
        wd.find_element_by_xpath("//ul[@id='c_ReferrerClass']//span[.='七年级43班']").click()
        if not ("该班级已推荐" in wd.find_element_by_tag_name("html").text):
            success = False
            print("verifyTextPresent6 failed")
        wd.find_element_by_id("c_RefBtn1").click()
        #进入预习测试页面
        wd.find_element_by_link_text("预习测试").click()
        #获得当前所有打开的窗口的句柄
        all_handles = wd.window_handles
        #进入新窗口
        for handle in all_handles:
            if handle != homepage_window:
#                print wd.title
                wd.switch_to_window(handle)
                print 'now yuxiceshi page!'
                print wd.title
#                if not ("季节不同，注定了雨的风格亦各不相同" in wd.find_element_by_tag_name("html").text):
#                   success = False
#                  print("verifyTextPresent5 failed")
#                wd.find_element_by_xpath(".//*[@id='ButtonFastFwd-Small14']").click()
                print wd.window_handles
                wd.close()
                print wd.window_handles
                wd.switch_to_window(homepage_window)
                print wd.window_handles
                print wd.title
        #返回首页        
        '''

        self.assertTrue(success)

    def test_05_sygxmw(self):
        '''首页-国学美文'''
        print u"开始测试！首页-国学美文"
        wd = self.wd
        success = True
         
        if not (len(wd.find_elements_by_id("User")) != 0):
            print(u"FAILED-登录失败！")
        
        wd.find_element_by_link_text("首页").click()
        if not ("美文常伴左右，读写能力自然提升" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-进入首页失败！")
            
        homepage_window = wd.current_window_handle
        #进入美文-春燕归来页面
        wd.find_element_by_xpath("//article/div/div[2]/div[5]/div[1]/div[2]/ul/li[2]/div/a").click()
        time.sleep(3)
        #获得当前所有打开的窗口的句柄
        all_handles = wd.window_handles
        #进入新窗口
        for handle in all_handles:
            if handle != homepage_window:
#                print wd.title
                wd.switch_to_window(handle)
                #print 'now chunyanguilai page!'
                #print wd.title
                if not ("春燕归来" in wd.title):
                    success = False
                    print(u"FAILED-进入美文详情页失败！")
                else:
                    print(u"PASS-进入美文详情页成功！")
#                wd.find_element_by_xpath(".//*[@id='ButtonFastFwd-Small14']").click()
                #print wd.window_handles
                wd.close()
                #print wd.window_handles
                wd.switch_to_window(homepage_window)
                #print wd.window_handles
                #print wd.title
        #进入美文列表页面
        wd.find_element_by_xpath("//div[@id='footerClumon']//a[.='更多精彩...']").click()
        if not ("名师指点" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-更多美文失败！")
        else:
            print(u"PASS-更多美文成功！")
        
        '''
        wd.find_element_by_link_text("一日的春光8267bbfd207e4460a6e391c0f765ae27").click()
        #获得当前所有打开的窗口的句柄
        all_handles = wd.window_handles
        #进入新窗口
        for handle in all_handles:
            if handle != homepage_window:
#                print wd.title
                wd.switch_to_window(handle)
                print 'now yuxiceshi page!'
                print wd.title
                if not ("《一日的春光》" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print("verifyTextPresent1 failed")
#                wd.find_element_by_xpath(".//*[@id='ButtonFastFwd-Small14']").click()
                print wd.window_handles
                wd.close()
                print wd.window_handles
                wd.switch_to_window(homepage_window)
                print wd.window_handles
                print wd.title
        wd.find_element_by_link_text("多感官描写景物60457a7d95e64b0fa33da640cf797e69").click()
        wd.find_element_by_xpath("//ul[@id='c_Crum']//a[.='首页']").click()
        '''

        #将滚动条移动到页面的顶部
        js="var q=document.documentElement.scrollTop=0"
        wd.execute_script(js)
        
        self.assertTrue(success)
            
    def tearDown(self):
        #退出
        logout.logout(self)
        self.wd.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == '__main__':
    unittest.main()
