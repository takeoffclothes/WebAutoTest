#coding=utf-8
'''
Created on 2017年8月25日
updated on 2018年1月26日
五好导学网-学生web端-预习中心 自动化测试脚本
@author: 房立信
'''

from selenium import webdriver
import sys,os
a = os.path.abspath(__file__)  # 得到绝对路径
print(os.path.dirname(a))  # 得到上一层路径
base_dir = os.path.dirname(os.path.dirname(a))  # 得到上上一层路径
sys.path.append(base_dir)
#from robotide.widgets import dialog
#from pip._vendor.pkg_resources import msg
from test_case.PubModule import login
from  test_case.PubModule import logout
from  test_case.PubModule import topmenu_t
#from selenium.webdriver.firefox.webdriver import WebDriver
#from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.support import expected_conditions as EC
import time, unittest,os
'''
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)
'''
#对异常弹窗的处理
def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_yxzx_s(unittest.TestCase):
    '''学生pc端-预习中心'''
    def setUp(self):
        #os.system("D:\\selenium_upfile\\changeprofile.bat")
        #定义浏览器下载配置
        profile = webdriver.FirefoxProfile("C:\\Users\\Administrator\\Application Data\\Mozilla\\Firefox\\Profiles\\mhibaxf2.default")
        #关闭flash自动检查是否最新版本
        profile.set_preference("extensions.blocklist.enabled", "false")
        #激活flash插件
        profile.set_preference("plugin.state.flash", 2)
        #定义浏览器，打开测试网站
        self.wd=webdriver.Firefox(profile)
        self.wd.implicitly_wait(30)
        self.wd.get("http://www.wuhaodaoxue.com")
        #脚本运行时，错误的信息将被打印到这个列表中。
        self.verificationErrors = []
        #是否继续接受下一下警告
        self.accept_next_alert = True
        #self.wd.maximize_window()
        wd = self.wd
        #登录
        login.login(self,"17200007072", "1qaz@WSX")
        #检查是否登录成功
        if not (len(wd.find_elements_by_id("User")) != 0):
            print(u"FAILED-登录失败！")

    def test_01_ksp(self):
        '''预习中心-看视频'''
        print (u"开始测试！预习中心-看视频")
        wd = self.wd
        success = True
        
        #进入预习中心-看视频
        topmenu_t.top_menu_ksp_s(self)
        if not ("看视频" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-视频列表页面初始化失败")
        else:
            print(u"PASS-视频列表页面初始化成功")
        #切换章节目录
        wd.find_element_by_xpath("//div[@id='fn_subject_div']//span[.='语文']").click()
        wd.find_element_by_xpath("//article/div/div[3]/div/ul/li[2]/div/span[2]").click()
        wd.find_element_by_xpath("//article/div/div[3]/div/ul/li[2]/div/span[5]").click()
        wd.find_element_by_xpath("//article/div/div[3]/div/ul/li[3]/div/span[2]").click()
        if not ("品味《动物笑谈》的语言艺术" in wd.find_element_by_xpath("//ul[@class='v_list']//p[.='品味《动物笑谈》的语言艺术']").text):
            success = False
            print(u"FAILED-学科章节切换失败")
        else:
            print(u"PASS-学科章节切换成功")
        wd.find_element_by_xpath("html/body/article/div/div[3]/div/div/div/ul/li[1]/a/div/p[2]").click()
        if not ("17 动物笑谈" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-视频播放页面加载失败")
        else:
            print(u"PASS-视频播放页面初始化成功")
        time.sleep(1)  
        #调用 shipin.exe 测试视频操作
        os.system("D:\\selenium_upfile\\shipin_s.exe")
        
        #print wd.title
        #title = EC.title_is(u"视频播放")
        #print title(wd)
        #点击分享按钮
        wd.find_element_by_xpath("//div[@class='functions']/span[5]").click()
        if not ("分享给好友" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-分享给好友弹窗失败")
        else:
            print(u"PASS-分享给好友弹窗成功")

        #获取老页面的窗口句柄
        oldpage_window = wd.current_window_handle
        #print oldpage_window
        #分享至QQ好友
        wd.find_element_by_css_selector("a.bds_sqq").click()
        #隐形等待30秒钟
        self.wd.implicitly_wait(30)
        #切换页面，验证新页面，关闭新页面
        all_handles = wd.window_handles
        #print all_handles
        for handle in all_handles:
            if handle != oldpage_window:
                #print wd.title
                wd.switch_to_window(handle) 
                #print handle
                time.sleep(1)
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
                except Exception as msg:
                    print (msg)
                # 判断title包含
                #title2 = EC.title_contains(u'QQ好友')
                #print title2(wd)
                wd.close()
                wd.switch_to_window(oldpage_window)
        
        #获取老页面的窗口句柄
        oldpage_window = wd.current_window_handle
        #分享至QQ空间
        wd.find_element_by_css_selector("a.bds_qzone").click()
        time.sleep(3)
        all_handles = wd.window_handles
        for handle2 in all_handles:
            if handle2 != oldpage_window:
                wd.switch_to_window(handle2)
                # 判断title包含
                #title2 = EC.title_contains(u'QQ空间')
                #print title2(wd)
                if not("QQ空间" in wd.title):
                    success = False
                    print(u"FAILED-分享到QQ空间失败")
                else:
                    print(u"PASS-分享到QQ空间成功") 

                wd.close()
                wd.switch_to_window(oldpage_window)
        #获取老页面的窗口句柄
        oldpage_window = wd.current_window_handle
        #分享至新浪微博
        wd.find_element_by_css_selector("a.bds_tsina").click()
        time.sleep(3)
        all_handles = wd.window_handles
        for handle3 in all_handles:
            if handle3 != oldpage_window:
                wd.switch_to_window(handle3)
                # 判断title包含
                #title2 = EC.title_contains(u'微博')
                #print title2(wd)
                if not("微博" in wd.title):
                    success = False
                    print(u"FAILED-分享到微博失败")
                else:
                    print(u"PASS-分享到微博成功") 
                wd.close()
                wd.switch_to_window(oldpage_window)
        #分享至微信
        wd.find_element_by_css_selector("a.bds_weixin").click()
        if not ("分享到微信朋友圈" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-微信分享弹窗失败")
        else:
            print(u"PASS-微信分享弹窗成功") 
        #关闭微信分享窗口
        wd.find_element_by_link_text("×").click()
        #关闭分享窗口
        wd.find_element_by_id("ShareClose").click()
        
        #获取原有窗口句柄
        oldpage_handle = wd.current_window_handle
        #点击预习测试
        wd.find_element_by_link_text("预习测试").click()
        all_handles = wd.window_handles
        for handle in all_handles:
            if handle != oldpage_handle:
                wd.switch_to_window(handle)
                if not ("预习测试" in wd.title):
                    success = False
                    print(u"FAILED-预习测试页面初始化失败")
                else:
                    print(u"PASS-预习测试页面初始化成功")
                try:
                    wd.find_element_by_xpath("//div[2]/div[1]/ul/li[1]/ul/li[1]/ul/li[3]/p").click()
                except Exception as msg:
                    print ("没有找到第一道题。：%s" %msg)
                try:
                    wd.find_element_by_xpath("//div[2]/div[1]/ul/li[2]/ul/li[1]/ul/li[1]/p").click()
                except Exception as msg:
                    print ("没有找到第二道题。：%s" %msg)
                try:
                    wd.find_element_by_xpath("//div[2]/div[1]/ul/li[3]/ul/li[1]/ul/li[4]/p").click()
                except Exception as msg:
                    print ("没有找到第三道题。：%s" %msg)
                try:
                    wd.find_element_by_xpath("//div[2]/div[1]/ul/li[4]/ul/li[1]/ul/li[2]/p").click()
                except Exception as msg:
                    print ("没有找到第四道题。：%s" %msg)
                
                #定位到提交按钮
                #mouse = wd.find_element_by_xpath("html/body/div[2]/div[1]/ul/input")  
                #鼠标移动至提交按钮上方悬浮
                #ActionChains(wd).move_to_element(mouse).perform()
                #点击提交
                wd.find_element_by_xpath("html/body/div[2]/div[1]/ul/input").click()
                #如果对话框元素出现，点击任性提交
                try:
                    wd.find_elements_by_xpath("//span[@class='model_paper_false_correr']").click()
                except Exception:
                    print(u"PASS-正常提交")
                else:    
                    print(u"还有题没有成功作答,任性提交")
                #这里应该增加判断，如果出现弹框点击，如果不出现跳过。
                if not("wrong" or "right" in wd.find_elements_by_xpath("//div[2]/div[1]/ul/li[1]/ul/li[1]/div/p/span/img").get_attribute("src")):
                    success = False
                    print(u"FAILED-预习测试提交失败")
                else:
                    print(u"PASS-预习测试提交成功")
                time.sleep(1)
                try:
                    wd.close()
                except Exception as msg:
                    print (msg)
                wd.switch_to_window(oldpage_handle)
        ###！！！点赞测试
        ###！！！验证点赞测试
        #返回看视频列表                    
            
        self.assertTrue(success)

    def test_02_typ(self):
        '''预习中心-听音频'''
        print (u"开始测试！预习中心-听音频")
        wd = self.wd
        success = True
        
        #下面开始听音频
        #进入听音频页面
        topmenu_t.top_menu_typ_s(self)
        if not ("听音频" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-音频列表页面初始化失败")
        else:
            print(u"PASS-音频列表页面初始化成功")        
        wd.find_element_by_xpath("//article/div/div[3]/div[1]/div[2]/div[1]/ul/li[3]").click()
        if not ("9.从百草园到三味书屋" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-单元切换失败")
        else:
            print(u"PASS-单元切换成功")        
        wd.find_element_by_xpath("//article/div/div[3]/div[1]/div[2]/div[2]/ul/li[2]").click()
        if not ("10.再塑生命的人" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-课时切换失败")
        else:
            print(u"PASS-课时切换成功")      
        #点击播放按钮  
        wd.find_element_by_id("Isplay").click()
        wd.find_element_by_css_selector("div.ComPlayer-volume-button").click()
        wd.find_element_by_css_selector("div.ComPlayer-volume-button").click()
        wd.find_element_by_id("Isplay").click()
        print(u"warning-音频播放完成，目前未判断音频是否播放，后续需要增加")
        #！！！此处后期应加入如何判断音频是否播放的检查。
        wd.find_element_by_xpath("//ul[@id='SubjectList']//li[.='英语']").click()
        wd.find_element_by_xpath("//ul[@id='CategoryList']//li[.='单词']").click()
        wd.find_element_by_id("cbfe66420fad43dc868b087a6988f4d8").click()
        wd.find_element_by_css_selector("p.ThisTab").click()
        if not ("Starter Units" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-学科切换失败")
        else:
            print(u"PASS-学科切换成功")        
        wd.find_element_by_xpath("//ul[@id='CategoryList']//li[.='单词']").click()
        wd.find_element_by_id("f217ad5e3ebe466ca5936c4467b20870").click()
        wd.find_element_by_css_selector("p.ThisTab").click()
        if not ("Read" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-单元切换失败")
        else:
            print(u"PASS-单元切换成功")        

        wd.find_element_by_id("cbfe66420fad43dc868b087a6988f4d8").click()
        wd.find_element_by_xpath("//ul[@id='CategoryList']//li[.='单词']").click()
        wd.find_element_by_css_selector("p.ThisTab").click()
        if not ("good" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-单元切换失败")
        else:
            print(u"PASS-单元切换成功")     
        #点击播放   
        wd.find_element_by_id("MediaPlayBtn").click()
        #点击暂停
        wd.find_element_by_id("MediaPlayBtn").click()
        
        wd.find_element_by_xpath("//div[@id='WordTab']//p[.='Dictate']").click()
        if  (wd.find_element_by_xpath(".//*[@id='DictateSwiper']/div/div[1]/div[1]/ul/li[1]").is_displayed()):
            print(u"PASS-拼写切换成功")     
        else:
            success = False
            print(u"FAILED-拼写切换失败")
        wd.find_element_by_id("g").click()
        wd.find_element_by_id("o").click()
        wd.find_element_by_id("o").click()
        wd.find_element_by_id("d").click()
        
        time.sleep(1.5)
        wd.find_element_by_id("y").click()
        wd.find_element_by_id("g").click()
        wd.find_element_by_id("f").click()
        wd.find_element_by_id("f").click()
        wd.find_element_by_id("f").click()
        wd.find_element_by_id("d").click()
        wd.find_element_by_id("d").click()
        if  (wd.find_element_by_css_selector("p.LookAnswer").is_displayed()):
            print(u"PASS-拼写测试通过")     
        else:
            success = False
            print(u"FAILED-拼写测试失败")
        
        wd.find_element_by_css_selector("p.LookAnswer").click()
        if not ("morning" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-查看答案失败")
        else:
            print(u"PASS-查看答案通过")     
        wd.find_element_by_xpath("//ul[@id='CategoryList']//li[.='1b']").click()
        if not (len(wd.find_elements_by_xpath("//div[@id='ListenClose']/img")) != 0):
            success = False
            print(u"FAILED-切换听力文章失败")
        else:
            print(u"PASS-切换听力文章通过")     
        wd.find_element_by_xpath("//p[@class='ListenBtn']//span[.='查看文本']").click()
        if not ("1b  Listen and repeat" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-查看文本失败")
        else:
            print(u"PASS-查看文本通过")     
        wd.find_element_by_xpath("//p[@class='ListenBtn']//span[.='收起文本']").click()
        #点击播放
        wd.find_element_by_id("Eng-Isplay").click()
        #点击音量关
        wd.find_element_by_css_selector("div.EngPlayer-volume-button").click()
        #点击音量开
        wd.find_element_by_css_selector("div.EngPlayer-volume-button").click()
        #点击暂停
        wd.find_element_by_id("Eng-Isplay").click()
        print(u"warning-音频播放完成，目前未判断音频是否播放，后续需要增加")
        #切换第二单元
        wd.find_element_by_xpath("//article/div/div[3]/div[1]/div[2]/div[1]/ul/li[3]").click()
        wd.find_element_by_xpath("//ul[@id='CategoryList']//li[.='单词']").click()
        wd.find_element_by_css_selector("p.ThisTab").click()
        #切换栏目2d
        wd.find_element_by_xpath("//ul[@id='CategoryList']//li[.='2d']").click()
        #点击播放
        wd.find_element_by_id("Eng-Isplay").click()
        #点击音量关
        wd.find_element_by_css_selector("div.EngPlayer-volume-button").click()
        #点击音量开
        wd.find_element_by_css_selector("div.EngPlayer-volume-button").click()
        #点击暂停
        wd.find_element_by_id("Eng-Isplay").click()
        if not ("Sally: Oh, Jane, this is my sister Kate." in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-歌词同步文档展示失败")
        else:
            print(u"PASS-歌词同步文档展示成功")     
            
        #退出登录
        self.assertTrue(success)
    
    def tearDown(self):
        logout.logout_s(self)
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
