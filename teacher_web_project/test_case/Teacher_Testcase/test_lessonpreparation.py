# -*- coding: utf-8 -*-
#编写人：Olivia.Wang
#时间：2018.2.5
#主要功能：备课视频，可以遍历完所有视频，做完所有测试；备课音频，可以遍历完所有音频，开始播放音频，快进，后退，暂停音频
#备课课件，可以遍历所有课件（其他功能待补充）
#时间：2018.02.25 更新了课件中的点赞，ppt的下一页，上一页，备注，ppt放映，下载等功能
# 时间：2018.08.30 新增了教师pc端备课上课脚本
import time
import unittest
from test_case.PubModule import login
from selenium.webdriver.firefox.webdriver import WebDriver


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_lessonpreparation(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        wd = self.wd
        # wd.get("http://preprod-whdx.bcbook.cn")
        wd.get(LOGIN_URL)
        login.login(self, "14600000071", "123456")
        time.sleep(2)

    # def test_01_videos(self):
    #     success = True
    #     wd = self.wd
    #     #wd.maximize_window()
    #     time.sleep(2)
    #     #登录账号、密码
    #     prepar = wd.find_elements_by_class_name("totalnav")
    #     ActionChains(wd).move_to_element(prepar[0]).perform()
    #     time.sleep(1)
    #     prepar1 = prepar[0].find_elements_by_tag_name("a")
    #     prepar1[0].click()
    #     video = wd.find_element_by_class_name("v_list")
    #     shipin = video.find_elements_by_tag_name("li")
    #     shipin[0].click()
    #     time.sleep(3)
    #     zan = wd.find_element_by_class_name("agreeNum")
    #     if ("color" in zan.get_attribute("style")):
    #         print("已经点过赞了！")
    #     else:
    #         print("还未点赞！")
    #         wd.find_element_by_class_name("ClickUp").click()
    #     #wd.refresh()
    #     #time.sleep(5)
    #     wd.find_element_by_class_name("prepareTest").click()
    #     handles = wd.window_handles
    #     wd.switch_to.window(handles[1])
    #     time.sleep(2)
    #     papertest = wd.find_element_by_class_name("paperTest")
    #     papertest1 = papertest.find_elements_by_class_name("t_option")
    #     # 随机做题功能
    #     for l in range(0, len(papertest1)):
    #         x = random.randint(0, 3)
    #         choise = papertest1[l].find_elements_by_class_name("t_optionLi")
    #         choise[x].click()
    #         time.sleep(1)
    #
    #     wd.find_element_by_class_name("btnSubmit").click()
    #     # 关闭窗口，跳回第一个窗口
    #     wd.close()
    #     handles = wd.window_handles
    #     wd.switch_to.window(handles[0])
    #     wd.back()
    #     time.sleep(2)
    #
    #
    #     '''
    #     #有几个层级菜单
    #     liebiao = wd.find_elements_by_class_name("c_DirectoryList")
    #     for i in range(0,len(liebiao)-1):
    #         liebiao = wd.find_elements_by_class_name("c_DirectoryList")
    #         subject = liebiao[i].find_elements_by_tag_name("li")
    #         #该层级下的子菜单数
    #         for j in range(0,len(subject)):
    #             liebiao = wd.find_elements_by_class_name("c_DirectoryList")
    #             subject = liebiao[i].find_elements_by_tag_name("li")
    #             #点击该层级下的子菜单数
    #             subject[j].click()
    #             time.sleep(1)
    #             liebiao = wd.find_elements_by_class_name("c_DirectoryList")
    #             unit = liebiao[i+1].find_elements_by_tag_name("li")
    #             #第二层级下的子菜单数
    #             for h in range(0,len(unit)):
    #                 liebiao = wd.find_elements_by_class_name("c_DirectoryList")
    #                 unit = liebiao[i + 1].find_elements_by_tag_name("li")
    #                 #点击子菜单
    #                 unit[h].click()
    #                 time.sleep(1)
    #                 vlist = wd.find_element_by_class_name("v_list")
    #                 #判断该视频下是否有视频
    #                 if len(vlist.find_elements_by_tag_name("a"))>0:
    #                     print("该单元下有视频！")
    #                     videolist = wd.find_element_by_class_name("v_list")
    #                     videolist1 = videolist.find_elements_by_tag_name("li")
    #                     #视频列表
    #                     for k in range(0, len(videolist1)):
    #                         videolist = wd.find_element_by_class_name("v_list")
    #                         videolist1 = videolist.find_elements_by_tag_name("li")
    #                         #遍历点击第几个视频
    #                         videolist1[k].click()
    #                         time.sleep(1)
    #                         #判断是否有预习测试按钮
    #                         if ("预习测试" in wd.find_element_by_class_name("c_Main ").text):
    #                             wd.find_element_by_class_name("prepareTest").click()
    #                             handles = wd.window_handles
    #                             wd.switch_to.window(handles[1])
    #                             time.sleep(2)
    #                             papertest = wd.find_element_by_class_name("paperTest")
    #                             papertest1 = papertest.find_elements_by_class_name("t_option")
    #                             #随机做题功能
    #                             for l in range(0, len(papertest1)):
    #                                 x = random.randint(0,3)
    #                                 choise = papertest1[l].find_elements_by_class_name("t_optionLi")
    #                                 choise[x].click()
    #                                 time.sleep(1)
    #
    #                             wd.find_element_by_class_name("btnSubmit").click()
    #                             #关闭窗口，跳回第一个窗口
    #                             wd.close()
    #                             handles = wd.window_handles
    #                             wd.switch_to.window(handles[0])
    #                             wd.back()
    #                             time.sleep(2)
    #                         else:
    #                             wd.back()
    #                             time.sleep(2)
    #                 else:
    #                     success = False
    #                     print("该单元下没视频！")
    #     '''
    #     self.assertTrue(success)
    #
    # def test_02_audios(self):
    #     success = True
    #     wd = self.wd
    #     time.sleep(2)
    #     #鼠标悬停操作
    #     prepar = wd.find_elements_by_class_name("totalnav")
    #     ActionChains(wd).move_to_element(prepar[0]).perform()
    #     time.sleep(1)
    #     prepar1 = prepar[0].find_elements_by_tag_name("a")
    #     prepar1[1].click()
    #     time.sleep(3)
    #     wd.find_element_by_id("playPause").click()
    #     time.sleep(3)
    #     if ("Pause" in wd.find_element_by_id("playPause").get_attribute("title")):
    #         print("开始播放音乐！")
    #     else:
    #         success = False
    #         print("播放音乐失败！")
    #     # 进度条右移150个像素，即快进操作
    #     jindutiao = wd.find_element_by_id("barLoaded")
    #     ActionChains(wd).click_and_hold(jindutiao).move_by_offset(150, 0).release().perform()
    #     time.sleep(3)
    #     # 进度条左移50个像素，即快进操作
    #     ActionChains(wd).click_and_hold(jindutiao).move_by_offset(-50, 0).release().perform()
    #     time.sleep(3)
    #     wd.find_element_by_id("playPause").click()
    #     time.sleep(3)
    #     if ("Play" in wd.find_element_by_id("playPause").get_attribute("title")):
    #         print("暂停音乐！")
    #     else:
    #         success = False
    #         print("暂停音乐失败！")
    #     # 验证快进快退后是否可以播放音乐
    #     wd.find_element_by_id("playPause").click()
    #     time.sleep(3)
    #     if ("Pause" in wd.find_element_by_id("playPause").get_attribute("title")):
    #         print("开始播放音乐！")
    #     else:
    #         success = False
    #         print("播放音乐失败！")
    #     time.sleep(3)
    #     '''
    #     #有几个层级
    #     liebiao = wd.find_elements_by_class_name("c_DirectoryList")
    #     for i in range(0,len(liebiao)-1):
    #         liebiao = wd.find_elements_by_class_name("c_DirectoryList")
    #         subject = liebiao[i].find_elements_by_tag_name("li")
    #         #点击该层级下的子菜单
    #         for j in range(0,len(subject)):
    #             subject = liebiao[i].find_elements_by_tag_name("li")
    #             subject[j].click()
    #             time.sleep(1)
    #             liebiao = wd.find_elements_by_class_name("c_DirectoryList")
    #             unit = liebiao[i+1].find_elements_by_tag_name("li")
    #             #单元下有几个音频
    #             for h in range(0,len(unit)):
    #                 liebiao = wd.find_elements_by_class_name("c_DirectoryList")
    #                 unit = liebiao[i+1].find_elements_by_tag_name("li")
    #                 unit[h].click()
    #                 time.sleep(1)
    #                 #判断可是下是否有内容
    #                 if("block" in wd.find_element_by_id("NoData").get_attribute("style")):
    #                     print("该课时下无内容！")
    #                 else:
    #                     wd.find_element_by_id("playPause").click()
    #                     time.sleep(3)
    #                     if ("Pause" in wd.find_element_by_id("playPause").get_attribute("title")):
    #                         print("开始播放音乐！")
    #                     else:
    #                         print("播放音乐失败！")
    #                     #进度条右移150个像素，即快进操作
    #                     jindutiao = wd.find_element_by_id("barLoaded")
    #                     ActionChains(wd).click_and_hold(jindutiao).move_by_offset(150,0).release().perform()
    #                     time.sleep(3)
    #                     # 进度条左移50个像素，即快进操作
    #                     ActionChains(wd).click_and_hold(jindutiao).move_by_offset(-50, 0).release().perform()
    #                     time.sleep(3)
    #                     wd.find_element_by_id("playPause").click()
    #                     time.sleep(3)
    #                     if ("Play" in wd.find_element_by_id("playPause").get_attribute("title")):
    #                         print("暂停音乐！")
    #                     else:
    #                         print("暂停音乐失败！")
    #                     #验证快进快退后是否可以播放音乐
    #                     wd.find_element_by_id("playPause").click()
    #                     time.sleep(3)
    #                     if ("Pause" in wd.find_element_by_id("playPause").get_attribute("title")):
    #                         print("开始播放音乐！")
    #                     else:
    #                         print("播放音乐失败！")
    #                     time.sleep(3)
    #     '''
    #     self.assertTrue(success)
    #
    # def test_03_courseware(self):
    #     success = True
    #     wd = self.wd
    #     time.sleep(2)
    #     #鼠标悬停操作
    #     prepar = wd.find_elements_by_class_name("totalnav")
    #     ActionChains(wd).move_to_element(prepar[0]).perform()
    #     time.sleep(1)
    #     prepar1 = prepar[0].find_elements_by_tag_name("a")
    #     prepar1[2].click()
    #     video = wd.find_element_by_id("p_CourseWareWrap")
    #     shipin = video.find_elements_by_tag_name("a")
    #     shipin[0].click()
    #     #判断是否点赞？未点赞，执行点赞操作
    #     zan = wd.find_element_by_class_name("p_ZanCount")
    #     if ("color" in zan.get_attribute("style")):
    #         print("已经点过赞了！")
    #     else:
    #         print("还未点赞！")
    #         wd.find_element_by_class_name("p_spriteImg").click()
    #         print("点赞成功！")
    #     time.sleep(3)
    #     #跳转frame
    #     wd.switch_to.frame("iframeReload")
    #     ppt = wd.find_elements_by_class_name("cui-ctl-iconContainer14")
    #     #点击ppt的下一页
    #     ppt[1].click()
    #     time.sleep(2)
    #     ppt[1].click()
    #     time.sleep(2)
    #     #点击ppt上一页
    #     ppt[0].click()
    #     time.sleep(2)
    #     ppt[0].click()
    #     time.sleep(2)
    #     ppt[2].click()
    #     #wd.find_element_by_id("ButtonFastFwd-Small14").click()
    #     #wd.find_element_by_id("ButtonFastFwd-Small14").click()
    #     time.sleep(3)
    #     #点击ppt的备注按钮
    #     if("幻灯片" in wd.find_element_by_class_name("ReadingNotesPanel").text):
    #         print("该备注按钮可点击！")
    #     else:
    #         success = False
    #         print("该备注按钮不可点击！")
    #     #点击ppt的放映按钮
    #     wd.find_element_by_id("PptReadingStatusBar.SlideShow-Small14").click()
    #     handles = wd.window_handles
    #     wd.switch_to.window(handles[1])
    #     time.sleep(8)
    #     if(wd.find_element_by_id("SlideshowNavigationPanel")):
    #         print("ppt放映成功！")
    #     else:
    #         success = False
    #         print("ppt放映失败！")
    #     wd.close()
    #     time.sleep(3)
    #     handle = wd.window_handles
    #     wd.switch_to.window(handle[0])
    #     wd.switch_to.default_content()
    #     wd.refresh()
    #
    #     wd.find_element_by_xpath(".//*[@id='p_CWOperationWrap_div']/button").click()
    #     if (wd.find_element_by_xpath(".//*[@id='p_CWOperationWrap_div']/button").click()):
    #         print("弹出下载弹窗失败！")
    #     else:
    #         #success = False
    #         print("弹出下载弹窗成功！")
    #     os.system(autoitfile_path+'cancel.exe')
    #
    #     '''
    #     #有几个层级
    #     liebiao = wd.find_elements_by_class_name("c_DirectoryList")
    #     for i in range(0, len(liebiao)-1):
    #         liebiao = wd.find_elements_by_class_name("c_DirectoryList")
    #         subject = liebiao[i].find_elements_by_tag_name("li")
    #         #点击该层级下的子菜单
    #         for j in range(0, len(subject)):
    #             liebiao = wd.find_elements_by_class_name("c_DirectoryList")
    #             subject = liebiao[i].find_elements_by_tag_name("li")
    #             subject[j].click()
    #             time.sleep(1)
    #             liebiao = wd.find_elements_by_class_name("c_DirectoryList")
    #             unit = liebiao[i+1].find_elements_by_tag_name("li")
    #             #单元下有几个课件
    #             for h in range(0, len(unit)):
    #                 liebiao = wd.find_elements_by_class_name("c_DirectoryList")
    #                 unit = liebiao[i + 1].find_elements_by_tag_name("li")
    #                 unit[h].click()
    #                 time.sleep(1)
    #                 course = wd.find_element_by_id("p_CourseWareWrap")
    #                 #判断该单元下是否有课件
    #                 if len(course.find_elements_by_tag_name("a"))>0:
    #                     print("该课时下有课件！")
    #                     course1 = course.find_elements_by_tag_name("a")
    #                     #遍历点击课件
    #                     for k in range(0,len(course1)):
    #                         course = wd.find_element_by_id("p_CourseWareWrap")
    #                         course1 = course.find_elements_by_tag_name("a")
    #                         course1[k].click()
    #                         time.sleep(2)
    #
    #                         #wd.find_element_by_class_name("cui-ctl-iconContainer14").click()
    #                         wd.back()
    #                         time.sleep(2)
    #                 else:
    #                     print("该课时下无数据！")
    #     '''
    #     self.assertTrue(success)
    def test_01_insertclass(self):
        success = True
        wd = self.wd
        time.sleep(2)
        # 进入备课页面
        wd.find_elements_by_class_name('menuId')[1].click()
        time.sleep(2)
        # 新增课时，先判断是否已有课时
        if ('none' in wd.find_element_by_class_name('noCourseData').get_attribute('style')):
            print('已经有新增的课时！')
        else:
            print('没有新增的课时！')
            # 没有新增课时，新增课时
            wd.find_element_by_class_name('addPrepareLesson').click()
            wd.find_element_by_class_name('submitBtn').click()
            if ('请输入课时名称' in wd.find_element_by_class_name('dialog-toast').text):
                print('课时名称不能为空，请输入课时名称！')
            else:
                success = False
                print('课时名称为空，可以添加成功！')
            # 取消新增课时
            wd.find_element_by_class_name('lessonName').send_keys('测试')
            wd.find_element_by_class_name('cancleBtn').click()
            time.sleep(1)
            if ('none' in wd.find_element_by_class_name('noCourseData').get_attribute('style')):
                success = False
                print('取消添加课时失败！')
            else:
                print('取消添加课时成功！')
            # 取消新增课时
            wd.find_element_by_class_name('addPrepareLesson').click()
            wd.find_element_by_class_name('submitBtn').click()
            wd.find_element_by_class_name('lessonName').send_keys('测试')
            wd.find_element_by_class_name('submitBtn').click()
            time.sleep(1)
            if ('none' in wd.find_element_by_class_name('noCourseData').get_attribute('style')):
                print('添加课时成功！')
            else:
                success = False
                print('添加课时失败！')
    def test_02_preparation(self):
        wd = self.wd
        success = True
        time.sleep(1)
        print("开始测试-老师备课流程")
        # 进入备课页面
        wd.find_elements_by_class_name('menuId')[1].click()
        time.sleep(2)
        # 获取备课资源数量
        resource_prepare_num = int(wd.find_element_by_class_name('resourceNum').text)
        # 备课资源大于0是进行资源浏览，删除资源
        if (resource_prepare_num > 0):
            #点击继续备课
            wd.find_element_by_class_name('continueBtn').click()
            # #点击添加资源
            # wd.find_element_by_xpath("//span[@class='resource-add']").click()

            # 资源类型遍历
            resourceul = wd.find_element_by_id('list')
            resources = resourceul.find_elements_by_tag_name('li')
            resources_num = len(resources)
            for i in range(0, len(resources)):
                # 已经添加资源遍历
                if not (resources[i].is_displayed() and resources[i].is_enabled()):
                    # wd.execute_script("arguments[0].focus();", resources[i])
                    js = "var q=resources[i].scrollTop=0"
                    wd.execute(self,js)
                    resources[i].click()
                else:
                    resources[i].click()
                    time.sleep(2)
            # 点击调整资源-取消操作
            wd.find_element_by_xpath("//p[@class='content-edit']").click()
            zhidaole = wd.find_element_by_xpath("//div[@class='introjs-tooltipbuttons']")
            if zhidaole.is_displayed():
                zhidaole.click()
            qxwc  = wd.find_element_by_xpath("//p[@class='content-editing']")
            if qxwc.is_displayed():
                #开始删除资源
                for i in range(0,resource_prepare_num):
                    wd.find_element_by_xpath("//i[@class='icon_delete']").click()
                    time.sleep(1)
                #点击取消
                wd.find_element_by_xpath("//p[@class='content-editing']/span[1]").click()
            else:
                print("调整资源失败：未找到完成按钮")
            # 点击调整资源-完成操作
            wd.find_element_by_xpath("//p[@class='content-edit']").click()
            qxwc  = wd.find_element_by_xpath("//p[@class='content-editing']")
            if qxwc.is_displayed():
                #开始删除资源
                for i in range(0,resource_prepare_num):
                    wd.find_element_by_xpath("//i[@class='icon_delete']").click()
                    time.sleep(1)
                #点击完成
                wd.find_element_by_xpath("//p[@class='content-editing']/span[2]").click()
            else:
                print("调整资源失败：未找到完成按钮")
        else:
            #资源是0则添加资源
            wd.find_element_by_class_name('beginBtn').click()
            time.sleep(2)
            # 资源类型遍历
            resource_type = wd.find_element_by_class_name('resource-type')
            resources_type = resource_type.find_elements_by_tag_name('li')
            resources_num = 0
            for i in range(0, len(resources_type)):
                resources_type[i].click()
                time.sleep(3)
                # 平台资源遍历
                resource = wd.find_element_by_class_name('resource-list')
                resources = resource.find_elements_by_tag_name('li')
                resources_num += len(resources)
                for j in range(0, len(resources)):
                    #点击加入课堂
                    resources[j].find_element_by_class_name('resource-add').click()
                    time.sleep(1)
            num = int(wd.find_element_by_class_name('icon-num').text)
            if (num == resources_num):
                print('遍历添加课时成功！')
            else:
                success = False
                print('遍历添加课时失败！')
            #点击已添加按钮
            wd.find_element_by_class_name('resource-num').click()

            wd.find_element_by_class_name('resource-add').click()
            if ('添加资源' in wd.find_element_by_class_name('Com_Crumbs_in').text):
                print("跳转添加资源页面成功！")
            else:
                success = False
                print('跳转添加资源页面失败！')
    def test_03_beginclass(self):
        wd = self.wd
        success = True
        # 进入备课页面
        wd.find_elements_by_class_name('menuId')[2].click()
        time.sleep(2)
        wd.find_element_by_class_name('beginBtn').click()
        if ('测试' in wd.find_element_by_class_name('Com_Crumbs').text):
            print('进入上课页面成功！')
        else:
            print('进入上课页面失败！')
    def test_04_deleteclass(self):
        wd = self.wd
        success = True
        time.sleep(1)
        # 进入备课页面
        wd.find_elements_by_class_name('menuId')[1].click()
        time.sleep(2)
        wd.find_element_by_class_name('delBtn').click()
        time.sleep(1)
        wd.find_element_by_class_name('submitBtn').click()
        time.sleep(1)
        if ('none' in wd.find_element_by_class_name('noCourseData').get_attribute('style')):
            success = False
            print('删除失败！')
        else:
            print('删除成功！')

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()