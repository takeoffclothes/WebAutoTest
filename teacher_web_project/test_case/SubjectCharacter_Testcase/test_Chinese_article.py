# -*- coding: utf-8 -*-
'''
Created on 2018年1月29日
updated on 2018年8月30日 v1.5版本修改
五好导学网-教师web端-国学美文 自动化测试脚本
@author: 阎恩明
房立信-20180510修复了文章更新产生的问题。
'''
'''
缺少：推荐
'''
from test_case.PubModule import login,logout
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

class test_Chinese_article(unittest.TestCase):
    #初始化&登录模块
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)
        self.wd.get(LOGIN_URL)
        wd.maximize_window()

    #语文-国学美文-美文
    def test_01Chinese_article_beautifulArticle(self):
        success = True
        wd = self.wd
        print(u"开始跑登录")
        login.login(self,"14200070001","123456")
        if not (len(wd.find_elements_by_id("User")) != 0):
            success = False
            print(u"FAILED-登录失败！")
        print("开始测试-语文-国学美文-美文")
        time.sleep(2)
        #定位到导航的国学美文
        article = wd.find_element_by_xpath(".//*[@id='Header']/header/div/nav/ul/li[7]")
        #鼠标停在国学美文
        ActionChains(wd).move_to_element(article).perform()
        time.sleep(3)
        #鼠标移动到二级导航-美文
        mouse = wd.find_element_by_xpath(".//*[@id='Header']/header/div/nav/ul/li[7]/ul/li[1]/a")
        #鼠标移动到二级导航-美文
        ActionChains(wd).move_to_element(mouse).perform()
        #点击二级导航-美文
        wd.find_element_by_xpath(".//*[@id='Header']/header/div/nav/ul/li[7]/ul/li[1]/a").click()
        #保存当前窗口句柄
        index_handle=self.wd.current_window_handle
        if ("美文" in wd.find_element_by_tag_name("html").text):
            print('Pass-成功打开美文列表页')
        else:
            success=False
            print('Failed-打开美文列表页失败')
        #点击文章名《春之怀古》打开文章详情页
        time.sleep(2)
        print('尝试打开文章“春之怀古”详情页')
        wd.find_element_by_xpath(".//*[@id='c_Content']/li[1]/div[1]/div/div[1]/ul/li[1]/a/span[1]").click()

        #进入多窗口操作
        # 获取打开的多个窗口句柄
        windows = self.wd.window_handles
        # 切换到当前最新打开的窗口
        self.wd.switch_to.window(windows[-1])
        time.sleep(1)
        if ("春之怀古" in wd.find_element_by_tag_name("html").text):
            print('Pass-打开文章详情《春之怀古》成功')
            article_handle=self.wd.current_window_handle
        else:
            success=False
            print('Failed-打开文章详情《春之怀古》失败')
        #下一篇切换功能
        time.sleep(3)
        print("开始测试'下一篇'切换功能")
        wd.find_element_by_xpath(".//*[@id='isdown']").click()
        if ("春天的梦" in wd.find_element_by_tag_name("html").text):
            print('Pass-下一篇切换成功')
        else:
            success=False
            print('Failed-下一篇切换失败')
        #上一篇切换功能
        time.sleep(3)
        print("开始测试'上一篇'切换功能")
        wd.find_element_by_xpath(".//*[@id='isup']").click()
        if ("春之怀古" in wd.find_element_by_tag_name("html").text):
            print('Pass-上一篇切换成功')
        else:
            success=False
            print('Failed-上一篇切换失败')
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
        '''
        #等待2秒钟
        time.sleep(3)
       #关闭当前窗口
        self.wd.close()
       #切换到第一个窗口---首页
        self.wd.switch_to.window(windows[0])
        logout.logout(self)
        self.assertTrue(success)

    #国学美文-国学
    def test_02Chinese_article_ChineseStudies(self):
        success = True
        wd = self.wd
        print(u"开始跑登录")
        login.login(self,"14200070001","123456")
        if not (len(wd.find_elements_by_id("User")) != 0):
            success = False
            print(u"FAILED-登录失败！")
        print("开始测试-语文-国学美文-国学")
        index_handle=self.wd.current_window_handle
        time.sleep(2)
        #定位到导航的国学美文
        article = wd.find_element_by_xpath(".//*[@id='Header']/header/div/nav/ul/li[7]")
        #鼠标停在国学美文
        ActionChains(wd).move_to_element(article).perform()
        time.sleep(3)
        #鼠标移动到二级导航-国学
        mouse = wd.find_element_by_xpath(".//*[@id='Header']/header/div/nav/ul/li[7]/ul/li[2]/a")
        ActionChains(wd).move_to_element(mouse).perform()
        #点击二级导航-国学
        wd.find_element_by_xpath(".//*[@id='Header']/header/div/nav/ul/li[7]/ul/li[2]/a").click()
        if ("国学" in wd.find_element_by_tag_name("html").text):
            print('Pass-成功打开国学列表页')
        else:
            success=False
            print('Failed-打开国学列表页失败')
        #点击文章名《增广贤文》打开文章详情页
        time.sleep(2)
        print('尝试打开文章《增广贤文》选读详情页')
        wd.find_element_by_xpath(".//*[@id='chinese_literature']/ul/li[1]/div/div/ul/li[1]/span").click()

        #进入多窗口操作
        # 获取打开的多个窗口句柄
        windows = self.wd.window_handles
        # 切换到当前最新打开的窗口
        self.wd.switch_to.window(windows[-1])
        time.sleep(2)
        if ("《增广贤文》选读" in wd.find_element_by_tag_name("html").text):
            print('Pass-打开文章详情《增广贤文》选读成功')
            article_handle=self.wd.current_window_handle
        else:
            success=False
            print('Failed-打开文章详情《增广贤文》选读失败')
        time.sleep(2)
        wd.close()
        self.wd.switch_to.window(windows[0])
        logout.logout(self)
        self.assertTrue(success)

    #国学美文--期刊
    def test_03Chinese_article_Periodical(self):
        success = True
        wd = self.wd
        print(u"开始跑登录")
        login.login(self,"14200070001","123456")
        if not (len(wd.find_elements_by_id("User")) != 0):
            success = False
            print(u"FAILED-登录失败！")
        print("开始测试-语文-国学美文-期刊")
        index_handle=self.wd.current_window_handle
        time.sleep(2)
        #定位到导航的国学美文
        article = wd.find_element_by_xpath(".//*[@id='Header']/header/div/nav/ul/li[7]")
        #鼠标停在国学美文
        ActionChains(wd).move_to_element(article).perform()
        time.sleep(3)
        #鼠标移动到二级导航-期刊
        mouse = wd.find_element_by_xpath(".//*[@id='Header']/header/div/nav/ul/li[7]/ul/li[3]/a")
        ActionChains(wd).move_to_element(mouse).perform()
        #点击二级导航-期刊
        wd.find_element_by_xpath(".//*[@id='Header']/header/div/nav/ul/li[7]/ul/li[3]/a").click()
        if ("期刊" in wd.find_element_by_tag_name("html").text):
            print('Pass-成功打开期刊列表页')
        else:
            success=False
            print('Failed-打开期刊列表页失败')
        time.sleep(2)
        print("开始测试切换期刊")
        #点击第二期
        wd.find_element_by_xpath(".//*[@id='img_1']").click()
        mouse=wd.find_element_by_xpath(".//*[@id='img_New']")
        ActionChains(wd).move_to_element(mouse).perform()
        if ("VR将怎样改变我们的生活" in wd.find_element_by_tag_name("html").text):
            print('Pass-切换期刊成功')
        else:
            success=False
            print('Failed-切换期刊失败')
        #点击文章名《VR将怎样改变我们的生活》打开文章详情页
        time.sleep(2)
        print('尝试打开当前期刊《VR将怎样改变我们的生活》详情页')
        #点击期刊中的文章《VR将怎样改变我们的生活》
        wd.find_element_by_xpath(".//*[@id='c_MenuList']/li[2]/a").click()
        time.sleep(2)
        #进入多窗口操作
        # 获取打开的多个窗口句柄
        windows = self.wd.window_handles
        # 切换到当前最新打开的窗口
        self.wd.switch_to.window(windows[-1])
        time.sleep(3)
        if ("VR将怎样改变我们的生活" in wd.find_element_by_tag_name("html").text):
            print('Pass-打开期刊文章详情《VR将怎样改变我们的生活》成功')
            article_handle=self.wd.current_window_handle
        else:
            success=False
            print('Failed-打开期刊文章详情《VR将怎样改变我们的生活》失败')
        time.sleep(3)
        wd.close()
        self.wd.switch_to.window(windows[0])
        logout.logout(self)
        self.assertTrue(success)


    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
