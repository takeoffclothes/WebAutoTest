#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' morenwei zhushi '
# 王帅 时间：2018-06-19
# 学生写暑假作业模块功能：1.可以打开智能培优，首先判断该学科是否全部做完，如果全部做完可自动切换至未做完的学科，继续做题
# 2.可以打开新课预习，打开电子教材、预习视频、预习测试并做题
# 3.可以打开天天阅读，遍历专题一的所有文章，遍历完并切换至英语学科，进行遍历
__author__ = 'Oliva.Wang'

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
        self.wd.implicitly_wait(5)
        wd = self.wd
        wd.get(LOGIN_URL)
        wd.find_element_by_id("Phone").click()
        wd.find_element_by_id("Phone").clear()
        #phone = int(input("请输入账号：\n->"))
        wd.find_element_by_id("Phone").send_keys('14600000701')
        wd.find_element_by_id("Pass").click()
        wd.find_element_by_id("Pass").clear()
        #password = int(input("请输入密码：\n->"))
        wd.find_element_by_id("Pass").send_keys('123456')
        wd.find_element_by_id("LoginBtn").click()
    def test_01_sumHomework_activation_or_not(self):
        success = True
        wd = self.wd
        print('开始测试学生写假期作业页面：')
        Menu_HDayHomework = wd.find_elements_by_class_name("Com_Li")[2]
        ActionChains(wd).move_to_element(Menu_HDayHomework).perform()
        time.sleep(2)#鼠标悬浮点击假期作业
        Menu_HDayHomework.find_elements_by_tag_name("li")[2].click()
        time.sleep(2)
        if ('假期作业' not in wd.find_element_by_class_name('Com_Crumbs').text):
            success = False
            print('进入假期作业页面失败！')
        else:
            print('进入假期作业页面成功！')
        pass
        '''
            if (len(wd.find_elements_by_class_name('noData'))>0):
                print(wd.find_element_by_class_name('Com_Main').text)
            else:
                if ('等待班主任开启假期作业' in wd.find_element_by_class_name('btndiv').text):
                    print('请联系班主任开启假期作业！')
                else:
                    if ('激活作业' in wd.find_element_by_class_name('btndiv').text):#不激活作业，存在风险
                        print('请激活假期作业！')
                        wd.find_element_by_class_name('btndiv').click()
                        card_number = wd.find_elements_by_tag_name('input')[0]
                        pass_word = wd.find_elements_by_tag_name('input')[1]
                        active = wd.find_elements_by_tag_name('input')[2]
                        card_number.send_keys('xxxxxxx')
                        pass_word.send_keys('xxxxxx')
                        active.click()
                    else:
                        print('请开始写作业吧！')
        '''
    def test_02_write_sumHomework_znpy(self):#智能培优
        success = True
        wd = self.wd
        print('开始测试学生写假期作业页面：')
        Menu_HDayHomework = wd.find_elements_by_class_name("Com_Li")[2]
        ActionChains(wd).move_to_element(Menu_HDayHomework).perform()
        time.sleep(2)
        Menu_HDayHomework.find_elements_by_tag_name("li")[2].click()
        time.sleep(2)#鼠标悬浮点击假期作业

        # subject_dict = {'语文':'0','数学':'1','英语':'2','政治':'3','历史':'4','地理':'5','生物':'6'}
        # subject_array = ['语文','数学','英语','政治','历史','地理','生物']
        # num_subject_array = len(subject_array)
        # empty_subject_array = []
        # print('开始测试学生写智能培优的作业：')
        # son_menu = wd.find_element_by_class_name('category')
        # znpy = son_menu.find_elements_by_tag_name('li')[0]
        # znpy.click()#点击智能培优菜单
        # if ('智能培优' not in wd.find_element_by_class_name('Com_Crumbs').text):
        #     print('进入智能培优页面失败！')
        #     success = False
        # else:
        #     print('进入智能培优页面成功！')
        # #切换学科，该账号政治学科全做完了
        #
        # wd.find_element_by_class_name('down').click()
        # change_subject = wd.find_element_by_class_name('title')
        # tag_change_subject = change_subject.find_elements_by_tag_name('li')
        # tag_change_subject[1].click()
        # time.sleep(2)
        #
        # certain = True
        # while certain:#判断该学科所有单元是否都有已完成标签，切换到未全部完成的学科
        #     finish_unit = []
        #     num_finish_unit = len(finish_unit)
        #     if num_finish_unit == num_subject_array:#如果所有的学科都已经全部完成，则跳出循环
        #         certain = False
        #     for i in range(0, 2):
        #         unit = wd.find_elements_by_class_name('all')[i]#定义所有学科
        #         tag_unit = unit.find_elements_by_tag_name('div')
        #         num_unit = len(tag_unit)
        #         finish_unit = []
        #         for j in range(0, num_unit):#挨个寻找有已完成标志的单元，如果该单元没有，则退出循环
        #             if len(tag_unit[j].find_elements_by_tag_name('i')) == 0:
        #                 finish_unit.append(j)
        #                 break
        #     if len(finish_unit) == 0:
        #         print('该学科全做完了，请切换学科！')
        #         title_subject = wd.find_element_by_class_name('title')
        #         choise_subject = title_subject.find_element_by_tag_name('span').text  # 智能培优所选择的学科
        #         print(choise_subject)
        #         empty_subject_array.append(choise_subject)  # 把该学科加入到新数组
        #         print(empty_subject_array)
        #         no_done_subject = list(set(subject_array).difference(set(empty_subject_array)))  # 获得该数组与所有学科数组的差集
        #         '''
        #         #自己方法实现
        #         suiji = random.sample(no_done_subject,1)#随机该数组
        #         print(suiji)
        #         str_empty = ''
        #         suiji_subject = int(subject_dict[str_empty.join(suiji)])#随机该数组元素转换int
        #         print(suiji_subject)
        #         wd.find_element_by_class_name('down').click()
        #         change_subject = wd.find_element_by_class_name('title')
        #         tag_change_subject = change_subject.find_elements_by_tag_name('li')
        #         tag_change_subject[suiji_subject].click()
        #         '''
        #         # 啊楼方法实现
        #         choise_subject_now = no_done_subject[random.randint(0, (len(no_done_subject) - 1))]#获得除该科目外的随机学科
        #         wd.find_element_by_class_name('down').click()
        #         change_subject = wd.find_element_by_class_name('title')
        #         tag_change_subject = change_subject.find_elements_by_tag_name('li')
        #         for l in range(0, len(tag_change_subject)):
        #             if (choise_subject_now == tag_change_subject[l].text):#判断该学科与网页中的是否相等，相等则点击
        #                 tag_change_subject[l].click()
        #                 time.sleep(2)
        #     else:
        #         certain = False
        # ztgg = wd.find_elements_by_class_name('all')[0]#专题巩固定位
        # tag_ztgg = ztgg.find_elements_by_tag_name('div')#专题巩固下的单元标签
        # num_ztgg = len(tag_ztgg)#专题巩固下的单元个数
        # zhlx = wd.find_elements_by_class_name('all')[1]#综合练习下的单元标签
        # tag_zhlx = zhlx.find_elements_by_tag_name('div')
        # num_zhlx = len(tag_zhlx)#综合练习下的单元个数
        # #print(len(ztgg.find_elements_by_tag_name('div')))
        # finish_ztgg = []
        # for i in range(0,num_ztgg):#查找第一个未完成单元的标签数
        #     if len(tag_ztgg[i].find_elements_by_tag_name('i'))==0:
        #         finish_ztgg.append(i)
        #         break
        # if len(finish_ztgg)==0:#判断专题巩固所有单元是否都有已完成标签
        #     print('专题巩固全做完了，开始做综合练习吧！')
        #     finish_zhlx = []
        #     for i in range(0,num_zhlx):
        #         if len(tag_zhlx[i].find_elements_by_tag_name('i'))==0:
        #             finish_zhlx.append(i)
        #             break
        #         if len(finish_zhlx)==0:
        #             print("该学科下的作业都做完了，切换学科，做下一科作业吧！")
        #
        # else:
        #     tag_ztgg_unit = tag_ztgg[i].find_elements_by_tag_name('li')
        #     num_ztgg_unit = len(tag_ztgg_unit)#定义专题巩固单元
        #     if num_ztgg_unit > 1 and tag_ztgg_unit[0].text == '水平自测':
        #         tag_ztgg_unit[1].click()
        #         # 验证提能训练解锁
        #         if (len(wd.find_elements_by_class_name('dialog-toast')) > 0):
        #             print('提能训练验证是否解锁成功！')
        #         else:
        #             wd.back()
        #             wd.refresh()
        #
        #     for j in range(0, num_ztgg_unit):
        #         ztgg = wd.find_elements_by_class_name('all')[0]
        #         tag_ztgg = ztgg.find_elements_by_tag_name('div')#定义专题巩固标签
        #         tag_ztgg_unit = tag_ztgg[i].find_elements_by_tag_name('li')
        #         tag_ztgg_unit[j].click()
        #         time.sleep(2)
        #         if ('水平自测' in wd.find_element_by_class_name('Com_Crumbs_in').text):
        #             print('进入水平自测页面成功！')
        #             if ('none' not in wd.find_element_by_class_name('self_test_submit').get_attribute('style')):
        #                 print('开始做水平自测吧')
        #                 all_questions = wd.find_elements_by_class_name('group')#定义所有题
        #                 num_questions = len(all_questions)
        #                 # print(num_questions)
        #                 for k in range(0, num_questions):#随机选择答案做水平自测
        #                     choise = all_questions[k].find_elements_by_class_name('choise-option')
        #                     num_choise = len(choise) - 1
        #                     # print(num_choise)
        #                     random_choise = random.randint(0, num_choise)#随机选项
        #                     choise[random_choise].click()
        #                     time.sleep(0.5)
        #                 wd.find_element_by_class_name('self_test_submit').click()#提交按钮
        #                 if ('提交成功' in wd.find_element_by_class_name('dialog-toast').text):
        #                     print('水平自测提交成功！')
        #                 else:
        #                     success = False
        #                     print('水平自测提交失败！')
        #             else:
        #                 print('水平自测做完了，去做提能训练吧！')
        #             wd.back()
        #             wd.refresh()
        #             time.sleep(2)
        #         elif ('提能训练' in wd.find_element_by_class_name('Com_Crumbs_in').text):
        #             print('进入提能训练页面成功，开始做提能训练吧！')
        #             all_questions = wd.find_elements_by_class_name('group')
        #             num_questions = len(all_questions)
        #             # print(num_questions)
        #             for k in range(0, num_questions):
        #                 choise = all_questions[k].find_elements_by_class_name('choise-option')
        #                 num_choise = len(choise)
        #                 if (num_choise>0):#判断是否有主观题，客观题随机做题
        #                 # print(num_choise)
        #                     random_choise = random.randint(0, (num_choise-1))
        #                     choise[random_choise].click()
        #             wd.find_element_by_id("uploadImgBtn").click()
        #             time.sleep(2)
        #             wd.find_element_by_class_name("upimg-btn").click()
        #             time.sleep(2)
        #             # 调用autoIT的程序，上传图片
        #             os.system(autoitfile_path + "uploadpicture.exe")
        #             time.sleep(2)
        #             wd.find_element_by_id("GetImgUrl").click()
        #             time.sleep(1)
        #             # 判断图片是否上传成功
        #             if not ("上传成功" in wd.find_element_by_id("dialogToast").text):
        #                 print("图片上传失败！")
        #             else:
        #                 print("图片上传成功！")
        #                 wd.find_element_by_id("submitBtn").click()
        #                 time.sleep(2)
        #             target = wd.find_element_by_id("submitSelfCorrentBtn")
        #             wd.execute_script("arguments[0].scrollIntoView();", target)
        #             time.sleep(2)
        #             # 判断试题是否提交成功
        #             if ("none" in wd.find_element_by_id("submitSelfCorrentBtn").get_attribute('style')):
        #                 print("试题提交失败！")
        #             else:
        #                 print("试题提交成功！")
        #                 # 获取批改按钮位置
        #                 tag_mark = wd.find_element_by_class_name("question-selfcorrent")
        #                 wd.execute_script("arguments[0].scrollIntoView();", target)
        #                 time.sleep(2)
        #                 # 自动批改功能实现
        #                 tag_marks = wd.find_elements_by_class_name("question-selfcorrent")
        #                 num_tag_marks = len(tag_marks)
        #                 if num_tag_marks>0:
        #                     # 寻找第i个批改框
        #                     for i in range(0, len(tag_marks)):
        #                         b = tag_marks[i].find_elements_by_tag_name("a")
        #                         # 批改框随机选择
        #                         x = random.randint(0, len(b) - 5)
        #                         b[x].click()
        #                         # c[j].click()
        #                     wd.find_element_by_id("submitSelfCorrentBtn").click()
        #             wd.back()
        #             wd.refresh()
        #             time.sleep(2)
        #         elif ('学科素养' in wd.find_element_by_class_name('Com_Crumbs_in').text):
        #             print('进入学科素养页面成功，开始做学科素养吧！')
        #             if ('block' in wd.find_element_by_id('myAnswerWrapper').get_attribute('style')):
        #                 print('该学科素养已做完！')
        #             else:
        #                 wd.find_element_by_id("uploadImgBtn").click()
        #                 wd.find_element_by_class_name("upimg-btn").click()
        #                 time.sleep(2)
        #                 # 调用autoIT的程序，上传图片
        #                 os.system(autoitfile_path + "uploadpicture.exe")
        #                 wd.find_element_by_id("GetImgUrl").click()
        #                 time.sleep(1)
        #                 # 判断图片是否上传成功
        #                 if not ("上传成功" in wd.find_element_by_id("dialogToast").text):
        #                     print("图片上传失败！")
        #                 else:
        #                     print("图片上传成功！")
        #                     wd.find_element_by_id("submitBtn").click()
        #                     time.sleep(2)
        #                 wd.find_element_by_id('submitBtn').click()
        #
        #             wd.back()
        #             wd.refresh()
        #             time.sleep(2)

        self.assertTrue(success)
    def test_03_write_sumHomework_xkyx(self):
        success = True
        wd = self.wd
        print('开始测试学生写假期作业页面：')
        Menu_HDayHomework = wd.find_elements_by_class_name("Com_Li")[2]
        ActionChains(wd).move_to_element(Menu_HDayHomework).perform()
        time.sleep(2)
        Menu_HDayHomework.find_elements_by_tag_name("li")[2].click()
        time.sleep(2)
        # subject_dict = {'语文': '0', '数学': '1', '英语': '2','物理':'3', '政治': '4', '历史': '5', '地理': '6', '生物': '7'}
        # subject_array = ['语文', '数学', '英语','物理', '政治', '历史', '地理', '生物']
        # num_subject_array = len(subject_array)
        # empty_subject_array = []
        # print('开始测试学生写新课预习的作业：')
        # son_menu = wd.find_element_by_class_name('category')
        # xkyx = son_menu.find_elements_by_tag_name('li')[1]
        # xkyx.click()
        # if ('新课预习' not in wd.find_element_by_class_name('Com_Crumbs').text):
        #     print('进入新课预习页面失败！')
        #     success = False
        # else:
        #     print('进入新课预习页面成功！')
        # # 切换学科，政治全做完，做测试对比
        #
        # wd.find_element_by_class_name('down').click()
        # change_subject = wd.find_element_by_class_name('title')
        # tag_change_subject = change_subject.find_elements_by_tag_name('li')
        # tag_change_subject[4].click()
        # time.sleep(2)
        # certain = True
        # while certain:#循环查找有未全部完成的学科，切换过去
        #     unit = wd.find_element_by_class_name('all')
        #     tag_unit = unit.find_elements_by_tag_name('div')
        #     num_unit = len(tag_unit)
        #     finish_unit = []
        #     num_finish_unit = len(finish_unit)
        #     if num_finish_unit == num_subject_array:#数组里的学科总数与页面内的学科总数一致，则跳出循环
        #         certain = False
        #     for j in range(0, num_unit):
        #         if len(tag_unit[j].find_elements_by_tag_name('i')) == 0:
        #             finish_unit.append(j)
        #             break
        #     if len(finish_unit) == 0:
        #         print('该学科全做完了，请切换学科！')
        #         title_subject = wd.find_element_by_class_name('title')
        #         choise_subject = title_subject.find_element_by_tag_name('span').text  # 新课预习所选择的学科
        #         print(choise_subject)
        #         empty_subject_array.append(choise_subject)  # 把该学科加入到新数组
        #         print(empty_subject_array)
        #         no_done_subject = list(set(subject_array).difference(set(empty_subject_array)))  # 获得该数组与所有学科数组的差集
        #         '''
        #         #自己方法实现
        #         suiji = random.sample(no_done_subject,1)#随机该数组
        #         print(suiji)
        #         str_empty = ''
        #         suiji_subject = int(subject_dict[str_empty.join(suiji)])#随机该数组元素转换int
        #         print(suiji_subject)
        #         wd.find_element_by_class_name('down').click()
        #         change_subject = wd.find_element_by_class_name('title')
        #         tag_change_subject = change_subject.find_elements_by_tag_name('li')
        #         tag_change_subject[suiji_subject].click()
        #         '''
        #         # 啊楼方法实现
        #         choise_subject_now = no_done_subject[random.randint(0, (len(no_done_subject) - 1))]
        #         wd.find_element_by_class_name('down').click()
        #         change_subject = wd.find_element_by_class_name('title')
        #         tag_change_subject = change_subject.find_elements_by_tag_name('li')
        #         for l in range(0, len(tag_change_subject)):
        #             if (choise_subject_now == tag_change_subject[l].text):
        #                 tag_change_subject[l].click()
        #                 time.sleep(2)
        #     else:
        #         certain = False
        # else:
        #     unit = wd.find_element_by_class_name('all')
        #     tag_unit = unit.find_elements_by_tag_name('div')
        #     num_unit = len(tag_unit)
        #     finish_unit = []
        #     for i in range(0, num_unit):
        #         if len(tag_unit[i].find_elements_by_tag_name('i')) == 0:
        #             finish_unit.append(i)
        #             break
        #     tag_xkyx_unit = tag_unit[i].find_elements_by_tag_name('li')
        #     num_xkyx_unit = len(tag_xkyx_unit)
        #     # 验证提能训练解锁
        #     for j in range(0, num_xkyx_unit):
        #         unit = wd.find_element_by_class_name('all')
        #         tag_xkyx = unit.find_elements_by_tag_name('div')
        #         tag_xkyx_unit = tag_xkyx[i].find_elements_by_tag_name('li')
        #         tag_xkyx_unit[j].click()
        #         time.sleep(2)
        #         if ('电子教材' in wd.find_element_by_class_name('Com_Crumbs_in').text):
        #             print('进入电子教材页面成功！')
        #             time.sleep(2)
        #         elif ('预习视频' in wd.find_element_by_class_name('Com_Crumbs_in').text):
        #             print('进入预习视频页面成功！')
        #             time.sleep(2)
        #         elif ('预习测试' in wd.find_element_by_class_name('Com_Crumbs_in').text):
        #             print('进入预习测试页面成功，开始做题吧！')
        #             time.sleep(2)
        #             tag_questions = wd.find_elements_by_class_name('group')
        #             num_questions = len(tag_questions)
        #             #print(num_questions)
        #             for x in range(0,num_questions):
        #                 tag_choise = tag_questions[x].find_elements_by_class_name('choise-option')
        #                 num_choise = len(tag_choise)-1
        #                 random_choise = random.randint(0,num_choise)
        #                 #print(random_choise)
        #                 tag_choise[random_choise].click()
        #         toast_menu = wd.find_element_by_class_name('Com_Crumbs_in')
        #         tag_toast_menu = toast_menu.find_elements_by_tag_name('a')
        #         tag_toast_menu[2].click()
        #         time.sleep(2)
    def test_04_write_sumHomework_ttyd(self):
        success = True
        wd = self.wd
        # print('开始测试学生写假期作业页面：')
        # Menu_HDayHomework = wd.find_elements_by_class_name("Com_Li")[2]
        # ActionChains(wd).move_to_element(Menu_HDayHomework).perform()
        # time.sleep(2)
        # Menu_HDayHomework.find_elements_by_tag_name("li")[2].click()
        # time.sleep(2)
        # subject_array = ['语文', '英语']
        # num_subject_array = len(subject_array)
        # empty_subject_array = []
        # print('开始测试学生天天阅读作业：')
        # son_menu = wd.find_element_by_class_name('category')
        # ttyd = son_menu.find_elements_by_tag_name('li')[2]
        # ttyd.click()
        # time.sleep(2)
        # if ('天天阅读' not in wd.find_element_by_class_name('Com_Crumbs').text):
        #     print('进入天天阅读页面失败！')
        #     success = False
        # else:
        #     print('进入天天阅读页面成功！')
        # chapter_title = wd.find_elements_by_class_name('reading_entrycontentli')
        # num_chapter_title = len(chapter_title)
        #
        # for i in range(0,1):#针对不同专题进行循环
        #     chapter_title = wd.find_elements_by_class_name('reading_entrycontentli')
        #     num_chapter_title = len(chapter_title)
        #     article_title_s = chapter_title[i].find_elements_by_tag_name('li')
        #     num_article_title_s = len(article_title_s)
        #     for j in range(0,num_article_title_s):#针对不同标题循环
        #         chapter_title = wd.find_elements_by_class_name('reading_entrycontentli')
        #         num_chapter_title = len(chapter_title)
        #         article_title_s = chapter_title[i].find_elements_by_tag_name('li')
        #         num_article_title_s = len(article_title_s)
        #         text_article_title = article_title_s[j].text
        #         article_title_s[j].click()#遍历标题
        #         #print('打开主题%d-%s成功'%(i+1),(article_title_s[j].text))
        #         print("打开主题%d--%s成功"%(i + 1,text_article_title))#输出专题和标题
        #         wd.back()
        #         time.sleep(2)
        #
        # #切换英语学科
        # #wd.find_element_by_class_name('down').click()
        # tag_change_subject = wd.find_elements_by_class_name('reading_entrysublist')
        # num_change_subject = len(tag_change_subject)
        # print(num_change_subject)
        # title_subject = wd.find_element_by_class_name('reading_entrysubword')
        # choise_subject = title_subject.text
        # print(choise_subject)
        # time.sleep(2)
        # if choise_subject == '语文':
        #     wd.execute_script("arguments[0].scrollIntoView();", title_subject)
        #     wd.find_element_by_class_name('reading_entrydown').click()
        #     tag_change_subject[1].click()
        # else:
        #     wd.find_element_by_class_name('reading_entrydown').click()
        #     tag_change_subject[0].click()
        # chapter_title = wd.find_elements_by_class_name('reading_entrycontentli')
        # num_chapter_title = len(chapter_title)
        # for i in range(0, 1):  # 针对不同专题进行循环
        #     chapter_title = wd.find_elements_by_class_name('reading_entrycontentli')
        #     num_chapter_title = len(chapter_title)
        #     article_title_s = chapter_title[i].find_elements_by_tag_name('li')
        #     num_article_title_s = len(article_title_s)
        #     for j in range(0, num_article_title_s-1):  # 针对不同标题循环
        #         chapter_title = wd.find_elements_by_class_name('reading_entrycontentli')
        #         num_chapter_title = len(chapter_title)
        #         article_title_s = chapter_title[i].find_elements_by_tag_name('li')
        #         num_article_title_s = len(article_title_s)
        #         time.sleep(1)
        #         text_article_title = article_title_s[j].text
        #         #print(j)
        #         article_title_s[j].click()  # 遍历标题
        #         # print('打开主题%d-%s成功'%(i+1),(article_title_s[j].text))
        #         print("打开主题%d--%s成功" % (i + 1, text_article_title))  # 输出专题和标题
        #         wd.find_element_by_class_name('Com_Crumbs_in').find_elements_by_tag_name('a')[2].click()
        #         time.sleep(2)
        # time.sleep(2)
        self.assertTrue(success)

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()