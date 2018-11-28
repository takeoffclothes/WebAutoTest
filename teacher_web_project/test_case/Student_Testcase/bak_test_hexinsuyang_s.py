#coding=utf-8
'''
Created on 2017年8月27日
updated on 2017年9月5日
五好导学网-教师web端-班级管理 自动化测试脚本
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
#from selenium.webdriver.support import expected_conditions as EC
import time, unittest
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

class test_hxsy_s(unittest.TestCase):
    '''学生pc端-核心素养'''
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
        wd.maximize_window()
        #登录
        login.login(self,"17200007072", "1qaz@WSX")
        #检查是否登录成功
        if not (len(wd.find_elements_by_id("User")) != 0):
            print(u"FAILED-登录失败！")


    def test_01_mw(self):
        '''核心素养-美文'''
        print u"开始测试！核心素养-美文"
        wd = self.wd
        success = True
 
        #进入国学美文页面
        topmenu_t.top_menu_gxmw_s(self)
        if not ("美文" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-国学美文初始化失败")
        else:
            print(u"PASS-国学美文初始化成功")
        #获取原页面句柄
        homepage_handle = wd.current_window_handle
        #print "国学美文页面句柄是：%s",homepage_handle
        #点击文章江南的冬景
        wd.find_element_by_xpath(".//*[@id='c_Content']/div[1]/div[1]/div/div[2]/ul/li[2]/a/span[1]").click()
        all_handles = wd.window_handles
        #print "当前所有页面的句柄是%s",all_handles
        for handle in all_handles:
            if handle != homepage_handle:
                wd.switch_to_window(handle)
                if not ("江南的冬景" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print(u"FAILED-文章详情展示失败")
                else:
                    print(u"PASS-文章详情展示成功")
                #点击分享按钮
                wd.find_element_by_xpath(".//*[@id='c_Share']").click()
                if not ("分享给好友" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print(u"FAILED-分享给好友弹窗失败")
                else:
                    print(u"PASS-分享给好友弹窗成功")
                time.sleep(1)
                #获取老页面的窗口句柄
                oldpage_window = wd.current_window_handle
                #print "江南的冬景 页面句柄：%s",oldpage_window
                #分享至QQ好友
                wd.find_element_by_css_selector("a.bds_sqq").click()
                time.sleep(3)
                #隐形等待30秒钟
                #self.wd.implicitly_wait(30)
                #切换页面，验证新页面，关闭新页面
                mid_handles = wd.window_handles
                #print "当前页面中所有的句柄，%s", mid_handles
                for handle1 in mid_handles:
                    if handle1 != oldpage_window and handle1 != homepage_handle:
                        #print "当前页面：%s",wd.title
                        wd.switch_to_window(handle1) 
                        #print "切换句柄后，当前页面句柄：%s", handle1
                        time.sleep(2)
                        #frame = wd.find_element_by_xpath(".//*[@id='login']")
                        try:
                            #切入iframe对话框
                            wd.switch_to_frame("login_frame")
                            #关闭登录对话框
                            wd.find_element_by_xpath("//div[@class='header']/a").click()
                            #切回原页面
                            wd.switch_to_default_content()
                            #判断title是否完全等于“发给QQ好友和群组”
                            #title1 = EC.title_is(u"发送给QQ好友和群组")
                            #print title1(wd)
                            #print wd.title
                            if not("发送给QQ好友和群组" in wd.title):
                                success = False
                                print(u"FAILED-分享到QQ失败")
                            else:
                                print(u"PASS-分享到QQ成功") 
                        except Exception:
                            #print msg
                            print u"FAILED-发送给QQ好友和群组页面加载失败"
                        # 判断title包含
                        #title2 = EC.title_contains(u'QQ好友')
                        #print title2(wd)
                        wd.close()
                        wd.switch_to_window(oldpage_window)
        
                #获取老页面的窗口句柄
                #oldpage_window = wd.current_window_handle
                #分享至QQ空间
                wd.find_element_by_css_selector("a.bds_qzone").click()
                time.sleep(2)
                mid_handles = wd.window_handles
                for handle2 in mid_handles:
                    if handle2 != oldpage_window and handle2 != homepage_handle:
                        wd.switch_to_window(handle2)
                        if not("QQ空间" in wd.title):
                            success = False
                            print(u"FAILED-分享到QQ空间失败")
                        else:
                            print(u"PASS-分享到QQ空间成功") 
                        # 判断title包含
                        #title2 = EC.title_contains(u'QQ空间')
                        #print title2(wd)
                        wd.close()
                        wd.switch_to_window(oldpage_window)
                #获取老页面的窗口句柄
                #oldpage_window = wd.current_window_handle
                #分享至新浪微博
                wd.find_element_by_css_selector("a.bds_tsina").click()
                time.sleep(2)
                mid_handles = wd.window_handles
                for handle3 in mid_handles :
                    if handle3 != oldpage_window and handle3 != homepage_handle:
                        wd.switch_to_window(handle3)
                        if not("微博" in wd.title):
                            success = False
                            print(u"FAILED-分享到微博失败")
                        else:
                            print(u"PASS-分享到微博成功") 
                        # 判断title包含
                        #title2 = EC.title_contains(u'微博')
                        #print title2(wd)
                        wd.close()
                        wd.switch_to_window(oldpage_window)
                #分享至微信
                wd.find_element_by_css_selector("a.bds_weixin").click()
                time.sleep(2)
                if not ("分享到微信朋友圈" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print(u"FAILED-微信分享弹窗失败")
                else:
                    print(u"PASS-微信分享弹窗成功") 
                #关闭微信分享窗口
                wd.find_element_by_link_text("×").click()
                #关闭分享窗口
                wd.find_element_by_id("ShareClose").click()
                #点击上一篇
                wd.find_element_by_xpath(".//*[@id='up']").click()
                #点击下一篇
                wd.find_element_by_xpath(".//*[@id='go']").click()
                
                wd.close()
                wd.switch_to_window(homepage_handle)

        wd.find_element_by_link_text("雨后池上2f7dfda54ddc49b9bcb1276d5be00adb").click()
        all_handles = wd.window_handles
        for handle in all_handles:
            if handle != homepage_handle:
                wd.switch_to_window(handle)
                if not ("雨后池上" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print(u"FAILED-文章雨后池上展示失败")
                else:
                    print(u"PASS-文章雨后池上展示成功")
                wd.close()
                wd.switch_to_window(homepage_handle)
            
        self.assertTrue(success)

    def test_02_gx(self):
        '''核心素养-国学'''
        print u"开始测试！核心素养-国学"
        wd = self.wd
        success = True
        
        topmenu_t.top_menu_gxmw_s(self)
        #点击切换国学标签
        wd.find_element_by_id("5d260be0a59e11e680f576304dec7eb7").click()
        homepage_handle = wd.current_window_handle
        wd.find_element_by_xpath("//ul[@id='c_CataList']//span[.='《孝经》选读']").click()
        all_handles = wd.window_handles
        for handle in all_handles:
            if handle != homepage_handle:
                wd.switch_to_window(handle)
                if not ("《孝经》选读" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print(u"FAILED-国学《孝经》选读详情展示失败")
                else:
                    print(u"PASS-国学《孝经》选读详情展示成功")
                wd.close()
                wd.switch_to_window(homepage_handle)
        wd.find_element_by_xpath("//div[@id='c_Content']//span[.='四季如诗']").click()
        all_handles = wd.window_handles
        for handle in all_handles:
            if handle != homepage_handle:
                wd.switch_to_window(handle)
                if not ("四季如诗" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print(u"FAILED-国学四季如诗详情展示失败")
                else:
                    print(u"PASS-国学四季如诗详情展示成功")
                wd.close()
                wd.switch_to_window(homepage_handle)
            
        self.assertTrue(success)

    def test_03_qk(self):
        '''核心素养-期刊'''
        print u"开始测试！核心素养-期刊"
        wd = self.wd
        success = True
        
        topmenu_t.top_menu_gxmw_s(self)
        
        #切换期刊标签
        wd.find_element_by_id("5d26109aa59e11e680f576304dec7eb7").click()
        if (wd.find_element_by_xpath("//div[3]/div[2]/div[1]/img").is_displayed()):
            print(u"PASS-期刊初始化成功")
        else:
            success = False
            print(u"FAILED-期刊初始化失败")
        #切换期刊期数
        wd.find_element_by_id("img_1").click()
        wd.find_element_by_id("img_0").click()
        
        #定位到大图期刊元素        
        article = wd.find_element_by_xpath(".//*[@id='img_New']")  
        #鼠标悬浮在大图期刊位置
        ActionChains(wd).move_to_element(article).perform()
        #等待1秒
        time.sleep(1)
        #定位到文章
        mouse = wd.find_element_by_xpath(".//*[@id='c_MenuList']/li[1]/a")  
        #鼠标移动至文章上方悬浮
        ActionChains(wd).move_to_element(mouse).perform()
        time.sleep(1)
        homepage_handle = wd.current_window_handle
        #点击文章
        wd.find_element_by_xpath(".//*[@id='c_MenuList']/li[1]/a").click()
        time.sleep(1)
        #切换句柄
        all_handles = wd.window_handles
        for handle in all_handles:
            if handle != homepage_handle:
                wd.switch_to_window(handle)
                if not ("君子如水" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print(u"FAILED-期刊君子如水展示失败")
                else:
                    print(u"PASS-期刊君子如水展示成功")
                wd.close()
                wd.switch_to_window(homepage_handle)
            
        self.assertTrue(success)

    def test_04_zbym(self):
        '''走遍英美'''
        print u"开始测试！走遍英美"
        wd = self.wd
        success = True
        
        #切换至走遍英美页面
        topmenu_t.top_menu_zbym_s(self)
        time.sleep(1)
        homepage_handle = wd.current_window_handle
        #进入The Choice of Companion文章页面        
        wd.find_element_by_xpath("//div[@id='c_Content']//span[.='The Choice of Companion']").click()
        time.sleep(1)
        #切换句柄
        all_handles = wd.window_handles
        for handle in all_handles:
            if handle != homepage_handle:
                wd.switch_to_window(handle)
                if not ("The Choice of Companion" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print(u"FAILED-英语The Choice of Companion展示失败")
                else:
                    print(u"PASS-英语The Choice of Companion展示成功")
                wd.close()
                wd.switch_to_window(homepage_handle)
        wd.find_element_by_xpath("//div[@id='c_Content']//span[.='The Fast Food']").click()
        time.sleep(0.5)
        #切换句柄
        all_handles = wd.window_handles
        for handle in all_handles:
            if handle != homepage_handle:
                wd.switch_to_window(handle)
                if not ("The Fast Food" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print(u"FAILED-英语The Fast Food展示失败")
                else:
                    print(u"PASS-英语The Fast Food展示成功")
                wd.close()
                wd.switch_to_window(homepage_handle)
        homepage_handle = wd.current_window_handle
        #print homepage_handle

        self.assertTrue(success)

    def test_05_sxsw(self):
        '''数学思维'''
        print u"开始测试！数学思维"
        wd = self.wd
        success = True
        
        #切换到数学思维页面
        topmenu_t.top_menu_sxsw_s(self)
        
        if not ("数学思维" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-数学思维初始化失败")
        else:
            print(u"PASS-数学思维初始化成功")
        
        homepage_handle= wd.current_window_handle
        wd.find_element_by_xpath("//div[3]/div[1]/div[1]/ul/li[3]/a/p").click()
        time.sleep(0.5)
        #切换句柄
        all_handles = wd.window_handles
        for handle in all_handles:
            if handle != homepage_handle:
                wd.switch_to_window(handle)
                if not ("三招搞定有理数的巧妙运算" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print(u"FAILED-数学三招搞定有理数的巧妙运算展示失败")
                else:
                    print(u"PASS-数学三招搞定有理数的巧妙运算展示成功")
                wd.close()
                wd.switch_to_window(homepage_handle)
        
        wd.find_element_by_xpath("//div[3]/div[1]/div[4]/ul/li[3]/a/p").click()
        time.sleep(0.5)
        #切换句柄
        all_handles = wd.window_handles
        for handle in all_handles:
            if handle != homepage_handle:
                wd.switch_to_window(handle)
                if not ("正方体的十一种表面展开图及找相对面的技巧" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print(u"FAILED-数学正方体的十一种表面展开图及找相对面的技巧展示失败")
                else:
                    print(u"PASS-数学正方体的十一种表面展开图及找相对面的技巧展示成功")
                wd.close()
                wd.switch_to_window(homepage_handle)

        #调用退出接口
        self.assertTrue(success)
    
    def tearDown(self):
        #将滚动条移动到页面的顶部
        js="var q=document.documentElement.scrollTop=0"
        self.wd.execute_script(js)
        
        logout.logout_s(self)
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
