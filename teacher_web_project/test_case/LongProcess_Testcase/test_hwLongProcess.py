'''
Created on 2018年1月29日
updated on 2018年2月7日
五好导学网-web端-测试长流程 自动化测试脚本
@author: 闫双双
2018年2月25日  测试长流程-修改登录调用
               测试长流程-将之前的作业改为测试
               测试长流程-布置测试  增加编辑功能（编辑试卷名称，时间，添加题目，删除题目，调整题型，设置分数）
2018年5月17日 测试长流程  所有功能脚本在判断后面添加success = False语句
              测试长流程  修改老师端因作业和测试菜单合并导致的布置测试/批改/报告入口问题
2018年7月18日 测试长流程-布置测试  修改v1.4版本改版的布置对象问题
2018年9月3日  测试长流程-布置测试 批改测试 老师报告  修改v1.5版本的菜单问题
'''
# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest
import sys, os
from Constant.sys_constant import *
from test_case.PubModule import login

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_hwLongProcess(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        success = True
        wd = self.wd
        # 登录测试环境
        wd.get(LOGIN_URL)
        # self.wd.get("http://preprod-whdx.bcbook.cn")


    # 老师-布置测试
    def test_01hwLongProcess_assign(self):
        print("开始测试老师-布置测试")
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
        # 定位首页作业并点击布置测试
        A = wd.find_element_by_xpath(".//*[@id='Header']/header/div/nav/ul/li[4]/span")
        ActionChains(wd).move_to_element(A).perform()
        time.sleep(3)
        wd.find_element_by_xpath(".//*[@id='Header']/header/div/nav/ul/li[4]/ul/li[2]/a").click()
        # 判断是否进入布置页面
        if not ("第一单元" in wd.find_element_by_xpath(".//*[@id='test']/div[1]/dl/dd/ul/li[1]").text):
            print("FAILED-进入布置测试页面失败！")
            success = False
        else:
            print("SUCCESS-进入布置测试页面成功！")
        # 点击第一单元
        wd.find_element_by_xpath(".//*[@id='test']/div[1]/dl/dd/ul/li[1]").click()
        time.sleep(1)
        # 点击课时练
        wd.find_element_by_xpath(".//*[@id='test']/div[2]/dl/dd/div/div[1]/div/a/img").click()
        time.sleep(1)
        # 判断是否成功进入课时练试题页面
        if not ("阶段检测卷（一）" in wd.find_element_by_xpath(".//*[@id='testpaper']/div[1]/p[1]").text):
            print("FAILED-进入课时练试题页面失败！")
            success = False
        else:
            print("SUCCESS-进入课时练试题页面成功！")
        time.sleep(2)
        # 定位并点击解析
        B = wd.find_element_by_xpath(".//*[@id='testpaper']/div[2]/ul[1]/li[1]")
        ActionChains(wd).move_to_element(B).perform()
        time.sleep(2)
        wd.find_element_by_xpath(".//*[@id='testpaper']/div[2]/ul[1]/li[1]/div/div[2]/input[2]").click()
        # 定位并点击收起解析
        C = wd.find_element_by_xpath(".//*[@id='testpaper']/div[2]/ul[1]/li[1]")
        ActionChains(wd).move_to_element(C).perform()
        time.sleep(2)
        wd.find_element_by_xpath(".//*[@id='testpaper']/div[2]/ul[1]/li[1]/div/div[2]/input[2]").click()
        # 定位并点击报错
        D = wd.find_element_by_xpath(".//*[@id='testpaper']/div[2]/ul[1]/li[1]")
        ActionChains(wd).move_to_element(D).perform()
        time.sleep(2)
        wd.find_element_by_xpath(".//*[@id='testpaper']/div[2]/ul[1]/li[1]/div/div[2]/input[1]").click()
        # 选择错误类型
        wd.find_element_by_xpath(".//*[@id='error']/div/ul/li[1]").click()
        time.sleep(1)
        # 输入错误原因
        wd.find_element_by_xpath(".//*[@id='error']/div/textarea").send_keys("测试报错功能是否OK")
        time.sleep(1)
        # 点击确定
        wd.find_element_by_xpath(".//*[@id='error']/div/p[3]/input[1]").click()
        time.sleep(0.5)
        # 判断报错是否成功
        if not ("报错成功" in wd.find_element_by_xpath(".//*[@id='c_ErrorMsg']").text):
            print("FAILED-报错失败！")
            success = False
        else:
            print("SUCCESS-报错成功！")
        time.sleep(2)
        # 点击编辑按钮
        wd.find_element_by_xpath(".//*[@id='testpaper']/div[4]/div/input[2]").click()
        time.sleep(1)
        # 判断是否进入编辑页面
        if not ("添加题目" in wd.find_element_by_xpath(".//*[@id='line0']/div/h3/span[4]/i").text):
            print("FAILED-进入编辑页面失败！")
            success = False
        else:
            print("SUCCESS-进入编辑页面成功！")
            time.sleep(2)
            # 添加题目
            wd.find_element_by_xpath(".//*[@id='line0']/div/h3/span[4]/i").click()
            time.sleep(1)
            # 添加题目选择知识点-字形
            wd.find_element_by_xpath(".//*[@id='ckknowledge']/span[2]").click()
            time.sleep(1)
            # 添加题目选择题型-填空题
            wd.find_element_by_xpath(".//*[@id='addtype']/span[2]").click()
            time.sleep(1)
            # 添加题目选择难度-基础
            wd.find_element_by_xpath(".//*[@id='diffs']/span[1]").click()
            time.sleep(1)
            # 点击选入
            wd.find_element_by_xpath(
                ".//*[@id='questionlib']/div/div[2]/div[1]/ul/li[1]/div/div[1]/div/span[3]").click()
            time.sleep(2)
            # 点击添加题目完成
            wd.find_element_by_xpath(".//*[@id='questionlib']/div/div[3]/div/input").click()
            time.sleep(2)
            # 删除题目
            E = wd.find_element_by_xpath(".//*[@id='line0']/li[1]")
            ActionChains(wd).move_to_element(E).perform()
            time.sleep(2)
            E.find_element_by_xpath("//input[@value='删除']").click()
            # wd.find_element_by_xpath(".//*[@id='line0']/li[2]/div/div[2]/input[1]").click()
            time.sleep(1)
            # 调整题型
            # 点击调整题型
            wd.find_element_by_xpath(".//*[@id='testpaper']/div[3]/div/input[3]").click()
            time.sleep(1)
            # 点击添加题型
            wd.find_element_by_xpath(".//*[@id='addbtn']/span").click()
            time.sleep(1)
            # 选择要添加的题型—选择题
            wd.find_element_by_xpath(".//*[@id='setLines']/div/div/div[1]/a[1]").click()
            time.sleep(1)
            # 点击删除题型
            F = wd.find_element_by_xpath(".//*[@id='alllines']/li[4]")
            ActionChains(wd).move_to_element(F).perform()
            time.sleep(2)
            wd.find_element_by_xpath(".//*[@id='alllines']/li[4]/i").click()
            time.sleep(1)
            # 点击调整题型完成按钮
            wd.find_element_by_xpath(".//*[@id='setLines']/div/div/div[2]/span[1]").click()
            time.sleep(1)
            # 点击设置分数按钮
            wd.find_element_by_xpath(".//*[@id='testpaper']/div[3]/div/input[2]").click()
            # 设置第5题分数
            wd.find_element_by_xpath(".//*[@id='setscore']/div[2]/div[1]/ul/li[5]/div/input").click()
            wd.find_element_by_xpath(".//*[@id='setscore']/div[2]/div[1]/ul/li[5]/div/input").clear()
            wd.find_element_by_xpath(".//*[@id='setscore']/div[2]/div[1]/ul/li[5]/div/input").send_keys("2")
            time.sleep(1)
            # 设置第7题分数
            wd.find_element_by_xpath(".//*[@id='setscore']/div[2]/div[1]/ul/li[7]/div/input").click()
            wd.find_element_by_xpath(".//*[@id='setscore']/div[2]/div[1]/ul/li[7]/div/input").clear()
            wd.find_element_by_xpath(".//*[@id='setscore']/div[2]/div[1]/ul/li[7]/div/input").send_keys("2")
            time.sleep(1)
            # 点击分数设置完成按钮
            wd.find_element_by_xpath(".//*[@id='setscore']/div[3]/input[1]").click()
            time.sleep(1)
            # 编辑试卷名称
            wd.find_element_by_xpath(".//*[@id='testpaper']/div[1]/p[1]/input").click()
            wd.find_element_by_xpath(".//*[@id='testpaper']/div[1]/p[1]/input").clear()
            wd.find_element_by_xpath(".//*[@id='testpaper']/div[1]/p[1]/input").send_keys("阶段检测卷（一）自动化")
            time.sleep(1)
            # 编辑试卷时间
            wd.find_element_by_xpath(".//*[@id='testpaper']/div[1]/p[2]/span[1]/input").click()
            wd.find_element_by_xpath(".//*[@id='testpaper']/div[1]/p[2]/span[1]/input").clear()
            wd.find_element_by_xpath(".//*[@id='testpaper']/div[1]/p[2]/span[1]/input").send_keys("60")
            time.sleep(1)
            # 编辑页面，点击编辑完成按钮
            wd.find_element_by_xpath(".//*[@id='testpaper']/div[3]/div/input[1]").click()
            time.sleep(1)
            # 判断编辑是否成功
            if not ("保存成功" in wd.find_element_by_xpath(".//*[@id='c_ErrorMsg']").text):
                print("FAILED-编辑失败！")
                success = False
            else:
                print("SUCCESS-编辑成功！")
                time.sleep(2)
        # 悬浮并点击布置按钮
        F = wd.find_elements_by_class_name("lay_btn")[2]
        ActionChains(wd).move_to_element(F).perform()
        time.sleep(2)
        wd.find_element_by_xpath(".//*[@id='testpaper']/div[4]/div/span/div/ul/li").click()
        time.sleep(1)
        # 点击布置给七年级1班
        wd.find_element_by_xpath(".//*[@id='testpaper']/div[3]/div/div[3]/ul/li[1]").click()
        time.sleep(1)
        # 点击确认按钮
        wd.find_element_by_xpath(".//*[@id='testpaper']/div[3]/div/div[4]/a[1]").click()
        time.sleep(0.4)
        # 判断布置是否成功
        if not ("布置成功 即将跳转" in wd.find_element_by_xpath(".//*[@id='c_ErrorMsg']").text):
            print("FAILED-布置作业失败！")
            success = False
        else:
            print("SUCCESS-布置作业成功！")
        time.sleep(2)
        self.assertTrue(success)

    # 学生-写作业
    def test_02hwLongProcess_writting(self):
        print("开始测试学生-写作业")
        success = True
        wd = self.wd
        wd.maximize_window()
        # 调用login()函数登录
        login.login(self, "19600000701", "123456")
        # 判断登录是否成功
        if not ("首页" in wd.find_element_by_xpath(".//*[@id='Com_NavMain']/li[1]/a").text):
            print("FAILED-登录失败！")
            success = False
        else:
            print("SUCCESS-登录成功！")
        # 定位首页作业和测试并点击写作业
        A = wd.find_element_by_xpath(".//*[@id='Com_NavMain']/li[3]/span[2]")
        ActionChains(wd).move_to_element(A).perform()
        time.sleep(3)
        wd.find_element_by_xpath(".//*[@id='Com_NavMain']/li[3]/ul/li[1]/a").click()
        # 判断是否进入写作业列表页面
        if not ("测试" in wd.find_element_by_xpath(
                ".//*[@id='homeWorkIndex']/div[1]/div[1]/div[2]/ul/ul/li[1]/span[1]").text):
            print("FAILED-进入写作业列表页面失败！")
            success = False
        else:
            print("SUCCESS-进入写作业列表页面成功！")
        # 点击去完成按钮
        finish = wd.find_elements_by_class_name("hwListEverTodo")
        finish[0].click()
        time.sleep(2)
        # 判断是否进入写作业页面
        if not ("注意事项" in wd.find_element_by_xpath("html/body/div[4]/div[1]/div[2]/div[3]/div/div[2]/p[1]").text):
            print("FAILED-进入写作业页面失败！")
            success = False
        else:
            print("SUCCESS-进入写作业页面成功！")
        time.sleep(2)
        # 遍历客观题，并都选择D
        # shiti = wd.find_element_by_class_name("task_paper")
        xuanxiang = wd.find_elements_by_class_name("optionchoose")
        for i in range(0, len(xuanxiang)):
            xuanxiang[i].click()
            #time.sleep(1)
        # 做客观题
        # wd.find_element_by_xpath("html/body/div[4]/div[1]/div[2]/div[1]/div[1]/div/div[1]/div/div/div[2]/div[1]").click()
        # wd.find_element_by_xpath("html/body/div[4]/div[1]/div[2]/div[1]/div[1]/div/div[5]/div/div/div[2]/div[1]").click()
        # wd.find_element_by_xpath("html/body/div[4]/div[1]/div[2]/div[1]/div[1]/div/div[6]/div/div/div[2]/div[1]").click()
        # wd.find_element_by_xpath("html/body/div[4]/div[1]/div[2]/div[1]/div[1]/div/div[7]/div/div/div[2]/div[1]/p/span").click()
        # 上传主观题图片
        # 点击上传按钮
        wd.find_element_by_xpath("html/body/div[4]/div[1]/div[2]/div[3]/div/div[4]/div[2]").click()
        time.sleep(2)
        # 点击添加图片按钮
        wd.find_element_by_xpath(".//*[@id='inputImage']").click()
        time.sleep(2)
        # 调用autoIT的程序，上传图片
        os.system(autoitfile_path+"uploadpicture.exe")
        time.sleep(2)
        # 点击确定修改按钮
        wd.find_element_by_id("GetImgUrl").click()
        time.sleep(2)
        # 判断图片是否上传成功
        # if not ("正在提交" in wd.find_element_by_id("c_ErrorMsg").text):
        # print("FAILED-图片上传失败！")
        # else:
        # print("SUCCESS-图片上传成功！")
        # 点击提交按钮
        wd.find_element_by_xpath("html/body/div[4]/div[1]/div[2]/div[3]/div/div[5]").click()
        time.sleep(2)
        # 判断作业提交是否成功
        if not ("数据分析" in wd.find_element_by_xpath("html/body/div[4]/div[1]/div[2]/span").text):
            print("FAILED-作业提交失败！")
            success = False
        else:
            print("SUCCESS-作业提交成功！")
        time.sleep(2)
        self.assertTrue(success)

    # 老师-批改测试
    def test_03hwLongProcess_Correcting(self):
        print("开始测试老师-批改测试")
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
        # 定位首页作业并点击批改
        A = wd.find_element_by_xpath(".//*[@id='Header']/header/div/nav/ul/li[4]/span")
        ActionChains(wd).move_to_element(A).perform()
        time.sleep(3)
        wd.find_element_by_xpath(".//*[@id='Header']/header/div/nav/ul/li[4]/ul/li[3]/a").click()
        time.sleep(2)
        # 判断是否进入批改测试列表页面
        if not ("阶段检测卷（一）" in wd.find_element_by_xpath(".//*[@id='correct']/div[1]/div[2]/div/ul/li[2]").text):
            print("FAILED-进入批改测试列表页面失败！")
            success = False
        else:
            print("SUCCESS-进入批改测试列表页面成功！")
        # 点击批改按钮
        wd.find_element_by_xpath(".//*[@id='correct']/div[1]/div[2]/div/ul/li[4]/input").click()
        time.sleep(1)
        # 判断是否成功进入批改页面
        if not ("旋转" in wd.find_element_by_xpath(".//*[@id='imgCon']/div[1]/ul/li[1]/span").text):
            print("FAILED-进入批改页面失败！")
            success = False
        else:
            print("SUCCESS-进入批改页面成功！")
        time.sleep(2)
        # 批改
        pigai = wd.find_element_by_class_name("correct_up")
        duihao = pigai.find_elements_by_tag_name("li")
        for i in range(0, len(duihao)):
            a = duihao[i].find_elements_by_tag_name("span")
            a[1].click()
            #time.sleep(1)
        # 点击旋转按钮
        wd.find_element_by_xpath(".//*[@id='imgCon']/div[1]/ul/li[1]").click()
        time.sleep(1)
        # 点击查看答案按钮
        wd.find_element_by_xpath(".//*[@id='correctting']/div[3]/div[2]/input[1]").click()
        time.sleep(1)
        # 点击关闭答案按钮
        wd.find_element_by_xpath(".//*[@id='answer']/p/i").click()
        time.sleep(1)
        # 点击结束批改按钮
        wd.find_element_by_xpath(".//*[@id='correctting']/div[3]/div[2]/input[2]").click()
        time.sleep(1)
        # 在弹窗中选择结束批改
        wd.find_element_by_xpath(".//*[@id='correctting']/div[4]/div/div[2]/input[2]").click()
        time.sleep(1)
        self.assertTrue(success)

    # 老师端测试报告
    def test_04hwLongProcess_TReport(self):
        print("开始测试老师-测试报告")
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
        # 定位首页作业并点击报告
        A = wd.find_element_by_xpath(".//*[@id='Header']/header/div/nav/ul/li[4]/span")
        ActionChains(wd).move_to_element(A).perform()
        time.sleep(3)
        wd.find_element_by_xpath(".//*[@id='Header']/header/div/nav/ul/li[4]/ul/li[4]/a").click()
        time.sleep(2)
        # 判断是否进入报告列表页面
        if not ("平均分" in wd.find_element_by_xpath(".//*[@id='w_HomeWorkList']/li/p[3]").text):
            print("FAILED-进入老师测试报告列表页面失败！")
            success = False
        else:
            print("SUCCESS-进入老师测试报告列表页面成功！")
        time.sleep(2)
        # 点击查看按钮
        wd.find_element_by_class_name("w_Looka0").click()
        time.sleep(2)
        # 判断是否成功进入答题情况页面
        if not ("讲评参考" in wd.find_element_by_xpath(".//*[@id='commentConference']").text):
            print("FAILED-进入答题情况页面失败！")
            success = False
        else:
            print("SUCCESS-进入答题情况页面成功！")
            time.sleep(2)
            # 在答题情况页面点击切换试题
            wd.find_element_by_xpath(".//*[@id='prev']").click()
            time.sleep(2)
            # 点击讲评参考按钮
            wd.find_element_by_xpath(".//*[@id='commentConference']").click()
            time.sleep(2)
            # 判断是否成功进入讲评参考页面
            if not ("打印" in wd.find_element_by_xpath(".//*[@id='print']").text):
                print("FAILED-进入讲评参考页面失败！")
                success = False
            else:
                print("SUCCESS-进入讲评参考页面成功！")
                time.sleep(1)
                # 点击解析按钮
                wd.find_element_by_xpath(".//*[@id='w_commentReferenceContent']/div[3]/p[4]/button[2]").click()
                time.sleep(1)
                # 点击收起按钮
                wd.find_element_by_xpath(".//*[@id='w_commentReferenceContent']/div[3]/p[4]/button[2]").click()
                time.sleep(1)
                # 点击报错按钮
                wd.find_element_by_xpath(".//*[@id='w_commentReferenceContent']/div[3]/p[4]/button[1]").click()
                time.sleep(1)
                # 选择错误类型
                wd.find_element_by_xpath(".//*[@id='errTypeBtnGrp']/button[1]").click()
                time.sleep(1)
                # 输入错误原因
                wd.find_element_by_xpath(".//*[@id='errTypeBtnGrp']/textarea").click()
                wd.find_element_by_xpath(".//*[@id='errTypeBtnGrp']/textarea").clear()
                wd.find_element_by_xpath(".//*[@id='errTypeBtnGrp']/textarea").send_keys("老师端答题情况报错自动化测试")
                time.sleep(1)
                # 点击确定按钮
                wd.find_element_by_xpath(".//*[@id='submitError']").click()
                time.sleep(1)
                # 判断报错是否成功
                # if not ("提交成功" in wd.find_element_by_xpath(".//*[@id='c_ErrorMsg']").text):
                # print("FAILED-报错失败！")
                # else:
                # print("SUCCESS-报错成功！")
                time.sleep(2)
                # 点击讲评提醒按钮
                wd.find_element_by_xpath(".//*[@id='w_commentReferenceContent']/div[3]/p[1]/span/button").click()
                time.sleep(1)
                # 输入讲评提醒
                wd.find_element_by_xpath(".//*[@id='w_commentReferenceContent']/div[3]/div[1]/div/textarea").click()
                wd.find_element_by_xpath(".//*[@id='w_commentReferenceContent']/div[3]/div[1]/div/textarea").clear()
                wd.find_element_by_xpath(".//*[@id='w_commentReferenceContent']/div[3]/div[1]/div/textarea").send_keys(
                    "老师端答题情况讲评提醒自动化测试")
                time.sleep(1)
                # 点击保存按钮
                wd.find_element_by_xpath(".//*[@id='w_commentReferenceContent']/div[3]/div[1]/div/p/button[3]").click()
                time.sleep(3)
                # 判断讲评提醒保存是否成功
                if not ("老师端答题情况讲评提醒自动化测试" in wd.find_element_by_xpath(
                        ".//*[@id='w_commentReferenceContent']/div[3]/div[1]/div/textarea").get_attribute("value")):
                    print("FAILED-讲评提醒保存失败！")
                    success = False
                else:
                    print("SUCCESS-讲评提醒保存成功！")
                    # 点击编辑按钮
                    wd.find_element_by_xpath(
                        ".//*[@id='w_commentReferenceContent']/div[3]/div[1]/div/p/button[2]").click()
                    time.sleep(1)
                    # 编辑讲评提醒
                    wd.find_element_by_xpath(".//*[@id='w_commentReferenceContent']/div[3]/div[1]/div/textarea").click()
                    wd.find_element_by_xpath(".//*[@id='w_commentReferenceContent']/div[3]/div[1]/div/textarea").clear()
                    wd.find_element_by_xpath(
                        ".//*[@id='w_commentReferenceContent']/div[3]/div[1]/div/textarea").send_keys(
                        "老师端答题情况编辑讲评提醒自动化测试")
                    time.sleep(1)
                    # 点击保存按钮
                    wd.find_element_by_xpath(
                        ".//*[@id='w_commentReferenceContent']/div[3]/div[1]/div/p/button[3]").click()
                    time.sleep(3)
                    # 判断讲评提醒编辑是否成功
                    if not ("老师端答题情况编辑讲评提醒自动化测试" in wd.find_element_by_xpath(
                            ".//*[@id='w_commentReferenceContent']/div[3]/div[1]/div/textarea").get_attribute("value")):
                        print("FAILED-讲评提醒编辑失败！")
                        success = False
                    else:
                        print("SUCCESS-讲评提醒编辑成功！")
                    time.sleep(2)
                    # 点击讲评提醒删除按钮
                    wd.find_element_by_xpath(
                        ".//*[@id='w_commentReferenceContent']/div[3]/div[1]/div/p/button[1]").click()
                    time.sleep(0.5)
                    # 判断删除是否成功
                    if not (wd.find_element_by_xpath(
                            ".//*[@id='w_commentReferenceContent']/div[3]/p[1]/span/button").is_displayed()):
                        print("FAILED-讲评提醒删除失败！")
                        success = False
                    else:
                        print("SUCCESS-讲评提醒删除成功！")
                    time.sleep(2)
                time.sleep(2)
                # 点击打印按钮
                wd.find_element_by_xpath(".//*[@id='print']").click()
                time.sleep(2)
                # 点击打印窗口关闭按钮
                wd.find_element_by_xpath(".//*[@id='printModal']/div/div/div[1]/button").click()
                time.sleep(2)
            # 返回答题情况页面
            wd.back()
            time.sleep(2)
            # 点击知识点统计
            a = wd.find_element_by_id("bcTab")
            b = a.find_elements_by_tag_name("li")
            b[2].click()
            time.sleep(2)
            # 判断是否成功进入知识点统计页面
            if not ("active" in b[2].get_attribute("class")):
                print("FAILED-进入知识点统计页面失败！")
                success = False
            else:
                print("SUCCESS-进入知识点统计页面成功！")
            time.sleep(2)
            # 点击学生详情按钮
            wd.find_element_by_xpath("//a[@href='#studentDetails']").click()
            time.sleep(2)
            # 判断是否成功进入学生详情页面
            if not ("序号" in wd.find_element_by_xpath(".//*[@id='firstUl']/li[1]").text):
                print("FAILED-进入学生详情页面失败！")
                success = False
            else:
                print("SUCCESS-进入学生详情页面成功！")
                time.sleep(2)
                # 点击查看按钮
                chakan = wd.find_element_by_xpath(".//*[@id='studentDetails']/div[1]/ul[2]/li[4]/a")
                name =  wd.find_element_by_xpath(".//*[@id='studentDetails']/div[1]/ul[2]/li[4]/a/../../li[2]").text
                chakan.click()
                time.sleep(2)
                # 判断是否成功进入学生详情试题页面
                if not (name in wd.find_element_by_tag_name("html").text):
                    print("FAILED-进入学生详情试题页面失败！")
                    success = False
                else:
                    print("SUCCESS-进入学生详情试题页面成功！")
                time.sleep(2)
        self.assertTrue(success)

    # 学生-看报告
    def test_05hwLongProcess_SReport(self):
        print("开始测试学生-看报告")
        success = True
        wd = self.wd
        wd.maximize_window()
        # 调用login()函数登录
        login.login(self, "19600000701", "123456")
        # 判断登录是否成功
        if not ("首页" in wd.find_element_by_xpath(".//*[@id='Com_NavMain']/li[1]/a").text):
            print("FAILED-登录失败！")
            success = False
        else:
            print("SUCCESS-登录成功！")
        # 定位首页作业和测试并点击看报告
        A = wd.find_element_by_xpath(".//*[@id='Com_NavMain']/li[3]/span[2]")
        ActionChains(wd).move_to_element(A).perform()
        time.sleep(3)
        wd.find_element_by_xpath(".//*[@id='Com_NavMain']/li[3]/ul/li[2]/a").click()
        time.sleep(2)
        # 判断是否进入看报告列表页面
        if not ("作业报告" in wd.find_element_by_xpath(".//*[@id='reportIndex']/div[2]/p[1]").text):
            print("FAILED-进入看报告列表页面失败！")
            success = False
        else:
            print("SUCCESS-进入看报告列表页面成功！")
        time.sleep(2)
        # 点击查看按钮
        # wd.find_element_by_xpath(".//*[@id='cf2dd8925ca24378a4592e55222e1d11']").click()
        a = wd.find_element_by_class_name("reportHomeEver")
        b = a.find_elements_by_tag_name("span")
        b[3].click()
        time.sleep(1)
        # 判断是否成功进入测试报告页面
        if not ("测试详情" in wd.find_element_by_xpath("html/body/div[4]/div[1]/div[6]").text):
            print("FAILED-进入测试报告页面失败！")
            success = False
        else:
            print("SUCCESS-进入测试报告页面成功！")
            time.sleep(2)

            # 点击班级目标按钮
            wd.find_element_by_xpath("html/body/div[4]/div[1]/div[2]/div").click()
            time.sleep(1)
            # 点击班级目标弹窗关闭按钮
            wd.find_element_by_xpath("html/body/div[4]/div[2]/div/i").click()
            time.sleep(2)
            # 点击需要讲按钮
            wd.find_element_by_xpath(".//*[@id='r_detail']/div[1]/div[2]/div[1]/div/div/div[1]/div").click()
            time.sleep(1)
            # 判断点击需要讲是否成功
            if ("需要讲" in wd.find_element_by_xpath(".//*[@id='r_detail']/div[1]/div[2]/div[1]/div/div/div[1]/div").text):
                print("FAILED-点击需要讲按钮失败！")
                success = False
            else:
                print("SUCCESS-点击需要讲按钮成功！")
                time.sleep(2)

        self.assertTrue(success)

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()