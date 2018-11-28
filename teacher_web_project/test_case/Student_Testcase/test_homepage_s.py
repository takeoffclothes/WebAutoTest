# coding：utf-8(定义源代码的编码:源代码的编码可以包含中文字符串)
# Created on 2018年1月29日
# updated on 2018年10月23日
# 五好导学网-学生web端-首页 自动化测试脚本
# 作者: 马春苗
# 优化：优化登录部分使用，使用公共登录模块；修改test02_work中写作业和看报告跳转验证方式

# 01banner：首页寒假作业banner验证-返回首页-首页复习测试banner验证-返回首页（未走流程：进入页面后的操作）
# 02写作业：写作业验证-返回首页-看报告验证-返回首页（未走流程：进入页面后的操作）
# 03视频：首页切换语文科目-视频详情页验证-返回首页-切换数学科目-视频详情页验证-返回首页-切换英语科目-视频详情页验证-切换“更多精彩”-视频列表页初始化（未走流程：进入页面后的操作）
# 04文章：首页语文文章验证-返回首页-切换数学科目-文章详情页验证-返回首页-切换英语科目-文章详情页验证-切换“更多精彩”（未走流程：进入页面后的操作）
# 05必刷题：首页必刷题数学科目链接验证-返回首页（未走流程：进入页面后的操作）



import time
import unittest
from selenium import webdriver
from Constant.sys_constant import *
from test_case.PubModule import login, logout


class test_homepage_s(unittest.TestCase):
    # 学生pc端-首页
    def setUp(self):
        #定义浏览器下载配置
        #profile = webdriver.FirefoxProfile(Firefox_Path)
        #profile = webdriver.FirefoxProfile("C:\\Users\\Administrator\\AppData\\Local\\Mozilla\\Firefox\\Profiles\\pl3wrsan.default")
        #定义浏览器，打开测试网站
        #self.wd=webdriver.Firefox(profile)
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.wd.get(LOGIN_URL)
        # self.wd.get("http://preprod-whdx.bcbook.cn/")##预生产环境
        #脚本运行时，错误的信息将被打印到这个列表中。
        self.verificationErrors = []
        #是否继续接受下一下警告
        self.accept_next_alert = True
        wd = self.wd
        # 窗口最大化
        wd.maximize_window()
        login.login(self, "17400007001", "123456")

    def test01_banner(self):
        # banner-寒假作业
        print("开始测试！首页初始化")
        wd = self.wd
        success = True
        # 调用login()函数登录
        # 登录学生账号:17400000071是正式账号;17200000000是测试账号18220000001是预生产账号
        if not ("1500万师生检验的好作业" in wd.find_element_by_tag_name("html").text):
            success = False
            print("首页初始化失败")
        else:
            print("首页初始化成功")
        '''
        #点击首页banner-复习测试
        print("开始测试！banner-复习测试")
        d = wd.find_elements_by_class_name("swiper-pagination-bullet")
        #print(len(d))
        d[0].click()
        c = wd.find_element_by_class_name("swiper-container")
        ActionChains(wd).move_to_element(c).perform()
        c.click()

        time.sleep(2)
        if not ("复习测试" in wd.find_element_by_tag_name("html").text):
            print("复习测试页初始化失败")
        else:
            print("复习测试页初始化成功")
        time.sleep(2)
        self.assertTrue(success)
        '''
    def test02_work(self):
        # 写作业、看报告测试
        print("开始测试！首页-写作业、看报告")
        wd = self.wd
        success = True

        homepage_handle = wd.current_window_handle
        # 点击写作业链接
        wd.find_element_by_xpath("//img[@src='/dist/images/homework.png']").click()
        time.sleep(1)
        all_handles = wd.window_handles
        for handle in all_handles:
            if handle != homepage_handle:
                wd.switch_to.window(handle)
                if ("写作业列表" != wd.title):
                    success = False
                    print("写作业跳转失败！")
                else:
                    print("写作业跳转成功！")
                wd.close()
                wd.switch_to.window(homepage_handle)
        if not ("1500万师生检验的好作业" in wd.find_element_by_tag_name("html").text):
            success = False
            print("返回首页失败！")
        time.sleep(2)
        # 点击看报告链接
        wd.find_element_by_xpath("//img[@src='/dist/images/Presentation.png']").click()
        time.sleep(1)
        all_handles = wd.window_handles
        for handle in all_handles:
            if handle != homepage_handle:
                wd.switch_to.window(handle)
                if ("看报告" != wd.title):
                    success = False
                    print("看报告跳转失败！")
                else:
                    print("看报告跳转成功！")
                wd.close()
                wd.switch_to.window(homepage_handle)

        if not ("1500万师生检验的好作业" in wd.find_element_by_tag_name("html").text):
            success = False
            print("返回首页失败！")

        self.assertTrue(success)
    def test03_video(self):
        # 首页-视频
        print("开始测试！首页-视频")
        wd = self.wd
        success = True

        homepage_handle = wd.current_window_handle
        subjectstr = ['语文', '数学', '英语', '物理','化学', '生物', '政治', '历史', '地理']
        print(len(subjectstr))
        for i in range(len(subjectstr)):
            subject_ul = wd.find_element_by_xpath("//ul[@class='subject_ul']")
            # 获取9个类型的学科元素
            subject = subject_ul.find_elements_by_xpath("li")
            subject[i].click()
            wd.find_element_by_xpath("//ul[@class='vedio_ul']/li[1]/img[1]").click()
            time.sleep(2)
            all_handles = wd.window_handles
            for handle in all_handles:
                if handle != homepage_handle:
                    wd.switch_to.window(handle)
                    if not ("视频播放" in wd.find_element_by_tag_name("html").text):
                        success = False
                        print(subjectstr[i]+"视频播放页初始化失败！")
                    else:
                        print(subjectstr[i]+"视频播放页初始化成功！")
                    wd.close()
                    wd.switch_to.window(homepage_handle)

            if not ("国家级研究课题，助力翻转课堂" in wd.find_element_by_tag_name("html").text):
                success = False
                print("返回首页失败！")
            pass
        wd.find_element_by_xpath("//div[@class='i_main']//a[.='更多精彩…']").click()
        time.sleep(2)
        all_handles = wd.window_handles
        for handle in all_handles:
            if handle != homepage_handle:
                wd.switch_to.window(handle)
                if not ("看视频" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print("视频列表页初始化失败！")
                else:
                    print("视频列表页初始化成功！")
                wd.close()
                wd.switch_to.window(homepage_handle)
        time.sleep(0.5)

        if not ("国家级研究课题，助力翻转课堂" in wd.find_element_by_tag_name("html").text):
            success = False
            print("返回首页失败！")
        #通过访问主页来定位到顶端，防止找不到头像无法退出
        self.wd.get(LOGIN_URL)
        time.sleep(1)
        self.assertTrue(success)
    def test04_coreliteracy(self):
        # 首页-核心素养
        print("开始测试！首页-核心素养")
        wd = self.wd
        success = True

        homepage_handle = wd.current_window_handle
        subjectstr = ['语文', '数学', '英语']
        for i in range(len(subjectstr)):
            subject_ul = wd.find_element_by_xpath("//ul[@class='across_subject_ul']")
            # 获取3个类型的学科元素
            subject = subject_ul.find_elements_by_xpath("li")
            #进入相应的学科
            subject[i].click()
            title = wd.find_element_by_xpath("//ul[@class='article_ul']/li[1]/a").text
            wd.find_element_by_xpath("//ul[@class='article_ul']/li[1]/a").click()
            time.sleep(2)
            all_handles = wd.window_handles
            for handle in all_handles:
                if handle != homepage_handle:
                    wd.switch_to.window(handle)
                    # print(wd.find_element_by_tag_name("html").text)
                    if not (title.strip() in wd.find_element_by_tag_name("html").text):
                        success = False
                        print(subjectstr[i] + "文章内容页初始化失败！")
                    else:
                        print(subjectstr[i] + "文章内容页初始化成功！"+title)
                    wd.close()
                    wd.switch_to.window(homepage_handle)

            if not ("刷题" in wd.find_element_by_tag_name("html").text):
                success = False
                print("返回首页失败！")
            pass
        wd.find_element_by_xpath("//ul[@class='across_subject_ul']/../a[text()='更多精彩…']").click()
        time.sleep(2)
        all_handles = wd.window_handles
        for handle in all_handles:
            if handle != homepage_handle:
                wd.switch_to.window(handle)
                if not ("走遍英美" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print("国学美文列表页初始化失败！")
                else:
                    print("国学美文列表页初始化成功！")
                wd.close()
                wd.switch_to.window(homepage_handle)
        time.sleep(0.5)

        if not ("走遍英美" in wd.find_element_by_tag_name("html").text):
            success = False
            print("返回首页失败！")
        # 通过访问主页来定位到顶端，防止找不到头像无法退出
        self.wd.get(LOGIN_URL)
        time.sleep(1)
        self.assertTrue(success)
    def test05_subject(self):
        '''首页-必刷题'''
        print ("开始测试！首页-必刷题")
        wd = self.wd
        success = True
  
        #点击必刷题-数学
        wd.find_element_by_css_selector("li.mu_Sub02").click()
        if not ("必刷题" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-数学必刷题页面初始化失败")
        else:
            print(u"PASS-数学必刷题页面初始化成功")

        self.assertTrue(success)
    def tearDown(self):
        logout.logout_s(self)
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
