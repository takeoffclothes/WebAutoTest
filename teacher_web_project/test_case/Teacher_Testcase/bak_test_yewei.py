#coding=utf-8
'''
Created on 2017年8月18日
updated on 2017年8月29日
五好导学网-页尾公共模块 自动化测试脚本
@author: 房立信
'''

from selenium import webdriver
import sys
sys.path.append('\PubModule')
#from test_case.PubModule import login
#from test_case.PubModule import logout
from ctypes.wintypes import HANDLE
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

class test_yewei(unittest.TestCase):
    '''教师pc端-页面底部二级菜单测试'''
    def setUp(self):
        #定义浏览器下载配置
        #profile = webdriver.FirefoxProfile("C:\\Users\\Administrator\\Application Data\\Mozilla\\Firefox\\Profiles\\nce5v0dx.default")
        #定义浏览器，打开测试网站
        #self.wd=webdriver.Firefox(profile)
        self.wd=webdriver.Firefox()
        self.wd.implicitly_wait(60)
        self.wd.get("http://www.wuhaodaoxue.com")
        self.wd.maximize_window()
        
    def test_yewei_gywm(self):
        '''页尾-关于我们'''
        success = True
        wd = self.wd
        print u"开始测试！页尾-关于我们"
        #点击关于我们
        wd.find_element_by_link_text("关于我们").click()
        if not ("五好导学网是山东百川图书有限公司面向全国中小学推出的一个专注于精品教学内容的互联网教育网站。" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-关于我们-验证页面文字失败")
        else:
            print(u"PASS-关于我们-验证页面文字通过")
        
        self.assertTrue(success)

    def test_yewei_qyhz(self):
        '''页尾-企业合作'''
        success = True
        wd = self.wd
        print u"开始测试：页尾-企业合作"
        #点击企业合作
        wd.find_element_by_link_text("企业合作").click()
        if not ("填写企业信息" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-企业合作-验证页面文字失败")
        else:
            print(u"PASS-企业合作-验证页面文字成功")

        print "开始测试：企业合作提交"
        #提交企业信息功能验证
        wd.find_element_by_id("Name").click()
        wd.find_element_by_id("Name").clear()
        wd.find_element_by_id("Name").send_keys(u"自动化测试")
        wd.find_element_by_id("UserName").click()
        wd.find_element_by_id("UserName").clear()
        wd.find_element_by_id("UserName").send_keys(u"房立信")
        wd.find_element_by_id("UserDuty").click()
        wd.find_element_by_id("UserDuty").clear()
        wd.find_element_by_id("UserDuty").send_keys(u"软件测试")
        wd.find_element_by_id("UserTell").click()
        wd.find_element_by_id("UserTell").clear()
        wd.find_element_by_id("UserTell").send_keys("18668933685")
        wd.find_element_by_id("Business").click()
        wd.find_element_by_id("Business").clear()
        wd.find_element_by_id("Business").send_keys(u"测试的信息，不用管。")
        wd.find_element_by_id("Purpose").click()
        wd.find_element_by_id("Purpose").clear()
        wd.find_element_by_id("Purpose").send_keys(u"测试的，直接删除")
        wd.find_element_by_css_selector("input.SubBtn").click()
        if not ("提交成功!" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-企业合作信息提交失败")
        else:
            print(u"PASS-企业合作信息提交成功")
            
        self.assertTrue(success)

    def test_yewei_xyhz(self):
        '''页尾-校园合作'''
        success = True
        wd = self.wd
        print u"开始测试：页尾-校园合作"
        #点击校园合作
        wd.find_element_by_link_text("校园合作").click()
        if not ("填写校园信息" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-校园合作-验证页面文字失败")
        else:
            print(u"PASS-校园合作-验证页面文字成功")

        print u"开始测试：校园合作提交"
        #提交校园信息功能验证
        wd.find_element_by_css_selector("div.AreaBox").click()
        wd.find_element_by_xpath("//ul[@id='ProVince']//li[.='山东省']").click()
        wd.find_element_by_id("CityCon").click()
        wd.find_element_by_xpath("//ul[@id='CityList']//li[.='济南市']").click()
        wd.find_element_by_css_selector("ul.List").click()
        wd.find_element_by_id("ContryCon").click()
        wd.find_element_by_xpath("//ul[@id='ContryList']//li[.='历下区']").click()
        wd.find_element_by_id("Name").click()
        wd.find_element_by_id("Name").clear()
        wd.find_element_by_id("Name").send_keys(u"自动化测试数据")
        wd.find_element_by_id("UserName").click()
        wd.find_element_by_id("UserName").clear()
        wd.find_element_by_id("UserName").send_keys(u"房立信")
        wd.find_element_by_id("UserDuty").click()
        wd.find_element_by_id("UserDuty").clear()
        wd.find_element_by_id("UserDuty").send_keys(u"测试")
        wd.find_element_by_id("UserTell").click()
        wd.find_element_by_id("UserTell").clear()
        wd.find_element_by_id("UserTell").send_keys("18600000000")
        wd.find_element_by_id("Purpose").click()
        wd.find_element_by_id("Purpose").clear()
        wd.find_element_by_id("Purpose").send_keys(u"自动化测试")
        wd.find_element_by_css_selector("input.SubBtn").click()
        if not ("提交成功!" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-校园合作信息提交失败")
        else:
            print(u"PASS-校园合作信息提交成功")
            
        self.assertTrue(success)
        
    def test_yewei_rczp(self):
        '''页尾-人才招聘'''
        success = True
        wd = self.wd
        print u"开始测试：页尾-人才招聘"
        #点击人才招聘
        wd.find_element_by_link_text("人才招聘").click()
        if not ("职位信息" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-人才招聘-验证页面文字失败")
        else:
            print(u"PASS-人才招聘-验证页面文字成功")
            
        self.assertTrue(success)
    def test_yewei_bzzx(self):
        '''页尾-帮助中心'''
        success = True
        wd = self.wd
        print u"开始测试：页尾-帮助中心"
            
        wd.find_element_by_link_text("帮助中心").click()
        if not ("常见问题" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-帮助中心-验证页面文字失败")
        else:
            print(u"PASS-帮助中心-验证页面文字成功")
        
        wd.find_element_by_xpath("//div[@class='ProblemsList']//li[.='学生注册']").click()
        if not ("登录【五好导学网】首页，新用户点击【注册】按钮" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-验证学生注册链接失败")
        else:
            print(u"PASS-验证学生注册链接成功")

        wd.find_element_by_xpath("//div[@class='ProblemsList']//li[.='头像修改']").click()
        if not ("第一步：鼠标滑入右上角头像位置，选择" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-验证头像修改链接失败")
        else:
            print(u"PASS-验证头像修改链接成功")

        wd.find_element_by_xpath("//div[@class='ProblemsList']//div[.='我是老师']").click()
        wd.find_element_by_xpath("//div[@class='ProblemsList']//li[.='身份认证']").click()
        if not ("只有认证的老师，才有下载网站资料的权限" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-验证我是老师-身份认证失败")
        else:
            print(u"PASS-验证我是老师-身份认证成功")
            
        wd.find_element_by_xpath("//div[@class='ProblemsList']//li[.='班级管理']").click()
        #点击转让班级
        wd.find_element_by_xpath("html/body/article/div/div/div[2]/ul/li[1]").click()
        if not ("选择【班级管理】，进入您所创建的班级" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-验证我是老师-班级管理-转让班级失败")
        else:
            print(u"PASS-验证我是老师-班级管理-转让班级成功")
            
        wd.find_element_by_css_selector("li.H_li.addcolor").click()
        wd.find_element_by_xpath("//ul[@class='H_conT']//li[.='邀请老师']").click()
        if not ("选择【班级管理】，进入您所创建的班级，点击【邀请】按钮" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-验证我是老师-班级管理-邀请老师失败")
        else:
            print(u"PASS-验证我是老师-班级管理-邀请老师成功")
            
        wd.find_element_by_xpath("//div[@class='ProblemsList']//li[.='作业流程']").click()
        wd.find_element_by_xpath("//ul[@class='H_conT']//li[.='作业报告']").click()
        if not ("选择【作业】-【作业报告】，进入相关界面" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-验证我是老师-作业流程-作业报告失败")
        else:
            print(u"PASS-验证我是老师-作业流程-作业报告成功")
            
        wd.find_element_by_xpath("//div[@class='ProblemsList']//span[.='我是学生']").click()
        wd.find_element_by_xpath("//div[@class='ProblemsList']//li[.='加入班级']").click()
        if not ("注册时已知班级码" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-验证我是学生-加入班级失败")
        else:
            print(u"PASS-验证我是学生-加入班级成功")

        self.assertTrue(success)
    def test_yewei_yjfk(self):
        '''页尾-意见反馈'''
        success = True
        wd = self.wd
        print u"开始测试：页尾-意见反馈"
            
        wd.find_element_by_link_text("意见反馈").click()
        if not ("意见反馈" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-意见反馈-验证页面文字失败")
        else:
            print(u"PASS-意见反馈-验证页面文字成功")
        wd.find_element_by_id("writeideas").click()
        wd.find_element_by_id("writeideas").clear()
        wd.find_element_by_id("writeideas").send_keys(u"自动化测试数据")
        wd.find_element_by_id("remineword").click()
        wd.find_element_by_id("remineword").clear()
        wd.find_element_by_id("remineword").send_keys("18600000000")
        wd.find_element_by_css_selector("input.SubBtn").click()
        if not ("提交成功!" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-意见反馈提交失败")
        else:
            print(u"PASS-意见反馈提交成功")
        self.assertTrue(success)

    def test_yewei_wbwxtb(self):
        '''页尾-新浪微博/百度贴吧'''
        success = True
        wd = self.wd
        print u"开始测试：新浪微博/百度贴吧"
        #获得当前窗口句柄
        homepage_window = wd.current_window_handle
        #点击新浪微博
        wd.find_element_by_css_selector(".Weibofocus").click()
        time.sleep(2) 
        #获得当前所有打开的窗口的句柄
        all_handles = wd.window_handles
        #进入课件窗口
        for handle in all_handles:
            if handle != homepage_window:
                wd.switch_to_window(handle)
                #print 'now xinlangweibo windows!'
                #print wd.title
                if not ("关注按钮" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print(u"FAILED-新浪微博窗口跳转失败")
                else:
                    print(u"PASS-新浪微博链接跳转成功")
                '''
                #此处内容为点击登录注册等操作，其实能打开窗口就可以了，下面的代码有些问题，暂时先不调试了，后续再说。
                #print wd.window_handles
                wd.find_element_by_xpath("//div[@class='login_form_container']/div[1]/input").send_keys("15305418685")
                time.sleep(1)
                wd.find_element_by_css_selector(".WB_input.input_password_note").send_keys("n123456")
                time.sleep(2)
                wd.find_element_by_xpath(".//*[@id='pl_follow_followframe']/div[2]/div[1]/div[1]").click()
                #点击取消下次自动登录
                if wd.find_element_by_css_selector("input.WB_checkbox2").is_selected():
                    wd.find_element_by_css_selector("input.WB_checkbox2").click()
                wd.find_element_by_link_text("登录并关注").click()
                if not ("山东百川图书有限公司" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print("FAILED-新浪微博登录注册失败")
                else:
                    print("PASS-新浪微博登录注册成功")
                '''
                time.sleep(2)
                wd.close()
                #print wd.window_handles
                wd.switch_to_window(homepage_window)
                #print wd.window_handles
                #print wd.title
        #贴吧
        #获得当前窗口句柄
        homepage_window = wd.current_window_handle
        #点击百度贴吧
        wd.find_element_by_xpath("//ul[@class='FooterIcoBox']/li[3]/a/img").click()
        #获得当前所有打开的窗口的句柄
        all_handles = wd.window_handles
        #进入课件窗口
        for handle in all_handles:
            if handle != homepage_window:
                #print wd.title
                wd.switch_to_window(handle)
                #print 'now 百度贴吧 windows!'
                #print wd.title
                time.sleep(2) 
                if not ("五好导学吧" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print(u"FAILED-百度贴吧跳转失败")
                else:
                    print(u"PASS-百度贴吧跳转成功")
#                wd.find_element_by_xpath(".//*[@id='ButtonFastFwd-Small14']").click()
                #print wd.window_handles
                wd.close()
                #print wd.window_handles
                wd.switch_to_window(homepage_window)
                #print wd.window_handles
                #print wd.title
        
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
