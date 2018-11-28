#coding=utf-8
'''
Created on 2017年8月10日
updated on 2017年8月30日
五好导学网-教师web端-班级管理 自动化测试脚本
@author: 房立信
'''

from selenium import webdriver
import sys
import os
sys.path.append('\PubModule')
from test_case.PubModule import login
from test_case.PubModule import logout
from test_case.PubModule import topmenu_t
#from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

class test_mycenter(unittest.TestCase):
    '''教师pc端-个人中心模块'''
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
        #进入个人中心
        topmenu_t.top_menu_grzx(self)

    
    def test_01_ggtx(self):
        '''更改头像'''
        print u"开始测试！更改头像"
        wd = self.wd
        success = True
        if wd.title != "个人中心":
            success = False
            print(u"FAILED-个人中心页面初始化失败")
        else:
            print(u"PASS-个人中心页面初始化成功！")
        
        #定位到更改头像
        article = wd.find_element_by_xpath("html/body/article/div/div[3]/div/div[1]")  
        #鼠标悬浮在用户头像位置
        ActionChains(wd).move_to_element(article).perform()
        #等待2秒
        time.sleep(1.5)
        #更改头像
        try:
            wd.find_element_by_xpath(".//*[@id='m_ChangeImg']").click()
        except Exception,msg:
            print msg
        
        if not ("选择文件" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-准备添加附件失败")
        else:
            print(u"PASS-准备添加附件成功！")

        #点击选择文件
        wd.find_element_by_xpath(".//*[@id='inputImage']").click()
        #调用 upfile.exe 上传程序上传图片
        os.system("D:\\selenium_upfile\\upfile.exe")
        
        #wd.find_element_by_css_selector("span.cropper-face").click()
        wd.find_element_by_id("GetImgUrl").click()
        time.sleep(1)
        if not ("保存成功" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-更改头像失败")
        else:
            print(u"PASS-更改头像成功！")
        #等待5秒
        time.sleep(4)
        self.assertTrue(success)

    def test_02_grzl(self):
        '''个人资料'''
        print u"开始测试！个人资料"
        wd = self.wd
        success = True
        if wd.title != "个人中心":
            success = False
            print(u"FAILED-个人中心页面初始化失败")

        #点击个人资料，进入个人资料页面
        wd.find_element_by_css_selector(".fs18.fc58.fl.mr20").click()
        if not ("个人资料" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-个人资料页面初始化失败")
        else:
            print(u"PASS-个人资料页面初始化成功！")
        #点击编辑
        wd.find_element_by_xpath(".//*[@id='m_Editit']/span").click()
        wd.find_element_by_id("m_UserName").click()
        wd.find_element_by_id("m_UserName").clear()
        wd.find_element_by_id("m_UserName").send_keys(u"房-语7自动化测试1")
        #保存个人资料
        wd.find_element_by_id("EditEnsure").click()
        time.sleep(0.5)
        if not ("修改成功" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-基本资料修改失败")
        else:
            print(u"PASS-基本资料修改成功！")
                
        time.sleep(4)
        
        #再次修改个人资料，还原个人资料信息
        #用户登录
        login.login(self,"17200000071", "1qaz@WSX")
        #进入个人中心
        topmenu_t.top_menu_grzx(self)
        #点击个人资料，进入个人资料页面
        wd.find_element_by_css_selector(".fs18.fc58.fl.mr20").click()
        time.sleep(1)
        wd.find_element_by_xpath(".//*[@id='m_Editit']/span").click()
        wd.find_element_by_id("m_UserName").click()
        wd.find_element_by_id("m_UserName").clear()
        wd.find_element_by_id("m_UserName").send_keys(u"房-语7")
        #保存个人资料
        wd.find_element_by_id("EditEnsure").click()
        time.sleep(4)
        
        #密码修改
        #用户登录
        login.login(self,"17200000071", "1qaz@WSX")
        #进入个人中心
        topmenu_t.top_menu_grzx(self)
        #点击个人资料，进入个人资料页面
        wd.find_element_by_css_selector(".fs18.fc58.fl.mr20").click()
        time.sleep(1)

        #点击修改密码
        wd.find_element_by_xpath(".//*[@id='ChangePass']").click()
        wd.find_element_by_id("m_OldPass0").click()
        wd.find_element_by_id("m_OldPass0").clear()
        wd.find_element_by_id("m_OldPass0").send_keys("1qaz@WSX")
        wd.find_element_by_id("m_NewPass0").click()
        wd.find_element_by_id("m_NewPass0").clear()
        wd.find_element_by_id("m_NewPass0").send_keys("123456")
        wd.find_element_by_id("m_NewPass1").click()
        wd.find_element_by_id("m_NewPass1").clear()
        wd.find_element_by_id("m_NewPass1").send_keys("123456")
        wd.find_element_by_id("m_PassEnsureBtn").click()
        if not ("修改成功" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-修改密码失败")
        else:
            print(u"PASS-修改密码成功！")
        time.sleep(5)
        
        #使用新密码登录,将新密码还原为旧密码
        login.login(self,"17200000071", "123456")
        #进入个人中心
        topmenu_t.top_menu_grzx(self)
        #点击个人资料，进入个人资料页面
        wd.find_element_by_css_selector(".fs18.fc58.fl.mr20").click()
        time.sleep(1)

        #点击修改密码
        wd.find_element_by_xpath(".//*[@id='ChangePass']").click()
        wd.find_element_by_id("m_OldPass0").click()
        wd.find_element_by_id("m_OldPass0").clear()
        wd.find_element_by_id("m_OldPass0").send_keys("123456")
        wd.find_element_by_id("m_NewPass0").click()
        wd.find_element_by_id("m_NewPass0").clear()
        wd.find_element_by_id("m_NewPass0").send_keys("1qaz@WSX")
        wd.find_element_by_id("m_NewPass1").click()
        wd.find_element_by_id("m_NewPass1").clear()
        wd.find_element_by_id("m_NewPass1").send_keys("1qaz@WSX")
        wd.find_element_by_id("m_PassEnsureBtn").click()
        if not ("修改成功" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-密码还原失败")
        else:
            print(u"PASS-密码还原成功！")
        time.sleep(5)
        
        login.login(self,"17200000071", "1qaz@WSX")
        time.sleep(0.5)

        self.assertTrue(success)

    def test_03_qdjb(self):
        '''签到金币'''
        print u"开始测试！签到金币"
        wd = self.wd
        success = True
        if wd.title != "个人中心":
            success = False
            print(u"FAILED-个人中心页面初始化失败")
        
        #判断是否有签到按钮，如果有，点击否则点击金币，进入金币页面
        if not ("签到" in wd.find_element_by_tag_name("html").text):
            wd.find_element_by_id("ThisSign").click()
            if not ("签到成功！" in wd.find_element_by_tag_name("html").text):
                #success = False
                print(u"WARNING-签到失败")
            else:
                print(u"PASS-签到成功")
        #进入金币页面        
        wd.find_element_by_id("GoldImg").click()
        if not ("金币" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-金币列表初始化失败")
        else:
            print(u"PASS-金币列表初始化成功")
           
        self.assertTrue(success)

    def test_04_qdjb(self):
        '''私人定制ppt'''
        print u"开始测试！私人定制ppt"
        wd = self.wd
        success = True
        if wd.title != "个人中心":
            success = False
            print(u"FAILED-个人中心页面初始化失败")
                
        try:
            #进入私人定制PPT
            wd.find_element_by_xpath("html/body/article/div/div[3]/ul/li[1]/a").click()
        except Exception,msg:
            print msg
        if not ("售价：2000金币" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-私人定制PPT页面初始化失败")
        else:
            print(u"PASS-私人定制PPT页面初始化成功")
        #点击立即定制
        wd.find_element_by_id("m_OrderBtn").click()
#！！！点击取消，此处应添加上定制ppt的操作，牵扯到数据库及判断逻辑，暂时先放置这里，后续补充。
        wd.find_element_by_id("m_ChoCancel").click()
        wd.find_element_by_link_text("购买记录").click()
        wd.find_element_by_css_selector("span.m_PurPrice").click()
        if not ("购买记录" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-购买记录链接验证失败")
        else:
            print(u"PASS-购买记录链接验证成功")

        self.assertTrue(success)

    def test_05_tg(self):
        '''投稿'''
        print u"开始测试！投稿"
        wd = self.wd
        success = True
        if wd.title != "个人中心":
            success = False
            print(u"FAILED-个人中心页面初始化失败")
        
        #进入投稿
        wd.find_element_by_xpath("html/body/article/div/div[3]/ul/li[2]/a").click()
        if not ("投稿" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-投稿页面初始化失败")
        else:
            print(u"PASS-投稿页面初始化成功")
        wd.find_element_by_id("file").click()
        #调用autoit进行上传文件
        os.system("D:\\selenium_upfile\\upfile_tougao.exe")
        
        wd.find_element_by_xpath("//div[@id='UpType']//span[.='试题']").click()
        wd.find_element_by_xpath("//div[@id='Submain']/i").click()
        wd.find_element_by_xpath("//ul[@id='Subject']//li[.='数学']").click()
        wd.find_element_by_id("materialShow").click()
        wd.find_element_by_id("070201").click()
        wd.find_element_by_css_selector("input.m_captin_select").click()
        wd.find_element_by_css_selector("input.m_captin_select").clear()
        wd.find_element_by_css_selector("input.m_captin_select").send_keys(u"自动化测试")
        wd.find_element_by_css_selector("textarea.m_briefcl").click()
        wd.find_element_by_css_selector("textarea.m_briefcl").send_keys("\\9")
        wd.find_element_by_css_selector("textarea.m_briefcl").click()
        wd.find_element_by_css_selector("textarea.m_briefcl").clear()
        wd.find_element_by_css_selector("textarea.m_briefcl").send_keys(u"自动化测试文件")
        wd.find_element_by_id("SubBtn").click()
        time.sleep(2)
        if not ("上传成功" or "上传中" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-投稿失败")
        else:
            print(u"PASS-投稿成功")
       
        wd.find_element_by_id("UpLIst").click()
        if not ("上传列表" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-上传列表展示失败")
        else:
            print(u"PASS-上传列表展示成功")

        self.assertTrue(success)

    def test_06_czzx(self):
        '''充值中心'''
        print u"开始测试！充值中心"
        wd = self.wd
        success = True
        if wd.title != "个人中心":
            success = False
            print(u"FAILED-个人中心页面初始化失败")
        
#      #上传规则
#      wd.find_element_by_xpath("html/body/div[2]/div[3]/div/div[1]/span[3]").click()
#      time.sleep(1)
        #关闭上传规则
#      wd.find_element_by_css_selector(".spriteImg.c_ruleico.m_rule_dele.ml70").click()
        time.sleep(3)
        #进入充值中心
        wd.find_element_by_xpath("html/body/article/div/div[3]/ul/li[3]/a").click()
        wd.find_element_by_xpath("//ul[@id='ActiveList']//p[.='0.01元']").click()
        wd.find_element_by_xpath(".//*[@id='PayTypeList']/li[1]").click()
        #点击立即支付
        wd.find_element_by_id("m_PayBtn").click()
        time.sleep(5)
        if wd.title != "支付宝 - 网上支付 安全快速！":
            success = False
            print(u"FAILED-支付宝支付跳转失败")
        else:
            print(u"PASS-支付宝支付跳转成功")

        wd.back()
        wd.find_element_by_xpath("//ul[@id='ActiveList']//p[.='0.01元']").click()
        wd.find_element_by_xpath(".//*[@id='PayTypeList']/li[2]").click()
        #点击立即支付
        wd.find_element_by_id("m_PayBtn").click()
        time.sleep(0.5)
        if not ("打开微信扫一扫" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-弹出微信支付二维码失败")
        else:
            print(u"PASS-弹出微信支付二维码成功")
        
        self.assertTrue(success)

    def test_07_lj(self):
        '''礼券'''
        print u"开始测试！礼券"
        wd = self.wd
        success = True
        if wd.title != "个人中心":
            success = False
            print(u"FAILED-个人中心页面初始化失败")

        wd.find_element_by_id("ScoupIco").click()
        if not ("礼券" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-礼券列表展示失败")
        else:
            print(u"PASS-礼券列表展示成功")
        
        self.assertTrue(success)
    
    def tearDown(self):
        logout.logout(self)
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
