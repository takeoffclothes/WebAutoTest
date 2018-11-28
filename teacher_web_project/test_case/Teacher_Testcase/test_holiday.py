# coding：utf-8(定义源代码的编码:源代码的编码可以包含中文字符串)
# Created on 2018年1月30日
# updated on 2018年1月31日
# 五好导学网-教师web端-假期作业 自动化测试脚本
# 作者: 马春苗
# 优化：马春苗 由于生产版本删除了首页假期作业banner图，把进入假期作业首页改为通过点菜单进入
# 优化：马春苗 智能培优下的：水平自测、综合练习，新课预习、天天阅读页面验证
# updated on 2018年5月17
# 01寒假作业首页：寒假作业首页初始化-关闭默认弹出的使用说明弹窗-验证使用说明弹窗显示-关闭显示-年级切换验证-检查作业初始化-切换班级验证（有学生/无学生）-学生详情页初始化-学生试卷切换（智能填空、水平自测、提能训练、学科素养）
# 01未走流程：检查作业页（页面元素数据检查）、查看学生详情页（页面元素数据检查）
# 02智能填空流程：进入寒假作业首页-智能填空页初始化-做题功能验证-未做全部题提示验证-不选择挖空提示验证-做完全部题点击提交按钮-智能填空页的水平自测按钮验证
# 03水平自测流程：进入寒假作业首页-水平自测页初始化-查看/收起解析-报错功能验证-水平自测页的智能填空按钮验证-返回寒假作业首页-水平自测页初始化-水平自测页的提能训练按钮验证
# 04提能训练流程：进入寒假作业首页-提能训练页初始化-二次再换一套提示验证-三次再换一套提示验证-查看/收起解析-报错功能验证-提能训练页的水平自测按钮验证-返回寒假作业首页-提能训练页初始化-提能训练页的学科素养按钮验证
# 04未走流程：试卷等级验证、
# 05学科素养流程：进入寒假作业首页-学科素养页初始化-学科素养页的提能训练按钮验证
# 06综合练习流程：进入寒假作业首页-综合练习页初始化-查看/收起解析-报错功能验证
# 07预习专题流程：进入寒假作业首页-预习课详情页初始化-预习测试详情页初始化-关闭
# 07未走流程：视频播放验证、预习测试做题验证
# updated on 2018年10月29日
#01合并智能培优流程
#02把代码中相同操作的代码进行了循环操作合并

import random
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from Constant.sys_constant import *

from test_case.PubModule import login


class test_summer_holiday_t(unittest.TestCase):
    # 老师pc端-假期作业
    def setUp(self):
        # 定义浏览器下载配置
        self.wd = webdriver.Firefox()
        # self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(5)
        self.wd.get(LOGIN_URL)
        # self.wd.get("http://preprod-whdx.bcbook.cn")  # 预生产环境
        # 脚本运行时，错误的信息将被打印到这个列表中。
        self.verificationErrors = []
        # 是否继续接受下一下警告
        self.accept_next_alert = True
        wd = self.wd
        time.sleep(1)
        # 窗口最大化
        wd.maximize_window()
        # 调用login()函数登录
        # 17470000002是正式账号17100000001是测试账号18210000001是预生产账号
        login.login(self, "17470000002", "123456")
        # 检查是否登录成功
        if not (len(wd.find_elements_by_id("User")) != 0):
            print("登录失败！")
        # 进入首页
        if not ("您讲课比赛的坚实后援" in wd.find_element_by_tag_name("html").text):
            success = False
            print("首页初始化失败")
        else:
            print("首页初始化成功")
        # 定位首页作业并点击假期作业
        work = wd.find_element_by_xpath(".//*[@id='Header']/header/div/nav/ul/li[4]/span")
        ActionChains(wd).move_to_element(work).perform()
        work.click()
        time.sleep(1)
        wd.find_element_by_xpath("//*[@id='Header']/header/div/nav/ul/li[4]/ul/li[6]/a").click()

        time.sleep(1)
        # 点击假期作业
        if ("暂未开放假期作业" in wd.find_element_by_tag_name("html").text):
            success = False
            print("未开放假期作业")
        else:
            print("假期作业已经开放")
            # 默认寒假作业说明弹窗关闭验证
            try:
                wd.find_element_by_xpath("//input[@class='know']").click()
            except:
                print("假期作业作业说明未弹出")
            else:
                print("假期作业说明关闭成功")
            time.sleep(0.5)

    ## 智能培优
    def test01_holiday_znpy(self):
        # print("开始测试！假期作业水平自测")
        wd = self.wd
        success = True
        if ("暂未开放假期作业" in wd.find_element_by_tag_name("html").text):
            success = False
            print("未开放假期作业")
            return
        # 获取假期作业类型行：智能培优，新课预习，天天阅读
        choiseornot = wd.find_element_by_class_name("t-ul")
        choiseornotli = choiseornot.find_elements_by_tag_name("li")
        time.sleep(2)
        # 如果第一个智能培优没有选中，选中智能培优
        if not ('on' in choiseornotli[0].get_attribute('class')):
            success = False
            print('智能培优未被点击！')
            choiseornotli[0].click()
        else:
            print('智能培优已被点击！')
        ##################开始循环进入智能培优的各类型界面##########################33
        znpytypestxt = ['水平自测', '提能训练', '学科素养', '综合练习']
        for i in range(len(znpytypestxt)):
            print("开始测试！假期作业：" + znpytypestxt[i])
            if ("水平自测" == znpytypestxt[i]):
                ##水平自测
                types = wd.find_elements_by_xpath("//li[text()='" + znpytypestxt[i] + "']")
                types[1].click()
                time.sleep(2)
                if not (znpytypestxt[i] in wd.find_element_by_class_name("title").text):
                    success = False
                    print("\t 进入" + znpytypestxt[i] + "失败！")
                else:
                    print("\t 进入" + znpytypestxt[i] + "成功！")
                # 在页面里查看解析报错功能
                TestAll = wd.find_elements_by_class_name("group")
                ActionChains(wd).move_to_element(TestAll[0]).perform()
                wd.find_element_by_xpath("//button[@class='analyseBtn']").click()
                time.sleep(2)
                if not ("收起" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print("\t 解析展开失败！")
                else:
                    print('\t 解析展开成功！')

                wd.find_element_by_xpath("//button[@class='analyseBtn chosen']").click()
                time.sleep(2)
                if not ("解析" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print("\t 解析收起失败！")
                else:
                    print('\t 解析收起成功！')
                wd.find_element_by_xpath("//button[@class='errorBtn']").click()
                wd.find_element_by_xpath("html/body/div[4]/div/ul/li[1]").click()
                wd.find_element_by_xpath("html/body/div[4]/div/textarea").send_keys("自动化测试请忽略！")
                wd.find_element_by_xpath("//div[4]/div/div/a[1]").click()
                if not ('操作成功' in wd.find_element_by_id("dialogToast").text):
                    success = False
                    print("\t 报错失败！")
                else:
                    print("\t 报错成功！")
                wd.find_element_by_xpath("/html/body/div[2]/div/a[text()='假期作业']").click()
                continue
                # 提能训练里有三套题，再换一套功能
            if ("提能训练" == znpytypestxt[i]):
                types = wd.find_elements_by_xpath("//li[text()='" + znpytypestxt[i] + "']")
                types[1].click()
                for i in range(1, 4):
                    changetxt = wd.find_element_by_xpath(".//*[@id='deployQuestionBtn']")
                    if (changetxt.is_displayed()):
                        changetxt.click()
                        time.sleep(1)
                        if not ('题型配置中' in wd.find_element_by_class_name("deploy-question-dialog-wrapper-des").text):
                            success = False
                            print("\t 再换一套失败！")
                        else:
                            print("\t 再换一套成功！")
                    time.sleep(2)
                wd.find_element_by_xpath("/html/body/div[2]/div/a[text()='假期作业']").click()
                continue
            if ("学科素养" == znpytypestxt[i]):
                ##执行校验学科素养界面元素，暂时正式环境无数据
                types = wd.find_elements_by_xpath("//li[text()='" + znpytypestxt[i] + "']")
                types[1].click()
                time.sleep(1)
                if not ("学科素养" in wd.title):
                    print(wd.title + "-------------------------------")
                    success = False
                    print("\t 学科素养初始化失败！")
                else:
                    print("\t 学科素养初始化成功！")
                wd.find_element_by_xpath("/html/body/div[2]/div/a[text()='假期作业']").click()
                continue
            if ("综合练习" == znpytypestxt[i]):
                types = wd.find_elements_by_xpath("//h3[contains(text(),'综合练习')]")
                types[0].click()
                time.sleep(2)
                if not (znpytypestxt[i] in wd.find_element_by_class_name("title").text):
                    success = False
                    print("\t 进入" + znpytypestxt[i] + "失败！")
                else:
                    print("\t 进入" + znpytypestxt[i] + "成功！")
                # 在页面里查看解析报错功能
                TestAll = wd.find_elements_by_class_name("group")
                ActionChains(wd).move_to_element(TestAll[0]).perform()
                wd.find_element_by_xpath("//div[@class='btn-group']/a[@data-type='seeDetail']").click()
                time.sleep(2)
                if not ("收起" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print("\t 解析展开失败！")
                else:
                    print('\t 解析展开成功！')

                wd.find_element_by_xpath("//div[@class='btn-group showDetail']/a[@data-type='closeDetail']").click()
                time.sleep(2)
                if not ("解析" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print("\t 解析收起失败！")
                else:
                    print('\t 解析收起成功！')
                wd.find_element_by_xpath("//div[@class='btn-group']/a[@data-type='reportError']").click()
                wd.find_element_by_xpath("html/body/div[4]/div/ul/li[1]").click()
                wd.find_element_by_xpath("html/body/div[4]/div/textarea").send_keys("自动化测试请忽略！")
                wd.find_element_by_xpath("//div[4]/div/div/a[1]").click()
                if not ('操作成功' in wd.find_element_by_id("dialogToast").text):
                    success = False
                    print("\t 报错失败！")
                else:
                    print("\t 报错成功！")
                # 返回到假期作业主页面
                wd.find_element_by_xpath("/html/body/div[2]/div/a[text()='假期作业']").click()
                continue

        self.assertTrue(success)
    ##新课预习
    def test02_holiday_xkyx(self):
        print("开始测试！假期作业新课预习")
        wd = self.wd
        success = True
        if ("暂未开放假期作业" in wd.find_element_by_tag_name("html").text):
            success = False
            print("未开放假期作业")
            return
        ChoiseorNot = wd.find_element_by_class_name("t-ul")
        ChoiseorNotli = ChoiseorNot.find_elements_by_tag_name("li")
        time.sleep(2)
        ChoiseorNotli[1].click()
        if ('on' in ChoiseorNotli[1].get_attribute('class')):
            print('新课预习被点击！')
        else:
            print('新课预习未被点击！')

        xkyxtypestxt = ['电子教材', '预习视频', '预习测试']
        for i in range(len(xkyxtypestxt)):
            print("开始测试！新课预习：" + xkyxtypestxt[i])
            types = wd.find_elements_by_xpath("//li[text()='"+xkyxtypestxt[i]+"']")
            types[0].click()
            time.sleep(2)
            if not (xkyxtypestxt[i] in wd.find_element_by_class_name("Com_Crumbs").text):
                success = False
                print("\t进入"+xkyxtypestxt[i]+"失败！")
            else:
                print("\t进入" + xkyxtypestxt[i] + "成功！")
            if ("预习测试" == xkyxtypestxt[i] ):
                TestAll = wd.find_elements_by_class_name("group")
                for i in range(0,len(TestAll)):
                    TestAll = wd.find_elements_by_class_name("group")
                    ChoiseOption = TestAll[i].find_elements_by_class_name("choise-option")
                    Choise = random.randint(0,3)
                    ChoiseOption[Choise].click()
                    time.sleep(2)
                wd.find_element_by_id("submitBtn").click()
                if not ('提交成功' in wd.find_element_by_class_name("dialog-toast").text):
                    success = False
                    print("\t预习测试提交失败！")
                else:
                    print("\t预习测试提交成功！")
            wd.find_element_by_xpath("/html/body/div[2]/div/a[text()='假期作业']").click()

        self.assertTrue(success)
    ##天天阅读
    def test03_holiday_ttyd(self):
        print("开始测试！假期作业天天阅读")
        wd = self.wd
        success = True
        if ("暂未开放假期作业" in wd.find_element_by_tag_name("html").text):
            success = False
            print("未开放假期作业")
            return
        ChoiseorNot = wd.find_element_by_class_name("t-ul")
        ChoiseorNotli = ChoiseorNot.find_elements_by_tag_name("li")
        time.sleep(2)
        ChoiseorNotli[2].click()
        if ('on' in ChoiseorNotli[2].get_attribute('class')):
            print('\t天天阅读被点击！')
        else:
            print('\t天天阅读未被点击！')

        wd.find_element_by_xpath("//div[@class='right']/ul[1]/li[1]").click()
        time.sleep(2)
        if not ("谈读书" in wd.find_element_by_class_name("Com_Crumbs").text):
            success = False
            print('\t进入天天阅读失败！')
        else:
            print('\t进入天天阅读成功！')

        wd.find_element_by_xpath("html/body/div[3]/div/div[4]/span").click()
        time.sleep(2)
        if not  ('偷偷读书' in wd.find_element_by_class_name("Com_Crumbs").text):
            success = False
            print("\t下一篇切换失败！")
        else:
            print('\t下一篇切换成功！')

        wd.find_element_by_xpath("html/body/div[3]/div/div[4]/span[1]").click()
        if not ("谈读书" in wd.find_element_by_class_name("Com_Crumbs").text):
            success = False
            print('\t上一篇切换失败！')
        else:
            print('\t上一篇切换成功！')

        self.assertTrue(success)
    ##假期作业首页
    def test04_holiday_sy(self):
        # 假期作业——首页
        print("开始测试！假期作业首页")
        wd = self.wd
        success = True
        if ("暂未开放假期作业" in wd.find_element_by_tag_name("html").text):
            success = False
            print("未开放假期作业")
            return
        # 寒假作业使用说明弹窗显示
        wd.find_element_by_xpath("//span[text()='使用说明']").click()
        time.sleep(0.5)
        # 关闭使用说明弹窗
        wd.find_element_by_xpath("//input[@class='know']").click()
        time.sleep(0.5)
        # 切换班级弹窗显示
        wd.find_element_by_class_name("down").click()
        if not ("选择班级" in wd.find_element_by_tag_name("html").text):
            success = False
            print("\t切换班级弹窗显示失败！")
        else:
            print("\t切换班级弹窗显示成功！")
        time.sleep(0.5)
        # 关闭切换年级弹窗
        wd.find_element_by_xpath("//div[@class='selectClass']/i").click()
        if not ("智能培优" in wd.find_element_by_tag_name("html").text):
            success = False
            print("\t关闭班级弹窗失败！")
        else:
            print("\t关闭班级弹窗成功！")
        # 检查作业页初始化
        wd.find_element_by_xpath("//button[text()='检查作业']").click()
        if not ("排名" in wd.find_element_by_tag_name("html").text):
                success = False
                print("\t检查作业页初始化失败！")
        else:
                print("\t检查作业页初始化成功！")
        time.sleep(0.5)
        # 进入学生详情页（点击查看按钮）
        # 进入检查作业页-点击列表内第一条的查看按钮
        wd.find_element_by_xpath("//div[@id='rank']//a[.='查看']").click()
        if not ("完成情况" in wd.find_element_by_tag_name("html").text):
            success = False
            print("\t学生详情页初始化失败")
        else:
            print("\t学生详情页初始化成功")
        # 切换左侧单元(切换到第三单元）
        unittxt = wd.find_elements_by_xpath("//ul[@class='everyone_report_subject']/li")
        if (unittxt.__sizeof__()>0):
            unittxt[-1].click()
            if not ("水平自测" in wd.find_element_by_tag_name("html").text):
                success = False
                print("切换单元失败")
            else:
                print("切换单元成功")

        # 切换作业类型
        worktypes = wd.find_elements_by_xpath("//ul[@class='everyone_report_column']/li")
        for i in range(len(worktypes)):
            worktypes[i].click()
            worktxt = worktypes[i].text
            # 页面初始化
            # 切换到iframe页面（当前页面中有两个或多个嵌入页面时）
            wd.switch_to.frame("iframeReload")
            # 查看页面是否有该元素
            resourcetext = wd.find_element_by_tag_name("html").text
            if not (("下列加点字" in resourcetext)or("根据语境" in resourcetext)or("作家汪曾祺" in resourcetext)):
                success = False
                print("\t学生详情页——"+worktxt+"页初始化失败")
            else:
                print("\t学生详情页——"+worktxt+"页初始化成功")
                # 切换出页面
            wd.switch_to.default_content()
            time.sleep(6)

        self.assertTrue(success)

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()

'''
from selenium import webdriver
from Constant.sys_constant import *
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest, os
#import exceptions

class test_holiday_t(unittest.TestCase):
    # 老师pc端-假期作业

    def setUp(self):
        # 定义浏览器下载配置
        profile = webdriver.FirefoxProfile(Firefox_Path)
        #profile = webdriver.FirefoxProfile("C:\\Users\\Administrator\\AppData\\Local\\Mozilla\\Firefox\\Profiles\\pl3wrsan.default")
        # 定义浏览器，打开测试网站
        self.wd = webdriver.Firefox(profile)
        #self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.wd.get(LOGIN_URL)
        #self.wd.get("http://www.wuhaodaoxue.com")
        # 脚本运行时，错误的信息将被打印到这个列表中。
        self.verificationErrors = []
        # 是否继续接受下一下警告
        self.accept_next_alert = True
        wd = self.wd
        time.sleep(1)
        #窗口最大化
        wd.maximize_window()
        # 登录
        wd.find_element_by_id("Phone").click()
        wd.find_element_by_id("Phone").clear()
        wd.find_element_by_id("Phone").send_keys("17470000002")
        wd.find_element_by_id("Pass").click()
        wd.find_element_by_id("Pass").clear()
        wd.find_element_by_id("Pass").send_keys("123456")
        wd.find_element_by_id("LoginBtn").click()
        # 检查是否登录成功
        if not (len(wd.find_elements_by_id("User")) != 0):
            print("登录失败！")
        #进入首页
        if not ("您讲课比赛的坚实后援" in wd.find_element_by_tag_name("html").text):
            success = False
            print("首页初始化失败")
        else:
            print("首页初始化成功")
        menu = wd.find_elements_by_class_name("totalnav")
        ActionChains(wd).move_to_element(menu[1]).perform()
        time.sleep(2)
        #wd.find_element_by_xpath(".//*[@id='Header']/header/div/nav/ul/li[3]/ul/li[5]/a").click()
        sonmenu = wd.find_elements_by_class_name("c_NavSecond")
        asonmenu = sonmenu[1].find_elements_by_tag_name("a")
        asonmenu[4].click()

        #从banner图进入假期作业首页
        wd.find_element_by_xpath("//div[@id='in_swiper']/div[1]/a").click()
        if not ("假期作业" in wd.find_element_by_tag_name("html").text):
            success = False
            print("寒假作业初始化失败！")
        else:
            print("寒假作业初始化成功！")
        time.sleep(2)

        #默认寒假作业说明弹窗关闭验证
        try:
            wd.find_element_by_xpath("//input[@class='know']").click()
        except:
            print("寒假作业作业说明未弹出")
        else:
            print("寒假作业说明关闭成功")

        time.sleep(0.5)

    def test01_holiday_sy(self):
        # 寒假作业——首页
        print("开始测试！寒假作业首页") 
        wd = self.wd
        success = True
        try:
            wd.find_element_by_xpath("html/body/div[3]/div[2]/div/input").click()
        except  :
            pass            
        # 寒假作业使用说明弹窗显示
        if ("block" in wd.find_element_by_class_name("finish").get_attribute("style")):
            print("上期寒暑假作业已结束，下个假期见呗！")
        else:
            print("假期作业非空,可测!")
            wd.find_element_by_xpath("//p[@class='usetext']").click()
            time.sleep(0.5)
            # 关闭使用说明弹窗
            wd.find_element_by_xpath("//input[@class='know']").click()
            time.sleep(0.5)
            # 切换年级弹窗显示
            wd.find_element_by_xpath("//i[@class='arrow']").click()
            time.sleep(0.5)
            # 切换年级
            wd.find_element_by_xpath("//ul[@id='grades']//li[.='八年级']").click()
            time.sleep(0.5)
            # 关闭切换年级弹窗
            wd.find_element_by_xpath("//input[@class='ensure']").click()
            if not ("八年级语文寒假作业" in wd.find_element_by_tag_name("html").text):
                success = False
                print("切换年级失败！")
            else:
                print("切换年级成功！")
            # 检查作业页初始化
            wd.find_element_by_xpath("//input[@id='checkwork']").click()
            if not ("寒假作业完成情况" in wd.find_element_by_tag_name("html").text):
                success = False
                print("检查作业页初始化失败！")
            else:
                print("检查作业页初始化成功！")
            time.sleep(0.5)
            # 切换班级
            wd.find_element_by_xpath("//ul[@class='allclass']//li[.='七年级2班']").click()
            if not ("还没有学生，快邀请学生加入吧~" in wd.find_element_by_tag_name("html").text):
                success = False
                print("切换班级失败！")
            else:
                print("切换班级成功！")
            time.sleep(0.5)
            # 切换回来
            wd.find_element_by_xpath("//ul[@class='allclass']//li[.='七年级1班']").click()
            if not ("苗-学-701" in wd.find_element_by_tag_name("html").text):
                success = False
                print("切换班级失败！")
            else:
                print("切换班级成功！")
            time.sleep(0.5)

            # 进入学生详情页（点击查看按钮）
            wd.find_element_by_xpath("//div[3]/div/div/ul[2]/li[5]/a").click()
            if not ("完成情况" in wd.find_element_by_tag_name("html").text):
                success = False
                print("学生详情页初始化失败")
            else:
                print("学生详情页初始化成功")
            wd.find_element_by_xpath("html/body/div[3]/div/div/div[2]/ul/li[1]").click()
            time.sleep(5)
            # 智能填空页初始化
            wd.switch_to.frame("iframeReload")
            # 查看页面是否有该元素
            if not ("一、字音辨识" in wd.find_element_by_tag_name("html").text):
                success = False
                print("学生详情页——智能填空页初始化失败")
            else:
                print("学生详情页——智能填空页初始化成功")
            # 切换出页面
            wd.switch_to.default_content()
            time.sleep(6)

            # 学生详情页——从智能填空页切换到水平自测试卷页
            wd.find_element_by_xpath("//ul[@class='everyone_report_column']//li[.='水平自测']").click()
            wd.implicitly_wait(6)
            # 切换到iframe页面（当前页面中有两个或多个嵌入页面时）
            wd.switch_to.frame("iframeReload")
            time.sleep(5)
            # 查看页面是否有该元素
            if not ("C．化妆　　慈善　　干涩　　花枝招展" in wd.find_element_by_tag_name("html").text):
                success = False
                print("学生详情页——水平自测页初始化失败")
            else:
                print("学生详情页——水平自测页初始化成功")
            # 切换出页面
            wd.switch_to.default_content()
            time.sleep(5)

            # 学生详情页——从水平自测页切换到提能训练试卷页
            wd.find_element_by_xpath("//ul[@class='everyone_report_column']//li[.='提能训练']").click()
            time.sleep(5)
            # 切换到iframe页面（当前页面中有两个或多个嵌入页面时）
            wd.switch_to.frame("iframeReload")
            # 查看页面是否有该元素
            if not ("一年好景秋须记" in wd.find_element_by_tag_name("html").text):
                success = False
                print("学生详情页——提能训练页初始化失败")
            else:
                print("学生详情页——提能训练页初始化成功")
            # 切换出页面
            wd.switch_to.default_content()
            time.sleep(3)

            # 学生详情页——从提能训练页切换到学科素养页
            wd.find_element_by_xpath("//ul[@class='everyone_report_column']//li[.='学科素养']").click()
            time.sleep(5)
            # 切换到iframe页面（当前页面中有两个或多个嵌入页面时）
            wd.switch_to.frame("iframeReload")
            # 查看页面是否有该元素
            if not ("冬天" in wd.find_element_by_tag_name("html").text):
                success = False
                print("学生详情页——学科素养页初始化失败")
            else:
                print("学生详情页——学科素养页初始化成功")
            wd.switch_to.default_content()
            wd.implicitly_wait(5)

            self.assertTrue(success)


    def test02_gap(self):
        # 智能填空
        print("开始测试！智能填空")
        wd = self.wd
        success = True
        # wd = self.wd
        # success = True
        # 点击智能填空
        wd.find_element_by_xpath("//ul[@class='list0']//a[.='智能填空']").click()
        if not ("智能填空" in wd.find_element_by_tag_name("html").text):
            success = False
            print("智能填空初始化失败！")
        else:
            print("智能填空初始化成功！")
        time.sleep(1)
        # 做题
        # 第一题
        wd.find_element_by_xpath("//div[@id='paperWrapper']//p[.='yùn']").click()
        wd.find_element_by_xpath("//div[@id='paperWrapper']//p[.='bò']").click()
        wd.find_element_by_xpath("//div[@id='paperWrapper']//p[.='hè']").click()
        wd.find_element_by_xpath("//div[@id='paperWrapper']//p[.='kàn']").click()
        wd.find_element_by_xpath("//div[@id='paperWrapper']//p[.='shù']").click()
        print("第一题做题完成")
        # 第二题
        wd.find_element_by_xpath("//div[@id='paperWrapper']//p[.='贬']").click()
        wd.find_element_by_xpath("//div[@id='paperWrapper']//p[.='蓑']").click()
        wd.find_element_by_xpath("//div[@id='paperWrapper']//p[.='嘹']").click()
        wd.find_element_by_xpath("//div[@id='paperWrapper']//p[.='敞']").click()
        wd.find_element_by_xpath("//div[@id='paperWrapper']//p[.='晌']").click()
        wd.find_element_by_xpath("//div[@id='paperWrapper']//p[.='镶']").click()
        wd.find_element_by_xpath("//div[@id='paperWrapper']//p[.='涣']").click()
        wd.find_element_by_xpath("//div[@id='paperWrapper']//p[.='鬃']").click()
        wd.find_element_by_xpath("//div[@id='paperWrapper']//p[.='轿']").click()
        wd.find_element_by_xpath("//div[@id='paperWrapper']//p[.='犷']").click()
        print("第二题做题完成")

        # 点击提交按钮,未完成全部题目弹窗验证
        wd.find_element_by_link_text("提交").click()
        if not ("还有空格没有填写呢，请完后提交" in wd.find_element_by_tag_name("html").text):
            success = False
            print("未完成全部题目弹窗验证失败！")
        else:
            print("未完成全部题目弹窗验证成功！")
        time.sleep(1)
        # 点击题目答案，不选择挖空弹窗验证
        wd.find_element_by_xpath("//div[@id='paperWrapper']//p[.='工夫']").click()
        if not ("请至少选择一个填空区域呢" in wd.find_element_by_tag_name("html").text):
            success = False
            print("不选择挖空弹窗验证失败！")
        else:
            print("不选择挖空弹窗验证成功！")
        time.sleep(1)
        # 第三题
        wd.find_element_by_xpath("//div[@id='paperWrapper']/div[3]/div[2]/div[1]/div/div/div[1]/p[1]/span").click()
        wd.find_element_by_xpath("//div[@id='paperWrapper']//p[.='功夫']").click()
        wd.find_element_by_xpath("//div[@id='paperWrapper']/div[3]/div[2]/div[1]/div/div/div[1]/p[2]/span").click()
        wd.find_element_by_xpath("//div[@id='paperWrapper']//p[.='工夫']").click()
        wd.find_element_by_xpath("//div[@id='paperWrapper']/div[3]/div[2]/div[2]/div/div/div[1]/p[1]/span").click()
        wd.find_element_by_xpath("//div[@id='paperWrapper']//p[.='应和']").click()
        wd.find_element_by_xpath("//div[@id='paperWrapper']/div[3]/div[2]/div[2]/div/div/div[1]/p[2]/span").click()
        wd.find_element_by_xpath("//div[@id='paperWrapper']//p[.='附和']").click()
        wd.find_element_by_xpath("//div[@id='paperWrapper']/div[3]/div[2]/div[3]/div/div/div[1]/p[1]/span").click()
        wd.find_element_by_xpath("//div[@id='paperWrapper']//p[.='宽敞']").click()
        wd.find_element_by_xpath("//div[@id='paperWrapper']/div[3]/div[2]/div[3]/div/div/div[1]/p[2]/span").click()
        wd.find_element_by_xpath("//div[@id='paperWrapper']//p[.='宽广']").click()
        wd.find_element_by_xpath("//div[@id='paperWrapper']/div[3]/div[2]/div[4]/div/div/div[1]/p[1]/span").click()
        wd.find_element_by_xpath("//div[@id='paperWrapper']//p[.='莅临']").click()
        wd.find_element_by_xpath("//div[@id='paperWrapper']/div[3]/div[2]/div[4]/div/div/div[1]/p[2]/span").click()
        wd.find_element_by_xpath("//div[@id='paperWrapper']//p[.='光临']").click()
        print("第三题完成")
        # 点击提交按钮,完成全部题目弹窗验证
        wd.find_element_by_link_text("提交").click()
        if not ("【答案】" in wd.find_element_by_tag_name("html").text):
            success = False
            print("智能填空答案页初始化失败！")
        else:
            print("智能填空答案页初始化成功！")
        time.sleep(1)

        # 智能填空页——水平自测按钮链接验证
        wd.find_element_by_link_text("水平自测").click()
        if not ("水平自测" in wd.find_element_by_tag_name("html").text):
            success = False
            print("智能填空页水平自测按钮链接验证失败！")
        else:
            print("智能填空页水平自测按钮链接验证成功！")
            # 返回寒假作业首页
            wd.find_element_by_xpath("//div[@class='Com_Crumbs']//a[.='假期作业']").click()
            time.sleep(2)
        self.assertTrue(success)


    def test03_level(self):
        # 水平自测
        print("开始测试！水平自测")
        wd = self.wd
        success = True
        # wd = self.wd
        # success = True
        # 点击水平自测
        wd.find_element_by_xpath("//ul[@class='list0']//a[.='水平自测']").click()
        if not ("水平自测" in wd.find_element_by_tag_name("html").text):
            success = False
            print("水平自测初始化失败！")
        else:
            print("水平自测初始化成功！")
        time.sleep(1)
        # 查看解析
        # 定位到题目元素
        article = wd.find_element_by_xpath("//div[@class='groups']/div[1]/div/div/div[2]/div[4]/p")
        # 鼠标悬浮在题目位置
        ActionChains(wd).move_to_element(article).perform()
        # 等待1秒
        time.sleep(1)
        # 定位到查看解析
        mouse = wd.find_element_by_xpath("//div[4]/div/div[1]/div/div[2]/div[1]/div/div/div[3]/a[3]")
        # 鼠标移动至查看解析上方悬浮
        ActionChains(wd).move_to_element(mouse).perform()
        # 查看解析展开/收起
        wd.find_element_by_xpath("//div[4]/div/div[1]/div/div[2]/div[1]/div/div/div[3]/a[3]").click()
        if not ("【答案】" in wd.find_element_by_tag_name("html").text):
            success = False
            print("查看解析失败！")
        else:
            print("查看解析成功！")
        time.sleep(5)
        # 收回解析
        wd.find_element_by_xpath("//div[4]/div/div[1]/div/div[2]/div[1]/div/div/div[3]/a[2]").click()
        if ("【答案】" in wd.find_element_by_tag_name("html").text):
            success = False
            print("收回解析失败！")
        else:
            print("收回解析成功！")
        time.sleep(2)
        # 点击报错--正常流程
        # 报错弹窗显示验证

        wd.find_element_by_xpath("//div[@class='groups']//a[.='报错']").click()
        wd.find_element_by_xpath("//div[5]/div/ul/li[1]").click()
        wd.find_element_by_xpath("//div[5]/div/ul/li[2]").click()
        time.sleep(1)
        wd.find_element_by_xpath("//textarea[@class='report-error-wrapper-text']").send_keys("自动化测试报错")
        time.sleep(2)
        wd.find_element_by_xpath("//div[5]/div/div/a[1]").click()
        if not ("操作成功" in wd.find_element_by_tag_name("html").text):
            success = False
            print("报错失败！")
        else:
            print("报错成功！")
        time.sleep(2)

        # 水平自测页——智能填空按钮链接验证
        wd.find_element_by_xpath("//div[@id='linkGroup']//a[.='智能填空']").click()
        if not ("智能填空" in wd.find_element_by_tag_name("html").text):
            success = False
            print("水平自测的智能填空按钮链接验证失败！")
        else:
            print("水平自测的智能填空按钮链接成功！")
        # 返回寒假作业首页
        wd.find_element_by_xpath("//div[@class='Com_Crumbs']//a[.='假期作业']").click()
        # 点击水平自测
        wd.find_element_by_xpath("//div[3]/div[1]/div[1]/div/section[1]/ul/li[1]/div/a[2]").click()
        # 水平自测页——提能训练按钮链接验证
        wd.find_element_by_xpath("//div[@id='linkGroup']//a[.='提能训练']").click()
        if not ("提能训练" in wd.find_element_by_tag_name("html").text):
            success = False
            print("水平自测的提能训练按钮链接失败！")
        else:
            print("水平自测的提能训练按钮链接成功！")
            time.sleep(2)
        self.assertTrue(success)



    def test04_improve(self):
        # 提能训练
        print("开始测试！提能训练")
        wd = self.wd
        success = True
        # 点击提能训练
        wd.find_element_by_xpath("//div[3]/div[1]/div[1]/div/section[1]/ul/li[1]/div/a[3]").click()
        if not ("提能训练" in wd.find_element_by_tag_name("html").text):
            success = False
            print("提能训练初始化失败！")
        else:
            print("提能训练初始化成功！")
        time.sleep(1)
        # 再换一套按钮验证
        wd.find_element_by_xpath("//a[@id='deployQuestionBtn']").click()
        if not ("题型配置中，请稍候..." in wd.find_element_by_tag_name("html").text):
            success = False
            print("再换一套按钮功能失败！")
        else:
            print("再换一套按钮功能成功！")
        time.sleep(5)
        # 再换一套按钮二次验证
        wd.find_element_by_xpath("//a[@id='deployQuestionBtn']").click()
        if not ("题型配置中，请稍候..." in wd.find_element_by_tag_name("html").text):
            success = False
            print("二次再换一套按钮功能失败！")
        else:
            print("二次再换一套按钮功能成功！")
        time.sleep(5)
        # 再换一套按钮三次验证
        wd.find_element_by_xpath("//a[@id='deployQuestionBtn']").click()
        if not ("试看机会用完了~" in wd.find_element_by_tag_name("html").text):
            success = False
            print("三次再换一套按钮功能失败！")
        else:
            print("三次再换一套按钮功能成功！")
        time.sleep(2)
        # 查看解析

        # 定位到题目元素
        article = wd.find_element_by_xpath("//div[@id='paperWrapper']/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/p")
        # 鼠标悬浮在题目位置
        ActionChains(wd).move_to_element(article).perform()
        # 等待1秒
        time.sleep(1)
        # 定位到查看解析
        mouse = wd.find_element_by_xpath("//div[3]/div/div[1]/div[1]/div[2]/div[1]/div/div/div[3]/a[3]")
        # 鼠标移动至查看解析上方悬浮
        ActionChains(wd).move_to_element(mouse).perform()
        # 查看解析展开/收起
        wd.find_element_by_xpath("//div[3]/div/div[1]/div[1]/div[2]/div[1]/div/div/div[3]/a[3]").click()
        if not ("【答案】" in wd.find_element_by_tag_name("html").text):
            success = False
            print("查看解析失败！")
        else:
            print("查看解析成功！")
        time.sleep(5)
        # 收回解析
        wd.find_element_by_xpath("//div[3]/div/div[1]/div[1]/div[2]/div[1]/div/div/div[3]/a[2]").click()
        if ("【答案】" in wd.find_element_by_tag_name("html").text):
            success = False
            print("收回解析失败！")
        else:
            print("收回解析成功！")
        time.sleep(5)
        # 点击报错--正常流程
        # 报错弹窗显示验证

        wd.find_element_by_xpath("//div[@id='paperWrapper']//a[.='报错']").click()
        wd.find_element_by_xpath("//div[4]/div/ul/li[1]").click()
        wd.find_element_by_xpath("//div[4]/div/ul/li[2]").click()
        time.sleep(1)
        wd.find_element_by_xpath("//textarea[@class='report-error-wrapper-text']").send_keys("自动化测试报错")
        time.sleep(2)
        wd.find_element_by_xpath("//div[4]/div/div/a[1]").click()
        if not ("操作成功" in wd.find_element_by_tag_name("html").text):
            success = False
            print("报错失败！")
        else:
            print("报错成功！")
        time.sleep(2)

        # 提能训练页——水平自测按钮链接验证
        # 点击水平自测按钮
        wd.find_element_by_xpath("//div[3]/div/div[2]/a[1]").click()
        if not ("专题一 第一单元巩固提升 水平自测"in wd.find_element_by_tag_name("html").text):
            success = False
            print("提能训练页-水平自测按钮链接验证失败")
        else:
            print("提能训练页-水平自测按钮链接验证成功")
        time.sleep(1)
        # 返回假期作业首页
        # 点击面包屑导航——假期作业
        wd.find_element_by_xpath("//div[@class='Com_Crumbs']//a[.='假期作业']").click()
        time.sleep(1)
        # 点击提能训练
        wd.find_element_by_xpath("//div[3]/div[1]/div[1]/div/section[1]/ul/li[1]/div/a[3]").click()
        # 提能训练页——学科素养按钮链接验证
        wd.find_element_by_xpath("//div[3]/div/div[2]/a[2]").click()
        if not ("专题一 第一单元巩固提升 学科素养" in wd.find_element_by_tag_name("html").text):
            success = False
            print("提能训练页-学科素养按钮链接失败！")
        else:
            print("提能训练页-学科素养按钮链接成功！")
        time.sleep(1)
        self.assertTrue(success)

    def test05_quality(self):
        # 学科素养
        print("开始测试！学科素养")
        wd = self.wd
        success = True
        # 点击学科素养
        time.sleep(5)
        wd.find_element_by_xpath("//div[3]/div[1]/div[1]/div/section[1]/ul/li[1]/div/a[4]").click()
        # 切换到iframe页面（当前页面中有两个或多个嵌入页面时）
        #wd.switch_to.frame("iframeReload")
        # 查看页面是否有该元素
        if not ("专题一 第一单元巩固提升 学科素养" in wd.find_element_by_tag_name("html").text):
            success = False
            print("学科素养页初始化失败")
        else:
            print("学科素养页初始化成功")
        time.sleep(2)
        # 切换出页面
        #wd.switch_to.default_content()
        #time.sleep(5)
        # 学科素养页——提能训练按钮链接验证
        wd.find_element_by_xpath("//div[4]/div/div/div[3]/a").click()
        if not ("专题一 第一单元巩固提升 提能训练" in wd.find_element_by_tag_name("html").text):
            success = False
            print("学科素养页-提能训练按钮链接失败！")
        else:
            print("学科素养页-提能训练按钮链接成功！")
        time.sleep(1)
        self.assertTrue(success)

    def test06_comprehensive(self):
        # 综合练习
        print("开始测试！综合练习")
        wd = self.wd
        success = True
        # 将滚动条拖到底部
        wd.execute_script("window.scrollBy(0,1500)")
        print("下拉成功")
        time.sleep(2)
        # 点击综合练习
        wd.find_element_by_xpath("//ul[@class='list1']//span[.='综合练习五']").click()
        if not ("综合练习五" in wd.find_element_by_tag_name("html").text):
            success = False
            print("综合练习五初始化失败！")
        else:
            print("综合练习五初始化成功！")
        time.sleep(5)
        # 查看解析
        # 定位到题目元素
        article = wd.find_element_by_xpath("//div[@id='paperWrapper']/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[3]/p")
        # 鼠标悬浮在题目位置
        ActionChains(wd).move_to_element(article).perform()
        # 等待1秒
        time.sleep(1)
        # 定位到查看解析
        mouse = wd.find_element_by_xpath("//div[3]/div/div/div[1]/div[2]/div[1]/div[2]/div/div[3]/a[3]")
        # 鼠标移动至查看解析上方悬浮
        ActionChains(wd).move_to_element(mouse).perform()
        # 查看解析展开/收起
        wd.find_element_by_xpath("//div[3]/div/div/div[1]/div[2]/div[1]/div[2]/div/div[3]/a[3]").click()
        if not ("【答案】" in wd.find_element_by_tag_name("html").text):
            success = False
            print("查看解析失败！")
        else:
            print("查看解析成功！")
        time.sleep(5)
        # 收回解析
        wd.find_element_by_xpath("//div[3]/div/div/div[1]/div[2]/div[1]/div[2]/div/div[3]/a[2]").click()
        if  ("【答案】" in wd.find_element_by_tag_name("html").text):
            success = False
            print("收回解析失败！")
        else:
            print("收回解析成功！")
        time.sleep(5)
        # 点击报错--正常流程
        # 报错弹窗显示验证
        wd.find_element_by_xpath("//div[3]/div/div/div[1]/div[2]/div[1]/div[2]/div/div[3]/a[1]").click()
        wd.find_element_by_xpath("//div[4]/div/ul/li[1]").click()
        wd.find_element_by_xpath("//div[4]/div/ul/li[2]").click()
        time.sleep(1)
        wd.find_element_by_xpath("//textarea[@class='report-error-wrapper-text']").send_keys("自动化测试报错")
        time.sleep(2)
        wd.find_element_by_xpath("//div[4]/div/div/a[1]").click()
        if not ("操作成功" in wd.find_element_by_tag_name("html").text):
            success = False
            print("报错失败！")
        else:
            print("报错成功！")
        time.sleep(2)
        self.assertTrue(success)

    def test07_prepare(self):
        # 预习专题
        print("开始测试！预习专题")
        wd = self.wd
        success = True
        # 将滚动条拖到底部
        wd.execute_script("window.scrollBy(0,1500)")
        print("下拉成功")
        time.sleep(2)
        # 点击预习视频
        wd.find_element_by_xpath("//div[3]/div[1]/div[1]/div/section[3]/ul/li[1]/h3/span").click()
        if not ("第1课 邓稼先" in wd.find_element_by_tag_name("html").text):
            success = False
            print("预习专题一初始化失败！")
        else:
            print("预习专题一初始化成功！")
        time.sleep(10)
        wd.execute_script("window.scrollBy(0,1000)")
        # 获取原页面句柄
        homepage_handle = wd.current_window_handle
        # 点击预习测试
        wd.find_element_by_xpath("//input[@id='preparetest']").click()
        time.sleep(5)
        # 获得当前所有打开的窗口的句柄
        all_handles = wd.window_handles
        # 进入做题窗口
        for handle in all_handles:
            if handle != homepage_handle:
                wd.switch_to.window(handle)
                if not ("1 邓稼先" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print("进入预习测试详情页失败！")
                else:
                    print("进入预习测试详情页成功！")
                wd.close()
                wd.switch_to.window(homepage_handle)
        time.sleep(2)
        self.assertTrue(success)

    def tearDown(self):
        wd = self.wd
        # 将滚动条移动到页面的顶部
        js = "var q=document.documentElement.scrollTop=0"
        self.wd.execute_script(js)
        # 退出
        # 定位到首页头像元素
        article = wd.find_element_by_xpath(".//*[@id='UserHeadImg']")
        # 鼠标悬浮再用户头像位置
        ActionChains(wd).move_to_element(article).perform()
        # 等待3秒
        time.sleep(2)
        # 定位到退出元素
        mouse = wd.find_element_by_xpath(".//*[@id='Quit']")
        # 鼠标移动至退出上方悬浮
        ActionChains(wd).move_to_element(mouse).perform()
        # 点击退出
        # wd.find_element_by_xpath(".//*[@id='menav']/li[3]/a").click()
        wd.find_element_by_xpath(".//*[@id='Quit']").click()
        time.sleep(0.5)
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
'''
