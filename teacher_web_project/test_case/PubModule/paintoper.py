#coding=utf-8
# Created on 2018年11月19日
# @author: 马春苗
# 在指定的画布元素上绘图
from selenium.webdriver.common.action_chains import ActionChains

def paintoper(self,canvas):
    wd = self.wd
    source = canvas
    action = ActionChains(wd)
    action.click_and_hold(source).move_by_offset(10, 50).move_by_offset(50, 10).move_by_offset(-10, -50).move_by_offset(
        -50, -10).release().perform();
