# coding：utf-8(定义源代码的编码:源代码的编码可以包含中文字符串)
# Created on 2018年1月30日
# updated on 2018年1月31日
# 五好导学网-学生web端-核心素养 自动化测试脚本
# 作者: 马春苗

# 01美文：导航菜单-文章详情页初始化-上/下一篇（未走流程：名师指点）
# 02国学：导航菜单-切换至国学标签页-文章详情页初始化(未走流程：分享功能）
# 03期刊：导航菜单-切换至期刊标签页-切换期刊-文章详情页初始化（未走流程：分享功能、上下篇切换）
# 04走遍英美：导航菜单-文章详情页初始化-上/下一篇（未走流程：查看翻译按钮、分享功能、上下篇切换、音频播放）
# 05数学思维：首页必刷题数学科目链接验证-返回首页（未走流程：分享功能、上下篇切换）


import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from Constant.sys_constant import *
from test_case.PubModule import login, topmenu_t


class test_keycompetence_s(unittest.TestCase):
    # 学生pc端-核心素养

    def setUp(self):
        # 定义浏览器下载配置
        #profile = webdriver.FirefoxProfile(Firefox_Path)
        #profile = webdriver.FirefoxProfile("C:\\Users\\Administrator\\AppData\\Local\\Mozilla\\Firefox\\Profiles\\pl3wrsan.default")
        # 定义浏览器，打开测试网站
        #self.wd = webdriver.Firefox(profile)
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.wd.get(LOGIN_URL)
        # self.wd.get("http://whdx.bcbook.cn/")
        # self.wd.get("http://preprod-whdx.bcbook.cn/")
        # 脚本运行时，错误的信息将被打印到这个列表中。
        self.verificationErrors = []
        # 是否继续接受下一下警告
        self.accept_next_alert = True
        wd = self.wd
        # 窗口最大化
        wd.maximize_window()
        # 登录 正式环境17400007001
        login.login(self,"17400007001","123456")


    def test01_beautiful(self):
        # 核心素养-美文
        print("开始测试！核心素养-美文")
        wd = self.wd
        success = True
        # 进入国学美文页
        topmenu_t.top_menu_gxmw_s(self)

        if not ("美文" in wd.find_element_by_tag_name("html").text):
            success = False
            print("国学美文初始化失败")
        else:
            print("国学美文初始化成功")
        time.sleep(1)

        # 获取原页面句柄
        homepage_handle = wd.current_window_handle
        # print "国学美文页面句柄是：%s",homepage_handle
        # 点击文章:江南的冬景
        A = wd.find_element_by_id("c_Content")
        B = A.find_elements_by_class_name("c_Catalogue")
        B1 = B[0].find_element_by_class_name("c_FicListMain")
        B2 = B1.find_elements_by_class_name("c_FicBox")
        B3 = B2[1].find_element_by_class_name("c_FicList")
        B4 = B3.find_elements_by_tag_name("li")[2]
        B4.find_element_by_class_name("name").click()
        time.sleep(0.5)
        all_handles = wd.window_handles
        for handle in all_handles:
            if handle != homepage_handle:
                wd.switch_to.window(handle)
                if not ("江南的冬景" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print("美文详情展示失败")
                else:
                    print("美文详情展示成功")
                time.sleep(0.5)
                # # 点击分享按钮
                # wd.find_element_by_xpath(".//*[@id='c_Share']").click()
                # if not ("分享给好友" in wd.find_element_by_tag_name("html").text):
                #     success = False
                #     print("分享给好友弹窗失败")
                # else:
                #     print("分享给好友弹窗成功")
                # time.sleep(1)
                #
                # # 获取老页面的窗口句柄
                # oldpage_window = wd.current_window_handle
                # # 分享至QQ好友
                # wd.find_element_by_css_selector("a.bds_sqq").click()
                # time.sleep(3)
                # # 隐形等待30秒钟
                # # self.wd.implicitly_wait(30)
                # # 切换页面，验证新页面，关闭新页面
                # mid_handles = wd.window_handles
                # # print "当前页面中所有的句柄，%s", mid_handles
                # for handle1 in mid_handles:
                #     if handle1 != oldpage_window and handle1 != homepage_handle:
                #         # print "当前页面：%s",wd.title
                #         wd.switch_to.window(handle1)
                #         # print "切换句柄后，当前页面句柄：%s", handle1
                #         time.sleep(2)
                #         # frame = wd.find_element_by_xpath(".//*[@id='login']")
                #         try:
                #             # 切入iframe对话框
                #             wd.switch_to.frame("login_frame")
                #             # 关闭登录对话框
                #             wd.find_element_by_xpath("//div[@class='header']/a").click()
                #             # 切回原页面
                #             wd.switch_to.default_content()
                #             # 判断title是否完全等于“发给QQ好友和群组”
                #             # title1 = EC.title_is(u"发送给QQ好友和群组")
                #             # print title1(wd)
                #             # print wd.title
                #             if not ("发送给QQ好友和群组" in wd.title):
                #                 success = False
                #                 print("分享到QQ失败")
                #             else:
                #                 print("分享到QQ成功")
                #         except Exception:
                #             # print msg
                #             print("发送给QQ好友和群组页面加载失败")
                #         # 判断title包含
                #         # title2 = EC.title_contains(u'QQ好友')
                #         # print title2(wd)
                #         wd.close()
                #         wd.switch_to.window(oldpage_window)
                #
                # # 获取老页面的窗口句柄
                # # oldpage_window = wd.current_window_handle
                # # 分享至QQ空间
                # wd.find_element_by_css_selector("a.bds_qzone").click()
                # time.sleep(2)
                # mid_handles = wd.window_handles
                # for handle2 in mid_handles:
                #     if handle2 != oldpage_window and handle2 != homepage_handle:
                #         wd.switch_to.window(handle2)
                #         if not ("QQ空间" in wd.title):
                #             success = False
                #             print("分享到QQ空间失败")
                #         else:
                #             print("分享到QQ空间成功")
                #             # 判断title包含
                #         # title2 = EC.title_contains(u'QQ空间')
                #         # print title2(wd)
                #         wd.close()
                #         wd.switch_to.window(oldpage_window)
                # # 获取老页面的窗口句柄
                # # oldpage_window = wd.current_window_handle
                # # 分享至新浪微博
                # wd.find_element_by_css_selector("a.bds_tsina").click()
                # time.sleep(3)
                # mid_handles = wd.window_handles
                # for handle3 in mid_handles:
                #     if handle3 != oldpage_window and handle3 != homepage_handle:
                #         wd.switch_to.window(handle3)
                #         if not ("微博" in wd.title):
                #             success = False
                #             print("分享到微博失败")
                #         else:
                #             print("分享到微博成功")
                #             # 判断title包含
                #         # title2 = EC.title_contains(u'微博')
                #         # print title2(wd)
                #         wd.close()
                #         wd.switch_to.window(oldpage_window)
                #
                # # 分享至微信
                # wd.find_element_by_css_selector("a.bds_weixin").click()
                # time.sleep(2)
                # if not ("分享到微信朋友圈" in wd.find_element_by_tag_name("html").text):
                #     success = False
                #     print("微信分享弹窗失败")
                # else:
                #     print("微信分享弹窗成功")
                #     # 关闭微信分享窗口
                # time.sleep(1)
                #
                # wd.find_element_by_link_text("×").click()
                # # 关闭分享窗口
                # wd.find_element_by_id("ShareClose").click()
                # 点击上一篇
                wd.find_element_by_xpath(".//*[@id='up']").click()
                print("上一篇初始化成功")
                time.sleep(1)
                # 点击下一篇
                wd.find_element_by_xpath(".//*[@id='go']").click()
                print("下一篇初始化成功")
                time.sleep(1)
                wd.close()
                wd.switch_to.window(homepage_handle)

        # 名师指点文章详情页
        # 点击文章:江南的冬景
        A = wd.find_element_by_id("c_Content")
        B = A.find_elements_by_class_name("c_Catalogue")
        B1 = B[0].find_element_by_class_name("c_CataTeList")
        B2 = B1.find_elements_by_tag_name("li")[0]
        B2.find_element_by_class_name("name").click()
        time.sleep(2)
        all_handles = wd.window_handles
        for handle in all_handles:
            if handle != homepage_handle:
                wd.switch_to.window(handle)
                if not ("多感官描写景物" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print("名师指点文章展示失败")
                else:
                    print("名师指点文章展示成功")
                wd.close()
                wd.switch_to.window(homepage_handle)

        # 调用退出接口
        self.assertTrue(success)

    def test02_country(self):
        # 核心素养-国学
        print("开始测试！核心素养-国学")
        wd = self.wd
        success = True
        topmenu_t.top_menu_gxmw_s(self)

        if not ("国学" in wd.find_element_by_tag_name("html").text):
            success = False
            print("国学美文初始化失败")
        else:
            print("国学美文初始化成功")

        # 点击切换国学标签
        wd.find_element_by_xpath("//li[text()='国学' and @mycla='sinology']").click()
        time.sleep(2)

        # 获取原页面句柄
        homepage_handle = wd.current_window_handle
        # 点击文章:《幼学琼林》选读
        A = wd.find_element_by_id("chinese_literature")
        B = A.find_element_by_class_name("chinese_literature_themetotal")
        B1 = B.find_elements_by_class_name("chinese_literature_theme_every")
        B2 = B1[0].find_element_by_class_name("chinese_literature_theme_every_total")
        B3 = B2.find_elements_by_tag_name("li")[1].click()
        time.sleep(0.5)

        all_handles = wd.window_handles
        for handle in all_handles:
            if handle != homepage_handle:
                wd.switch_to.window(handle)
                if not ("称教馆曰设帐" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print("国学详情展示失败")
                else:
                    print("国学详情展示成功")
                time.sleep(0.5)

                # # 点击分享按钮
                # wd.find_element_by_xpath(".//*[@id='c_Share']").click()
                # if not ("分享给好友" in wd.find_element_by_tag_name("html").text):
                #     success = False
                #     print("分享给好友弹窗失败")
                # else:
                #     print("分享给好友弹窗成功")
                # time.sleep(1)
                #
                # # 获取老页面的窗口句柄
                # oldpage_window = wd.current_window_handle
                # # 分享至QQ好友
                # wd.find_element_by_css_selector("a.bds_sqq").click()
                # time.sleep(3)
                # # 隐形等待30秒钟
                # # self.wd.implicitly_wait(30)
                # # 切换页面，验证新页面，关闭新页面
                # mid_handles = wd.window_handles
                # # print "当前页面中所有的句柄，%s", mid_handles
                # for handle1 in mid_handles:
                #     if handle1 != oldpage_window and handle1 != homepage_handle:
                #         # print "当前页面：%s",wd.title
                #         wd.switch_to.window(handle1)
                #         # print "切换句柄后，当前页面句柄：%s", handle1
                #         time.sleep(2)
                #         # frame = wd.find_element_by_xpath(".//*[@id='login']")
                #         try:
                #             # 切入iframe对话框
                #             wd.switch_to.frame("login_frame")
                #             # 关闭登录对话框
                #             wd.find_element_by_xpath("//div[@class='header']/a").click()
                #             # 切回原页面
                #             wd.switch_to.default_content()
                #             # 判断title是否完全等于“发给QQ好友和群组”
                #             # title1 = EC.title_is(u"发送给QQ好友和群组")
                #             # print title1(wd)
                #             # print wd.title
                #             if not ("发送给QQ好友和群组" in wd.title):
                #                 success = False
                #                 print("分享到QQ失败")
                #             else:
                #                 print("分享到QQ成功")
                #         except Exception:
                #             # print msg
                #             print("发送给QQ好友和群组页面加载失败")
                #         # 判断title包含
                #         # title2 = EC.title_contains(u'QQ好友')
                #         # print title2(wd)
                #         wd.close()
                #         wd.switch_to.window(oldpage_window)
                #
                # # 获取老页面的窗口句柄
                # # oldpage_window = wd.current_window_handle
                # # 分享至QQ空间
                # wd.find_element_by_css_selector("a.bds_qzone").click()
                # time.sleep(2)
                # mid_handles = wd.window_handles
                # for handle2 in mid_handles:
                #     if handle2 != oldpage_window and handle2 != homepage_handle:
                #         wd.switch_to.window(handle2)
                #         if not ("QQ空间" in wd.title):
                #             success = False
                #             print("分享到QQ空间失败")
                #         else:
                #             print("分享到QQ空间成功")
                #             # 判断title包含
                #         # title2 = EC.title_contains(u'QQ空间')
                #         # print title2(wd)
                #         wd.close()
                #         wd.switch_to.window(oldpage_window)
                # # 获取老页面的窗口句柄
                # # oldpage_window = wd.current_window_handle
                # # 分享至新浪微博
                # wd.find_element_by_css_selector("a.bds_tsina").click()
                # time.sleep(2)
                # mid_handles = wd.window_handles
                # for handle3 in mid_handles:
                #     if handle3 != oldpage_window and handle3 != homepage_handle:
                #         wd.switch_to.window(handle3)
                #         if not ("微博" in wd.title):
                #             success = False
                #             print("分享到微博失败")
                #         else:
                #             print("分享到微博成功")
                #             # 判断title包含
                #         # title2 = EC.title_contains(u'微博')
                #         # print title2(wd)
                #         wd.close()
                #         wd.switch_to.window(oldpage_window)
                #
                # # 分享至微信
                # wd.find_element_by_css_selector("a.bds_weixin").click()
                # time.sleep(2)
                # if not ("分享到微信朋友圈" in wd.find_element_by_tag_name("html").text):
                #     success = False
                #     print("微信分享弹窗失败")
                # else:
                #     print("微信分享弹窗成功")
                #     # 关闭微信分享窗口
                # time.sleep(1)
                #
                # wd.find_element_by_link_text("×").click()
                # # 关闭分享窗口
                # wd.find_element_by_id("ShareClose").click()
                # 点击上一篇
                wd.find_element_by_xpath(".//*[@id='up']").click()
                print("上一篇初始化成功")
                time.sleep(1)
                # 点击下一篇
                wd.find_element_by_xpath(".//*[@id='go']").click()
                print("下一篇初始化成功")
                time.sleep(1)
                wd.close()
                wd.switch_to.window(homepage_handle)

        self.assertTrue(success)

    def test03_periodical(self):
        # 核心素养-期刊
        print("开始测试！核心素养-期刊")
        wd = self.wd
        success = True
        # 进入国学美文页
        topmenu_t.top_menu_gxmw_s(self)
        # 验证期刊栏目存在
        if not ("期刊" in wd.find_element_by_tag_name("html").text):
            success = False
            print("国学美文期刊初始化失败")
        else:
            print("国学美文期刊初始化成功")

        # 切换到期刊标签
        wd.find_element_by_xpath("//li[text()='期刊' and @mycla='magazine']").click()

        time.sleep(2)
        if not ("目录" in wd.find_element_by_tag_name("html").text):
            success = False
            print("期刊初始化失败")
        else:
            print("期刊初始化成功")
        # 切换期刊期数
        wd.find_element_by_xpath("//img[@id='img_1']").click()
        time.sleep(2)
        print("切换期刊1成功")
        wd.find_element_by_xpath("//img[@id='img_0']").click()
        time.sleep(2)
        print("切换期刊0成功")

        # 获取原页面句柄
        homepage_handle = wd.current_window_handle
        # 鼠标悬浮到左侧期刊
        A = wd.find_element_by_class_name("c_MagLeft")
        ActionChains(wd).move_to_element(A).perform()
        time.sleep(1)
        # 定位到文章并点击
        B = A.find_element_by_class_name("c_MenuList")
        B1 =B.find_elements_by_tag_name("li")
        B1[2].click()
        time.sleep(1)

        # 切换句柄
        all_handles = wd.window_handles
        for handle in all_handles:
            if handle != homepage_handle:
                wd.switch_to.window(handle)
                if not ("那个坐在路边为你鼓掌的人" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print("期刊文章详情页展示失败")
                else:
                    print("期刊文章详情页展示成功")

                # 点击上一篇
                wd.find_element_by_xpath(".//*[@id='up']").click()
                print("上一篇初始化成功")
                time.sleep(1)
                # 点击下一篇
                wd.find_element_by_xpath(".//*[@id='go']").click()
                print("下一篇初始化成功")
                time.sleep(1)
                wd.close()
                wd.switch_to.window(homepage_handle)
        self.assertTrue(success)

    def test04_English(self):
        # 走遍英美
        print("开始测试！走遍英美")
        wd = self.wd
        success = True
        time.sleep(2)
        # 进入走遍英美页
        topmenu_t.top_menu_zbym_s(self)
        # 获取原页面句柄
        homepage_handle = wd.current_window_handle
        # 点击文章:
        wenzhang = wd.find_element_by_xpath("//div[@id='c_Content'][1]/div[1]/ul[1]/li[1]")
        title  = wenzhang.find_element_by_tag_name("a").get_attribute("title")
        wenzhang.click()
        time.sleep(0.5)

        # 切换句柄
        all_handles = wd.window_handles
        for handle in all_handles:
            if handle != homepage_handle:
                wd.switch_to.window(handle)
                if not (title in wd.find_element_by_tag_name("html").text):
                    success = False
                    print("英语详情页展示失败")
                else:
                    print("英语详情页展示成功")
                # # 点击分享按钮
                # wd.find_element_by_xpath(".//*[@id='c_Share']").click()
                # if not ("分享给好友" in wd.find_element_by_tag_name("html").text):
                #     success = False
                #     print("分享给好友弹窗失败")
                # else:
                #     print("分享给好友弹窗成功")
                # time.sleep(1)
                #
                # # 获取老页面的窗口句柄
                # oldpage_window = wd.current_window_handle
                # # 分享至QQ好友
                # wd.find_element_by_css_selector("a.bds_sqq").click()
                # time.sleep(3)
                # # 隐形等待30秒钟
                # # self.wd.implicitly_wait(30)
                # # 切换页面，验证新页面，关闭新页面
                # mid_handles = wd.window_handles
                # # print "当前页面中所有的句柄，%s", mid_handles
                # for handle1 in mid_handles:
                #     if handle1 != oldpage_window and handle1 != homepage_handle:
                #         # print "当前页面：%s",wd.title
                #         wd.switch_to.window(handle1)
                #         # print "切换句柄后，当前页面句柄：%s", handle1
                #         time.sleep(2)
                #         # frame = wd.find_element_by_xpath(".//*[@id='login']")
                #         try:
                #             # 切入iframe对话框
                #             wd.switch_to.frame("login_frame")
                #             # 关闭登录对话框
                #             wd.find_element_by_xpath("//div[@class='header']/a").click()
                #             # 切回原页面
                #             wd.switch_to.default_content()
                #             # 判断title是否完全等于“发给QQ好友和群组”
                #             # title1 = EC.title_is(u"发送给QQ好友和群组")
                #             # print title1(wd)
                #             # print wd.title
                #             if not ("发送给QQ好友和群组" in wd.title):
                #                 success = False
                #                 print("分享到QQ失败")
                #             else:
                #                 print("分享到QQ成功")
                #         except Exception:
                #             # print msg
                #             print("发送给QQ好友和群组页面加载失败")
                #         # 判断title包含
                #         # title2 = EC.title_contains(u'QQ好友')
                #         # print title2(wd)
                #         wd.close()
                #         wd.switch_to.window(oldpage_window)
                #
                # # 获取老页面的窗口句柄
                # # oldpage_window = wd.current_window_handle
                # # 分享至QQ空间
                # wd.find_element_by_css_selector("a.bds_qzone").click()
                # time.sleep(2)
                # mid_handles = wd.window_handles
                # for handle2 in mid_handles:
                #     if handle2 != oldpage_window and handle2 != homepage_handle:
                #         wd.switch_to.window(handle2)
                #         if not ("QQ空间" in wd.title):
                #             success = False
                #             print("分享到QQ空间失败")
                #         else:
                #             print("分享到QQ空间成功")
                #             # 判断title包含
                #         # title2 = EC.title_contains(u'QQ空间')
                #         # print title2(wd)
                #         wd.close()
                #         wd.switch_to.window(oldpage_window)
                # # 获取老页面的窗口句柄
                # # oldpage_window = wd.current_window_handle
                # # 分享至新浪微博
                # wd.find_element_by_css_selector("a.bds_tsina").click()
                # time.sleep(3)
                # mid_handles = wd.window_handles
                # for handle3 in mid_handles:
                #     if handle3 != oldpage_window and handle3 != homepage_handle:
                #         wd.switch_to.window(handle3)
                #         if not ("微博" in wd.title):
                #             success = False
                #             print("分享到微博失败")
                #         else:
                #             print("分享到微博成功")
                #             # 判断title包含
                #         # title2 = EC.title_contains(u'微博')
                #         # print title2(wd)
                #         wd.close()
                #         wd.switch_to.window(oldpage_window)
                # time.sleep(1)
                # # 分享至微信
                # wd.find_element_by_css_selector("a.bds_weixin").click()
                # time.sleep(2)
                # if not ("分享到微信朋友圈" in wd.find_element_by_tag_name("html").text):
                #     success = False
                #     print("微信分享弹窗失败")
                # else:
                #     print("微信分享弹窗成功")
                #     # 关闭微信分享窗口
                # time.sleep(1)
                #
                # wd.find_element_by_link_text("×").click()
                # # 关闭分享窗口
                
                # 查看/收起翻译
                fanyi = wd.find_element_by_class_name("text_li")
                if fanyi.is_displayed():
                    fanyi.click()
                    print(fanyi.text)
                    time.sleep(1)
                    if not ("收起翻译" in fanyi.text):
                        success = False
                        print("翻译展示失败")
                    else:
                        print("翻译展示成功")
                    time.sleep(0.5)
                    fanyi.click()
                    time.sleep(1)
                    if not ("查看翻译" in wd.find_element_by_xpath("//span[@class='text_li']").text):
                        success = False
                        print("翻译收起失败")
                    else:
                        print("翻译收起成功")
                    time.sleep(0.5)
                else:
                    print("未找到翻译按钮")



                nexttitle = wd.find_element_by_xpath("//p[@id='c_NextArt']/span[1]").text
                wd.find_element_by_id("isdown").click()
                # B2 = A1.find_element_by_class_name("isTitle").click()
                if not (nexttitle in wd.find_element_by_tag_name("html").text):
                    success = False
                    print("下一篇失败")
                else:
                    print("下一篇成功")
                time.sleep(1)
                # 点击上一篇
                pretitle = wd.find_element_by_xpath("//p[@id='c_PreArt']/span[1]").text
                wd.find_element_by_id("isup").click()
                if not (pretitle in wd.find_element_by_tag_name("html").text):
                    success = False
                    print("上一篇失败")
                else:
                    print("上一篇成功")
                time.sleep(1)

                wd.close()
                wd.switch_to.window(homepage_handle)
            self.assertTrue(success)

    def test05_math(self):
        '''数学思维'''
        print("开始测试！数学思维")
        wd = self.wd
        success = True
        # 进入数学思维页
        topmenu_t.top_menu_sxsw_s(self)

        # 获取原页面句柄
        homepage_handle = wd.current_window_handle
        # 点击文章:有理数的大小比较方法选用
        A = wd.find_element_by_class_name("learn_contentBox")
        B = A.find_elements_by_class_name("learn_titleBox")[0]
        B.find_elements_by_class_name("learn_contentLi")[1].click()
        time.sleep(0.5)

        # 切换句柄
        all_handles = wd.window_handles
        for handle in all_handles:
            if handle != homepage_handle:
                wd.switch_to.window(handle)
                if not ("有理数的大小比较方法选用" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print("数学详情页展示失败")
                else:
                    print("数学详情页展示成功")
                # 点击下一篇
                wd.find_element_by_id("isdown").click()
                if not ("数学思想方法——数形结合思想" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print("下一篇失败")
                else:
                    print("下一篇成功")
                time.sleep(1)
                # 点击上一篇
                wd.find_element_by_id("isup").click()
                if not ("有理数的大小比较方法选用" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print("上一篇失败")
                else:
                    print("上一篇成功")
                time.sleep(1)
                wd.close()
                wd.switch_to.window(homepage_handle)

        # 调用退出接口
        self.assertTrue(success)

    def tearDown(self):
        '''
        #将滚动条移动到页面的顶部
        js="var q=document.documentElement.scrollTop=0"
        self.wd.execute_script(js)
        wd = self.wd
        '''
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()