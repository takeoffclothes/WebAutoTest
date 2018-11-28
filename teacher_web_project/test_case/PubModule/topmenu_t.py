#coding=utf-8
#from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time

#视频菜单
def top_menu_sp(self):
    wd = self.wd
    #进入视频列表页
    #定位到备课元素        
    article = wd.find_element_by_xpath(".//*[@id='Header']/header/div/nav/ul/li[2]/span")  
    #鼠标悬浮在备课位置
    ActionChains(wd).move_to_element(article).perform()
    #等待2秒
    time.sleep(3)
    #定位到视频元素
    mouse = wd.find_element_by_xpath(".//*[@id='Header']/header/div/nav/ul/li[2]/ul/li[1]/a")  
    #鼠标移动至视频上方悬浮
    ActionChains(wd).move_to_element(mouse).perform()
    time.sleep(1)
    #点击视频
    wd.find_element_by_xpath(".//*[@id='Header']/header/div/nav/ul/li[2]/ul/li[1]/a").click()


#音频菜单
def top_menu_yp(self):
    wd = self.wd
    #进入音频列表页
    #定位到备课元素        
    article = wd.find_element_by_xpath(".//*[@id='Header']/header/div/nav/ul/li[2]/span")  
    #鼠标悬浮在备课位置
    ActionChains(wd).move_to_element(article).perform()
    #等待2秒
    time.sleep(2)
    #定位到音频元素
    mouse = wd.find_element_by_xpath(".//*[@id='Header']/header/div/nav/ul/li[2]/ul/li[2]/a")  
    #鼠标移动至音频上方悬浮
    ActionChains(wd).move_to_element(mouse).perform()
    #点击音频
    wd.find_element_by_xpath(".//*[@id='Header']/header/div/nav/ul/li[2]/ul/li[2]/a").click()


#课件菜单
def top_menu_kj(self):
    wd = self.wd
    #进入课件列表页
    #定位到备课元素        
    article = wd.find_element_by_xpath(".//*[@id='Header']/header/div/nav/ul/li[2]/span")  
    #鼠标悬浮在课件位置
    ActionChains(wd).move_to_element(article).perform()
    #等待3秒
    time.sleep(2)
    #定位到课件元素
    mouse = wd.find_element_by_xpath(".//*[@id='Header']/header/div/nav/ul/li[2]/ul/li[3]/a")  
    #鼠标移动至课件上方悬浮
    ActionChains(wd).move_to_element(mouse).perform()
    #点击课件
    wd.find_element_by_xpath(".//*[@id='Header']/header/div/nav/ul/li[2]/ul/li[3]/a").click()

#布置作业
def top_menu_bzzy(self):
    wd = self.wd
    #进入布置作业
    #定位到作业元素        
    A = wd.find_element_by_xpath("//ul[@class='c_Nav ']/li[4]")
    ActionChains(wd).move_to_element(A).perform()
    time.sleep(1)
    wd.find_element_by_xpath("//ul[@class='c_Nav ']/li[4]/ul/li[1]/a").click()

#批改作业
def top_menu_pgzy(self):
    wd = self.wd
    #进入批改作业
    #定位到作业元素        
    A = wd.find_element_by_xpath("//ul[@class='c_Nav ']/li[4]")
    ActionChains(wd).move_to_element(A).perform()
    time.sleep(1)
    wd.find_element_by_xpath("//ul[@class='c_Nav ']/li[4]/ul/li[3]/a").click()

#作业报告
def top_menu_zybg(self):
    wd = self.wd
    #进入作业报告
    #定位到作业元素        
    A = wd.find_element_by_xpath("//ul[@class='c_Nav ']/li[4]")
    ActionChains(wd).move_to_element(A).perform()
    time.sleep(1)
    wd.find_element_by_xpath("//ul[@class='c_Nav ']/li[4]/ul/li[4]/a").click()

#错题本
def top_menu_ctb(self):
    wd = self.wd
    #进入错题本
    #定位到作业元素        
    A = wd.find_element_by_xpath("//ul[@class='c_Nav ']/li[4]")
    ActionChains(wd).move_to_element(A).perform()
    time.sleep(1)
    wd.find_element_by_xpath("//ul[@class='c_Nav ']/li[4]/ul/li[5]/a").click()

#布置测试
def top_menu_bzcs(self):
    wd = self.wd
    #进入布置测试
    #定位到测试        
    A = wd.find_element_by_xpath("//ul[@class='c_Nav ']/li[4]")
    ActionChains(wd).move_to_element(A).perform()
    time.sleep(1)
    wd.find_element_by_xpath("//ul[@class='c_Nav ']/li[4]/ul/li[2]/a").click()

#作业测试
def top_menu_pgcs(self):
    wd = self.wd
    #进入作业批改
    A = wd.find_element_by_xpath("//ul[@class='c_Nav ']/li[4]")
    ActionChains(wd).move_to_element(A).perform()
    time.sleep(1)
    wd.find_element_by_xpath("//ul[@class='c_Nav ']/li[4]/ul/li[3]/a").click()

#测试报告
def top_menu_csbg(self):
    wd = self.wd
    #进入测试报告
    #定位到测试       
    A = wd.find_element_by_xpath("//ul[@class='c_Nav ']/li[4]")
    ActionChains(wd).move_to_element(A).perform()
    time.sleep(1)
    wd.find_element_by_xpath("//ul[@class='c_Nav ']/li[4]/ul/li[4]/a").click()

#五年真题
def top_menu_wnzt(self):
    wd = self.wd
    #进入五年真题
    #定位到试题     
    A = wd.find_element_by_xpath("//ul[@class='c_Nav ']/li[6]")
    ActionChains(wd).move_to_element(A).perform()
    time.sleep(1)
    wd.find_element_by_xpath("//ul[@class='c_Nav ']/li[6]/ul/li[1]/a").click()

#三年模拟
def top_menu_snmn(self):
    wd = self.wd
    #进入三年模拟
    #定位到试题     
    A = wd.find_element_by_xpath("//ul[@class='c_Nav ']/li[6]")
    ActionChains(wd).move_to_element(A).perform()
    time.sleep(1)
    wd.find_element_by_xpath("//ul[@class='c_Nav ']/li[6]/ul/li[2]/a").click()
    
#美文
def top_menu_mw(self):
    wd = self.wd
    #进入美文
    #定位到国学美文       
    A = wd.find_element_by_xpath("//ul[@class='c_Nav ']/li[7]")
    ActionChains(wd).move_to_element(A).perform()
    time.sleep(1)
    wd.find_element_by_xpath("//ul[@class='c_Nav ']/li[7]/ul/li[1]/a").click()
   
#国学
def top_menu_gx(self):
    wd = self.wd
    #进入国学
    #定位到国学美文 
    A = wd.find_element_by_xpath("//ul[@class='c_Nav ']/li[7]")
    ActionChains(wd).move_to_element(A).perform()
    time.sleep(1)
    wd.find_element_by_xpath("//ul[@class='c_Nav ']/li[7]/ul/li[2]/a").click()

#期刊
def top_menu_qk(self):
    wd = self.wd
    #进入期刊
    #定位到国学美文
    A = wd.find_element_by_xpath("//ul[@class='c_Nav ']/li[7]")
    ActionChains(wd).move_to_element(A).perform()
    time.sleep(1)
    wd.find_element_by_xpath("//ul[@class='c_Nav ']/li[7]/ul/li[3]/a").click()

#消息
def top_menu_xx(self):
    wd = self.wd
    #进入消息
    #定位到用户头像       
    article = wd.find_element_by_xpath(".//*[@id='User']")  
    #鼠标悬浮在用户头像位置
    ActionChains(wd).move_to_element(article).perform()
    #等待3秒
    time.sleep(2)
    #定位到消息元素
    mouse = wd.find_element_by_xpath(".//*[@id='menav']/li[1]/a")  
    #鼠标移动至消息上方悬浮
    ActionChains(wd).move_to_element(mouse).perform()
    #点击消息
    wd.find_element_by_xpath(".//*[@id='menav']/li[1]/a").click()

#个人中心
def top_menu_grzx(self):
    wd = self.wd
    #进入个人中心
    #定位到用户头像       
    article = wd.find_element_by_xpath("//img[@id='UserHeadImg']")
    ActionChains(wd).move_to_element(article).perform()
    time.sleep(2)
    #定位到个人中心元素
    wd.find_element_by_xpath("//ul[@id='menav']/li[2]").click()


#学生看视频菜单
def top_menu_ksp_s(self):
    wd = self.wd
    #进入看视频列表页
    #定位到预习中心元素        
    A = wd.find_element_by_xpath("//*[@id='Com_NavMain']/li[2]")
    ActionChains(wd).move_to_element(A).perform()
    time.sleep(1)
    wd.find_element_by_xpath(".//*[@id='Com_NavMain']/li[2]/ul/li[1]/a").click()


#学生听音频菜单
def top_menu_typ_s(self):
    wd = self.wd
    #进入音频列表页
    A = wd.find_element_by_xpath("//*[@id='Com_NavMain']/li[2]")
    ActionChains(wd).move_to_element(A).perform()
    time.sleep(1)
    wd.find_element_by_xpath(".//*[@id='Com_NavMain']/li[2]/ul/li[2]/a").click()


#学生写作业菜单
def top_menu_xzy_s(self):
    wd = self.wd
    #进入写作业页
    # 定位首页作业和测试并点击写作业
    A = wd.find_element_by_xpath("//*[@id='Com_NavMain']/li[3]")
    ActionChains(wd).move_to_element(A).perform()
    time.sleep(1)
    wd.find_element_by_xpath(".//*[@id='Com_NavMain']/li[3]/ul/li[1]/a").click()
    # 判断是否进入写作业列表页面
    if not ("写作业" in wd.find_element_by_tag_name("html").text):
        print("进入写作业列表页面失败！")
    else:
        print("进入写作业列表页面成功！")

#学生看报告菜单
def top_menu_kbg_s(self):
    wd = self.wd
    #进入看报告页面
    #定位到作业与测试元素        
    # 定位首页作业和测试并点击写作业
    A = wd.find_element_by_xpath("//*[@id='Com_NavMain']/li[3]")
    ActionChains(wd).move_to_element(A).perform()
    time.sleep(1)
    wd.find_element_by_xpath(".//*[@id='Com_NavMain']/li[3]/ul/li[2]/a").click()

#学生-国学美文
def top_menu_gxmw_s(self):
    wd = self.wd
    #进入国学美文
    #定位到核心素养元素        
    article = wd.find_element_by_xpath("//span[text()='核心素养']")
    #鼠标悬浮在核心素养位置
    article.click()
    #等待1秒
    time.sleep(1)
    #定位到国学美文元素
    chinese = wd.find_element_by_xpath("//a[text()='国学美文']")
    chinese.click()

#学生-走遍英美
def top_menu_zbym_s(self):
    wd = self.wd
    #进入走遍英美
    #定位到核心素养元素        
    article = wd.find_element_by_xpath("//span[text()='核心素养']")
    #鼠标悬浮在核心素养位置
    article.click()
    #等待1秒
    time.sleep(1)
    #定位到国学美文元素
    english = wd.find_element_by_xpath("//a[text()='走遍英美']")
    english.click()
#学生-数学思维
def top_menu_sxsw_s(self):
    wd = self.wd
    #进入数学思维
    # 定位到核心素养元素
    article = wd.find_element_by_xpath("//span[text()='核心素养']")
    # 鼠标悬浮在核心素养位置
    article.click()
    # 等待1秒
    time.sleep(1)
    # 定位到国学美文元素
    math = wd.find_element_by_xpath("//a[text()='数学思维']")
    math.click()

#学生-必会题
def top_menu_bht_s(self):
    wd = self.wd
    #进入必会题
    #定位到天天刷题       
    article = wd.find_element_by_xpath(".//*[@id='Com_NavMain']/li[5]/span")  
    #鼠标悬浮在天天刷题位置
    ActionChains(wd).move_to_element(article).perform()
    #等待3秒
    time.sleep(2)
    #定位到必会题元素
    mouse = wd.find_element_by_xpath(".//*[@id='Com_NavMain']/li[5]/ul/li[1]/a")  
    #鼠标移动至必会题上方悬浮
    ActionChains(wd).move_to_element(mouse).perform()
    #点击必会题
    wd.find_element_by_xpath(".//*[@id='Com_NavMain']/li[5]/ul/li[1]/a").click()

#学生-必刷题
def top_menu_bst_s(self):
    wd = self.wd
    #进入必刷题
    #定位到天天刷题
    article = wd.find_element_by_xpath(".//*[@id='Com_NavMain']/li[5]/span")  
    #鼠标悬浮在天天刷题位置
    ActionChains(wd).move_to_element(article).perform()
    #等待3秒
    time.sleep(2)
    #定位到必刷题元素
    mouse = wd.find_element_by_xpath(".//*[@id='Com_NavMain']/li[5]/ul/li[2]/a")  
    #鼠标移动至必刷题上方悬浮
    ActionChains(wd).move_to_element(mouse).perform()
    #点击必刷题
    wd.find_element_by_xpath(".//*[@id='Com_NavMain']/li[5]/ul/li[2]/a").click()

#学生-消息
def top_menu_xx_s(self):
    wd = self.wd
    #进入消息
    #定位到用户头像       
    article = wd.find_element_by_xpath(".//*[@id='UserHeadImg']")  
    #鼠标悬浮在用户头像位置
    ActionChains(wd).move_to_element(article).perform()
    #等待3秒
    time.sleep(2)
    #点击消息
    wd.find_element_by_xpath("//a[text()='消息']").click()

#个人中心
def top_menu_grzx_s(self):
    wd = self.wd
    #进入个人中心
    #定位到用户头像       
    article = wd.find_element_by_xpath(".//*[@id='UserHeadImg']")  
    #鼠标悬浮在用户头像位置
    ActionChains(wd).move_to_element(article).perform()
    #等待3秒
    time.sleep(2)
    #定位到个人中心元素
    mouse = wd.find_element_by_xpath(".//*[@id='Com_SignBox']/ul/li[2]/a")  
    #鼠标移动至个人中心上方悬浮
    ActionChains(wd).move_to_element(mouse).perform()
    #点击个人中心
    wd.find_element_by_xpath(".//*[@id='Com_SignBox']/ul/li[2]/a").click()
