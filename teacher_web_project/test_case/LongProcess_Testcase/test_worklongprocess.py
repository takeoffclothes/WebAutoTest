# -*- coding: utf-8 -*-
# Created on 2018年2月1日
# updated on 2018年2月5日
# 五好导学网-教师web端-假期作业 自动化测试脚本
# @author: 马春苗
# 01 老师课时练首页流程：导航菜单-切换章节-课时练链接验证-分层作业（3个等级）链接验证-自主组卷链接验证-退出
# 02 老师编辑课时练流程：导航菜单-切换章节-课时练详情页初始化-查看/收起解析-报错功能-添加题目按钮验证-切换知识点-切换题型-切换难度-查看/收起解析-报错功能-选择题目功能-取消选择题目功能-选择题目功能-完成按钮-退出
# 02 老师布置课时练流程：课时练初始化-布置（修改截止时间、选择布置对象（有/无学生验证）、确定按钮）-退出
# 03 学生写作业：导航菜单-去完成按钮-做题（做选择题）-上传主观题图片-提交按钮-退出
# 04 老师批改作业：导航菜单-退出
# 05 学生查看报告：导航菜单-周报更多按钮-查看周报详情-返回报告首页-查看作业报告详情-班级目标弹窗验证-需要讲按钮验证-退出
# 06 老师查看报告：导航菜单-退出


# 引用库
import os
import time
import unittest

# 导入python版的selenium(webdriver)
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# 引用模块
from Constant.sys_constant import *
from test_case.PubModule import login, paintoper, topmenu_t,logout


class test_work_t(unittest.TestCase):
    def setUp(self):
        # 定义浏览器，打开测试网站
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.wd.get(LOGIN_URL)
        # self.wd.get("http://whdx.bcbook.cn/") ##  这个是测试环境地址
        # self.wd.get("http://preprod-whdx.bcbook.cn/")##  这个是预生产环境地址
        # 脚本运行时，错误的信息将被打印到这个列表中。
        self.verificationErrors = []
        # 是否继续接受下一下警告
        self.accept_next_alert = True
        wd = self.wd
        time.sleep(1)
        # 窗口最大化
        wd.maximize_window()

    def test01_assign(self):
        wd = self.wd
        success = True
        # 作业长流程-布置作业首页
        print("开始测试！作业长流程,检查页面初始化功能")
        # 登录
        # 调用login()函数登录
        #17400000071是正式账号17100000001是测试账号18210000001是预生产账号
        login.login(self, "17400000071", "123456")
        time.sleep(2)
        ##############################导航菜单功能点####################################

        # 导航选择：整个导航条
        Nav = wd.find_element_by_class_name("c_Nav ")
        time.sleep(1)
        # 菜单选择：整个导航下有下拉样式的菜单
        Sels = Nav.find_elements_by_class_name("totalnav")
        time.sleep(1)
        # 移动到第一个有下拉菜单的元素上：作业
        ActionChains(wd).move_to_element(Sels[0]).perform()
        time.sleep(1)
        # 菜单选择：整个作业菜单下所有的菜单
        Fmenus = Sels[0].find_elements_by_class_name("menuId")
        # 点击作业菜单下第一个元素：布置作业
        Fmenus[0].click()
        time.sleep(2)
        #############################章节切换功能点####################################

        # 切换章节到第二单元
        wd.find_element_by_xpath("//dl[1]/dd/ul/li[@title='第二单元']").click()
        time.sleep(2)
        #点击第六课
        wd.find_element_by_xpath("//li[text()='第6课']").click()
        time.sleep(1)
        #############################循环验证以下各个功能点####################################
        types = ['课时练', '分层作业-及格线', '分层作业-考A吧', '分层作业-冲A+', '自主组卷']
        for i in range(len(types)):
            # 作业类型
            Worklay = wd.find_element_by_class_name("lay_types")
            #获取6个类型的作业元素
            Lays = Worklay.find_elements_by_class_name("lay_wtype")
            Lays[i].click()
            time.sleep(1)
            if not ("建议用时" in wd.find_element_by_tag_name("html").text):
                Nodata = wd.find_element_by_xpath("//*[@id='testpaper']/img[@class='nodata']")
                if Nodata.is_displayed():
                    print(types[i]+"页初始化:暂无数据")
                else:
                    success = False
                    print(types[i]+"初始化失败")
            else:
                print(types[i]+"页初始化成功")
            time.sleep(2)
            # 点击面包屑：首页>布置作业>课时练,返回布置作业页
            wd.find_element_by_id("testhref").click()
            time.sleep(0.5)

        #############################自主上传功能点####################################
        # 点击自主上传
        # 作业类型
        Worklay = wd.find_element_by_class_name("lay_types")
        # 获取6个类型的作业元素
        Lays = Worklay.find_elements_by_class_name("lay_wtype")
        Lays[5].click()
        time.sleep(1)
        if not ("自主上传" in wd.find_element_by_tag_name("html").text):
            success = False
            print("自主上传弹窗显示失败")
        else:
            print("自主上传弹窗显示成功")
        # 关闭弹窗
        wd.find_element_by_xpath("//a[@class='file-upload-wrapper-close-btn']").click()
        time.sleep(2)
        self.assertTrue(success)

    def test02_Edit(self):
        wd = self.wd
        success = True
        # 作业长流程-编辑、打印、布置课时练
        print("开始测试！作业长流程-编辑课时练")
        ##############################登录功能点####################################
        # 调用login()函数登录
        # 17400000071是正式账号;17100000001是测试账号;18210000001是预生产账号
        login.login(self, "17400000071", "123456")
        # 进入首页
        if not ("您讲课比赛的坚实后援" in wd.find_element_by_tag_name("html").text):
            success = False
            print("首页初始化失败")
        else:
            print("首页初始化成功")
        time.sleep(1)
        ##############################导航菜单功能点####################################
        # 导航选择：整个导航条
        Nav = wd.find_element_by_class_name("c_Nav ")
        time.sleep(1)
        # 菜单选择：整个导航下有下拉样式的菜单
        Sels = Nav.find_elements_by_class_name("totalnav")
        time.sleep(1)
        # 移动到第一个有下拉菜单的元素上：作业
        ActionChains(wd).move_to_element(Sels[0]).perform()
        time.sleep(1)
        # 菜单选择：整个作业菜单下所有的菜单
        Fmenus = Sels[0].find_elements_by_class_name("menuId")
        # 点击作业菜单下第一个元素：布置作业
        Fmenus[0].click()
        time.sleep(2)

        #############################章节切换功能点####################################
        # 切换章节到第二单元
        wd.find_element_by_xpath("//dl[1]/dd/ul/li[@title='第二单元']").click()
        time.sleep(2)
        #点击第六课,进入课时练初始始化页面
        wd.find_element_by_xpath("//li[text()='第6课']").click()
        time.sleep(1)
        # 作业类型
        Worklay = wd.find_element_by_class_name("lay_types")
        # 获取6个类型的作业元素
        Lays = Worklay.find_elements_by_class_name("lay_wtype")
        # 点击课时练
        Lays[0].click()
        print("切换章节到第二单元第六课！")
        time.sleep(1)
        ############################解析报错功能,并提交报错功能点####################################
        # 定位到题目元素
        article = wd.find_element_by_xpath("//div[@class='lay_paper']/ul[1]/li[1]")
        # 鼠标悬浮在题目位置
        ActionChains(wd).move_to_element(article).perform()
        # 等待1秒
        time.sleep(1)
        # 定位到查看解析
        jxbx = article.find_elements_by_class_name("lay_right")
        # mouse = wd.find_element_by_xpath("//div[@class='lay_paper']/ul[1]/li[1]/div/div[2]/input[2]")
        # 鼠标移动至解析上方悬浮
        ActionChains(wd).move_to_element(jxbx[1]).perform()
        # 查看解析展开/收起
        # wd.find_element_by_xpath("//div[@class='lay_paper']/ul[1]/li[1]/div/div[2]/input[2]").click()
        jxbx[1].click()
        if not ("【答案】" in wd.find_element_by_tag_name("html").text):
            success = False
            print("查看解析失败！")
        else:
            print("查看解析成功！")
        time.sleep(2)
        # 收回解析
        jxbx[1].click()
        if ("【答案】" in wd.find_element_by_tag_name("html").text):
            success = False
            print("收回解析失败！")
        else:
            print("收回解析成功！")
        time.sleep(1)

        # 报错功能点:正常流程
        # 点击报错按钮
        jxbx[0].click()
        #输入报错内容项
        wd.find_element_by_xpath("//textarea[@class='error_text']").send_keys("自动化测试报错")
        #选择报错类型为:其它有误 备选:知识点有误,答案有误,解析有误,题干有误,
        wd.find_element_by_xpath("//li[text()='其他有误']").click()
        #点击报错确定按钮
        wd.find_element_by_xpath("//input[@value='确定']").click()
        if not ("报错成功" in wd.find_element_by_tag_name("html").text):
            success = False
            print("报错失败！")
        else:
            print("报错成功！")
        #########################################课时练编辑功能点###################################
        # 编辑按钮链接验证
        wd.find_element_by_xpath("//div[@class='backff']/input[@value='编辑']").click()
        time.sleep(5)
        # 修改作业名称为原名称追加_测试
        title = wd.find_element_by_xpath("//*[@id='testpaper']/div[1]/p[1]/input")
        titletxt = title.text
        title.send_keys(titletxt+"_测试")
        # 修改建议用时为10
        wd.find_element_by_class_name("testTime").click()
        wd.find_element_by_class_name("testTime").clear()
        wd.find_element_by_class_name("testTime").send_keys("10")

        # 课时练编辑:点击添加题目按钮
        wd.find_element_by_css_selector("i.line_addQuestion").click()
        time.sleep(5)
        if not ("知识点" in wd.find_element_by_tag_name("html").text):
            success = False
            print("添加题目页初始化失败!")
        else:
            print("添加题目页初始化成功!")

        # 课时练编辑添加题目:点击知识点“字音”
        wd.find_element_by_xpath("//dd[@id='ckknowledge']//span[.='字音']").click()
        # 课时练编辑添加题目:选择题型“选择题”
        wd.find_element_by_xpath("//dd[@id='addtype']//span[.='选择题']").click()
        # 课时练编辑添加题目:选择“难度”
        wd.find_element_by_xpath("//dd[@id='diffs']//span[.='基础']").click()

        # 课时练编辑添加题目:定位到题目元素
        article = wd.find_element_by_xpath("//div/div[2]/div[3]/div/div[2]/div[1]/ul/li[1]/div/ul/li[3]/p")
        # 鼠标悬浮在题目位置
        ActionChains(wd).move_to_element(article).perform()
        # 等待1秒
        time.sleep(1)
        # 课时练编辑添加题目:定位到查看解析
        mouse = wd.find_element_by_xpath("//div[@class='addLineQuestion_middle_questions']//span[.='解析']")
        # 鼠标移动至查看解析上方悬浮
        ActionChains(wd).move_to_element(mouse).perform()
        # 课时练编辑添加题目:查看解析展开/收起
        wd.find_element_by_css_selector("span.options_analysis").click()
        if not ("【答案】" in wd.find_element_by_tag_name("html").text):
            success = False
            print("点击解析按钮，验证答案显示失败！")
        else:
            print("点击解析按钮，验证答案显示成功！")
        time.sleep(1)
        wd.find_element_by_css_selector("span.options_analysis").click()
        if ("【答案】" in wd.find_element_by_tag_name("html").text):
            success = False
            print("点击收起按钮，验证答案不显示失败！")
        else:
            print("点击收起按钮，验证答案不显示成功！")
        time.sleep(1)

        # 课时练编辑添加题目:报错
        wd.find_element_by_css_selector("span.options_error").click()
        wd.find_element_by_xpath("//div/div[2]/div[4]/div/ul/li[1]").click()
        wd.find_element_by_xpath("//div/div[2]/div[4]/div/ul/li[2]").click()
        time.sleep(1)
        wd.find_element_by_xpath("//textarea[@class='error_text']").send_keys("自动化测试报错")
        time.sleep(2)
        wd.find_element_by_xpath("//input[@class='state_selected']").click()
        if not ("报错成功" in wd.find_element_by_tag_name("html").text):
            success = False
            print("报错失败！")
        else:
            print("报错成功！")

        # 课时练编辑状态下添加题目,选入题目
        wd.find_element_by_xpath("//span[text()='选入']").click()
        if not ("已选择" in wd.find_element_by_tag_name("html").text):
            success = False
            print("选入题目失败！")
        else:
            print("选入题目成功！")
        time.sleep(0.5)

        # 课时练编辑状态下添加题目:取消选入该题目
        wd.find_element_by_xpath("//span[text()='取消选入']").click()
        if not ("请选择题目" in wd.find_element_by_tag_name("html").text):
            success = False
            print("取消选入题目失败！")
        else:
            print("取消选入题目成功！")
        time.sleep(0.5)

        # 课时练编辑状态下添加题目取消再次选入该题目
        wd.find_element_by_xpath("//span[text()='选入']").click()
        if not ("已选择" in wd.find_element_by_tag_name("html").text):
            success = False
            print("再次选入题目,失败！")
        else:
            print("再次选入题目,成功！")
        time.sleep(0.5)

        # 课时练编辑状态下添加题目:点击完成按钮
        wd.find_element_by_css_selector("input.lay_btn.state_selected").click()
        if not ("建议用时" in wd.find_element_by_tag_name("html").text):
            success = False
            print("添加题目保存失败！")
        else:
            print("添加题目保存成功！")
        time.sleep(0.5)
        # 点击保存按钮，保存试卷
        wd.find_element_by_xpath("//div[@class='backff']/input[@value='完成']").click()
        if not ("保存成功，将在3秒内返回" in wd.find_element_by_tag_name("html").text):
            success = False
            print("修改试卷保存失败！")
        else:
            print("修改试卷保存成功！")
        time.sleep(4)
        '''
        # 作业长流程-打印试卷（课时练）
        print("开始测试！作业长流程-打印课时练")
        # 点击打印按钮
        wd.find_element_by_xpath("//div[@class='backff']/input[1]").click()
        wd.find_element_by_xpath("//div[@class='print_in']//div[.='普通打印']").click()
        print("普通打印成功")
        time.sleep(0.5)
        # 调用autoit程序。
        #os.system("D:\\selenium_upfile\\print_cancel.exe")
        # 带解析打印
        wd.find_element_by_css_selector("div.print_btn.withAnalyze").click()
        time.sleep(1)
        #try:
            # 调用autoit程序。
        #    os.system("D:\\selenium_upfile\\print_cancel.exe")
        #except Exception:
        #    print("FAILED-打印功能出错")
        #else:
        #    print("PASS-打印功能正常")
        wd.find_element_by_xpath("//div[@class='print_in']//div[.='带解析打印']").click()
        print("带解析打印成功")
        # 关闭打印窗口
        wd.find_element_by_xpath("//div[@class='print_in']/i").click()
        '''
        ##############################作业长流程,布置课时练######################
        print("开始测试！作业长流程-布置课时练")
        # 定位到布置按钮
        A = wd.find_elements_by_class_name("lay_btn")[2]
        # 悬浮到布置按钮上
        ActionChains(wd).move_to_element(A).perform()
        # 找到布置按钮下的布置给班级并点击
        B = wd.find_element_by_class_name("publish_label")
        # 点击布置按钮下的布置给班级
        B.find_element_by_tag_name("li").click()
        time.sleep(1)
        if not ("作业名称" in wd.find_element_by_tag_name("html").text):
            print("布置对象界面初始化失败")
        else:
            print("布置对象界面初始化成功")
        # 修改布置作业截止时间:暂未实现
        # wd.find_element_by_xpath("//a[@class='param-for-assignment-inner-lastTime-hour-minus']").click()
        time.sleep(0.5)
        # 选择布置对象（班级内有学生）:八年级1班
        clsssele = wd.find_elements_by_xpath("//ul[@class='param-for-assignment-inner-list-grade']//li")
        for banji in clsssele:
            if not("noStu" in banji.get_attribute("class")):
                banji.click()
                break
        time.sleep(0.5)
        # 点击确定按钮
        wd.find_element_by_xpath("//a[@class='param-for-assignment-inner-submit-btn']").click()
        time.sleep(1)
        # 验证列表中的记录
        now = time.strftime("%Y-%m-%d")
        resourcetext = wd.find_element_by_xpath("//ul[@class='list-ul']/li[1]").text
        if ("_测试" in resourcetext) and (now in resourcetext):
            print("布置课时练成功")
        else:
            success = False
            print("布置课时练失败")
        time.sleep(2)
        self.assertTrue(success)

    def test03_Edit(self):
        wd = self.wd
        success = True
        ##############################作业长流程-分层作业布置弹窗验证#######################
        print("开始测试！作业长流程-分层作业布置弹窗")
        # 登录
        # 调用login()函数登录
        # 17400000071是正式账号17100000001是测试账号18210000001是预生产账号
        login.login(self, "17400000071", "123456")
        # 进入首页
        if not ("您讲课比赛的坚实后援" in wd.find_element_by_tag_name("html").text):
            success = False
            print("首页初始化失败")
        else:
            print("首页初始化成功")
        time.sleep(1)
        ##############################导航菜单功能点####################################
        # 导航选择：整个导航条
        Nav = wd.find_element_by_class_name("c_Nav ")
        time.sleep(1)
        # 菜单选择：整个导航下有下拉样式的菜单
        Sels = Nav.find_elements_by_class_name("totalnav")
        time.sleep(1)
        # 移动到第一个有下拉菜单的元素上：作业
        ActionChains(wd).move_to_element(Sels[0]).perform()
        time.sleep(1)
        # 菜单选择：整个作业菜单下所有的菜单
        Fmenus = Sels[0].find_elements_by_class_name("menuId")
        # 点击作业菜单下第一个元素：布置作业
        Fmenus[0].click()
        time.sleep(2)
        #############################章节切换功能点####################################
        # 切换章节到第二单元
        print("切换章节到第二单元第六课！")
        wd.find_element_by_xpath("//dl[1]/dd/ul/li[@title='第二单元']").click()
        time.sleep(2)
        #点击第六课
        wd.find_element_by_xpath("//li[text()='第6课']").click()
        time.sleep(1)
        # 分层作业-及络线-布置弹窗验证
        # 作业类型
        Worklay = wd.find_element_by_class_name("lay_types")
        # 获取6个类型的作业元素
        Lays = Worklay.find_elements_by_class_name("lay_wtype")
        #############################分层作业-及络线页初始化##############################
        #0是课时练,1是 '分层作业-及格线',2是'分层作业-考A吧',3是 '分层作业-冲A+', 4是'自主组卷', 5是'自主上传'
        Lays[1].click()
        time.sleep(1)
        if not ("建议用时" in wd.find_element_by_tag_name("html").text):
            success = False
            print("分层作业-及格线页初始化失败")
        else:
            print("分层作业-及络线页初始化成功")

        menustxt = ['布置班级作业', '布置分层作业', '布置个人作业']
        for i in range(len(menustxt)):
            # 定位到布置按钮
            bzsel = wd.find_elements_by_class_name("lay_btn")[2]
            # 悬浮到布置按钮上
            ActionChains(wd).move_to_element(bzsel).perform()
            # 获取子菜单框内容
            menus = wd.find_elements_by_xpath("//*[@id='testpaper']/div[4]/div/span/div/ul/li")
            # 点击子菜单里的第X个元素
            menus[i].click()
            time.sleep(1)
            if not (menustxt[i] in wd.find_element_by_tag_name("html").text):
                print("分层作业-及络线:"+menustxt[i] + "弹窗初始化失败")
            else:
                print("分层作业-及络线:"+menustxt[i] + "页初始化成功")
                if("布置班级作业" == menustxt[i]):
                    # 选择布置对象（班级内有学生）:八年级1班
                    clsssele = wd.find_elements_by_xpath("//ul[@class='param-for-assignment-inner-list-grade']//li")
                    for banji in clsssele:
                        if not ("noStu" in banji.get_attribute("class")):
                            banji.click()
                            break
                    # 点击取消按钮
                    wd.find_element_by_xpath("//a[@class='param-for-assignment-inner-cancel-btn']").click()
                    print("分层作业-及络线:" + menustxt[i] + "，弹窗关闭成功")
                if ("布置分层作业" == menustxt[i]):
                    # 选择布置对象（分层内有学生）:优秀层
                    divurl = "//ul[@class='param-for-assignment-inner-list-group']/li[1]/div/span"
                    divele = wd.find_elements_by_xpath(divurl)
                    for div in divele:
                        if not ("group noStu" in div.get_attribute("class")):
                            div.click()
                            break
                    # 点击取消按钮
                    wd.find_element_by_xpath("//a[@class='param-for-assignment-inner-cancel-btn']").click()
                    print("分层作业-及络线:" + menustxt[i] + "，弹窗关闭成功")
                if ("布置个人作业" == menustxt[i]):
                    # 选择布置对象（分层内有学生）
                    studenturl = "//ul[@class='param-for-assignment-inner-list-student']/li[1]/div/span"
                    studentele = wd.find_elements_by_xpath(studenturl)
                    for student in studentele:
                        if not ("group noStu" in student.get_attribute("class")):
                            student.click()
                            break
                    # 点击取消按钮
                    wd.find_element_by_xpath("//a[@class='param-for-assignment-inner-cancel-btn']").click()
                    print("分层作业-及络线:" + menustxt[i] + "，弹窗关闭成功")
                time.sleep(2)
        self.assertTrue(success)

    def test04_writting(self):
        wd = self.wd
        success = True
        # 作业长流程-学生写作业
        print("开始测试！作业长流程-学生写作业")
        # 登录 预生产环境18220000001 生产环境17400007001
        login.login(self, "17400007001", "123456")
        time.sleep(3)
        # 进入首页
        if not ("1500万师生检验的好作业" in wd.find_element_by_tag_name("html").text):
            success = False
            print("首页初始化失败")
        else:
            print("首页初始化成功")

        # 定位首页作业和测试并点击写作业
        A = wd.find_element_by_xpath("//*[@id='Com_NavMain']/li[3]")
        ActionChains(wd).move_to_element(A).perform()
        time.sleep(1)
        wd.find_element_by_xpath(".//*[@id='Com_NavMain']/li[3]/ul/li[1]/a").click()
        # 判断是否进入写作业列表页面
        if not ("写作业" in wd.find_element_by_tag_name("html").text):
            print("进入写作业列表页面失败！")
        else:
            print("进入写作业列表页面成功！")

        print(wd.find_element_by_xpath(".//ul[@class='hwListEver'][1]").text)
        # 写作业
        # 进入写作业列表-点击列表内第一条作业的去完成按钮
        d = wd.find_elements_by_class_name("hwListEverTodo")
        #print(len(d))
        span = d[0]
        c = span.find_element_by_tag_name("span")
        c.click()
        #  d[0].click()
        time.sleep(2)
        # 判断是否进入写作业页面
        if not ("提交" in wd.find_element_by_tag_name("html").text):
            print("进入写作业页面失败！")
        else:
            print("进入写作业页面成功！")

        xz = wd.find_elements_by_class_name("optionchoose")
        for i in range(0, len(xz)):
            xz[i].click()
            time.sleep(0.2)
        time.sleep(2)
        # 点击上传按钮
        wd.find_element_by_xpath("//*/div[@class='task_up']/span[contains(text(),'上传')]").click()
        time.sleep(2)
        # 上传主观题图片（反向验证：未上传答案图片）
        # 点击确定修改按钮
        wd.find_element_by_id("GetImgUrl").click()
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

    def test05_Correcting(self):
        wd = self.wd
        success = True
        # 作业长流程-老师批改
        print("开始测试！作业长流程-老师批改作业")
        # 登录# 17400000071是正式账号17100000001是测试账号18210000001是预生产账号
        login.login(self, "17400000071", "123456")
        # 进入首页
        if not ("您讲课比赛的坚实后援" in wd.find_element_by_tag_name("html").text):
            success = False
            print("首页初始化失败")
        else:
            print("首页初始化成功")
        time.sleep(2)
        # 导航选择作业--批改作业
        topmenu_t.top_menu_pgzy(self)
        time.sleep(2)
        # 判断是否进入批改作业列表页面
        if not ("批改" in wd.find_element_by_tag_name("html").text):
            success = False
            print("点击作业-批改菜单,进入批改作业列表页面失败！")
        else:
            print("点击作业-批改菜单,进入批改作业列表页面成功！")
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
        print("循环批改对错完成")
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
        wd.find_element_by_xpath("//input[@value='查看答案']").click()
        if not ("查看答案" in wd.find_element_by_xpath("//div[@id='answer']/p").text):
            success = False
            print("答案未显示")
        else:
            print("答案显示成功")
            # 关闭答案
            wd.find_element_by_xpath("html/body/div[2]/div[2]/div[2]/i").click()
        time.sleep(2)
        #在图上进行批改
        # 导航选择作业--批改作业
        source = wd.find_element_by_xpath("//div[@id='canvasCon']/canvas")  # 需要滑动的元素
        paintoper.paintoper(self,source)
        # 点击旋转按钮
        wd.find_element_by_xpath("//span[text()='旋转']/parent::node()").click()
        time.sleep(2)
        # 点击结束批改按钮
        wd.find_element_by_xpath("//input[@value='结束批改']").click()
        # 结束批改弹窗--下次再批
        wd.find_element_by_xpath("//input[@value='稍后再批']").click()
        time.sleep(1)
        # 在列表中点击批改按钮
        wd.find_element_by_xpath(".//*[@id='correct']/div[1]/div[2]/div/ul/li[4]/input").click()
        # 点击结束批改按钮
        wd.find_element_by_xpath("//input[@value='结束批改']").click()
        time.sleep(2)
        # 结束批改弹窗--结束批改
        wd.find_element_by_xpath("//input[@value='确定结束']").click()
        time.sleep(2)
        # 退出
        logout.logout(self)
        time.sleep(0.5)
        self.assertTrue(success)

    def test06_xReport(self):
        wd = self.wd
        success = True
        # 作业长流程-学生看报告
        print("开始测试！作业长流程-学生看报告")
        # 登录生产账号17470007001预生产账号18220000001
        login.login(self, "18220000001", "123456")
        # 进入看报告页面
        topmenu_t.top_menu_kbg_s(self)
        time.sleep(0.5)
        if not ("看报告" in wd.find_element_by_xpath("//div[@class='Com_Crumbs_in']//span[.='看报告']").text):
            print("进入看报告列表页面失败！")
        else:
            print("进入看报告列表页面成功！")
        # 点击周报的更多按钮
        more = wd.find_element_by_link_text("更多>")
        if more.is_displayed():
            wd.find_element_by_link_text("更多>").click()
            if not ("全部作业周报" in wd.find_element_by_xpath("//div[@class='Com_Crumbs_in']//span[.='全部作业周报']").text):
                print("进入周报列表页失败！")
            else:
                print("进入周报列表页成功！")
            zb_window = wd.current_window_handle
            # 进入列表第一条的周报详情页
            a = wd.find_element_by_class_name("r_content")
            b = a.find_elements_by_tag_name("ul")
            b[1].click()
            print("全部作业周报页面中，点击第一条作业报告进行查看")
            time.sleep(5)
            # 获得当前所有打开的窗口的句柄
            all_handles = wd.window_handles
            # 进入新窗口
            for handle in all_handles:
                if handle != zb_window:
                    wd.switch_to.window(handle)
                    if not ("一周大数据" in wd.find_element_by_tag_name("html").text):
                        success = False
                        print("/t进入周报详情页失败！")
                    else:
                        print("/t进入周报详情页成功！")
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
            print("点击第一条记录查看，报告详情页初始化失败！")
        else:
            print("点击第一条记录查看，报告详情页初始化成功！")
        # 点击班级目标
        wd.find_element_by_class_name("r_classtarget").click()
        time.sleep(1)
        bjmb = wd.find_element_by_xpath("//dl[2]/dd").get_property("textContent")
        print("获取班级目标成功："+bjmb)
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
        wd.find_element_by_xpath(".//*[@id='Quit']").click()
        time.sleep(1)

        self.assertTrue(success)

    def test07_txReport(self):
        wd = self.wd
        success = True
        # 作业长流程-老师看报告
        print("开始测试！作业长流程-老师看报告")
        # 登录17400000071
        # 登录
        login.login(self, "17400000071", "123456")
        # 进入首页
        if not ("您讲课比赛的坚实后援" in wd.find_element_by_tag_name("html").text):
            success = False
            print("首页初始化失败")
        else:
            print("首页初始化成功")

        print("开始测试！作业长流程-看报告")

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
        if not ("【答案统计】" in wd.find_element_by_class_name("answerStatistics").text):
            success = False
            print("试题切换失败")
        else:
            print("试题切换成功")
        # 报告页--答题情况--讲评参考
        a = wd.find_element_by_id("answerStatus")
        b = a.find_element_by_id("commentConference")
        b.click()
        time.sleep(2)
        if not ("讲评提醒" in wd.find_element_by_class_name("remind").text):
            success = False
            print("讲评参考页初始化失败")
        else:
            print("讲评参考页初始化成功")
        # 报告页--答题情况--讲评参考--讲评提醒
        wd.find_element_by_class_name("remind").click()
        print("点击讲评提醒按钮成功")
        time.sleep(2)
        # 讲评提醒输入内容
        wd.find_element_by_xpath("html/body/article/div/div[3]/div/div[1]/div[2]/div[1]/div/textarea").send_keys(
            "自动化测试讲评提醒")
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
        wd.find_element_by_xpath("html/body/article/div/div[3]/div/div[1]/div[2]/div[1]/div/textarea").send_keys(
            "自动化测试讲评提醒编辑测试")
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
        wd.find_element_by_class_name("analyse").click()
        if not ("【答案】" in wd.find_element_by_tag_name("html").text):
            success = False
            print("查看解析失败！")
        else:
            print("查看解析成功！")
        time.sleep(5)
        # 收回解析
        wd.find_element_by_class_name("analyse").click()
        time.sleep(5)
        # 点击报错--正常流程
        # 报错弹窗显示验证
        wd.find_element_by_class_name("error").click()
        a = wd.find_elements_by_class_name("errTypeBtn")
        # print(len(a))
        b = a[1].click()
        time.sleep(2)
        wd.find_element_by_xpath("html/body/div[2]/div/div/div[2]/textarea").send_keys("自动化测试报错")
        time.sleep(2)
        wd.find_element_by_id("submitError").click()
        if not ("提交成功" in wd.find_element_by_tag_name("html").text):
            success = False
            print("报错失败！")
        else:
            print("报错成功！")
        time.sleep(2)

        # 返回到报告页
        wd.find_element_by_xpath("html/body/article/div/div[2]/div/ul/li[3]/a").click()
        # 切换到知识点统计
        a = wd.find_element_by_id("bcTab")
        b = a.find_elements_by_tag_name("li")
        b[1].click()
        time.sleep(2)
        # 判断是否成功进入知识点统计页面
        if not ("active" in b[1].get_attribute("class")):
            print("进入知识点统计页面失败！")
        else:
            print("进入知识点统计页面成功！")
        time.sleep(2)

        # 切换到学生详情
        a = wd.find_element_by_id("bcTab")
        b = a.find_elements_by_tag_name("li")
        b[2].click()
        time.sleep(2)
        # 判断是否成功进入学生详情页面
        if not ("序号" in wd.find_element_by_xpath(".//*[@id='firstUl']/li[1]").text):
            print("进入学生详情页面失败！")
        else:
            print("进入学生详情页面成功！")
        # 点击查看按钮
        wd.find_element_by_xpath(".//*[@id='studentDetails']/div[1]/ul[2]/li[4]/a").click()
        if not ("学生答案" in wd.find_element_by_tag_name("html").text):
            success = False
            print("查看学生试卷失败")
        else:
            print("查看学生试卷成功")
        time.sleep(0.5)

        self.assertTrue(success)

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()