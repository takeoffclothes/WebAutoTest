#作者：王帅
# 功能：test_01_sharevideos教师推荐视频，
#       test_02_watchvideos学生看视频， 做题，
#       test_03_watchreport学生查看报告，
#       test_04_homeworkreport教师查看报告
#待优化功能：视频点赞，统计学生做题对错
# 2018.08.30 优化教师端导航栏变化导致的问题
# -*- coding: utf-8 -*-
import random
import time
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.webdriver import WebDriver
from Constant.sys_constant import *
from test_case.PubModule import login,topmenu_t


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_sharevideos(unittest.TestCase):
    def setUp(self):

        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        wd = self.wd
        wd.get(LOGIN_URL)
        # wd.get("http://preprod-whdx.bcbook.cn")
    def qtest_01_sharevideos(self):
        success = True
        wd = self.wd
        wd.maximize_window()
        #登录账号密码
        login.login(self, "14600000071", "123456")
        # 点击首页视频大图
        time.sleep(2)
        wd.find_element_by_xpath("//div[@class='clear']").send_keys(Keys.CONTROL+Keys.DOWN)
        time.sleep(2)
        wd.find_element_by_xpath("//div[@class='i_Video_max_wrap']/img").click()
        time.sleep(2)
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
                    # 点击推荐按钮
                    wd.find_element_by_xpath("//span[@id='recommend']").click()
                    #获取推荐对象
                    cls = wd.find_element_by_xpath("//ul[@class='recommend_content_total']")
                    clsli = cls.find_elements_by_tag_name("li")
                    print(len(clsli))
                    # 判断班级是否推荐过
                    for i in range(0,len(clsli)):
                        classname = clsli[i].text
                        classname = classname.strip()
                        if ("recommend_content_every" != clsli[i].get_attribute("class")):
                            print(classname+"班级已经推荐过了！")
                        else:
                            print(classname + "班级未推荐过！")
                            clsli[i].click()
                    wd.find_element_by_xpath("//div[@id='recommendWrapper']//textarea").send_keys("自动化测试，视频推荐功能！")
                    wd.find_element_by_xpath("//span[text()='确定']").click()
                    time.sleep(1)
                    if ("推荐成功" in wd.find_element_by_tag_name("html").text):
                        print("推荐成功！")
                    else:
                        print("推荐失败！")
                    time.sleep(2)
                wd.close()
                wd.switch_to.window(homepage_window)
        self.assertTrue(success)

    def qtest_02_watchvideos(self):
        success = True
        wd = self.wd
        #登录账号、密码14600000701
        wd.maximize_window()
        #登录账号密码
        login.login(self, "14600000701", "123456")
        #悬停进入写作业页面
        topmenu_t.top_menu_xzy_s(self)
        time.sleep(1)
        #点击看视频作业的去完成按钮
        watchvidestodo = wd.find_element_by_xpath("//span[text()='看视频']/../../li[3]/span")
        watchvidestodo.click()
        time.sleep(2)
        #在视频播放页面点击预习测试按钮
        wd.find_element_by_class_name("test_see").click()
        #做测试，引入随机数
        test = wd.find_elements_by_class_name("questionTitle")
        for i in range(0,len(test)):
            choise = test[i].find_elements_by_class_name("optionchoose")
            x = random.randint(0,3)
            choise[x].click()
            time.sleep(2)
            #提交作业
        wd.find_element_by_xpath("//div[text()='提交']").click()
        self.assertTrue(success)

    def qtest_03_watchreport(self):
        success = True
        wd = self.wd
        wd.maximize_window()
        #登录账号、密码14600000701
        login.login(self, "14600000701", "123456")
        time.sleep(2)
        #悬停鼠标，进入看报告页面
        preview = wd.find_element_by_class_name("Com_NavMain")
        preview1 = preview.find_elements_by_class_name("Com_Li")
        ActionChains(wd).move_to_element(preview1[2]).perform()
        time.sleep(1)
        preview2 = preview1[2].find_elements_by_tag_name("li")
        preview2[1].click()
        time.sleep(2)
        report = wd.find_elements_by_class_name("reportHomeList")
        print(report[0].find_element_by_class_name("reportHomeEverEndTime").text)
        report1 = report[0].find_elements_by_tag_name("span")
        report1[4].click()
        #判断是否进入预习测试页面成功
        if ("预习测试" in wd.find_element_by_class_name("r_ttitle").text):
            print("进入看报告页面成功！")
        else:
            print("进入看报告页面失败！")
        self.assertTrue(success)

    def test_04_homeworkreport(self):
        success = True
        wd = self.wd
        wd.maximize_window()
        #登录账号、密码14600000071
        login.login(self,"14600000071","123456")
        time.sleep(2)
        #进入老师端的作业-报告
        topmenu_t.top_menu_zybg(self)
        # 判断是否进入报告页面
        if ("报告" in wd.find_element_by_tag_name("html").text):
            print("进入看报告页面成功！")
        else:
            print("进入看报告页面失败！")
        time.sleep(2)
        wd.find_element_by_xpath("//span[text()='视频']/../../p/a[text()='查看'][1]").click()
        time.sleep(1)
        #点击详情链接并输出未提交名单
        wd.find_element_by_id("submitDetail").click()
        time.sleep(2)
        #判断是否弹出详情弹窗
        head = wd.find_elements_by_class_name("modal-header")
        head1 =head[1].find_element_by_tag_name("span")
        if ("未提交名单" in head1.text):
            print("进入详情弹窗成功！")
            print("未提交名单如下：")
            print(wd.find_element_by_id("noSubmitStudentLists").text)
        else:
            print("进入详情弹窗失败！")
        #判断解析展开、收起是否成功
        button =wd.find_elements_by_class_name("modal-footer")
        button[1].find_element_by_tag_name("button").click()
        time.sleep(2)
        jiexi = wd.find_elements_by_class_name("fontReset")
        jiexi[0].find_element_by_class_name("analyse").click()
        time.sleep(2)
        if ("block" in jiexi[0].find_element_by_class_name("resultBorder").get_attribute("style")):
            print("解析展开成功！")
        else:
            print("解析展开失败！")
        jiexi = wd.find_elements_by_class_name("fontReset")
        jiexi[0].find_element_by_class_name("analyse").click()
        time.sleep(2)
        if ("none" in jiexi[0].find_element_by_class_name("resultBorder").get_attribute("style")):
            print("解析折叠成功！")
        else:
            print("解析折叠失败！")
        self.assertTrue(success)

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()