# coding：utf-8(定义源代码的编码:源代码的编码可以包含中文字符串)
# Created on 2018年1月29日
# updated on 2018年1月29日
# 五好导学网-老师web端-首页 自动化测试脚本
# 作者: 马春苗
#优化：王帅 针对教师端打开假期作业，使用说明是否默认打开加了判断 时间：2018.03.05

# 01banner：首页寒假作业banner验证-返回首页-首页期末复习banner验证-返回首页（未走流程：进入页面后的操作）
# 02课件：首页课件链接验证-“更多精彩”课件列表页初始化（未走流程：进入页面后的操作）
# 03作业：首页布置作业页面初始化-返回首页-批改作业页面初始化-返回首页-作业报告页面初始化（未走流程：进入页面后的操作）
# 04视频：首页视频详情页链接验证-“更多精彩”视频列表页初始化（未走流程：进入页面后的操作）
# 05文章：首页文章链接验证-“更多精彩”文章列表页初始化（未走流程：进入页面后的操作）


import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from Constant.sys_constant import *
from test_case.PubModule import login, logout


class test_homepage_t(unittest.TestCase):
    # 教师pc端-首页测试
    def setUp(self):
        # 定义浏览器下载配置
        #profile = webdriver.FirefoxProfile(Firefox_Path)
        # profile = webdriver.FirefoxProfile("C:\\Users\\Administrator\\AppData\\Local\\Mozilla\\Firefox\\Profiles\\pl3wrsan.default")
        # 定义浏览器，打开测试网站
        #self.wd = webdriver.Firefox(profile)
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.wd.get(LOGIN_URL)
        # self.wd.get("http://www.wuhaodaoxue.com")
        # 脚本运行时，错误的信息将被打印到这个列表中。
        self.verificationErrors = []
        # 是否继续接受下一下警告
        self.accept_next_alert = True
        wd = self.wd
        # 窗口最大化
        wd.maximize_window()
        # 登录正式账号17470000002
        login.login(self,"17470000002","123456")

    def test01_banner(self):
        # banner-寒假作业

        print("开始测试！首页banner")
        wd = self.wd
        success = True
        if not ("1500万师生检验的好作业" in wd.find_element_by_tag_name("html").text):
            success = False
            print("首页初始化失败")
        else:
            print("首页初始化成功")
        '''
        # 点击首页banner——寒假作业
        menu = wd.find_elements_by_class_name("totalnav")
        ActionChains(wd).move_to_element(menu[1]).perform()
        time.sleep(2)
        # wd.find_element_by_xpath(".//*[@id='Header']/header/div/nav/ul/li[3]/ul/li[5]/a").click()
        sonmenu = wd.find_elements_by_class_name("c_NavSecond")
        asonmenu = sonmenu[1].find_elements_by_tag_name("a")
        asonmenu[4].click()
        if ("block" in wd.find_element_by_class_name("usepop").get_attribute("style")):
            # 默认寒假作业说明弹窗关闭验证
            wd.find_element_by_xpath("//input[@class='know']").click()
            print("寒假作业说明关闭成功")
        elif("假期作业" in wd.find_element_by_class_name("Com_Crumbs_in").text):
            print("进入假期作业成功！")
        # 返回首页
        wd.find_element_by_xpath("//div[2]/div/a").click()
        if not ("1500万师生检验的好作业" in wd.find_element_by_tag_name("html").text):
            success = False
            print("返回首页失败！")
        else:
            print("返回首页成功！")
        time.sleep(2)
        
        print("开始测试！banner-期末复习")
        wd.find_element_by_class_name("swiper-container").click()
        time.sleep(2)
        if not ("复习" in wd.find_element_by_id("c_Crum1").text):
            print("进入期末复习失败")
        else:
            print("进入期末复习成功")
        time.sleep(2)
        '''
        # 点击首页banner——暑假新学期计划 即将开启
        print("开始测试！首页轮播图")
        #需要等待轮播图小圆圈出现.
        time.sleep(3)
        #下一页，下一页
        prevswiper = wd.find_element_by_xpath("//div[@class='swiper-button-prev swiper-button-white']")
        prevswiper.click()
        nextswiper = wd.find_element_by_xpath("//div[@class='swiper-button-next swiper-button-white']")
        nextswiper.click()
        #小圆点
        wd.find_element_by_xpath("//span[@class='swiper-pagination-bullet swiper-pagination-bullet-active']").click()
        #  轮播图点击功能未验证
        # if not ("单元" in wd.find_element_by_id("c_Kownledge").text):
        #     print("进入课件页失败")
        # else:
        #     print("进入课件页成功")
        time.sleep(2)
        self.assertTrue(success)

    def test02_courseware(self):
        # 首页-课件
        print("开始测试！首页-课件")
        wd = self.wd
        success = True
        # 获得当前窗口句柄
        homepage_window = wd.current_window_handle
        # 点击第一个课件
        wd.find_element_by_xpath("html/body/article/div/div[2]/div[2]/div[1]/div[2]/div/div[1]/a/img").click()
        time.sleep(2)
        # 获得当前所有打开的窗口的句柄
        all_handles = wd.window_handles
        # 进入课件窗口
        for handle in all_handles:
            if handle != homepage_window:
                wd.switch_to.window(handle)
                if not ("课件播放" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print("课件详情页初始化失败！")
                else:
                    print("课件详情页初始化成功！")
                wd.close()
                wd.switch_to.window(homepage_window)
        '''
        # 点击更多精彩
        wd.find_element_by_xpath("//a[@id='sort9']").click()
        if not ("第一单元" or "第二单元" in wd.find_element_by_tag_name("html").text):
            success = False
            print("更多课件失败！")
        else:
            print("更多课件成功！")
        '''
        self.assertTrue(success)

    def test03_work(self):
        # 首页-作业
        print("开始测试！首页-作业")
        wd = self.wd
        success = True
        # 进入布置作业页面
        wd.find_element_by_xpath("//a[@id='sort21']/div/img").click()
        time.sleep(0.5)
        if not ("布置作业" in wd.find_element_by_tag_name("html").text):
            success = False
            print("布置作业页面初始化失败！")
        else:
            print("布置作业页面初始化成功！")
        # 返回首页
        wd.find_element_by_xpath("//div[2]/div/a").click()
        time.sleep(0.5)
        # 进入批改作业页面
        wd.find_element_by_xpath("//a[@id='sort23']/div/img").click()
        if not ("批改" in wd.title):
            success = False
            print("批改作业页面初始化失败！")
        else:
            print("批改作业页面初始化成功！")
            time.sleep(0.5)
        # 返回首页
        wd.find_element_by_css_selector("a.fl").click()
        #wd.find_element_by_xpath("//div[2]/div/a").click()
        # 进入作业报告页面
        time.sleep(0.5)
        #wd.find_element_by_css_selector("a.fl.fc65").click()
        wd.find_element_by_xpath("//a[@id='sort25']/div/img").click()
        if not ("报告" in wd.title):
            success = False
            print("作业报告页面初始化失败！")
        else:
            print("作业报告页面初始化成功！")
        self.assertTrue(success)

    def test04_video(self):
        # 首页-视频
        print("开始测试！首页-视频")
        wd = self.wd
        success = True
        # 点击首页视频大图
        wd.find_element_by_xpath("//div[@class='clear']").send_keys(Keys.CONTROL+Keys.DOWN)
        wd.find_element_by_xpath("//div[@class='i_Video_max_wrap']/img").click()
        time.sleep(0.5)
        homepage_window = wd.current_window_handle
        # 获得当前所有打开的窗口的句柄
        all_handles = wd.window_handles
        # 进入视频窗口
        for handle in all_handles:
            if handle != homepage_window:
                wd.switch_to.window(handle)
                if not ("视频播放" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print("进入视频详情页失败！")
                else:
                    print("进入视频详情页成功！")
                wd.close()
                wd.switch_to.window(homepage_window)
        self.assertTrue(success)

    def test05_article(self):
        # 首页-国学美文
        print("开始测试！首页-国学美文")
        wd = self.wd
        success = True
        time.sleep(2)
        wd.find_element_by_xpath("//div[@class='clear']").send_keys(Keys.CONTROL+Keys.DOWN)
        if not ("美文常伴左右" in wd.find_element_by_tag_name("html").text):
            success = False
            print("进入首页失败！")
        homepage_window = wd.current_window_handle
        # 进入美文-三颗枸杞豆
        wd.find_element_by_xpath("//article/div/div[2]/div[5]/div[1]/div[2]/ul/li[2]/div/a").click()
        title = wd.find_element_by_xpath("//article/div/div[2]/div[5]/div[1]/div[2]/ul/li[2]/div/a").get_property("title")
        time.sleep(1)
        # 获得当前所有打开的窗口的句柄
        all_handles = wd.window_handles
        # 进入新窗口
        for handle in all_handles:
            if handle != homepage_window:
                wd.switch_to.window(handle)
                if not (title in wd.title):
                    success = False
                    print("进入美文详情页失败！")
                else:
                    print("进入美文详情页成功！")
                wd.close()
                wd.switch_to.window(homepage_window)
        # 点击更多精彩
        wd.find_element_by_xpath("html/body/article/div/div[2]/div[5]/div[1]/div[1]/a").click()
        if not ("美文" in wd.find_element_by_tag_name("html").text):
            success = False
            print("美文列表详情页初始化失败！")
        else:
            print("美文列表详情页初始化成功！")
        # 将滚动条移动到页面的顶部
        js = "var q=document.documentElement.scrollTop=0"
        wd.execute_script(js)
        self.assertTrue(success)

    def tearDown(self):
        # 将滚动条移动到页面的顶部
        js = "var q=document.documentElement.scrollTop=0"
        self.wd.execute_script(js)
        wd = self.wd
        logout.logout(self)
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
