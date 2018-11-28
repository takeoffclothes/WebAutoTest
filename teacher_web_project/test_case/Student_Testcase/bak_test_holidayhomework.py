# -*- coding: utf-8 -*-
#作者：Olivia.Wang
#时间：2018.1.31
#功能：语数外水平自测、提能训练自动做题功能，水平自测可以随机选项做题，提能训练目前只支持遍历（默认选择D）
#提能训练可以自动做题，批改
# 更新代码时间2018.2.1
# 新加了综合练习、新课预习做题功能
#更新代码时间2018.2.2
#新加了政史地生做题功能，数理化不能做（因为有知识网络，页面调用的插件无法获取）
#需要自己填账号及密码，如果需要激活，也需要自己填激活卡及秘钥
#更新代码时间2018.2.6
#新增查看该科目下的班级排行情况
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest,os
import random
from Constant.sys_constant import *
def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class holidayhomework(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        wd = self.wd
        wd.get(LOGIN_URL)
        wd.find_element_by_id("Phone").click()
        wd.find_element_by_id("Phone").clear()
        phone = int(input("请输入账号：\n->"))
        wd.find_element_by_id("Phone").send_keys(phone)
        wd.find_element_by_id("Pass").click()
        wd.find_element_by_id("Pass").clear()
        password = int(input("请输入密码：\n->"))
        wd.find_element_by_id("Pass").send_keys(password)
        wd.find_element_by_id("LoginBtn").click()
    def test_doholidayhomework(self):
        success = True
        wd = self.wd
        time.sleep(2)
        #鼠标悬停操作
        above = wd.find_element_by_xpath(".//*[@id='Com_NavMain']/li[3]/span")
        ActionChains(wd).move_to_element(above).perform()
        time.sleep(2)
        wd.find_element_by_xpath(".//*[@id='Com_NavMain']/li[3]/ul/li[3]/a").click()
        time.sleep(2)
        if ("block" in wd.find_element_by_class_name("notActive").get_attribute("style")):
            print("未激活")
            wd.find_element_by_tag_name("input").click()
            card = input("请输入卡号：\n->")
            wd.find_element_by_id("cardNum").send_keys(card)
            kami = input("请输入卡密：\n->")
            wd.find_element_by_id("code").send_keys(kami)
            wd.find_element_by_id("acitivate").click()
            time.sleep(1)
            print(wd.find_element_by_id("c_ErrorMsg").text)
            time.sleep(2)
            wd.refresh()

        print("已激活")
        # 支持使用者手动输入想做题的学科

        while True:
            z = input("Are U ready？\ny/n\n->")
            if z=="y":
                sb = wd.find_element_by_id("subjectList")
                sb1 = sb.find_elements_by_tag_name("li")
                i = int(input("请输入你想做的科目：0.语文 1.数学 2.英语 3.生物 4.政治 5.历史 6.地理\n不要选1\n不要选1\n不要选1\n->"))
                sb1[i].click()
                time.sleep(1)

                if (i in range(0, 3)):
                    print("语英数做题适用！")
                    # 获取专题数组
                    zhuanti = wd.find_element_by_id("t_c_list")
                    zhuanti1 = zhuanti.find_elements_by_tag_name("li")
                    # 分别获取专题X（X代表不同的专题）
                    for n in range(0, len(zhuanti1)):
                        zhuanti = wd.find_element_by_id("t_c_list")
                        zhuanti1 = zhuanti.find_elements_by_tag_name("li")
                        zhuanti2 = zhuanti1[n].find_elements_by_tag_name("a")
                        # 获取该专题下的水平自测、提能训练
                        for j in range(0, len(zhuanti2) - 1):
                            zhuanti = wd.find_element_by_id("t_c_list")
                            zhuanti1 = zhuanti.find_elements_by_tag_name("li")
                            zhuanti2 = zhuanti1[n].find_elements_by_tag_name("a")
                            zhuanti2[j].click()
                            time.sleep(2)
                            # 判断是否为水平自测（水平自测和提能训练的代码不同，需要分开执行）
                            if ("水平自测" in wd.find_element_by_class_name("Com_Crumbs_in").text):
                                # 水平自测自动做题
                                print("进入专题%d水平自测成功！"%(n+1))
                                zice = wd.find_elements_by_class_name("group")
                                for l in range(0, len(zice)):
                                    zice1 = zice[l].find_elements_by_class_name("choise-option")
                                    # 引入随机数，水平自测就可以随机做题啦
                                    m = random.randint(0, 3)
                                    zice1[m].click()
                                    time.sleep(1)
                                wd.find_element_by_class_name("self_test_up").click()
                                wd.back()
                                time.sleep(2)
                                # 页面刷新，因为老是找不到元素只能刷新页面啦
                                wd.refresh()
                                time.sleep(2)
                            # 智能填空做题功能实现
                            elif ("选题填空" in wd.find_element_by_class_name("Com_Crumbs_in").text):
                                print("进入专题%d智能填空成功！"%(n+1))
                                fill = wd.find_elements_by_class_name("group")
                                for p in range(0, len(fill)):
                                    # 获取选项及答案框
                                    fill1 = fill[p].find_elements_by_class_name("kkk")
                                    fill2 = fill[p].find_elements_by_class_name("fillin-option")
                                    # 判断是否有多于一个的答案框
                                    if len(fill1) > 1:
                                        for q in range(0, 2):
                                            # 答案框一一匹配
                                            fill1[q].click()
                                            fill2[q].click()
                                    else:
                                        # 一个答案框对应多个选项
                                        fill1 = fill[p].find_elements_by_class_name("kkk")
                                        fill2 = fill[p].find_elements_by_class_name("fillin-option")
                                        # 引入随机数，随机填空
                                        k = random.randint(0, len(fill2) - 1)
                                        fill2[k].click()
                                # 提交智能填空
                                wd.find_element_by_id("submitBtn").click()
                                wd.back()
                                time.sleep(2)
                                wd.refresh()
                                time.sleep(2)
                            # 核心速记直接返回
                            elif ("核心速记" in wd.find_element_by_class_name("Com_Crumbs_in").text):
                                print("进入专题%d核心速记成功！" % (n+1))
                                wd.back()
                                time.sleep(2)
                                wd.refresh()
                                time.sleep(2)
                            elif ("学科素养" in wd.find_element_by_class_name("Com_Crumbs_in").text):
                                print("进入专题%d学科素养成功！" % (n+1))
                                wd.back()
                                time.sleep(2)
                                wd.refresh()
                                time.sleep(2)
                            # 提能训练做题
                            else:
                                print("进入专题%d提能训练成功！" % (n+1))
                                zuoti = wd.find_element_by_class_name("question-wrapper")
                                xuanxiang = zuoti.find_elements_by_class_name("choise-option")
                                # 提能训练遍历答题，都选D（不是大鹏唱的都选C哈哈哈）
                                for i in range(0, len(xuanxiang)):
                                    xuanxiang[i].click()
                                    # time.sleep(2)
                                # 遍历完之后提交
                                wd.find_element_by_id("uploadImgBtn").click()
                                wd.find_element_by_class_name("upimg-btn").click()
                                time.sleep(2)
                                # 调用autoIT的程序，上传图片
                                os.system(autoitfile_path+"uploadpicture.exe")
                                wd.find_element_by_id("GetImgUrl").click()
                                time.sleep(1)
                                # 判断图片是否上传成功
                                if not ("上传成功" in wd.find_element_by_class_name("normal-msg").text):
                                    print("图片上传失败！")
                                else:
                                    print("图片上传成功！")
                                    wd.find_element_by_id("submitBtn").click()
                                    time.sleep(2)
                                # 获取批完了按钮位置
                                target = wd.find_element_by_id("submitSelfCorrentBtn")
                                wd.execute_script("arguments[0].scrollIntoView();", target)
                                time.sleep(2)
                                # 判断试题是否提交成功
                                if not ("批完了" in wd.find_element_by_id("submitSelfCorrentBtn").text):
                                    print("试题提交失败！")
                                else:
                                    print("试题提交成功！")
                                    # 获取批改按钮位置
                                    target = wd.find_element_by_class_name("question-selfcorrent")
                                    wd.execute_script("arguments[0].scrollIntoView();", target)
                                    time.sleep(2)
                                    # 自动批改功能实现
                                    a = wd.find_elements_by_class_name("question-selfcorrent")
                                    # 寻找第i个批改框
                                    for i in range(0, len(a)):
                                        b = a[i]
                                        c = b.find_elements_by_tag_name("a")
                                        # 批改框随机选择
                                        x = random.randint(0, len(c) - 5)
                                        c[x].click()
                                        # c[j].click()
                                    wd.find_element_by_id("submitSelfCorrentBtn").click()
                                # 返回上一页
                                wd.back()
                                wd.refresh()
                                time.sleep(2)
                    # 综合练习做题
                    zonghe = wd.find_element_by_class_name("comprehensive-exercises")
                    zonghe1 = zonghe.find_elements_by_tag_name("span")

                    # 综合练习列表遍历
                    for r in range(0, len(zonghe1)):
                        zonghe = wd.find_element_by_class_name("comprehensive-exercises")
                        zonghe1 = zonghe.find_elements_by_tag_name("span")
                        zonghe1[r].click()
                        time.sleep(2)
                        print("进入综合练习%d成功！" % (r+1))
                        try:
                            wd.find_element_by_class_name("choise-option")
                            a = True
                        except:
                            a = False
                        if a == True:
                            print("该页面有主观题，非主观题")
                            zhzuoti = wd.find_element_by_class_name("question-wrapper")
                            zhxuanxiang = zhzuoti.find_elements_by_class_name("choise-option")
                            # 综合练习遍历答题，都选D（不是大鹏唱的都选C哈哈哈）
                            for d in range(0, len(zhxuanxiang)):
                                zhxuanxiang[d].click()
                                # time.sleep(2)
                            # 遍历完之后提交
                            wd.find_element_by_id("uploadImgBtn").click()
                            wd.find_element_by_class_name("upimg-btn").click()
                            time.sleep(2)
                            # 调用autoIT的程序，上传图片
                            os.system(autoitfile_path+"uploadpicture.exe")
                            wd.find_element_by_id("GetImgUrl").click()
                            time.sleep(1)

                            wd.find_element_by_id("submitBtn").click()
                            time.sleep(2)
                            # 获取批完了按钮位置
                            target = wd.find_element_by_id("submitSelfCorrentBtn")
                            wd.execute_script("arguments[0].scrollIntoView();", target)
                            time.sleep(2)
                            # 判断试题是否提交成功
                            if not ("批完了" in wd.find_element_by_id("submitSelfCorrentBtn").text):
                                print("试题提交失败！")
                            else:
                                print("试题提交成功！")
                                # 获取批改按钮位置
                                target = wd.find_element_by_class_name("question-selfcorrent")
                                wd.execute_script("arguments[0].scrollIntoView();", target)
                                time.sleep(2)
                                # 自动批改，都选半对半错，只能遍历目前
                                a = wd.find_elements_by_class_name("question-selfcorrent")
                                for e in range(0, len(a)):
                                    b = a[e]
                                    c = b.find_elements_by_tag_name("a")
                                    x = random.randint(0, len(c) - 5)
                                    c[x].click()
                                    # c[j].click()
                                wd.find_element_by_id("submitSelfCorrentBtn").click()
                            # wd.find_element_by_class_name("scroll-top-btn").click()
                            # 返回上一页
                            wd.back()
                            time.sleep(1)
                            wd.refresh()
                            time.sleep(2)
                        else:
                            print("该页面只有主观题")
                            wd.find_element_by_id("uploadImgBtn").click()
                            wd.find_element_by_class_name("upimg-btn").click()
                            time.sleep(2)
                            # 调用autoIT的程序，上传图片
                            os.system(autoitfile_path+"uploadpicture.exe")
                            wd.find_element_by_id("GetImgUrl").click()
                            time.sleep(1)

                            wd.find_element_by_id("submitBtn").click()
                            time.sleep(2)
                            # 获取批完了按钮位置
                            target = wd.find_element_by_id("submitSelfCorrentBtn")
                            wd.execute_script("arguments[0].scrollIntoView();", target)
                            time.sleep(2)
                            # 判断试题是否提交成功
                            if not ("批完了" in wd.find_element_by_id("submitSelfCorrentBtn").text):
                                print("试题提交失败！")
                            else:
                                print("试题提交成功！")
                                # 获取批改按钮位置
                                target = wd.find_element_by_class_name("question-selfcorrent")
                                wd.execute_script("arguments[0].scrollIntoView();", target)
                                time.sleep(2)
                                # 自动批改，都选半对半错，只能遍历目前
                                a = wd.find_elements_by_class_name("question-selfcorrent")
                                for e in range(0, len(a)):
                                    b = a[e]
                                    c = b.find_elements_by_tag_name("a")
                                    x = random.randint(0, len(c) - 5)
                                    c[x].click()
                                    # c[j].click()
                                wd.find_element_by_id("submitSelfCorrentBtn").click()
                            # wd.find_element_by_class_name("scroll-top-btn").click()
                            # 返回上一页
                            wd.back()
                            time.sleep(1)
                            wd.refresh()
                            time.sleep(2)

                    # 新课预习做题
                    xinke = wd.find_element_by_class_name("newlesson-preparation")
                    xinke1 = xinke.find_elements_by_tag_name("span")
                    # 新课预习列表遍历
                    for g in range(0, len(xinke1)):
                        xinke = wd.find_element_by_class_name("newlesson-preparation")
                        xinke1 = xinke.find_elements_by_tag_name("span")
                        # 新课预习列表点击
                        xinke1[g].click()
                        time.sleep(1)
                        print("进入新课预习%d成功！" % (g+1))
                        wd.find_element_by_id("preparetest").click()
                        # 获取当前打开的所有窗口句柄
                        # window_1 = wd.current_window_handle
                        windows = wd.window_handles


                        # 打开第二个窗口
                        wd.switch_to.window(windows[1])
                        xkzuoti = wd.find_elements_by_class_name("question")
                        # 预习测试随机做题
                        for h in range(0, len(xkzuoti)):
                            xkzuoti1 = xkzuoti[h].find_elements_by_class_name("choise-option")
                            s = random.randint(0, len(xkzuoti1) - 1)
                            xkzuoti1[s].click()
                        wd.find_element_by_class_name("testbtn").click()
                        wd.switch_to.window(windows[0])
                        time.sleep(2)
                        wd.back()
                        time.sleep(2)

                else:
                    print("政史地生做题适用！")
                    # 获取专题数组
                    zhuanti = wd.find_element_by_id("t_c_list")
                    zhuanti1 = zhuanti.find_elements_by_tag_name("li")
                    # 分别获取专题X（X代表不同的专题）
                    for n in range(0, len(zhuanti1)):
                        zhuanti = wd.find_element_by_id("t_c_list")
                        zhuanti1 = zhuanti.find_elements_by_tag_name("li")
                        zhuanti2 = zhuanti1[n].find_elements_by_tag_name("a")
                        # 获取该专题下的提能训练、学科素养
                        for j in range(0, len(zhuanti2)):
                            zhuanti = wd.find_element_by_id("t_c_list")
                            zhuanti1 = zhuanti.find_elements_by_tag_name("li")
                            zhuanti2 = zhuanti1[n].find_elements_by_tag_name("a")
                            zhuanti2[j].click()
                            time.sleep(2)
                            # 判断是否为水平自测（水平自测和提能训练的代码不同，需要分开执行）
                            if ("提能训练" in wd.find_element_by_class_name("Com_Crumbs_in").text):
                                print("进入专题%d提能训练成功！" % (n+1))
                                zuoti = wd.find_element_by_class_name("question-wrapper")
                                xuanxiang = zuoti.find_elements_by_class_name("choise-option")
                                # 提能训练遍历答题，都选D（不是大鹏唱的都选C哈哈哈）
                                for i in range(0, len(xuanxiang)):
                                    xuanxiang[i].click()
                                    # time.sleep(2)
                                # 遍历完之后提交
                                wd.find_element_by_id("uploadImgBtn").click()
                                wd.find_element_by_class_name("upimg-btn").click()
                                time.sleep(2)
                                # 调用autoIT的程序，上传图片
                                os.system(autoitfile_path+"uploadpicture.exe")
                                wd.find_element_by_id("GetImgUrl").click()
                                time.sleep(1)
                                # 判断图片是否上传成功
                                if not ("上传成功" in wd.find_element_by_class_name("normal-msg").text):
                                    print("图片上传失败！")
                                else:
                                    print("图片上传成功！")
                                    wd.find_element_by_id("submitBtn").click()
                                    time.sleep(2)
                                # 获取批完了按钮位置
                                target = wd.find_element_by_id("submitSelfCorrentBtn")
                                wd.execute_script("arguments[0].scrollIntoView();", target)
                                time.sleep(2)
                                # 判断试题是否提交成功
                                if not ("批完了" in wd.find_element_by_id("submitSelfCorrentBtn").text):
                                    print("试题提交失败！")
                                else:
                                    print("试题提交成功！")
                                    # 获取批改按钮位置
                                    target = wd.find_element_by_class_name("question-selfcorrent")
                                    wd.execute_script("arguments[0].scrollIntoView();", target)
                                    time.sleep(2)
                                    # 自动批改功能实现
                                    a = wd.find_elements_by_class_name("question-selfcorrent")
                                    # 寻找第i个批改框
                                    for i in range(0, len(a)):
                                        b = a[i]
                                        c = b.find_elements_by_tag_name("a")
                                        # 批改框随机选择
                                        x = random.randint(0, len(c) - 5)
                                        c[x].click()
                                        # c[j].click()
                                    wd.find_element_by_id("submitSelfCorrentBtn").click()
                                # 返回上一页
                                wd.back()
                                wd.refresh()
                                time.sleep(2)

                            # 提能训练做题
                            else:
                                print("进入专题%d学科素养成功！" % (n+1))
                                zz = input("请输入我的答案：\n->")
                                wd.find_element_by_class_name("politics_core_intype_word").send_keys(zz)
                                wd.find_element_by_class_name("politics_core_botton").click()
                                wd.back()
                                wd.refresh()
                                time.sleep(2)

                    # 综合练习做题
                    zonghe = wd.find_element_by_class_name("comprehensive-exercises")
                    zonghe1 = zonghe.find_elements_by_tag_name("span")

                    # 综合练习列表遍历
                    for r in range(0, len(zonghe1)):
                        zonghe = wd.find_element_by_class_name("comprehensive-exercises")
                        zonghe1 = zonghe.find_elements_by_tag_name("span")
                        zonghe1[r].click()
                        time.sleep(2)
                        print("进入综合练习%d成功！" % (r+1))
                        try:
                            wd.find_element_by_class_name("choise-option")
                            a = True
                        except:
                            a = False
                        if a == True:
                            print("该页面有主观题，非主观题")
                            zhzuoti = wd.find_element_by_class_name("question-wrapper")
                            zhxuanxiang = zhzuoti.find_elements_by_class_name("choise-option")
                            # 提能训练遍历答题，都选D（不是大鹏唱的都选C哈哈哈）
                            for d in range(0, len(zhxuanxiang)):
                                zhxuanxiang[d].click()
                                # time.sleep(2)
                            # 遍历完之后提交
                            wd.find_element_by_id("uploadImgBtn").click()
                            wd.find_element_by_class_name("upimg-btn").click()
                            time.sleep(2)
                            # 调用autoIT的程序，上传图片
                            os.system(autoitfile_path+"uploadpicture.exe")
                            wd.find_element_by_id("GetImgUrl").click()
                            time.sleep(1)

                            wd.find_element_by_id("submitBtn").click()
                            time.sleep(2)
                            # 获取批完了按钮位置
                            target = wd.find_element_by_id("submitSelfCorrentBtn")
                            wd.execute_script("arguments[0].scrollIntoView();", target)
                            time.sleep(2)
                            # 判断试题是否提交成功
                            if not ("批完了" in wd.find_element_by_id("submitSelfCorrentBtn").text):
                                print("试题提交失败！")
                            else:
                                print("试题提交成功！")
                                # 获取批改按钮位置
                                target = wd.find_element_by_class_name("question-selfcorrent")
                                wd.execute_script("arguments[0].scrollIntoView();", target)
                                time.sleep(2)
                                # 自动批改，都选半对半错，只能遍历目前
                                a = wd.find_elements_by_class_name("question-selfcorrent")
                                for e in range(0, len(a)):
                                    b = a[e]
                                    c = b.find_elements_by_tag_name("a")
                                    x = random.randint(0, len(c) - 5)
                                    c[x].click()
                                    # c[j].click()
                                wd.find_element_by_id("submitSelfCorrentBtn").click()
                            # wd.find_element_by_class_name("scroll-top-btn").click()
                            # 返回上一页
                            wd.back()
                            time.sleep(1)
                            wd.refresh()
                            time.sleep(2)
                        else:
                            print("该页面只有主观题")
                            wd.find_element_by_id("uploadImgBtn").click()
                            wd.find_element_by_class_name("upimg-btn").click()
                            time.sleep(2)
                            # 调用autoIT的程序，上传图片
                            os.system(autoitfile_path+"uploadpicture.exe")
                            wd.find_element_by_id("GetImgUrl").click()
                            time.sleep(1)

                            wd.find_element_by_id("submitBtn").click()
                            time.sleep(2)
                            # 获取批完了按钮位置
                            target = wd.find_element_by_id("submitSelfCorrentBtn")
                            wd.execute_script("arguments[0].scrollIntoView();", target)
                            time.sleep(2)
                            # 判断试题是否提交成功
                            if not ("批完了" in wd.find_element_by_id("submitSelfCorrentBtn").text):
                                print("试题提交失败！")
                            else:
                                print("试题提交成功！")
                                # 获取批改按钮位置
                                target = wd.find_element_by_class_name("question-selfcorrent")
                                wd.execute_script("arguments[0].scrollIntoView();", target)
                                time.sleep(2)
                                # 自动批改，都选半对半错，只能遍历目前
                                a = wd.find_elements_by_class_name("question-selfcorrent")
                                for e in range(0, len(a)):
                                    b = a[e]
                                    c = b.find_elements_by_tag_name("a")
                                    x = random.randint(0, len(c) - 5)
                                    c[x].click()
                                    # c[j].click()
                                wd.find_element_by_id("submitSelfCorrentBtn").click()
                            # wd.find_element_by_class_name("scroll-top-btn").click()
                            # 返回上一页
                            wd.back()
                            time.sleep(1)
                            wd.refresh()
                            time.sleep(2)

                wd.find_element_by_class_name("rightrank").click()
                if ("班级排行榜" in wd.find_element_by_class_name("Com_Crumbs_in").text):
                    print("进入班级排行榜成功！")
                    gerenxinxi = wd.find_element_by_class_name("tempstu")
                    gg = gerenxinxi.find_elements_by_tag_name("li")
                    print("排名：", int(gg[0].find_element_by_tag_name("span").get_attribute("data-num"))+1)
                    print("姓名：", gg[1].text)
                    print("完成专题数：", gg[2].text)
                    print("正确率：", gg[3].text)

                else:
                    print("进入班级排行榜失败！")
                wd.back()
                wd.refresh()
                time.sleep(2)
                wd.back()
                wd.refresh()
                time.sleep(2)

            elif z=="n":
                return False

        self.assertTrue(success)

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()