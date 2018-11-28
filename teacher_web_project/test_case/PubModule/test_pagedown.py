# -*- coding: utf-8 -*-
# 王帅 功能：首页页脚功能遍历
# 2018.08.30 优化页面底部去掉微博，贴吧问题
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_pagedown(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        wd = self.wd
        wd.get("http://www.wuhaodaoxue.com")

    def test_01_aboutus(self):
        print("开始测试：\n关于我们")
        success = True
        wd = self.wd

        target = wd.find_element_by_link_text("关于我们")
        wd.execute_script("arguments[0].scrollIntoView();", target)
        wd.find_element_by_link_text('关于我们').click()
        # 判断页面是否有网站简介四个字
        # self.assertEqual(self.wd.find_element_by_xpath('html/body/article/div/p[3]/span').text,'网站简介','进入页面失败')
        # 判断页面是否有定位的xpath元素
        # a=self.assertIsNotNone(self.wd.find_element_by_xpath('html/body/article/div/p[3]/span'),'进入关于我们页面失败')

        if not ("网站简介" in wd.find_element_by_class_name('Content').text):
            success = False
            print("进入关于我们页面失败！")
        else:
            print("进入关于我们页面成功！")
        self.assertTrue(success)

    # 企业合作

    def test_02_cooperation(self):
        print("开始测试：\n企业合作")
        success = True
        wd = self.wd

        target = wd.find_element_by_link_text("企业合作")
        wd.execute_script("arguments[0].scrollIntoView();", target)
        wd.find_element_by_link_text('企业合作').click()
        if not ("合作意向" in wd.find_element_by_class_name('Content').text):
            success = False
            print("进入企业合作页面失败！")
        else:
            print("进入企业合作页面成功！")

        print('请输入以下信息：')
        #name = input('公司名称：')
        wd.find_element_by_id('Name').send_keys("1")
        #username = input('联系人姓名：')
        wd.find_element_by_id('UserName').send_keys("1")
        #userduty = input('联系人职务：')
        wd.find_element_by_id('UserDuty').send_keys("1")
        #usertell = input('联系人电话：')
        wd.find_element_by_id('UserTell').send_keys("1")
        #business = input('主营业务：')
        wd.find_element_by_id('Business').send_keys("1")
        #purpose = input('合作意向：')
        wd.find_element_by_id('Purpose').send_keys("1")
        wd.find_element_by_class_name('SubBtn').click()

        if not ("提交成功" in wd.find_element_by_xpath(".//*[@id='c_ErrorMsg']").text):
            success = False
            print('企业信息提交失败！')
        else:
            print('企业信息提交成功！')
        self.assertTrue(success)

    # 校园合作

    def test_03_cooperation(self):
        print("开始测试：\n校园合作")
        success = True
        wd = self.wd

        target = wd.find_element_by_link_text("校园合作")
        wd.execute_script("arguments[0].scrollIntoView();", target)
        wd.find_element_by_link_text('校园合作').click()
        if not ("填写校园信息" in wd.find_element_by_class_name("Content").text):
            success = False
            print("进入校园合作页面失败！")
        else:
            print("进入校园合作页面成功！")
        wd.find_element_by_css_selector("p").click()
        wd.find_element_by_xpath("//ul[@id='ProVince']//li[.='天津']").click()
        wd.find_element_by_xpath("//ul[@class='List']/li[1]/div[2]/p").click()
        wd.find_element_by_xpath("//ul[@id='CityList']//li[.='天津市']").click()
        wd.find_element_by_xpath("//div[@id='Contry']/p").click()
        wd.find_element_by_xpath("//ul[@id='ContryList']//li[.='河西区']").click()
        print('请输入以下信息：')
        #name = input('学校名称：')
        wd.find_element_by_id('Name').send_keys("1")
        #username = input('联系人姓名：')
        wd.find_element_by_id('UserName').send_keys("1")
        #userduty = input('联系人职务：')
        wd.find_element_by_id('UserDuty').send_keys("1")
        #usertell = input('联系人电话：')
        wd.find_element_by_id('UserTell').send_keys("1")
        #purpose = input('合作意向：')
        wd.find_element_by_id('Purpose').send_keys("1")

        wd.find_element_by_class_name('SubBtn').click()
        # time.sleep(3)
        # a = len(wd.find_element_by_id('c_ErrorMsg'))
        # print(a)
        # a=wd.find_element_by_xpath(".//*[@id='c_ErrorMsg']").text
        # print(a)

        if not ("提交成功" in wd.find_element_by_xpath(".//*[@id='c_ErrorMsg']").text):
            success = False
            print('学校信息提交失败！')
        else:
            print('学校信息提交成功！')
        self.assertTrue(success)

    # 人才招聘模块
    def test_04_recruitment(self):
        print("开始测试：\n人才招聘")
        success = True
        wd = self.wd

        target = wd.find_element_by_link_text("人才招聘")
        wd.execute_script("arguments[0].scrollIntoView();", target)
        wd.find_element_by_link_text('人才招聘').click()
        # 判断页面是否有网站简介四个字
        # self.assertEqual(self.wd.find_element_by_xpath('html/body/article/div/p[3]/span').text,'网站简介','进入页面失败')
        # 判断页面是否有定位的xpath元素
        # a=self.assertIsNotNone(self.wd.find_element_by_xpath('html/body/article/div/p[3]/span'),'进入关于我们页面失败')

        if not ("职位职能" in wd.find_element_by_class_name('Content').text):
            success = False
            print("进入人才招聘页面失败！")
        else:
            print("进入人才招聘页面成功！")
        self.assertTrue(success)

    # 帮助中心
    def test_05_helpcenter(self):
        print("开始测试：\n帮助中心")
        success = True
        wd = self.wd

        target = wd.find_element_by_link_text("帮助中心")
        wd.execute_script("arguments[0].scrollIntoView();", target)
        wd.find_element_by_link_text('帮助中心').click()
        # 判断页面是否有网站简介四个字
        # self.assertEqual(self.wd.find_element_by_xpath('html/body/article/div/p[3]/span').text,'网站简介','进入页面失败')
        # 判断页面是否有定位的xpath元素
        # a=self.assertIsNotNone(self.wd.find_element_by_xpath('html/body/article/div/p[3]/span'),'进入关于我们页面失败')
        # 子菜单遍历
        menu = wd.find_elements_by_class_name('H_objlist')
        for i in range(0, 3):
            menu[i].click()
            sonmenu = menu[i].find_elements_by_class_name('H_li')
            for j in sonmenu:
                j.click()
                time.sleep(1)
        # 判断能否遍历到最后测试子菜单
        if not ("必刷题" in wd.find_element_by_class_name("ProblemsContent").text):
            success = False
            print("子菜单遍历失败！")
        else:
            print("子菜单遍历成功！")
        self.assertTrue(success)

    # 意见反馈
    def test_06_suggest(self):
        print("开始测试：\n意见反馈")
        success = True
        wd = self.wd

        target = wd.find_element_by_link_text("意见反馈")
        wd.execute_script("arguments[0].scrollIntoView();", target)
        wd.find_element_by_link_text('意见反馈').click()
        # 判断进入页面是否成功
        if not ("QQ客服" in wd.find_element_by_xpath("html/body/article/div/div[3]").text):
            success = False
            print("进入意见反馈页面失败！")
        else:
            print("进入意见反馈页面成功！")
        '''
        wd.find_element_by_xpath("html/body/article/div/div[3]/a/img").click()
            handles = wd.window_handles

            for handle in handles:
                if handle !=wd.current_window_handle:
                    wd.switch_to_window(handle)
                    break
        '''
        #suggestion = input("请输入您的宝贵意见：")
        wd.find_element_by_id('writeideas').send_keys("1")
        #phone = input("请输入练习方式：")
        wd.find_element_by_id('remineword').send_keys("1")
        wd.find_element_by_class_name('SubBtn').click()
        time.sleep(2)
        if not ("提交成功" in wd.find_element_by_id('c_ErrorMsg').text):
            success = False
            print("提交失败！")
        else:
            print("提交成功！")
        self.assertTrue(success)
        '''
        if not ("发起网页聊天" in wd.find_element_by_xpath(".//*[@id='open-webaio']").text):
            success = False
            print("可以QQ交谈！")
        else:
            print("不可以QQ交谈！")
        self.assertTrue(success)
        '''
        self.assertTrue(success)

    # 点击公司微博

    # def test_07_weibo(self):
    #     print("开始测试：\n公司微博")
    #     success = True
    #     wd = self.wd
    #
    #     target = wd.find_element_by_link_text("关于我们")
    #     wd.execute_script("arguments[0].scrollIntoView();", target)
    #     time.sleep(2)
    #     foot = wd.find_element_by_class_name("FooterIcoBox")
    #     weibo = foot.find_elements_by_tag_name("li")
    #     weibo[0].click()
    #     time.sleep(2)
    #     handles = wd.window_handles
    #     wd.switch_to.window(handles[1])
    #     if not ("五好导学网" in wd.find_element_by_class_name("name_line_a").text):
    #         success = False
    #         print("微博点击失败！")
    #     else:
    #         print("微博点击成功！")
    #     time.sleep(2)
    #     self.assertTrue(success)

    # 点击贴吧页面

    # def test_08_tieba(self):
    #     print("开始测试：\n公司贴吧")
    #     success = True
    #     wd = self.wd
    #
    #     target = wd.find_element_by_link_text("关于我们")
    #     wd.execute_script("arguments[0].scrollIntoView();", target)
    #     time.sleep(2)
    #     foot = wd.find_element_by_class_name("FooterIcoBox")
    #     weibo = foot.find_elements_by_tag_name("li")
    #     weibo[1].click()
    #     time.sleep(2)
    #     handles = wd.window_handles
    #     wd.switch_to.window(handles[1])
    #     if not ("五好导学吧" in wd.find_element_by_class_name("card_title").text):
    #         success = False
    #         print("贴吧点击失败！")
    #     else:
    #         print("贴吧点击成功！")
    #     time.sleep(2)
    #     self.assertTrue(success)
    #     print("底部菜单测试成功，请开始下一步测试。")
    #     self.assertTrue(success)

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
