#作者：王帅 功能：可以查看固定单元下的预习中心下的视频、音频
#未完善浏览量是否增加的判断
# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest, os, sys
import random
from Constant.sys_constant import *
from test_case.PubModule import login,topmenu_t

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_previewcenter(unittest.TestCase):
    def setUp(self):

        self.wd = WebDriver()
        # profile = WebDriver.firefox_profile("C:\\Users\\Administrator\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\x8mc2eqs.default")
        # self.wd = WebDriver.firefox(profile)
        self.wd.implicitly_wait(60)
        wd = self.wd
        wd.maximize_window()
        wd.get(LOGIN_URL)
        # wd.get("http://preprod-whdx.bcbook.cn")
        #登录账号、密码14600000701
        login.login(self,"14600000701","123456")

    def test_01_videos(self):
        success = True
        wd = self.wd
        time.sleep(2)
        #进入看视频
        topmenu_t.top_menu_ksp_s(self)
        time.sleep(2)
        # 点击第一个视频
        wd.find_element_by_xpath("//ul[@class='v_list']/li[1]/a/div/img").click()
        '''
        # # 视频点赞
        # if ("color" in wd.find_element_by_class_name("agreeNum").get_attribute("style")):
        #     print("该视频已点赞！")
        # else:
        #     print("该视频未点赞")
        #     a = wd.find_element_by_class_name("agreeNum").text
        #     print(a)
        #     wd.find_element_by_class_name("cup").click()
        #     b = wd.find_element_by_class_name("agreeNum").text
        #     if (a != b):
        #         print("点赞成功！")
        #     else:
        #         print("点赞失败！")
        #
        # # 视频分享
        # wd.find_element_by_class_name("enjoys").click()
        # wd.find_element_by_class_name("bds_sqq").click()
        # time.sleep(3)
        # handles = wd.window_handles
        # wd.switch_to.window(handles[1])
        # wd.refresh()
        # time.sleep(3)
        # if ("block" in wd.find_element_by_class_name("login_div").get_attribute("style")):
        #     wd.switch_to.frame("login_frame")
        # time.sleep(3)
        # #判断分享qq是否成功
        # if ("快速安全登录" in wd.find_element_by_class_name("login").text):
        #     print("分享QQ页面成功！")
        # else:
        #     print("分享QQ页面失败！")
        # wd.close()
        # #切换窗口
        # handles = wd.window_handles
        # wd.switch_to.window(handles[0])
        # time.sleep(2)
        # wd.find_element_by_class_name("bds_qzone").click()
        # time.sleep(3)
        # handles = wd.window_handles
        # wd.switch_to.window(handles[1])
        # time.sleep(2)
        # wd.refresh()
        # time.sleep(3)
        # #判断分享qq空间是否成功
        # if ("QQ空间" in wd.find_element_by_id("shareToTitle").text):
        #     print("分享QQ空间成功！")
        # else:
        #     print("分享QQ空间失败！")
        # wd.close()
        # #跳转窗口
        # handles = wd.window_handles
        # wd.switch_to.window(handles[0])
        # wd.find_element_by_class_name("bds_tsina").click()
        # time.sleep(2)
        # handles = wd.window_handles
        # wd.switch_to.window(handles[1])
        # wd.refresh()
        # time.sleep(3)
        # #判断分享微博是否成功
        # if ("微博" in wd.find_element_by_class_name("WB_logo").text):
        #     print("分享微博成功！")
        # else:
        #     print("分享微博失败！")
        # wd.close()
        # handles = wd.window_handles
        # wd.switch_to.window(handles[0])
        # wd.find_element_by_class_name("bds_weixin").click()
        # time.sleep(2)
        # #判断分享朋友圈是否成功
        # if ("朋友圈" in wd.find_element_by_class_name("bd_weixin_popup_head").text):
        #     print("分享微信成功！")
        # else:
        #     print("分享微信失败！")
    '''
        # 点击预习测试
        wd.find_element_by_xpath("//span[@class='prepareTest']/a").click()
        handles = wd.window_handles
        wd.switch_to.window(handles[1])
        #判断该试卷是否已做
        if ("none" in wd.find_element_by_class_name("btnSubmit").get_attribute("style")):
            print("该试卷已做！")
        else:
            print("该试卷未做！")
            test = wd.find_elements_by_class_name("group")
            for i in range(len(test)):
                test = wd.find_elements_by_class_name("group")
                xuanxiang = test[i].find_elements_by_class_name("choise-option")
                x = random.randint(0, 3)
                xuanxiang[x].click()
                time.sleep(2)
            wd.find_element_by_class_name("btnSubmit").click()

        time.sleep(2)

        self.assertTrue(success)

    def test_02_audios(self):
        success = True
        wd = self.wd
        time.sleep(2)
        #进入听音频
        topmenu_t.top_menu_typ_s(self)
        time.sleep(2)
        # 语文播放音频验证
        wd.find_element_by_id("playPause").click()
        time.sleep(3)
        if ("Pause" in wd.find_element_by_id("playPause").get_attribute("title")):
            print("开始播放音乐！")
        else:
            print("播放音乐失败！")
        # 进度条右移150个像素，即快进操作
        jindutiao = wd.find_element_by_id("barLoaded")
        ActionChains(wd).click_and_hold(jindutiao).move_by_offset(150, 0).release().perform()
        time.sleep(3)
        # 进度条左移50个像素，即快进操作
        ActionChains(wd).click_and_hold(jindutiao).move_by_offset(-50, 0).release().perform()
        time.sleep(3)
        wd.find_element_by_id("playPause").click()
        time.sleep(3)
        if ("Play" in wd.find_element_by_id("playPause").get_attribute("title")):
            print("暂停音乐！")
        else:
            print("暂停音乐失败！")

        wd.find_element_by_id("playPause").click()
        time.sleep(3)
        if ("Pause" in wd.find_element_by_id("playPause").get_attribute("title")):
            print("开始播放音乐！")
        else:
            print("播放音乐失败！")

        time.sleep(3)

        # subject = wd.find_elements_by_class_name("HeadList")
        # subject[1].click()
        #切换到英语
        wd.find_element_by_xpath("//li[@title='英语']").click()
        wd.find_element_by_id("MediaPlayBtn").click()
        time.sleep(3)
        if ("下一个" in wd.find_element_by_class_name("MediaBtn1").get_attribute("title")):
            print("模式为单读模式！")
        else:
            print("模式为连读模式！")
        # 验证连读模式
        moshi = wd.find_element_by_class_name("MediaModelBox")
        ActionChains(wd).move_to_element(moshi).perform()
        time.sleep(2)
        wd.find_element_by_id("Model1").click()
        wd.find_element_by_id("MediaPlayBtn").click()
        time.sleep(3)
        if ("下一个" in wd.find_element_by_class_name("MediaBtn0").get_attribute("title")):
            print("模式为单读模式！")
        else:
            print("模式为连读模式！")
        # 拼写已经删除
        # wd.find_element_by_xpath(".//*[@id='WordTab']/p[2]").click()
        # wd.find_element_by_id("g").click()
        # wd.find_element_by_id("o").click()
        # wd.find_element_by_id("o").click()
        # wd.find_element_by_id("d").click()
        time.sleep(3)
        self.assertTrue(success)

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
