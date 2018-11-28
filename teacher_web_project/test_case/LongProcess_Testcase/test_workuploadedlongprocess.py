# -*- coding: utf-8 -*-
# Created on 2018年2月1日
# updated on 2018年2月5日
# 五好导学网-教师web端-自主上传作业长流程 自动化测试脚本
# @author: 马春苗



# 引用库
import time, unittest, os
# 导入python版的selenium(webdriver)
from selenium import webdriver
#引用模块
from Constant.sys_constant import *
from selenium.webdriver.common.action_chains import ActionChains
from test_case.PubModule import login,topmenu_t

class test_workuploaded(unittest.TestCase):
    def setUp(self):
        # 定义浏览器下载配置
        #profile = webdriver.FirefoxProfile(Firefox_Path)
        # 定义浏览器，打开测试网站
        self.wd = webdriver.Firefox()
        #profile = WebDriver.firefox_profile("C:\\Users\\Administrator\\AppData\\Local\\Mozilla\\Firefox\\Profiles\\pl3wrsan.default")
        #self.wd = WebDriver.firefox(profile)
        self.wd.implicitly_wait(30)
        self.wd.get(LOGIN_URL)
        # self.wd.get("http://preprod-whdx.bcbook.cn")
        # self.wd.get("http://whdx.bcbook.cn")
        # 脚本运行时，错误的信息将被打印到这个列表中。
        self.verificationErrors = []
        # 是否继续接受下一下警告
        self.accept_next_alert = True
        wd = self.wd
        time.sleep(1)
        # 窗口最大化
        wd.maximize_window()

    def test01_upload(self):
        wd = self.wd
        success = True
        # 上传作业长流程-上传试卷
        print("开始测试！上传试卷")
        # 登录
        wd.find_element_by_id("Phone").click()
        wd.find_element_by_id("Phone").clear()
        wd.find_element_by_id("Phone").send_keys("17400000071")
        wd.find_element_by_id("Pass").click()
        wd.find_element_by_id("Pass").clear()
        wd.find_element_by_id("Pass").send_keys("123456")
        wd.find_element_by_id("LoginBtn").click()
        # 检查是否登录成功
        if  (len(wd.find_elements_by_id("User")) != 0):
            print("登录成功！")
        time.sleep(1)

        # 导航选择
        A = wd.find_element_by_class_name("c_Nav ")
        time.sleep(1)
        A1 = A.find_elements_by_class_name("totalnav")
        time.sleep(1)
        ActionChains(wd).move_to_element(A1[0]).perform()
        time.sleep(1)
        A2 = A1[0].find_elements_by_class_name("menuId")
        A2[0].click()
        time.sleep(2)

        # 切换章节
        wd.find_element_by_xpath("//div[3]/div/div[1]/dl[1]/dd/ul/li[2]").click()
        time.sleep(2)
        wd.find_element_by_xpath("//div[@id='test']//li[normalize-space(.)='第6课']").click()
        time.sleep(1)

        # 点击自主上传
        wd.find_element_by_xpath("//div[@class='lay_types']/div[6]/div/a/img").click()
        time.sleep(1)
        if not ("自主上传" in wd.find_element_by_tag_name("html").text):
            success = False
            print("自主上传弹窗显示失败")
        else:
            print("自主上传弹窗显示成功")


        #反向：不上传试卷点击上传按钮
        # 点击上传按钮
        wd.find_element_by_class_name("file-upload-wrapper-content-submit-btn").click()
        time.sleep(2)
        #正向：上传试卷点击上传按钮
        # 点击选择word文件按钮
        wd.find_element_by_class_name("file-upload-wrapper-content-choose-file-input").click()
        time.sleep(2)
        # 调用autoIT的程序，上传图片
        os.system(autoitfile_path+"uploaded.exe")
        #os.system(autoitfile_path+"shangchuanzuoyeshijuan.exe")
        time.sleep(2)
        # 点击上传按钮
        wd.find_element_by_class_name("file-upload-wrapper-content-submit-btn").click()
        time.sleep(2)
        # 判断提示是否正确
        if not ("上传成功" in wd.find_element_by_tag_name("html").text):
            print("提示不正确！")
        else:
            print("提示正确！")
        # 上传作业长流程-布置试卷
        print("开始测试！布置试卷")
        time.sleep(5)
        # 试卷页初始化
        if not ("语文自主上传" in wd.find_element_by_tag_name("html").text):
            print("试卷初始化失败！")
        else:
            print("试卷初始化成功！")


        # 查看/收起解析
        # 定位到题目元素
        article = wd.find_element_by_xpath("//div[@id='paperWrapper']/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/p")
        # 鼠标悬浮在题目位置
        ActionChains(wd).move_to_element(article).perform()
        # 等待1秒
        time.sleep(1)
        # 定位到查看解析
        mouse = wd.find_element_by_xpath("//div[@id='paperWrapper']//a[.='解析']")
        # 鼠标移动至查看解析上方悬浮
        ActionChains(wd).move_to_element(mouse).perform()
        # 查看解析展开/收起
        wd.find_element_by_xpath("//div[@id='paperWrapper']//a[.='解析']").click()
        if not ("【答案】" in wd.find_element_by_tag_name("html").text):
            success = False
            print("查看解析失败！")
        else:
            print("查看解析成功！")
        time.sleep(2)
        # 收回解析
        wd.find_element_by_xpath("//div[@id='paperWrapper']//a[.='收起']").click()
        if ("【答案】" in wd.find_element_by_tag_name("html").text):
            success = False
            print("收回解析失败！")
        else:
            print("收回解析成功！")
        time.sleep(1)
        # 点击布置按钮
        wd.find_element_by_class_name("assignment-btn").click()
        time.sleep(1)
        # 修改截止时间
        # wd.find_element_by_class_name("param-for-assignment-inner-lastTime-hour-minus").click()
        #wd.find_element_by_css_selector("span.up").click()
        time.sleep(0.5)
        '''
        # 选择布置对象(班级内无学生）
        wd.find_element_by_xpath("//ul[@class='param-for-assignment-inner-list-grade']//li[.='七年级6班']").click()
        if not ("此班级中无学生" in wd.find_element_by_tag_name("html").text):
            success = False
            print("布置对象内无学生提示验证失败")
        else:
            print("布置对象内无学生提示验证成功")
        time.sleep(1)
        '''
        # 选择布置对象（班级内有学生）
        wd.find_element_by_xpath("//ul[@class='param-for-assignment-inner-list-grade']//li[.='八年级1班']").click()
        time.sleep(0.5)
        # 点击确定按钮
        wd.find_element_by_class_name("param-for-assignment-inner-submit-btn").click()
        '''
        if not ("布置成功" in wd.find_element_by_tag_name("html").text):
            success = False
            print("布置上传作业失败")
        else:
            print("布置上传作业成功")
        '''
        time.sleep(2)
        self.assertTrue(success)

    def test02_writting(self):
        wd = self.wd
        success = True
        # 作业长流程-学生写作业
        print("开始测试！学生写作业")

        # 登录
        wd.find_element_by_id("Phone").click()
        wd.find_element_by_id("Phone").clear()
        wd.find_element_by_id("Phone").send_keys("17400007001")
        wd.find_element_by_id("Pass").click()
        wd.find_element_by_id("Pass").clear()
        wd.find_element_by_id("Pass").send_keys("123456")
        wd.find_element_by_id("LoginBtn").click()
        # 检查是否登录成功
        if not (len(wd.find_elements_by_id("User")) != 0):
            print("登录失败！")

        # 进入写作业页
        # 定位到作业与测试元素
        article = wd.find_element_by_xpath(".//*[@id='Com_NavMain']/li[3]")
        # 鼠标悬浮在作业与测试位置
        ActionChains(wd).move_to_element(article).perform()
        # 等待3秒
        time.sleep(2)
        # 定位到写作业元素
        mouse = wd.find_element_by_xpath(".//*[@id='Com_NavMain']/li[3]/ul/li[1]")
        # 鼠标移动至写作业上方悬浮
        ActionChains(wd).move_to_element(mouse).perform()
        time.sleep(0.5)
        # 点击写作业
        wd.find_element_by_xpath(".//*[@id='Com_NavMain']/li[3]/ul/li[1]/a").click()
        # 判断是否进入写作业列表页面
        if not ("写作业" in wd.find_element_by_tag_name("html").text):
            print("进入写作业列表页面失败！")
        else:
            print("进入写作业列表页面成功！")

        # 写作业
        # 进入写作业列表-点击列表内第一条作业的去完成按钮
        d = wd.find_elements_by_class_name("hwListEverTodo")
        # print(len(d))
        span = d[0]
        c = span.find_element_by_tag_name("span")
        c.click()
        #  d[0].click()
        time.sleep(2)
        # 判断是否进入写作业页面
        if not ("注意事项" in wd.find_element_by_xpath("//div[4]/div[1]/div[2]/div[3]/div/div[2]/p[1]").text):
            print("进入写作业页面失败！")
        else:
            print("进入写作业页面成功！")

        xz = wd.find_elements_by_class_name("optionchoose")
        for i in range(0, len(xz)):
            xz[i].click()
            time.sleep(1)
        time.sleep(2)
        # 点击上传按钮
        wd.find_element_by_xpath("html/body/div[4]/div[1]/div[2]/div[3]/div/div[4]/div[2]").click()
        time.sleep(2)
        # 上传主观题图片（反向验证：未上传答案图片）
        # 点击确定修改按钮
        wd.find_element_by_id("GetImgUrl").click()
        time.sleep(2)
        # 点击添加图片按钮
        wd.find_element_by_xpath(".//*[@id='inputImage']").click()
        time.sleep(2)
        # 调用autoIT的程序，上传图片
        os.system(autoitfile_path + "uploadpicture.exe")
        #os.system(autoitfile_path + "zuoyeshangchuan.exe")
        time.sleep(2)
        # 点击确定修改按钮
        wd.find_element_by_id("GetImgUrl").click()
        time.sleep(2)
        # 点击提交按钮
        wd.find_element_by_xpath("html/body/div[4]/div[1]/div[2]/div[3]/div/div[5]").click()
        time.sleep(2)
        # 判断作业提交是否成功
        if not ("数据分析" in wd.find_element_by_xpath("html/body/div[4]/div[1]/div[2]/span").text):
            print("作业提交失败！")
        else:
            print("作业提交成功！")
        time.sleep(2)

        self.assertTrue(success)

    def test03_Correcting(self):
        wd = self.wd
        success = True
        # 作业长流程-老师批改
        print("开始测试！老师批改作业")
        # 登录
        wd.find_element_by_id("Phone").click()
        wd.find_element_by_id("Phone").clear()
        wd.find_element_by_id("Phone").send_keys("17400000071")
        wd.find_element_by_id("Pass").click()
        wd.find_element_by_id("Pass").clear()
        wd.find_element_by_id("Pass").send_keys("123456")
        wd.find_element_by_id("LoginBtn").click()
        # 检查是否登录成功
        if not (len(wd.find_elements_by_id("User")) != 0):
            print("登录失败！")

        time.sleep(2)
        # 导航选择作业--批改作业
        A = wd.find_element_by_class_name("c_Nav ")
        time.sleep(1)
        A1 = A.find_elements_by_class_name("totalnav")
        time.sleep(1)
        ActionChains(wd).move_to_element(A1[0]).perform()
        time.sleep(1)
        A2 = A1[0].find_elements_by_class_name("menuId")
        A2[2].click()
        time.sleep(2)


        # 判断是否进入批改作业列表页面
        if not ("提交" in wd.find_element_by_tag_name("html").text):
            success = False
            print("进入批改作业列表页面失败！")
        else:
            print("进入批改作业列表页面成功！")
        time.sleep(3)

        # 进入批改列表-点击列表内第一条作业的批改按钮
        #d = wd.find_elements_by_class_name("correct_ul")
        #print(len(d))
        # 点击批改按钮
        wd.find_element_by_xpath(".//*[@id='correct']/div[1]/div[2]/div/ul/li[4]/input").click()
        if not ("旋转" in wd.find_element_by_xpath("html/body/div[2]/div[2]/div/div[2]/div[1]/ul/li[1]/span").text):
            print("进入批改页面失败！")
        else:
            print("进入批改页面成功！")
        time.sleep(2)
        # 批改
        pigai = wd.find_element_by_class_name("correct_up")
        dui = pigai.find_elements_by_tag_name("li")
        for i in range(0, len(dui)):
            a = dui[i].find_elements_by_tag_name("span")
            a[1].click()
        # 上/下一张图片
        wd.find_element_by_xpath("html/body/div[2]/div[2]/div/div[2]/div[1]/img[1]").click()
        if not ("这已经是第一张了"in wd.find_element_by_tag_name("html").text):
            success = False
            print("上一张无图片提示失败")
        else:
            print("上一张无图片提示成功")
        time.sleep(5)
        wd.find_element_by_xpath("html/body/div[2]/div[2]/div/div[2]/div[1]/img[2]").click()
        if not ("这已经是最后一张了，休息一下吧"in wd.find_element_by_tag_name("html").text):
            success = False
            print("下一张无图片提示失败")
        else:
            print("下一张无图片提示成功")
        time.sleep(5)
        # 查看答案
        wd.find_element_by_xpath("html/body/div[2]/div[2]/div/div[3]/div[2]/input[1]").click()

        # 关闭答案
        wd.find_element_by_xpath("html/body/div[2]/div[2]/div[2]/i").click()
        time.sleep(2)
        # 点击旋转按钮
        wd.find_element_by_xpath(".//*[@id='imgCon']/div[1]/ul/li[1]").click()
        time.sleep(2)
        # 点击结束批改按钮
        wd.find_element_by_xpath(".//*[@id='correctting']/div[3]/div[2]/input[2]").click()
        time.sleep(1)
        # 结束批改弹窗--下次再批
        wd.find_element_by_xpath("//*[@id='correctting']/div[4]/div/div[2]/input[@value='稍后再批']").click()
        time.sleep(1)
        # 点击批改按钮
        wd.find_element_by_xpath(".//*[@id='correct']/div[1]/div[2]/div/ul/li[4]/input").click()
        # 点击结束批改按钮
        wd.find_element_by_xpath(".//*[@id='correctting']/div[3]/div[2]/input[2]").click()
        time.sleep(1)
        # 结束批改弹窗--结束批改
        wd.find_element_by_xpath("html/body/div[2]/div[2]/div/div[4]/div/div[2]/input[@value='确定结束']").click()
        time.sleep(2)

    def test04_xReport(self):
        wd = self.wd
        success = True
        # 作业长流程-学生看报告
        print("开始测试！学生看报告")
        # 登录17400007001
        login.login(self,"17400007001","123456")
        time.sleep(2)
        # 导航选择作业和测试--看报告
        topmenu_t.top_menu_kbg_s(self)
        time.sleep(2)
        # 判断是否进入报告列表
        if not ("看报告" in wd.find_element_by_xpath("//div[@class='Com_Crumbs_in']//span[.='看报告']").text):
            print("进入看报告列表页面失败！")
        else:
            print("进入看报告列表页面成功！")

        # 点击周报的更多按钮
        wd.find_element_by_link_text("更多>").click()
        time.sleep(1)
        if not ("全部作业周报" in wd.find_element_by_tag_name("html").text):
            print("进入周报列表页失败！")
        else:
            print("进入周报列表页成功！")

        zb_window = wd.current_window_handle
        # 进入列表第一条的周报详情页
        a = wd.find_element_by_class_name("r_content")
        b = a.find_elements_by_tag_name("ul")
        b[1].click()
        time.sleep(5)
        # 获得当前所有打开的窗口的句柄
        all_handles = wd.window_handles
        # 进入新窗口
        for handle in all_handles:
            if handle != zb_window:
                wd.switch_to.window(handle)
                if not ("一周大数据" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print("进入周报详情页失败！")
                else:
                    print("进入周报详情页成功！")
                wd.close()
                wd.switch_to.window(zb_window)

        # 返回到看报告首页
        wd.find_element_by_xpath("//div[@class='Com_Crumbs_in']//a[.='看报告']").click()
        time.sleep(1)

        # 点击列表页第一条作业报告的查看按钮
        a = wd.find_element_by_class_name("reportHomeEver")
        b = a.find_elements_by_tag_name("span")
        b[3].click()
        time.sleep(1)
        if not ("数据分析" in wd.find_element_by_tag_name("html").text):
            success = False
            print("报告详情页初始化失败！")
        else:
            print("报告详情页初始化成功！")


        # 点击班级目标
        wd.find_element_by_class_name("r_classtarget").click()
        time.sleep(1)
        # 关闭窗口
        wd.find_element_by_xpath("//div[4]/div[2]/div/i").click()
        time.sleep(1)

        # 点击试卷内第一个题的需要讲按钮
        try:
            wd.find_element_by_class_name("Needspeak")
            a = True
        except:
            a = False
        if a == True:
            print("该页面有未点击的需要讲按钮")
            d = wd.find_elements_by_class_name("Needspeak")
            d[0].click()
            time.sleep(0.5)
            wd.find_element_by_xpath("//div[@class='Com_Crumbs_in']//a[.='看报告']").click()
            time.sleep(0.5)
        else:
            print("该页面需要讲按钮已全部变为已提问")
            wd.find_element_by_xpath("//div[@class='Com_Crumbs_in']//a[.='看报告']").click()
            time.sleep(0.5)

        self.assertTrue(success)

    def test05_tReport(self):
        wd = self.wd
        success = True
        # 作业长流程-老师看报告
        # 登录
        wd.find_element_by_id("Phone").click()
        wd.find_element_by_id("Phone").clear()
        wd.find_element_by_id("Phone").send_keys("17400000071")
        wd.find_element_by_id("Pass").click()
        wd.find_element_by_id("Pass").clear()
        wd.find_element_by_id("Pass").send_keys("123456")
        wd.find_element_by_id("LoginBtn").click()
        # 检查是否登录成功
        if not (len(wd.find_elements_by_id("User")) != 0):
            print("登录失败！")

        # 导航选择
        A = wd.find_element_by_class_name("c_Nav ")
        time.sleep(1)
        A1 = A.find_elements_by_class_name("totalnav")
        time.sleep(1)
        ActionChains(wd).move_to_element(A1[0]).perform()
        time.sleep(1)
        A2 = A1[0].find_elements_by_class_name("menuId")
        A2[3].click()
        time.sleep(2)

        # 看报告
        # 进入看报告列表-点击列表内第一条报告的查看按钮
        d = wd.find_elements_by_class_name("w_PaperList")
        # print(len(d))
        a = d[0]
        c = a.find_element_by_class_name("w_Looka0")
        c.click()
        time.sleep(2)
        if not ("答题情况" in wd.find_element_by_class_name("active").text):
            success = False
            print("作业报告页初始化失败")
        else:
            print("作业报告页初始化成功")

        # 报告页--答题情况--切换试题
        a = wd.find_elements_by_class_name("questionNumLi")
        # print(len(a))
        b = a[1]
        b.click()
        time.sleep(2)
        if not ("阅读下面的语段，根据拼音写出相应的汉字" in wd.find_element_by_tag_name("html").text):
            success = False
            print("试题切换失败")
        else:
            print("试题切换成功")

        # 报告页--答题情况--讲评参考
        a = wd.find_element_by_id("answerStatus")
        b = a.find_element_by_id("commentConference")
        b.click()
        time.sleep(2)
        if not ("讲评提醒" in wd.find_element_by_class_name("remindBtn").text):
            success = False
            print("讲评参考页初始化失败")
        else:
            print("讲评参考页初始化成功")

        # 报告页--答题情况--讲评参考--讲评提醒
        wd.find_element_by_class_name("remindBtn").click()
        print("点击讲评提醒按钮成功")
        time.sleep(2)
        # 讲评提醒输入内容
        wd.find_element_by_xpath("//div[@id='w_commentReferenceContent']/div[1]/div[2]/div[1]/div/div/div[3]/div/textarea").send_keys("自动化测试讲评提醒")
        time.sleep(2)
        # 保存讲评提醒内容
        wd.find_element_by_class_name("remindSave").click()
        if not ("编辑" in wd.find_element_by_class_name("remindEdit").text):
            success = False
            print("保存讲评提醒内容失败")
        else:
            print("保存评语提醒内容成功")
        time.sleep(2)
        # 编辑讲评提醒内容
        wd.find_element_by_class_name("remindEdit").click()
        time.sleep(2)
        # 修改评语提醒内容
        wd.find_element_by_xpath("//div[@id='w_commentReferenceContent']//textarea[.='自动化测试讲评提醒']").send_keys("自动化测试讲评提醒编辑测试")
        time.sleep(2)
        # 保存讲评提醒内容
        wd.find_element_by_class_name("remindSave").click()
        if not ("编辑" in wd.find_element_by_class_name("remindEdit").text):
            success = False
            print("编辑保存讲评提醒内容失败")
        else:
            print("编辑保存评语提醒内容成功")
        time.sleep(2)
        # 删除讲评提醒内容
        wd.find_element_by_class_name("remindCancel").click()
        if ("编辑" in wd.find_element_by_class_name("remindEdit").text):
            success = False
            print("删除讲评提醒内容失败")
        else:
            print("删除评语提醒内容成功")
        time.sleep(2)

        # 查看解析展开/收起
        wd.find_element_by_class_name("analyseBtn").click()
        if not ("【答案】" in wd.find_element_by_tag_name("html").text):
            success = False
            print("查看解析失败！")
        else:
            print("查看解析成功！")
        time.sleep(5)
        # 收回解析
        wd.find_element_by_class_name("analyseBtn").click()

        if ("【答案】" in wd.find_element_by_tag_name("html").text):
            success = False
            print("收回解析失败！")
        else:
            print("收回解析成功！")

        # 返回到报告页
        wd.find_element_by_xpath("//div[@class='Com_Crumbs']//a[.='报告']").click()

        # 看报告
        # 进入看报告列表-点击列表内第一条报告的查看按钮
        d = wd.find_elements_by_class_name("w_PaperList")
        # print(len(d))
        a = d[0]
        c = a.find_element_by_class_name("w_Looka0")
        c.click()
        time.sleep(2)

        # 切换到学生详情
        a = wd.find_element_by_id("bcTab")
        b = a.find_elements_by_tag_name("li")
        b[1].click()
        time.sleep(2)
        # 判断是否成功进入学生详情页面
        if not ("序号" in wd.find_element_by_xpath(".//*[@id='firstUl']/li[1]").text):
            print("进入学生详情页面失败！")
        else:
            print("进入学生详情页面成功！")
        # 点击列表内第一个查看按钮
        #A = wd.find_element_by_id("studentDetails")
        #A1 = A.find_elements_by_tag_name("div")
        #A2 = A1[0].find_elements_by_tag_name("li")
        #A2[1].click()
        # 点击查看按钮
        wd.find_element_by_xpath("//div[@id='studentDetails']//a[.='查看']").click()
        if not ("学生详情" in wd.find_element_by_xpath("//article/div/div[2]/div/span").text):
            success = False
            print("查看学生试卷失败")
        else:
            print("查看学生试卷成功")
        self.assertTrue(success)

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()