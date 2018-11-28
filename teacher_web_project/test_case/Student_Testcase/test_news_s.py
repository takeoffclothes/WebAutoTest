# coding：utf-8(定义源代码的编码:源代码的编码可以包含中文字符串)
# Created on 2018年1月30日
# updated on 2018年1月30日
# 五好导学网-学生web端-消息 自动化测试脚本
# 作者: 马春苗

# 消息流程：导航菜单-消息页初始化-上一页/下一页/尾页-退出
# 未走流程：定位翻页、删除功能

from selenium import webdriver
from Constant.sys_constant import *
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest
from test_case.PubModule import login, logout,topmenu_t

class test_news_s(unittest.TestCase):
    # 学生pc端-消息

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
        # 登录17470007001
        login.login(self, "17400007001", "123456")
    def test_news(self):
        print("开始测试！个人中心-消息")
        # 进入消息页
        wd = self.wd
        success = True
        topmenu_t.top_menu_xx_s(self)

        if not ("消息" in wd.find_element_by_tag_name("html").text):
            success = False
            print("消息页初始化失败")
        else:
            print("消息页初始化成功")
        time.sleep(2)
        wd.find_element_by_xpath("//span[@class='pageBtnWrap']//a[.='下一页']").click()
        print("下一页翻页成功")
        time.sleep(2)
        wd.find_element_by_xpath("html/body/div[4]/div/div[1]/span[1]/a[2]").click()
        print("上一页翻页成功")
        time.sleep(2)
        wd.find_element_by_xpath("//span[@class='pageBtnWrap']//a[.='尾页']").click()
        print("尾页翻页成功")
        # 输入要翻的页数
        wd.find_element_by_id("kkpager_btn_go_input").clear()
        wd.find_element_by_id("kkpager_btn_go_input").send_keys("1")
        wd.find_element_by_id("kkpager_btn_go").click()

        print("定位到转到")
        time.sleep(2)
        print("开始测试！个人中心-消息删除")
        msglist = wd.find_element_by_xpath("//ul[@id='SystemList']")
        msg = msglist.find_elements_by_xpath("./li")
        msg[-1].find_element_by_xpath("./span[@class='m_MsgDel']").click()
        if not ("删除成功" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"消息删除失败")
        else:
            print(u"消息删除成功")
        logout.logout_s(self)
    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
