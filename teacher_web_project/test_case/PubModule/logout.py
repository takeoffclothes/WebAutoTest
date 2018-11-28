#coding=utf-8
from selenium.webdriver.common.action_chains import ActionChains
#from selenium import webdriver
import time
#退出
def logout(self):
    wd = self.wd
    
    #定位到首页头像元素        
    #article = wd.find_element_by_xpath(".//*[@id='UserHeadImg']")  
    article = wd.find_element_by_xpath(".//*[@id='User']")  
    #鼠标悬浮再用户头像位置
    ActionChains(wd).move_to_element(article).perform()
    #等待3秒
    time.sleep(0.5)
    #定位到退出元素 .//*[@id='menav']/li[3]/a
    #mouse = wd.find_element_by_xpath(".//*[@id='menav']/li[3]/a")  
    mouse = wd.find_element_by_xpath("//li[@class='quite']/a")  
    #鼠标移动至退出上方悬浮
    ActionChains(wd).move_to_element(mouse).perform()
    #点击退出
    #wd.find_element_by_xpath(".//*[@id='menav']/li[3]/a").click()
    wd.find_element_by_xpath("//li[@class='quite']/a").click()
    time.sleep(0.5)
    
def logout_s(self):
    wd = self.wd
    
    #定位到首页头像元素        
    article = wd.find_element_by_id("UserHeadImg")
    #鼠标悬浮再用户头像位置
    ActionChains(wd).move_to_element(article).perform()
    #定位到退出元素
    time.sleep(1)
    wd.find_element_by_id("Quit").click()
    time.sleep(1)
 
    