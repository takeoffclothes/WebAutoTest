#coding=utf-8

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui

#   该方法用来确认元素是否存在，如果存在返回flag=true，否则返回false        
def isElementCssExist(self,element):
    flag=True
    wd=self.wd
    try:
        wd.find_element_by_css_selector(element)
        return flag
        
    except:
        flag=False
        return flag
    
def isElementXpathExist(self,element):
    flag=True
    wd=self.wd
    try:
        wd.find_element_by_xpath(element)
        return flag
        
    except:
        flag=False
        return flag

# 一直等待某元素可见，默认超时10秒
def is_visible(self,locator, timeout=10):
    wd = self.wd
    try:
        ui.WebDriverWait(wd, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
        return True
    except TimeoutException:
        return False

# 一直等待某个元素消失，默认超时10秒
def is_not_visible(self,locator, timeout=10):
    wd = self.wd
    try:
        ui.WebDriverWait(wd, timeout).until_not(EC.visibility_of_element_located((By.XPATH, locator)))
        return True
    except TimeoutException:
        return False