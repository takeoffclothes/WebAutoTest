'''
Created on 2018年1月29日
updated on 2018年2月7日
五好导学网-老师web端-个人中心 自动化测试脚本
@author: 闫双双
2018年2月25日  老师-个人中心-签到--修改判断已签到1天改为已签到
               老师-个人中心---修改登录调用
               老师-个人中心-充值中心--修改微信支付
2018年5月17日  老师-个人中心  所有功能脚本在判断后面添加success = False语句
2018年6月19日  老师-个人中心-个人资料修改  将教材修改为七年级下册
2018年7月18日  老师-个人中心 修改v1.4版本个人中心页面和个人资料改版问题
2018年9月4日   老师-个人中心-删除去认证功能
               老师-个人中心-头像上传  投稿  礼券  私人订制PPT，修改1.5版本导致的菜单问题
2018年11月19日   老师-个人中心-删除签到，金币，礼券功能
'''

# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest
import sys, os
from Constant.sys_constant import *
from test_case.PubModule import login ,topmenu_t

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_TPersonalCenter(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        success = True
        wd = self.wd
        # 登录测试环境
        wd.get(LOGIN_URL)

    # 个人中心-上传个人头像

    def test_01PerCen_UploadPicture(self):
        print("开始测试个人中心-上传头像")
        success = True
        wd = self.wd
        # 调用login()函数登录
        login.login(self, "19600000071", "123456")
        # 判断登录是否成功
        if not ("首页" in wd.find_element_by_xpath(".//*[@id='Header']/header/div/nav/ul/li[1]/a").text):
            print("FAILED-登录失败！")
            success = False
        else:
            print("SUCCESS-登录成功！")
        # 定位首页头像并点击个人中心菜单
        time.sleep(2)
        topmenu_t.top_menu_grzx(self)
        # 判断是否进入个人中心页面
        if not ("个人资料" in wd.find_element_by_tag_name("html").text):
            print("FAILED-进入个人中心失败！")
            success = False
        else:
            print("SUCCESS-进入个人中心成功！")
        # 点击头像上传
        wd.find_element_by_class_name("personal_center_info_headimg").click()
        # 点击选择文件
        wd.find_element_by_xpath(".//*[@id='inputImage']").click()
        # 利用autoit工具上传图片
        os.system(autoitfile_path+"uploadpicture.exe")
        time.sleep(4)
        # 点击保存
        wd.find_element_by_xpath(".//*[@id='GetImgUrl']").click()
        time.sleep(1)
        # 判断保存是否成功
        if not ("保存成功" in wd.find_element_by_xpath(".//*[@id='c_ErrorMsg']").text):
            print("FAILED-头像上传失败！")
            success = False
        else:
            print("SUCCESS-头像上传成功")
        time.sleep(2)
        self.assertTrue(success)

    # 个人中心-个人资料修改

    def test_02PerCen_PesonalData(self):
        print("开始测试个人中心-个人资料修改")
        success = True
        wd = self.wd
        # 调用login()函数登录
        login.login(self, "19600000071", "123456")
        # 判断登录是否成功
        if not ("首页" in wd.find_element_by_xpath(".//*[@id='Header']/header/div/nav/ul/li[1]/a").text):
            print("FAILED-登录失败！")
            success = False
        else:
            print("SUCCESS-登录成功！")
        # 定位首页头像并点击个人中心菜单
        topmenu_t.top_menu_grzx(self)
        # 点击个人资料
        wd.find_element_by_xpath(".//*[@id='personal_center']/div/dl/dt[2]").click()
        # 判断是否正常进入个人资料页面
        if not ("基本资料" in wd.find_element_by_xpath(".//*[@id='personal_data']/div[1]/p/span[1]").text):
            print("FAILED-进入个人资料页面失败！")
            success = False
        else:
            print("SUCCESS-进入个人资料页面成功！")
        # 点击编辑
        wd.find_element_by_xpath(".//*[@id='m_Editit']/span[1]").click()
        # 编辑
        # 点击修改性别
        wd.find_element_by_xpath(".//*[@id='InfoEdit']/div[2]/span[2]").click()
        wd.find_element_by_xpath(".//*[@id='InfoEdit']/div[2]/span[2]/ul/li[2]").click()
        time.sleep(1)
        # 点击生日
        wd.find_element_by_xpath(".//*[@id='selectDate']").click()
        #选择年份
        wd.find_element_by_xpath(".//*[@id='ui-datepicker-div']/div[1]/div/select[1]").click()
        wd.find_elements_by_css_selector(".ui-datepicker-year>option")[0].click()
        #选择月份
        wd.find_element_by_xpath(".//*[@id='ui-datepicker-div']/div[1]/div/select[2]").click()
        wd.find_elements_by_css_selector(".ui-datepicker-month>option")[0].click()
        #选择日
        wd.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[1]/td[1]/a").click()
        time.sleep(1)
        # 点击修改教材
        wd.find_element_by_xpath(".//*[@id='InfoEdit']/div[4]/div[2]").click()
        wd.find_element_by_xpath(".//*[@id='m_MaterialList']/li[3]").click()
        time.sleep(1)
        # 点击确定
        wd.find_element_by_xpath(".//*[@id='EditEnsure']").click()
        time.sleep(1)
        # 判断是否编辑成功，跳转到登录页面
        #if not ("修改成功，请重新登录" in wd.find_element_by_xpath(".//*[@id='c_ErrorMsg']").text):
            #print("FAILED-编辑个人资料失败！")
            #success = False
        #else:
            #print("SUCCESS-编辑个人资料成功！")
        #time.sleep(3)
        self.assertTrue(success)

    '''个人中心-签到

    def test_03PerCen_SignIn(self):
        print("开始测试个人中心-签到")
        success = True
        wd = self.wd
        # 调用login()函数登录
        login.login(self, "19600000071", "123456")
        # 判断登录是否成功
        if not ("首页" in wd.find_element_by_xpath(".//*[@id='Header']/header/div/nav/ul/li[1]/a").text):
            print("FAILED-登录失败！")
            success = False
        else:
            print("SUCCESS-登录成功！")
        # 定位首页头像并点击个人中心菜单
        A = wd.find_element_by_xpath(".//*[@id='UserHeadImg']")
        ActionChains(wd).move_to_element(A).perform()
        time.sleep(3)
        wd.find_element_by_xpath(".//*[@id='menav']/li[2]/a").click()
        # 判断是否进入个人中心页面
        if not ("个人资料" in wd.find_element_by_xpath(".//*[@id='personal_center']/div/dl/dt[2]").text):
            print("FAILED-进入个人中心失败！")
            success = False
        else:
            print("SUCCESS-进入个人中心成功！")
        wd.maximize_window()
        time.sleep(3)
        if ("已签到" in wd.find_element_by_xpath(".//*[@id='personal_center']/div/div[1]/li[4]/span").text):
            print("今天已签到，明天再来签到吧！")
        else:
            print("今天还未签到，继续进行签到吧！")
            # 点击签到按钮
            wd.find_element_by_xpath(".//*[@id='personal_center']/div/div[1]/li[4]/span").click()
            time.sleep(1)
            # 判断签到是否成功
            if not ("签到成功" in wd.find_element_by_xpath(".//*[@id='c_ErrorMsg']").text):
                print("FAILED-签到失败！")
                success = False
            else:
                print("SUCCESS-签到成功")
        time.sleep(2)
        self.assertTrue(success)
    '''
    '''# 个人中心-去认证(该功能已删除)

    def test_04PerCen_Certification(self):
        print("开始测试个人中心-去认证")
        success = True
        wd = self.wd
        # 调用login()函数登录
        login.login(self, "19600000071", "123456")
        # 判断登录是否成功
        if not ("首页" in wd.find_element_by_xpath(".//*[@id='Header']/header/div/nav/ul/li[1]/a").text):
            print("FAILED-登录失败！")
            success = False
        else:
            print("SUCCESS-登录成功！")
        # 定位首页头像并点击个人中心菜单
        A = wd.find_element_by_xpath(".//*[@id='UserHeadImg']")
        ActionChains(wd).move_to_element(A).perform()
        time.sleep(3)
        wd.find_element_by_xpath(".//*[@id='menav']/li[2]/a").click()
        # 判断是否进入个人中心页面
        if not ("个人资料" in wd.find_element_by_xpath(".//*[@id='personal_center']/div/dl/dt[2]").text):
            print("FAILED-进入个人中心失败！")
            success = False
        else:
            print("SUCCESS-进入个人中心成功！")
        # 点击去认证按钮
        wd.find_element_by_xpath(".//*[@id='personal_center']/div/ul/li[3]/span[1]").click()
        # 判断是否成功进入去认证页面
        if not ("认证条件" in wd.find_element_by_xpath("html/body/article/div/div[3]/div[1]/h2").text):
            print("FAILED-进入认证页面失败！")
            success = False
        else:
            print("SUCCESS-进入认证页面成功！")
        time.sleep(2)
        self.assertTrue(success)
    '''
    '''个人中心-金币

    def test_05PerCen_GoldCoins(self):
        print("开始测试个人中心-金币")
        success = True
        wd = self.wd
        # 调用login()函数登录
        login.login(self, "19600000071", "123456")
        # 判断登录是否成功
        if not ("首页" in wd.find_element_by_xpath(".//*[@id='Header']/header/div/nav/ul/li[1]/a").text):
            print("FAILED-登录失败！")
            success = False
        else:
            print("SUCCESS-登录成功！")
        # 定位并点击进入个人中心
        A = wd.find_element_by_xpath(".//*[@id='UserHeadImg']")
        ActionChains(wd).move_to_element(A).perform()
        time.sleep(3)
        wd.find_element_by_xpath(".//*[@id='menav']/li[2]/a").click()
        # 判断是否进入个人中心页面
        if not ("个人资料" in wd.find_element_by_xpath(".//*[@id='personal_center']/div/dl/dt[2]").text):
            print("FAILED-进入个人中心失败！")
            success = False
        else:
            print("SUCCESS-进入个人中心成功！")
        time.sleep(2)
        # 点击金币
        wd.find_element_by_xpath(".//*[@id='personal_center']/div/div[2]").click()
        time.sleep(3)
        # 判断是否进入金币页面
        if not ("我的金币" in wd.find_element_by_xpath("html/body/article/div/div[3]/div[1]/h2/span").text):
            print("FAILED-金币页面展示不成功！")
            success = False
        else:
            print("SUCCESS-金币页面展示成功！")
        time.sleep(3)
        self.assertTrue(success)
    '''
    # 个人中心-投稿

    def test_06PerCen_Contribute(self):
        print("开始测试个人中心-投稿")
        success = True
        wd = self.wd
        wd.maximize_window()
        # 调用login()函数登录
        login.login(self, "19600000071", "123456")
        # 判断登录是否成功
        if not ("首页" in wd.find_element_by_xpath(".//*[@id='Header']/header/div/nav/ul/li[1]/a").text):
            print("FAILED-登录失败！")
            success = False
        else:
            print("SUCCESS-登录成功！")
        # 定位并点击进入个人中心
        topmenu_t.top_menu_grzx(self)
        # 判断是否进入个人中心页面
        if not ("个人资料" in wd.find_element_by_xpath(".//*[@id='personal_center']/div/dl/dt[2]").text):
            print("FAILED-进入个人中心失败！")
            success = False
        else:
            print("SUCCESS-进入个人中心成功！")
        time.sleep(2)
        # 点击投稿
        wd.find_element_by_xpath(".//*[@id='personal_center']/ul/li[1]/div[2]/div[1]").click()
        # 点击选择文件
        wd.find_element_by_xpath(".//*[@id='file']").click()
        # 调用文件上传
        os.system(autoitfile_path+"Knowledgesummary.exe")
        # 点击类型
        wd.find_element_by_xpath(".//*[@id='UpType']/span[3]").click()
        # 点击学科
        wd.find_element_by_xpath(".//*[@id='Submain']").click()
        time.sleep(1)
        # 选择数学学科
        wd.find_element_by_xpath(".//*[@id='Subject']/li[2]").click()
        # 点击教材
        wd.find_element_by_xpath(".//*[@id='materialMain']").click()
        time.sleep(1)
        # 点击人教版数学七年级上册
        wd.find_element_by_xpath(".//*[@id='070201']").click()
        # 点击标题并输入
        wd.find_element_by_xpath("html/body/div[2]/div[3]/div/form/div[5]/input").click()
        wd.find_element_by_xpath("html/body/div[2]/div[3]/div/form/div[5]/input").clear()
        wd.find_element_by_xpath("html/body/div[2]/div[3]/div/form/div[5]/input").send_keys("测试老师自动化投稿")
        time.sleep(1)
        # 点击简介并输入
        wd.find_element_by_xpath("html/body/div[2]/div[3]/div/form/div[6]/textarea").click()
        wd.find_element_by_xpath("html/body/div[2]/div[3]/div/form/div[6]/textarea").clear()
        wd.find_element_by_xpath("html/body/div[2]/div[3]/div/form/div[6]/textarea").send_keys("测试老师自动化投稿")
        time.sleep(1)
        # 点击上传按钮
        wd.find_element_by_xpath(".//*[@id='SubBtn']").click()
        time.sleep(1)
        # 判断是否上传成功
        if not ("上传成功" in wd.find_element_by_tag_name("html").text):
            print("FAILED-上传失败！")
            success = False
        else:
            print("SUCCESS-上传成功！")
        time.sleep(2)
        # 点击上传列表
        wd.find_element_by_xpath(".//*[@id='UpLIst']").click()
        time.sleep(2)
        # 点击上传规则
        wd.find_element_by_xpath("html/body/div[2]/div[3]/div/div[1]/span[3]").click()
        time.sleep(2)
        # 点击上传规则关闭
        wd.find_element_by_xpath("html/body/div[4]/div/i").click()
        time.sleep(2)
        self.assertTrue(success)

    ''' 个人中心-礼券

    def test_07PerCen_Gift(self):
        print("开始测试个人中心-礼券")
        success = True
        wd = self.wd
        # 调用login()函数登录
        login.login(self, "19600000071", "123456")
        # 判断登录是否成功
        if not ("首页" in wd.find_element_by_xpath(".//*[@id='Header']/header/div/nav/ul/li[1]/a").text):
            print("FAILED-登录失败！")
            success = False
        else:
            print("SUCCESS-登录成功！")
        # 定位并点击进入个人中心
        A = wd.find_element_by_xpath(".//*[@id='UserHeadImg']")
        ActionChains(wd).move_to_element(A).perform()
        time.sleep(3)
        wd.find_element_by_xpath(".//*[@id='menav']/li[2]/a").click()
        # 判断是否进入个人中心页面
        if not ("个人资料" in wd.find_element_by_xpath(".//*[@id='personal_center']/div/dl/dt[2]").text):
            print("FAILED-进入个人中心失败！")
            success = False
        else:
            print("SUCCESS-进入个人中心成功！")
        time.sleep(2)
        # 判断是否有可使用的礼券
        if (wd.find_element_by_xpath(".//*[@id='personal_center']/div/div[3]/span[1]").text == '0'):
            print("暂时没有可以使用的礼券！")
            # 点击礼券
            wd.find_element_by_xpath(".//*[@id='personal_center']/div/div[3]").click()
            time.sleep(3)
            # 判断是否进入礼券页面
            if not ("我的礼券" in wd.find_element_by_xpath("html/body/article/div/div[3]/div/h2").text):
                print("FAILED-进入礼券页面不成功！")
                success = False
            else:
                print("SUCCESS-进入礼券页面成功！")
        else:
            print("存在可以使用的礼券！")
            # 点击礼券
            wd.find_element_by_xpath(".//*[@id='personal_center']/div/div[3]").click()
            time.sleep(3)
            # 判断是否进入礼券页面
            if not ("我的礼券" in wd.find_element_by_xpath("html/body/article/div/div[3]/div/h2").text):
                print("FAILED-进入礼券页面不成功！")
                success = False
            else:
                print("SUCCESS-进入礼券页面成功！")
                # 点击立即使用按钮
                wd.find_element_by_xpath("html/body/article/div/div[3]/div/ul/li/input").click()
                time.sleep(2)
                # 判断是否成功进入私人订制页面
                print(wd.find_element_by_xpath(".//*[@id='m_OrderBtn']").text)
                if not ("购买记录" in wd.find_element_by_xpath("html/body/article/div/div[3]/div[1]/div/div/div/a").text):
                    print("FAILED-点击立即使用不成功！")
                    success = False
                else:
                    print("SUCCESS-点击立即使用成功！")
        time.sleep(3)
        self.assertTrue(success)
    '''
    '''个人中心-私人订制PPT

    def test_08PerCen_PPT(self):
        print("开始测试个人中心-私人订制PPT")
        success = True
        wd = self.wd
        # 调用login()函数登录
        login.login(self, "19600000071", "123456")
        # 判断登录是否成功
        if not ("首页" in wd.find_element_by_xpath(".//*[@id='Header']/header/div/nav/ul/li[1]/a").text):
            print("FAILED-登录失败！")
            success = False
        else:
            print("SUCCESS-登录成功！")
        # 定位并点击进入个人中心
        A = wd.find_element_by_xpath(".//*[@id='UserHeadImg']")
        ActionChains(wd).move_to_element(A).perform()
        time.sleep(3)
        wd.find_element_by_xpath(".//*[@id='menav']/li[2]/a").click()
        # 判断是否进入个人中心页面
        if not ("个人资料" in wd.find_element_by_xpath(".//*[@id='personal_center']/div/dl/dt[2]").text):
            print("FAILED-进入个人中心失败！")
            success = False
        else:
            print("SUCCESS-进入个人中心成功！")
        time.sleep(2)
        # 判断是否有可使用的礼券
        if (wd.find_element_by_xpath(".//*[@id='personal_center']/div/div[3]/span[1]").text == '0'):
            print("暂时没有可以使用的礼券！")
        else:
            print("存在可以使用的礼券！")
            # 点击私人订制
            wd.find_element_by_xpath(".//*[@id='personal_center']/ul/li[1]/div[1]/div[1]").click()
            time.sleep(2)
            # 判断是否进入私人订制页面
            if not ("购买记录" in wd.find_element_by_xpath("html/body/article/div/div[3]/div[1]/div/div/div/a").text):
                print("FAILED-进入私人订制页面不成功！")
                success = False
            else:
                print("SUCCESS-进入私人订制页面成功！")
                time.sleep(2)
                # 点击立即订制按钮
                wd.find_element_by_xpath(".//*[@id='m_OrderBtn']").click()
                time.sleep(2)
                # 点击使用代金券
                wd.find_element_by_xpath(".//*[@id='m_UsePpt1']").click()
                time.sleep(2)
                # 点击确定按钮
                wd.find_element_by_xpath(".//*[@id='m_GO']").click()
                time.sleep(2)
                # 点击输入手机号
                wd.find_element_by_xpath(".//*[@id='m_PhoneTel']").click()
                wd.find_element_by_xpath(".//*[@id='m_PhoneTel']").clear()
                wd.find_element_by_xpath(".//*[@id='m_PhoneTel']").send_keys("15552886411")
                time.sleep(2)
                # 点击输入QQ号
                wd.find_element_by_xpath(".//*[@id='QQ']").click()
                wd.find_element_by_xpath(".//*[@id='QQ']").clear()
                wd.find_element_by_xpath(".//*[@id='QQ']").send_keys("1941404619")
                time.sleep(2)
                # 点击输入微信
                wd.find_element_by_xpath(".//*[@id='weixin']").click()
                wd.find_element_by_xpath(".//*[@id='weixin']").clear()
                wd.find_element_by_xpath(".//*[@id='weixin']").send_keys("15552886411")
                time.sleep(2)
                # 点击输入要求
                wd.find_element_by_xpath(".//*[@id='m_TextIn']").click()
                wd.find_element_by_xpath(".//*[@id='m_TextIn']").clear()
                wd.find_element_by_xpath(".//*[@id='m_TextIn']").send_keys("我是自动化测试数据哈哈哈哈哈")
                time.sleep(2)
                # 点击确定按钮
                wd.find_element_by_xpath(".//*[@id='m_GoOn']").click()
                time.sleep(0.5)
                # 判断提交是否成功
                if not ("定制成功" in wd.find_element_by_xpath(".//*[@id='c_ErrorMsg']").text):
                    print("FAILED-定制失败！")
                    success = False
                else:
                    print("SUCCESS-定制成功！")
                wd.find_element_by_xpath(".//*[@id='c_Crum']/li[2]/a").click()
                time.sleep(2)

        # 判断金币是否充足
        if not (int(wd.find_element_by_xpath(".//*[@id='personal_center']/div/div[2]/span[1]").text) >= 2000):
            print("金币不足，请充值！")
            # 点击私人订制
            wd.find_element_by_xpath(".//*[@id='personal_center']/ul/li[1]/div[1]/div[1]").click()
            time.sleep(2)
            # 判断是否进入私人订制页面
            if not ("购买记录" in wd.find_element_by_xpath("html/body/article/div/div[3]/div[1]/div/div/div/a").text):
                print("FAILED-进入私人订制页面不成功！")
                success = False
            else:
                print("SUCCESS-进入私人订制页面成功！")
                time.sleep(2)
                # 点击立即订制按钮
                wd.find_element_by_xpath(".//*[@id='m_OrderBtn']").click()
                time.sleep(2)
                # 点击使用金币
                wd.find_element_by_xpath(".//*[@id='m_UsePpt0']").click()
                time.sleep(2)
                # 点击确定按钮
                wd.find_element_by_xpath(".//*[@id='m_GO']").click()
                time.sleep(2)
                # 点击请充值按钮
                wd.find_element_by_xpath(".//*[@id='m_PayMsg']/div/p/a").click()
                time.sleep(2)
                # 判断是否成功进入充值页面
                if not ("当前账户" in wd.find_element_by_xpath(".//*[@id='m_UserInfo']/span[1]").text):
                    print("FAILED-进入充值页面失败！")
                    success = False
                else:
                    print("SUCCESS-进入充值页面成功！")
                    time.sleep(2)
        else:
            print("金币充足，可以继续进行私人订制PPT！")
            time.sleep(2)
            # 点击私人订制
            wd.find_element_by_xpath(".//*[@id='personal_center']/ul/li[1]/div[1]/div[1]").click()
            time.sleep(2)
            # 判断是否进入私人订制页面
            if not ("购买记录" in wd.find_element_by_xpath("html/body/article/div/div[3]/div[1]/div/div/div/a").text):
                print("FAILED-进入私人订制页面不成功！")
                success = False
            else:
                print("SUCCESS-进入私人订制页面成功！")
                time.sleep(2)
                # 点击立即订制按钮
                wd.find_element_by_xpath(".//*[@id='m_OrderBtn']").click()
                time.sleep(2)
                # 点击使用金币
                wd.find_element_by_xpath(".//*[@id='m_UsePpt0']").click()
                time.sleep(2)
                # 点击确定按钮
                wd.find_element_by_xpath(".//*[@id='m_GO']").click()
                time.sleep(2)
                # 点击输入手机号
                wd.find_element_by_xpath(".//*[@id='m_PhoneTel']").click()
                wd.find_element_by_xpath(".//*[@id='m_PhoneTel']").clear()
                wd.find_element_by_xpath(".//*[@id='m_PhoneTel']").send_keys("15552886411")
                time.sleep(2)
                # 点击输入QQ号
                wd.find_element_by_xpath(".//*[@id='QQ']").click()
                wd.find_element_by_xpath(".//*[@id='QQ']").clear()
                wd.find_element_by_xpath(".//*[@id='QQ']").send_keys("1941404619")
                time.sleep(2)
                # 点击输入微信
                wd.find_element_by_xpath(".//*[@id='weixin']").click()
                wd.find_element_by_xpath(".//*[@id='weixin']").clear()
                wd.find_element_by_xpath(".//*[@id='weixin']").send_keys("15552886411")
                time.sleep(2)
                # 点击输入要求
                wd.find_element_by_xpath(".//*[@id='m_TextIn']").click()
                wd.find_element_by_xpath(".//*[@id='m_TextIn']").clear()
                wd.find_element_by_xpath(".//*[@id='m_TextIn']").send_keys("我是自动化测试数据哈哈哈哈哈")
                time.sleep(2)
                # 点击确定按钮
                wd.find_element_by_xpath(".//*[@id='m_GoOn']").click()
                time.sleep(0.5)
                # 判断提交是否成功
                if not ("定制成功" in wd.find_element_by_xpath(".//*[@id='c_ErrorMsg']").text):
                    print("FAILED-定制失败！")
                    success = False
                else:
                    print("SUCCESS-定制成功！")
                time.sleep(2)
        self.assertTrue(success)
    '''
    ''' 个人中心-充值中心

    def test_09PerCen_TopUp(self):
        print("开始测试个人中心-充值")
        success = True
        wd = self.wd
        # 调用login()函数登录
        login.login(self, "19600000071", "123456")
        # 判断登录是否成功
        if not ("首页" in wd.find_element_by_xpath(".//*[@id='Header']/header/div/nav/ul/li[1]/a").text):
            print("FAILED-登录失败！")
            success = False
        else:
            print("SUCCESS-登录成功！")
        # 定位并点击进入个人中心
        A = wd.find_element_by_xpath(".//*[@id='UserHeadImg']")
        ActionChains(wd).move_to_element(A).perform()
        time.sleep(3)
        wd.find_element_by_xpath(".//*[@id='menav']/li[2]/a").click()
        # 判断是否进入个人中心页面
        if not ("个人资料" in wd.find_element_by_xpath(".//*[@id='personal_center']/div/dl/dt[2]").text):
            print("FAILED-进入个人中心失败！")
            success = False
        else:
            print("SUCCESS-进入个人中心成功！")
        time.sleep(2)
        # 点击充值
        wd.find_element_by_xpath(".//*[@id='personal_center']/ul/li[2]/div[1]/div[1]").click()
        time.sleep(2)
        # 判断是否进入充值页面
        if not ("当前账户" in wd.find_element_by_xpath(".//*[@id='m_UserInfo']/span[1]").text):
            print("FAILED-进入充值页面不成功！")
            success = False
        else:
            print("SUCCESS-进入充值页面成功！")
        time.sleep(2)
        # 选择充值金额
        wd.find_element_by_xpath(".//*[@id='ActiveList']/li[2]").click()
        time.sleep(1)
        # 点击微信支付
        wd.find_element_by_xpath(".//*[@id='PayTypeList']/li[2]").click()
        time.sleep(1)
        # 点击立即支付
        wd.find_element_by_xpath(".//*[@id='m_PayBtn']").click()
        time.sleep(1)
        # 判断是否成功跳转到支付页面
        if not ("打开微信扫一扫" in wd.find_element_by_xpath(".//*[@id='WeiXin']/p").text):
            print("FAILED-微信支付出现支付二维码不成功！")
            success = False
        else:
            print("SUCCESS-微信支付出现支付二维码成功！")
        time.sleep(1)
        #点击关闭微信支付二维码
        wd.find_element_by_xpath(".//*[@id='m_WeiXinClose']").click()
        time.sleep(2)
        # 选择充值金额
        wd.find_element_by_xpath(".//*[@id='ActiveList']/li[3]").click()
        time.sleep(1)
        # 点击支付宝
        wd.find_element_by_xpath(".//*[@id='PayTypeList']/li[1]").click()
        time.sleep(1)
        # 点击立即支付
        wd.find_element_by_xpath(".//*[@id='m_PayBtn']").click()
        time.sleep(1)
        # 判断是否成功跳转到支付页面
        if not ("收款方" in wd.find_element_by_xpath(".//*[@id='order']/div[1]/div[2]/span[2]").text):
            print("FAILED-支付宝支付进入支付页面不成功！！")
            success = False
        else:
            print("SUCCESS-支付宝支付进入支付页面成功！！")
        time.sleep(2)

        self.assertTrue(success)
    '''
    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
