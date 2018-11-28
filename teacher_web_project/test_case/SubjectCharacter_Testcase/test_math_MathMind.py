# -*- coding: utf-8 -*-
'''
Created on 2018年2月2日
updated on 2018年8月30日  v1.5版本修改
五好导学网-教师web端-数学思维(拓展提升） 自动化测试脚本
@author: 阎恩明
'''
from test_case.PubModule import logout,login
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from Constant.sys_constant import *
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_math_MathMind(unittest.TestCase):
    #初始化&登录
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)
        self.wd.get(LOGIN_URL)

    def test_MathMind(self):
        success = True
        wd = self.wd
        login.login(self,"14200070002","123456")
        if not (len(wd.find_elements_by_id("User")) != 0):
            success = False
            print(u"FAILED-登录失败！")
        print(u"开始测试数学-数学思维")
        #点击导航-数学思维
        time.sleep(2)
        wd.find_element_by_xpath(".//*[@id='Header']/header/div/nav/ul/li[7]").click()
        if ("数学思维" in wd.find_element_by_xpath(".//*[@id='c_Crum']/li[2]").text):
            print('Pass-成功打开数学思维列表页')
            index_handle=self.wd.current_window_handle
        else:
            success=False
            print('Failed-打开数学思维列表页失败')
        #文章列表页的下载功能
        #定位到第一篇文章
        mouse = wd.find_element_by_xpath("html/body/article/div/div[2]/div[2]/div[1]/div[3]/li[1]/a/p")
        #鼠标移动到第一篇文章的标题悬浮-出现“下载”按钮
        ActionChains(wd).move_to_element(mouse).perform()
        #点击下载按钮
        #wd.find_element_by_xpath("html/body/article/div/div[2]/div[2]/div[1]/div[3]/li[1]/div/span[1]").click()
        #点击文章名《有理数的大小比较方法选用》打开文章详情页
        time.sleep(2)
        print('尝试打开文章《命题、定义、基本事实、定理的简单理》详情页')
        chapter = wd.find_elements_by_class_name("learn_titleBox")
        chapter1 = chapter[0].find_elements_by_tag_name("li")
        chapter1[0].click()
        #进入多窗口操作
        # 获取打开的多个窗口句柄
        windows = self.wd.window_handles
        # 切换到当前最新打开的窗口
        self.wd.switch_to.window(windows[-1])
        time.sleep(2)
        if ("判断一件事情的语句" in wd.find_element_by_tag_name("html").text):
            print('Pass-打开文章详情《命题、定义、基本事实、定理的简单理》成功')
            article_handle=self.wd.current_window_handle
        else:
            success=False
            print('Failed-打开文章详情《命题、定义、基本事实、定理的简单理》失败')
        #下一篇切换功能
        time.sleep(3)
        print("开始测试'下一篇'切换功能")
        wd.find_element_by_xpath(".//*[@id='isdown']").click()
        if ("轻松学习平行线与相交线" in wd.find_element_by_tag_name("html").text):
            print('Pass-下一篇切换成功')
        else:
            success=False
            print('Failed-下一篇切换失败')
        #上一篇切换功能
        time.sleep(3)
        print("开始测试'上一篇'切换功能")
        wd.find_element_by_xpath(".//*[@id='isup']").click()
        if ("判断一件事情的语句" in wd.find_element_by_tag_name("html").text):
            print('Pass-上一篇切换成功')
        else:
            success=False
            print('Failed-上一篇切换失败')
        time.sleep(2)
        #下载
        #wd.find_element_by_xpath("html/body/article/div[1]/div[1]/div/div[4]/p[2]").click()
        '''
        #分享功能
        time.sleep(3)
        print("开始测试分享功能")
        wd.find_element_by_xpath(".//*[@id='c_Share']").click()
        if ("分享给好友" in wd.find_element_by_tag_name("html").text):
            print('Pass-分享弹窗显示成功')
        else:
            success=False
            print('Failed-分享弹窗显示失败')
        #分享给QQ好友
        print("分享给QQ好友")
        time.sleep(2)
        wd.find_element_by_class_name("bds_sqq").click()
        #等待3秒钟
        time.sleep(3)
        #切换页面，验证新页面，关闭新页面
        all_handles = wd.window_handles
        #print all_handles
        for handle in all_handles:
            if handle != index_handle and handle != article_handle:
                #print wd.title
                wd.switch_to.window(handle)
                #print handle
                time.sleep(1)
                #切回原页面
                wd.switch_to.default_content()
                #判断title是否完全等于“发给QQ好友和群组”
                #title1 = EC.title_is(u"发送给QQ好友和群组")
                #print(self.wd.title)
                if (self.wd.title != "发送给QQ好友和群组"):
                    print (u"FAILED-打开QQ好友分享页面失败")
                    success = False
                else:
                    print (u"PASS-打开QQ好友分享页面成功")
                wd.close()
                wd.switch_to.window(article_handle)

        #分享到QQ空间
        print("分享到QQ空间")
        time.sleep(2)
        wd.find_element_by_class_name("bds_qzone").click()
        #等待3秒钟
        time.sleep(3)
        #切换页面，验证新页面，关闭新页面
        all_handles = wd.window_handles
        #print all_handles
        for handle in all_handles:
            if handle != index_handle and handle != article_handle:
                #print wd.title
                wd.switch_to.window(handle)
                #print handle
                time.sleep(1)
                #切回原页面
                wd.switch_to.default_content()
                #判断title是否完全等于“发给QQ好友和群组”
                #print(self.wd.title)
                if (self.wd.title != "分享到QQ空间"):
                    print (u"FAILED-打开QQ空间分享页面失败")
                    success = False
                else:
                    print (u"PASS-打开QQ空间分享页面成功")
                wd.close()
                wd.switch_to.window(article_handle)

        #分享到新浪微博
        print("分享到新浪微博")
        time.sleep(2)
        wd.find_element_by_class_name("bds_tsina").click()
        #等待3秒钟
        time.sleep(3)
        #切换页面，验证新页面，关闭新页面
        all_handles = wd.window_handles
        #print all_handles
        for handle in all_handles:
            if handle != index_handle and handle != article_handle:
                #print wd.title
                wd.switch_to.window(handle)
                #print handle
                time.sleep(1)
                #切回原页面
                wd.switch_to.default_content()
                #判断title是否包含“微博”
                title2=EC.title_contains(u"微博")
                #print(title2(wd)) 打印出来是true
                if (title2(wd)):
                    print(u"PASS-分享到新浪微博页面跳转成功")
                else:
                    print(u"FAILED-分享到新浪微博页面跳转失败")
                    success = False
                wd.close()
                wd.switch_to.window(article_handle)

        #分享到微信朋友圈
        print("分享到微信朋友圈")
        time.sleep(2)
        wd.find_element_by_class_name("bds_weixin").click()
        if not ("分享到微信朋友圈" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-分享到微信朋友圈弹框失败")
        else:
            print(u"PASS-分享到微信朋友圈弹框成功")
        # 关闭微信分享窗口
        wd.find_element_by_link_text("×").click()
        # 关闭分享窗口
        wd.find_element_by_id("ShareClose").click()
        #等待2秒钟
        '''
        time.sleep(3)
        #关闭当前窗口
        wd.close()
        #切换到第一个窗口-首页
        self.wd.switch_to.window(windows[0])
        print(u"开始跑退出")
        logout.logout(self)
        self.assertTrue(success)

    #退出模块
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()



