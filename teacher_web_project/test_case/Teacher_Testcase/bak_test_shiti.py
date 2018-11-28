#coding=utf-8
'''
Created on 2017年8月17日
updated on 2017年8月29日
五好导学网-教师PC端-试题模块 自动化测试脚本
@author: 房立信
'''

from selenium import webdriver
import sys
sys.path.append('\PubModule')
from test_case.PubModule import login
from test_case.PubModule import logout
from test_case.PubModule import topmenu_t
from selenium.webdriver.firefox.webdriver import WebDriver
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

class test_shiti(unittest.TestCase):
    '''教师pc端-试题模块测试'''
    def setUp(self):
        #定义浏览器下载配置
        profile = webdriver.FirefoxProfile("C:\\Users\\Administrator\\Application Data\\Mozilla\\Firefox\\Profiles\\nce5v0dx.default")
        #定义浏览器，打开测试网站
        self.wd=webdriver.Firefox(profile)
        self.wd.implicitly_wait(30)
        #self.base_url="http://www.wuhaodaoxue.com/"
        #脚本运行时，错误的信息将被打印到这个列表中。
        self.verificationErrors = []
        #是否继续接受下一下警告
        self.accept_next_alert = True
        self.wd.get("http://www.wuhaodaoxue.com")
        #self.wd.maximize_window()
    
    def test_test_wnzt(self):
        '''五年真题'''
        success = True
        wd = self.wd
        #wd.get(self.base_url)
        print u"开始测试！五年真题"
        #登录
        login.login(self,"17200000071", "1qaz@WSX")
        #检查是否登录成功
        if not (len(wd.find_elements_by_id("User")) != 0):
            success = False
            print(u"FAILED-登录失败！")
        else:
            print(u"PASS-登录成功！")
        
        #进入五年真题页面
        topmenu_t.top_menu_wnzt(self)
        #检查是否成功进入五年真题页面
        if not ("五年真题" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-五年真题页面进入失败！")
        else:
            print(u"PASS-五年真题页面进入成功！页面初始化成功！")

        wd.find_element_by_xpath("//div[@class='r_condition']//li[.='辽宁']").click()
        if not ("2015年辽宁省朝阳市中考语文试题" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-试题按省份-辽宁筛选失败！")
        else:
            print(u"PASS-试题按省份-辽宁筛选成功！")
        #wd.find_element_by_xpath("//div[@class='r_condition']//li[.='全部']").click()
        wd.find_element_by_xpath("html/body/article/div/div[3]/div[1]/div[1]/ul[1]/li[1]").click()
        wd.find_element_by_xpath("//div[@class='r_condition']//li[.='2015']").click()
        if not ("2015年福建省南平市中考语文试题" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-试题按年份-2015筛选失败！")
        else:
            print(u"PASS-试题按年份-2015筛选成功！")
        wd.find_element_by_xpath("html/body/article/div/div[3]/div[1]/div[1]/ul[2]/li[1]").click()
        #多窗口操作开始
        wd.find_element_by_xpath("//div[@class='r_condition']//li[.='河北']").click()
        if not ("2017年河北省中考语文试题（全解全析）" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-试题按省份-河北筛选失败！")
        else:
            print(u"PASS-试题按省份-河北筛选成功！")
        #print wd.window_handles
        #获得当前窗口句柄
        questionspage_window = wd.current_window_handle
        #进入试题详情页面
        wd.find_element_by_link_text("2017年河北省中考语文试题（全解全析）").click()
        time.sleep(2) 
        #获得当前所有打开的窗口的句柄
        all_handles = wd.window_handles
        #进入2017年河北省中考语文试题（全解全析）页面
        for handle in all_handles:
            if handle != questionspage_window:
                #print wd.title
                wd.switch_to_window(handle)
                #print 'now zhenti page!'
                #print wd.title
                if not ("2017年河北省中考语文试题（全解全析）" in wd.find_element_by_tag_name("html").text):
                    print(u"FAILED-试题详情页面进入失败！或展示失败！")
                else:
                    print(u"PASS-试题详情页面进入成功，试题展示成功！")
                #print wd.window_handles
                wd.find_element_by_xpath(".//*[@id='moveDiv']/span[2]").click()
                print(u"下载完成，请去下载文件夹检查下载结果，下载文件：2017年河北省中考语文试题（全解全析）")
                wd.close()
                #print wd.window_handles
                wd.switch_to_window(questionspage_window)
                #print wd.window_handles
                #print wd.title

        #获得当前所有打开的窗口的句柄
        all_handles = wd.window_handles
        for handle in all_handles:
            if handle != questionspage_window:
                wd.switch_to_window(handle)
                #print 'now 现在是第二个句柄 page!'
                #打印第二个句柄的标题，打印完发现还是标题是空的。
                #print wd.title
                #print wd.window_handles
                wd.close()
                #print wd.window_handles
                wd.switch_to_window(questionspage_window)
                #print wd.window_handles
                #print wd.title
        logout.logout(self)
        self.assertTrue(success)

    def test_test_snmn(self):
        '''三年模拟'''
        success = True
        wd = self.wd
        print u"开始测试！三年模拟"
        
        #登录
        login.login(self,"17200000071", "1qaz@WSX")
        #检查是否登录成功
        if not (len(wd.find_elements_by_id("User")) != 0):
            success = False
            print(u"FAILED-登录失败！")
        else:
            print(u"PASS-登录成功！")
                        
        #进入三年模拟页面
        topmenu_t.top_menu_snmn(self)
        #检查是否成功进入五年真题页面
        if not ("三年模拟" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-三年模拟页面进入失败！")
        else:
            print(u"PASS-三年模拟页面进入成功！页面初始化成功！")
        wd.find_element_by_xpath("//div[@class='r_condition']//li[.='贵州']").click()
        if not ("2016年贵州省松桃县牛郎镇中学七年级（上）第三单元测试" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-试题按省份-贵州筛选失败！")
        else:
            print(u"PASS-试题按省份-贵州筛选成功！")
        wd.find_element_by_xpath("//div[@class='r_condition']//li[.='湖南']").click()
        if not ("2016年湖南省郴州市第八中学七年级(上)第二单元测试语文试题" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-试题按省份-湖南筛选失败！")
        else:
            print(u"PASS-试题按省份-湖南筛选成功！")
        wd.find_element_by_xpath("//div[@class='r_condition']//li[.='全部']").click()
        wd.find_element_by_xpath("//div[@class='r_condition']//li[.='2016']").click()
        if not ("2016" in wd.find_element_by_xpath(".//*[@id='r_dimension']/ul[1]/li[1]/a").text):
            success = False
            print(u"FAILED-试题按年份-2016筛选失败！")
        else:
            print(u"PASS-试题按年份-2016筛选成功！")
        #点击全部
        wd.find_element_by_xpath("//div[@class='r_condition']/ul[2]/li[1]").click()
        wd.find_element_by_xpath("//div[@class='r_condition']//li[.='期中']").click()
        if not ("期中" in wd.find_element_by_xpath(".//*[@id='r_dimension']/ul[1]/li[1]/a").text):
            success = False
            print(u"FAILED-试题按类型-期中筛选失败！")
        else:
            print(u"PASS-试题按类型-期中筛选成功！")
        wd.find_element_by_xpath("//div[@class='r_condition']//li[.='月考']").click()
        if not ("月考" in wd.find_element_by_xpath(".//*[@id='r_dimension']/ul[2]/li[1]/a").text):
            success = False
            print(u"FAILED-试题按类型-月考筛选失败！")
        else:
            print(u"PASS-试题按类型-月考筛选成功！")
        wd.find_element_by_xpath("html/body/article/div/div[3]/div[1]/div[1]/ul[3]/li[1]").click()
        questionspage_window = wd.current_window_handle
        #进入2017七年级（上）第六单元测试语文试题页面
        wd.find_element_by_xpath(".//*[@id='r_dimension']/ul[1]/li[1]/a").click()
        time.sleep(2) 
        #获得当前所有打开的窗口的句柄
        all_handles = wd.window_handles
        #print wd.window_handles
        #进入2017年河北省中考语文试题（全解全析）页面
        for handle in all_handles:
            if handle != questionspage_window:
                #print wd.title
                wd.switch_to_window(handle)
                #print 'now moniti page!'
                #print wd.title
                if not (wd.find_element_by_xpath(".//*[@id='moveDiv']/span[2]").is_displayed()):
                    success = False
                    print(u"FAILED-试题详情页面进入失败！或展示失败！")
                else:
                    print(u"PASS-试题详情页面进入成功，试题展示成功！")
                #print wd.window_handles
                wd.find_element_by_xpath(".//*[@id='moveDiv']/span[2]").click()
                print(u"下载完成，请去下载文件夹检查下载结果，下载文件：2017七年级（上）第六单元测试语文试题")
                #print wd.window_handles
                wd.close()
                #print wd.window_handles
                wd.switch_to_window(questionspage_window)
                #print wd.window_handles
                #print wd.title
                        
        wd.find_element_by_xpath("//div[@class='r_condition']/ul[3]/li[1]").click()
        logout.logout(self)
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == '__main__':
    unittest.main()
