'''
Created on 2018年6月14日
五好导学网-web端-布置测试自主上传长流程 自动化测试脚本
@author: 闫双双
功能包括：
1.自主上传和布置功能
2.写作业功能
3.批改功能
4.老师端报告
5.学生端报告

2018年7月16日 ：修改v1.4版本改版的自主上传和布置功能
2018年9月4日  布置测试自主上传长流程-布置测试 批改测试 老师报告  修改v1.5版本的菜单问题
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


class test_uploadedLongProcess(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        success = True
        wd = self.wd
        # 登录测试环境
        wd.get(LOGIN_URL)
        # self.wd.get("http://preprod-whdx.bcbook.cn")


    # 老师-自主上传并布置测试

    def test_01uploadedLongProcess_assign(self):
        print("开始测试老师-自主上传并布置测试")
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
        time.sleep(1)
        # 判断是否进入布置页面
        if not ("单元" in wd.find_element_by_xpath(".//*[@id='test']/div[1]/dl/dt").text):
            print("FAILED-进入布置测试页面失败！")
            success = False
        else:
            print("SUCCESS-进入布置测试页面成功！")
        # 点击第一单元
        wd.find_element_by_xpath(".//*[@id='test']/div[1]/dl/dd/ul/li[1]").click()
        time.sleep(1)
        # 点击自主上传
        wd.find_element_by_xpath(".//*[@id='test']/div[2]/dl/dd/div/div[5]/div/a/img").click()
        time.sleep(1)
        # 判断是否成功弹出自主上传弹窗
        if not ("自主上传" in wd.find_element_by_xpath(".//*[@id='fileUploadWrapper']/div/div[1]/p[1]").text):
            print("FAILED-弹出自主上传弹窗失败！")
            success = False
        else:
            print("SUCCESS-弹出自主上传弹窗成功！")
        time.sleep(2)
        #点击选择Word文件
        wd.find_element_by_xpath(".//*[@id='fileUploadWrapper']/div/div[1]/div/span/input").click()
        time.sleep(1)
        # 调用autoIT的程序，上传自主上传文档
        os.system(autoitfile_path+"uploaded.exe")
        time.sleep(2)
        #点击上传按钮
        wd.find_element_by_xpath(".//*[@id='fileUploadWrapper']/div/div[1]/a").click()
        time.sleep(1)
        #判断是否成功进入试题预览页面
        if not("积累运用"in wd.find_element_by_xpath(".//*[@id='paperWrapper']/div[1]/div[1]").text):
            print("FAILED-进入试题预览页面失败！")
            success = False
        else:
            print("SUCCESS-进入试题预览页面成功！")
        time.sleep(2)
        # 定位并点击解析
        B = wd.find_element_by_xpath(".//*[@id='paperWrapper']/div[1]/div[2]/div[1]/div")
        ActionChains(wd).move_to_element(B).perform()
        time.sleep(2)
        wd.find_element_by_xpath(".//*[@id='paperWrapper']/div[1]/div[2]/div[1]/div/div/a").click()
        # 定位并点击收起解析
        C = wd.find_element_by_xpath(".//*[@id='paperWrapper']/div[1]/div[2]/div[1]/div")
        ActionChains(wd).move_to_element(C).perform()
        time.sleep(2)
        wd.find_element_by_xpath(".//*[@id='paperWrapper']/div[1]/div[2]/div[1]/div/div/a").click()
        time.sleep(1)
        # 点击布置按钮
        wd.find_element_by_xpath(".//*[@id='wrapper']/a").click()
        time.sleep(1)
        # 点击布置给七年级1班
        wd.find_element_by_xpath(".//*[@id='vueWrapper']/div[1]/div/div[3]/ul/li[1]").click()
        time.sleep(1)
        # 点击确认按钮
        wd.find_element_by_xpath(".//*[@id='vueWrapper']/div[1]/div/div[4]/a[1]").click()
        time.sleep(2)
        # 判断布置是否成功
        if not ("我的测试" in wd.find_element_by_tag_name("html").text):
            print("FAILED-布置作业失败！")
            success = False
        else:
            print("SUCCESS-布置作业成功！")
        time.sleep(2)
        self.assertTrue(success)

    # 学生-写作业

    def test_02uploadedLongProcess_writting(self):
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
        if not ("自主上传" in wd.find_element_by_xpath(
                ".//*[@id='homeWorkIndex']/div[1]/div[1]/div[2]/ul/ul[1]/li[1]/span[1]").text):
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

    def test_03uploadedLongProcess_Correcting(self):
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
        if not ("语文自主上传" in wd.find_element_by_xpath(".//*[@id='correct']/div[1]/div[2]/div/ul[1]/li[2]").text):
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
        wd.find_element_by_xpath(".//*[@id='answer']/i").click()
        time.sleep(1)
        # 点击结束批改按钮
        wd.find_element_by_xpath(".//*[@id='correctting']/div[3]/div[2]/input[2]").click()
        time.sleep(1)
        # 在弹窗中选择结束批改
        wd.find_element_by_xpath(".//*[@id='correctting']/div[4]/div/div[2]/input[2]").click()
        time.sleep(1)
        self.assertTrue(success)

    # 老师端测试报告
    def test_04uploadedLongProcess_TReport(self):
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
        if not ("平均正确率" in wd.find_element_by_xpath(".//*[@id='w_HomeWorkList']/li[1]/p[3]").text):
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
                wd.find_element_by_xpath(".//*[@id='w_commentReferenceContent']/div[1]/div[2]/div[1]/div/div/p[2]/button").click()
                time.sleep(1)
                # 点击收起按钮
                wd.find_element_by_xpath(".//*[@id='w_commentReferenceContent']/div[1]/div[2]/div[1]/div/div/p[2]/button").click()
                time.sleep(1)
                # 点击讲评提醒按钮
                wd.find_element_by_xpath(".//*[@id='w_commentReferenceContent']/div[1]/div[2]/div[1]/div/div/div[3]/button").click()
                time.sleep(1)
                # 输入讲评提醒
                wd.find_element_by_xpath(".//*[@id='w_commentReferenceContent']/div[1]/div[2]/div[1]/div/div/div[3]/div/textarea").click()
                wd.find_element_by_xpath(".//*[@id='w_commentReferenceContent']/div[1]/div[2]/div[1]/div/div/div[3]/div/textarea").clear()
                wd.find_element_by_xpath(".//*[@id='w_commentReferenceContent']/div[1]/div[2]/div[1]/div/div/div[3]/div/textarea").send_keys(
                    "老师端答题情况讲评提醒自动化测试")
                time.sleep(1)
                # 点击保存按钮
                wd.find_element_by_xpath(".//*[@id='w_commentReferenceContent']/div[1]/div[2]/div[1]/div/div/div[3]/div/p/button[3]").click()
                time.sleep(3)
                # 判断讲评提醒保存是否成功
                if not ("老师端答题情况讲评提醒自动化测试" in wd.find_element_by_xpath(
                        ".//*[@id='w_commentReferenceContent']/div[1]/div[2]/div[1]/div/div/div[3]/div/textarea").get_attribute("value")):
                    print("FAILED-讲评提醒保存失败！")
                    success = False
                else:
                    print("SUCCESS-讲评提醒保存成功！")
                    # 点击编辑按钮
                    wd.find_element_by_xpath(
                        ".//*[@id='w_commentReferenceContent']/div[1]/div[2]/div[1]/div/div/div[3]/div/p/button[2]").click()
                    time.sleep(1)
                    # 编辑讲评提醒
                    wd.find_element_by_xpath(".//*[@id='w_commentReferenceContent']/div[1]/div[2]/div[1]/div/div/div[3]/div/textarea").click()
                    wd.find_element_by_xpath(".//*[@id='w_commentReferenceContent']/div[1]/div[2]/div[1]/div/div/div[3]/div/textarea").clear()
                    wd.find_element_by_xpath(
                        ".//*[@id='w_commentReferenceContent']/div[1]/div[2]/div[1]/div/div/div[3]/div/textarea").send_keys(
                        "老师端答题情况编辑讲评提醒自动化测试")
                    time.sleep(1)
                    # 点击保存按钮
                    wd.find_element_by_xpath(
                        ".//*[@id='w_commentReferenceContent']/div[1]/div[2]/div[1]/div/div/div[3]/div/p/button[3]").click()
                    time.sleep(3)
                    # 判断讲评提醒编辑是否成功
                    if not ("老师端答题情况编辑讲评提醒自动化测试" in wd.find_element_by_xpath(
                            ".//*[@id='w_commentReferenceContent']/div[1]/div[2]/div[1]/div/div/div[3]/div/textarea").get_attribute("value")):
                        print("FAILED-讲评提醒编辑失败！")
                        success = False
                    else:
                        print("SUCCESS-讲评提醒编辑成功！")
                    time.sleep(2)
                    # 点击讲评提醒删除按钮
                    wd.find_element_by_xpath(
                        ".//*[@id='w_commentReferenceContent']/div[1]/div[2]/div[1]/div/div/div[3]/div/p/button[1]").click()
                    time.sleep(1)
                    # 判断删除是否成功
                    # 点击讲评提醒按钮
                    wd.find_element_by_xpath(
                        ".//*[@id='w_commentReferenceContent']/div[1]/div[2]/div[1]/div/div/div[3]/button").click()
                    time.sleep(1)
                    if not (""in wd.find_element_by_xpath
                        (".//*[@id='w_commentReferenceContent']/div[1]/div[2]/div[1]/div/div/div[3]/div/textarea").text):
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
            # 点击学生详情按钮
            wd.find_element_by_xpath(".//*[@id='bcTab']/li[2]").click()
            time.sleep(2)
            # 判断是否成功进入学生详情页面
            if not ("序号" in wd.find_element_by_xpath(".//*[@id='firstUl']/li[1]").text):
                print("FAILED-进入学生详情页面失败！")
                success = False
            else:
                print("SUCCESS-进入学生详情页面成功！")
                time.sleep(2)
                # 点击查看按钮
                wd.find_element_by_xpath(".//*[@id='studentDetails']/div[1]/ul[2]/li[4]/a").click()
                time.sleep(2)
                # 判断是否成功进入学生详情试题页面
                if not ("积累运用" in wd.find_element_by_xpath(".//*[@id='paperContent']/div[1]/div[1]").text):
                    print("FAILED-进入学生详情试题页面失败！")
                    success = False
                else:
                    print("SUCCESS-进入学生详情试题页面成功！")
                time.sleep(2)
        self.assertTrue(success)

    # 学生-看报告

    def test_05uploadedLongProcess_SReport(self):
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