#coding=utf-8
import time
#登录
def login(self,username,password):
    wd = self.wd
    wd.find_element_by_xpath(".//*[@id='Phone']").click()
    wd.find_element_by_xpath(".//*[@id='Phone']").clear()
    wd.find_element_by_xpath(".//*[@id='Phone']").send_keys(username)
    wd.find_element_by_xpath(".//*[@id='Pass']").click()
    wd.find_element_by_xpath(".//*[@id='Pass']").clear()
    wd.find_element_by_xpath(".//*[@id='Pass']").send_keys(password)
    wd.find_element_by_xpath(".//*[@id='LoginBtn']").click()
    self.wd.implicitly_wait(10)
    if (len(wd.find_elements_by_id("User")) != 0):
        print(username+"登录成功！")
    else:
        print(username+"登录失败！")