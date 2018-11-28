# coding：utf-8(定义源代码的编码:源代码的编码可以包含中文字符串)
# Created on 2018年1月30日
# updated on 2018年1月30日
# 五好导学网-教师web端-消息 自动化测试脚本
# 作者: 马春苗

# 消息流程：导航菜单-消息页初始化-切换消息标签-上一页/下一页/尾页-退出
# 未走流程：定位翻页、删除功能、切换标签

from selenium import webdriver
from Constant.sys_constant import *
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest
from test_case.PubModule import login, logout


class test_news_t(unittest.TestCase):
    # 老师pc端-消息

    def setUp(self):
        # 定义浏览器下载配置
        #profile = webdriver.FirefoxProfile(Firefox_Path)
        #profile = webdriver.FirefoxProfile("C:\\Users\\Administrator\\AppData\\Local\\Mozilla\\Firefox\\Profiles\\pl3wrsan.default")
        # 定义浏览器，打开测试网站
        #self.wd = webdriver.Firefox(profile)
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.wd.get(LOGIN_URL)
        #self.wd.get("http://www.wuhaodaoxue.com")
        # 脚本运行时，错误的信息将被打印到这个列表中。
        self.verificationErrors = []
        # 是否继续接受下一下警告
        self.accept_next_alert = True
        wd = self.wd
        time.sleep(1)
        # 窗口最大化
        wd.maximize_window()
        # 登录
        login.login(self, "17470000001", "123456")

    def test_news(self):
        print("开始测试！个人中心-消息")
        # 进入消息页
        wd = self.wd
        success = True

        # 进入消息
        # 定位到用户头像
        article = wd.find_element_by_xpath(".//*[@id='User']")
        try:
            article.is_displayed()
            article.click()
            # 鼠标悬浮在用户头像位置
            ActionChains(wd).move_to_element(article).perform()
            # 等待3秒
            time.sleep(2)
            # 定位到消息元素
            mouse = wd.find_element_by_xpath(".//*[@id='menav']/li[1]/a")
            # 鼠标移动至消息上方悬浮
            ActionChains(wd).move_to_element(mouse).perform()
            # 点击消息
            wd.find_element_by_xpath(".//*[@id='menav']/li[1]/a").click()

            if not ("消息" in wd.find_element_by_tag_name("html").text):
                success = False
                print("消息页初始化失败")
            else:
                print("消息页初始化成功")
            time.sleep(2)
        except Exception:
            print("定位用户头像异常")
        # 切换到申请消息标签
        wd.find_element_by_class_name("message_select_play ").click()
        time.sleep(2)
        if not("入班申请" in wd.find_element_by_tag_name("html").text):
            success = False
            print("切换消息标签失败")
        else:
            print("切换消息标签成功")
        # 删除消息
        msglist = wd.find_element_by_xpath("//ul[@class='message_select_play_ideas']")
        msg = msglist.find_elements_by_tag_name("li")
        if msg.__len__()>1:
            msg[-1].find_element_by_xpath("./span[@class='message_select_play_ideas_every_delete']").click()
            if not ("删除成功" in wd.find_element_by_tag_name("html").text):
                success = False
                print(u"消息删除失败")
            else:
                print(u"消息删除成功")
        #切换回系统消息
        wd.find_element_by_class_name("message_select_system ").click()
        print("切换至系统消息标签")
        time.sleep(2)
        wd.find_element_by_xpath("//span[@class='pageBtnWrap']//a[.='下一页']").click()
        print("下一页翻页成功")
        time.sleep(1)
        wd.find_element_by_xpath("//span[@class='pageBtnWrap']//a[.='上一页']").click()
        print("上一页翻页成功")
        time.sleep(2)
        wd.find_element_by_xpath("//span[@class='pageBtnWrap']//a[.='尾页']").click()
        print("尾页翻页成功")
        time.sleep(2)
        self.assertTrue(success)

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
