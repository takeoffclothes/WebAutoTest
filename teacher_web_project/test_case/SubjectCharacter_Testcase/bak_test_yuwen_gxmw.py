#coding=utf-8
'''
Created on 2017年8月26日
updated on 2017年9月5日
五好导学网-教师web端-班级管理 自动化测试脚本
@author: 房立信
'''

from selenium import webdriver
import sys
#import os
#sys.path.append('\PubModule')
from test_case.PubModule import login
from test_case.PubModule import logout
from test_case.PubModule import topmenu_t
from test_case.PubModule import link_db
from test_case.PubModule import link_mongo
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

class test_yuwen_gxmw(unittest.TestCase):
    '''语文老师-国学美文'''
    def setUp(self):
        #定义浏览器下载配置
        #profile = webdriver.FirefoxProfile("F:\\Firefoxprofile\\lem0g08f.selenium")  
        #定义浏览器，打开测试网站        
        #self.wd=webdriver.Firefox(profile)
        self.wd=webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.wd.get("http://www.wuhaodaoxue.com")
        #脚本运行时，错误的信息将被打印到这个列表中。
        self.verificationErrors = []
        #是否继续接受下一下警告
        self.accept_next_alert = True
        wd = self.wd
        wd.maximize_window()
        #登录
        login.login(self,"17200000071", "1qaz@WSX")
        #检查是否登录成功
        if not (len(wd.find_elements_by_id("User")) != 0):
            print(u"FAILED-登录失败！")


    def test_yuwen_gxmw_mw(self):
        '''语文-国学美文-美文'''
        print u"开始测试！语文-国学美文-美文"
        wd = self.wd
        success = True
        
        #进入美文
        topmenu_t.top_menu_mw(self)
        #验证美文页面
        if not ("美文" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-美文初始化失败")
        else:
            print(u"PASS-美文初始化成功")
        
        #切换窗口进入文章详情页面
        #多窗口操作开始
        #print wd.window_handles
        #获得当前窗口句柄
        articlelistpage_window = wd.current_window_handle
        #点击文章
        wd.find_element_by_xpath("//ul[@id='c_Content']//span[.='江南的冬景']").click()
        time.sleep(2) 
        #获得当前所有打开的窗口的句柄
        all_handles = wd.window_handles
        #进入江南的冬景页面
        for handle in all_handles:
            if handle != articlelistpage_window:
                #print wd.title
                wd.switch_to_window(handle)
                
                #开始测试推荐文章
                #1、获取文章ID
                #获取当前页面URL
                now_url = wd.current_url
                #两次截取，获得资源编码，[1]代表切割右边部分，如果是[0]代表切割左边部分
                article_id = now_url.split('html?id=')[1]
                #点击推荐
                wd.find_element_by_xpath("//input[@id='c_Recommend']").click()
                #2、获取隐藏标签内的值
                element1 = wd.find_element_by_xpath("//article/div[2]/div[3]/div/ul/li[3]/span[2]")
                final_class_id = element1.get_attribute("textContent")
                #点击班级
                wd.find_element_by_xpath("//article/div[2]/div[3]/div/ul/li[3]/span[1]").click()
                #点击确定推荐
                wd.find_element_by_xpath("//article/div[2]/div[3]/div/input[1]").click()
                time.sleep(0.5)
                if not ("推荐成功" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print(u"FAILED-推荐失败")
                else:
                    print(u"PASS-推荐成功")
                
                
                #开始测试分享文章
                #点击分享按钮
                wd.find_element_by_xpath("//article/div[2]/div[2]/div/div[4]/p").click()
                if not ("分享给好友" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print(u"FAILED-分享给好友对话框打开失败")
                else:
                    print(u"PASS-分享给好友对话框打开！")

                #获取老页面的窗口句柄
                oldpage_window = wd.current_window_handle
                #print oldpage_window
                time.sleep(1)
                #分享至QQ好友
                wd.find_element_by_css_selector("a.bds_sqq").click()
                #等待3秒钟
                time.sleep(3)
                #切换页面，验证新页面，关闭新页面
                all_handles = wd.window_handles
                #print all_handles
                for handle in all_handles:
                    if handle != oldpage_window and handle != articlelistpage_window:
                        #print wd.title
                        wd.switch_to_window(handle) 
                        #print handle
                        time.sleep(1)
                        #frame = wd.find_element_by_xpath(".//*[@id='login']")
                        try:
                            #切入iframe对话框
                            wd.switch_to_frame("login_frame")
                        except Exception:
                            print (u"FAILED-没有打开发送给QQ好友对话框")
                        else:
                            #关闭登录对话框
                            wd.find_element_by_xpath("//div[@class='header']/a").click()
                            #切回原页面
                            wd.switch_to_default_content()
                            #判断title是否完全等于“发给QQ好友和群组”
                            title1 = EC.title_is(u"发送给QQ好友和群组")
                            if title1(wd) != "发送给QQ好友和群组":
                                print (u"FAILED-没有打开发送给QQ好友对话框")
                            else:
                                print (u"PASS-验证QQ邀请页面成功")
    
                        wd.close()
                        # 判断title包含
                        #title2 = EC.title_contains(u'QQ好友')
                        #print title2(wd)
                        #wd.close()
                        wd.switch_to_window(oldpage_window)
        
                #获取老页面的窗口句柄
                oldpage_window = wd.current_window_handle
                #分享至QQ空间
                wd.find_element_by_css_selector("a.bds_qzone").click()
                time.sleep(3)
                all_handles = wd.window_handles
                for handle2 in all_handles:
                    if handle2 != oldpage_window and handle2 != articlelistpage_window:
                        wd.switch_to_window(handle2)
                        # 判断title包含
                        title2 = EC.title_contains(u'QQ空间')
                        if title2(wd) != u"QQ空间":
                            print (u"FAILED-分享QQ空间页面跳转失败")
                        else:
                            print (u"PASS-分享QQ空间页面跳转成功")
                        wd.close()
                        wd.switch_to_window(oldpage_window)
                #获取老页面的窗口句柄
                oldpage_window = wd.current_window_handle
                #分享至新浪微博
                wd.find_element_by_css_selector("a.bds_tsina").click()
                time.sleep(3)
                all_handles = wd.window_handles
                for handle3 in all_handles:
                    if handle3 != oldpage_window and handle3 != articlelistpage_window:
                        wd.switch_to_window(handle3)
                        # 判断title包含
                        title2 = EC.title_contains(u'微博')
                        if title2(wd) != u"微博":
                            print (u"FAILED-分享到新浪微博页面跳转失败")
                        else:
                            print (u"PASS-分享到新浪微博页面跳转成功")
                        wd.close()
                        wd.switch_to_window(oldpage_window)
                #分享至微信
                wd.find_element_by_css_selector("a.bds_weixin").click()
                if not ("分享到微信朋友圈" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print (u"FAILED-分享到微信朋友圈弹框失败")
                else:
                    print (u"PASS-分享到微信朋友圈弹框成功")
                #关闭微信分享窗口
                wd.find_element_by_link_text("×").click()
                #关闭分享窗口
                wd.find_element_by_id("ShareClose").click()
                
                if not ("江南的冬景" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print(u"FAILED-文章江南的冬景展示失败")
                else:
                    print(u"PASS-文章江南的冬景展示成功")
                #print wd.window_handles
                #wd.find_element_by_xpath(".//*[@id='moveDiv']/span[2]").click()
                wd.close()
                #print wd.window_handles
                wd.switch_to_window(articlelistpage_window)
                #print wd.window_handles
                #print wd.title
        
        ######下面还原数据库推荐文章数据##########################################
        #3、获取完相关ID后，链接数据库
        link_db.link_db(self)
        #final_class_id = '9692388d61c04e3ebe54b9e14201e5cc'
        #article_id = '3f22efcffaa549bc86536b2c4861c2d5'
        
        #4、组装统计结果sql、查询sql,判断如果查询出结果是1条，且查询的时间与系统当前时间相差不超过1分钟的，执行备份sql，删除sql，否则打印：删除试卷不成功。
        count_sql = "SELECT count(*) FROM res_paper_assign t WHERE t.`class_id` = '"+final_class_id+"' AND t.type LIKE '40%' AND t.`paper_res_id` = '"+article_id+"' AND t.`user_id` = (SELECT id FROM user_info a WHERE a.`mobile` = '17200000071') ORDER BY t.`assign_time` DESC;"
        #print count_sql
        select_sql = "SELECT * FROM res_paper_assign t WHERE t.`class_id` = '"+final_class_id+"' AND t.type LIKE '40%' AND t.`paper_res_id` = '"+article_id+"' AND t.`user_id` = (SELECT id FROM user_info a WHERE a.`mobile` = '17200000071') ORDER BY t.`assign_time` DESC;"
        #print select_sql
        #5、调用执行语句
        count_num = link_db.exec_count(self,count_sql)
        #print count_num
        #获取到布置时间
        ass_time = link_db.exec_select(self,select_sql,"assign_time")
        
        #获取到布置id
        assign_id = link_db.exec_select(self,select_sql,"id")
        #print "布置id",assign_id
        #6、获取当前系统时间
        sys_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
 
        #7、开始逻辑判断，如果统计条数为1条，且时间差不超过60秒，可以进行下面的步骤。
        #time_dif = (sys_time - ass_time).seconds
        #计算时间差
        time_chuo =time.mktime(ass_time.timetuple())  - time.mktime(time.strptime(sys_time, '%Y-%m-%d %H:%M:%S'))
        if count_num == 1:
            if time_chuo < 60:
                #组装备份sql-布置作业记录表
                #bak_sql = "SELECT * FROM res_paper_assign t WHERE t.`class_id` = '"+final_class_id+"' AND t.`type` = '300' AND t.`paper_res_id` = '"+article_id+"' AND t.`user_id` = (SELECT id FROM user_info a WHERE a.`mobile` = '17200000071')  into outfile '/tmp/flx/selenium/res_paper_assign"+sys_final_time+".txt'"
                bak_sql1 = "INSERT INTO res_paper_assign_autotest_bak SELECT * FROM res_paper_assign WHERE id = '"+assign_id+"';"
                #执行备份sql
                bak_result = link_db.exec_bak(self,bak_sql1)
                #print bak_result
                if bak_result:
                    print(u"备份mysql-布置作业记录表成功")
                else:
                    print(u"备份mysql-布置作业记录表失败")
                #组装备份sql-布置对象表
                #bak_sql = "SELECT * FROM res_paper_assign t WHERE t.`class_id` = '"+final_class_id+"' AND t.`type` = '300' AND t.`paper_res_id` = '"+article_id+"' AND t.`user_id` = (SELECT id FROM user_info a WHERE a.`mobile` = '17200000071')  into outfile '/tmp/flx/selenium/res_paper_assign"+sys_final_time+".txt'"
                bak_sql2 = "INSERT INTO res_paper_assign_obj_autotest_bak SELECT * FROM res_paper_assign_obj WHERE assign_id = '"+assign_id+"';"
                #执行备份sql
                bak_result = link_db.exec_bak(self,bak_sql2)
                if bak_result:
                    print(u"备份mysql-布置对象表成功")
                else:
                    print(u"备份mysql-布置对象表失败")
                #print bak_result
                                
                #组装删除sql-布置作业记录表
                del_sql = "DELETE FROM res_paper_assign  WHERE id = '"+assign_id+"';"
                #执行删除sql
                del_result = link_db.exec_del(self,del_sql)
                if del_result:
                    print(u"删除mysql-布置作业记录表数据成功")
                else:
                    print(u"删除mysql-布置作业记录表数据失败")
                #print del_result
                #print "布置作业记录表-删除推荐视频数据成功"
                #组装删除sql-布置对象表
                del_sql = "DELETE FROM res_paper_assign_obj  WHERE assign_id = '"+assign_id+"';"
                #执行删除sql
                del_result = link_db.exec_del(self,del_sql)
                if del_result:
                    print(u"删除mysql-布置对象表数据成功")
                else:
                    print(u"删除mysql-布置对象表数据失败")
                #print del_result
                #print "布置对象表-删除推荐视频数据成功"

                #组装mongo布置试卷用户表备份数据
                mon_select_str_sql =  "{\"resPaperAssignId\":\""+assign_id+"\"}"
                #print mon_select_str_sql
                #将字符串类型转换为字典类型
                mon_select_list_sql = eval(mon_select_str_sql)
                #print mon_select_list_sql
                #查询所有符合条件的布置试卷用户表数据
                my_collection = link_mongo.link_mongo("ResPaperUser")
                bak_data = link_mongo.select_many_docs(my_collection,mon_select_list_sql)
                #备份布置试卷用户表数据
                my_collection = link_mongo.link_mongo("ResPaperUserAutoTestBak")
                result_bak_ResPaper = link_mongo.insert_multi_docs(my_collection,bak_data)
                if result_bak_ResPaper:
                    print(u"mongo-ResPaperUser表-备份推荐视频数据成功")
                else:
                    print(u"mongo-ResPaperUser表-备份推荐视频数据失败")
                    
                #删除原布置试卷用户表数据
                my_collection = link_mongo.link_mongo("ResPaperUser")
                result_del_ResPaper = link_mongo.delete_datas(my_collection,mon_select_list_sql)
                if result_del_ResPaper:
                    print(u"mongo-ResPaperUser表-删除推荐视频数据成功")
                else:
                    print(u"mongo-ResPaperUser表-删除推荐视频数据失败")
                
                #组装mongo试卷快照备份数据
                mon_select_str_sql =  "{\"paperAssignIds\":\""+assign_id+"\"}"
                #print mon_select_str_sql
                #将字符串类型转换为字典类型
                mon_select_list_sql = eval(mon_select_str_sql)
                #print mon_select_list_sql
                #查询所有符合条件的试卷快照数据
                my_collection = link_mongo.link_mongo("PaperSnapshotData")
                bak_data = link_mongo.select_many_docs(my_collection,mon_select_list_sql)
                #备份试卷快照数据
                my_collection = link_mongo.link_mongo("PaperSnapshotDataAutoTestBak")
                result_bak_PaperSnapshot = link_mongo.insert_multi_docs(my_collection,bak_data)
                if result_bak_PaperSnapshot:
                    print(u"mongo-PaperSnapshotData表-备份推荐视频数据成功")
                else:
                    print(u"mongo-PaperSnapshotData表-备份推荐视频数据失败")
                #删除原试卷快照数据
                my_collection = link_mongo.link_mongo("PaperSnapshotData")
                result_del_PaperSnapshot = link_mongo.delete_datas(my_collection,mon_select_list_sql)
                if result_del_PaperSnapshot:
                    print(u"mongo-PaperSnapshotData表-删除推荐视频数据成功")
                else:
                    print(u"mongo-PaperSnapshotData表-删除推荐视频数据失败")
                    
                print (u"数据库数据还原成功！")
            else:
                print"推荐视频作业与当前系统时间差超过60秒，不删除数据"
                #直接退出
        elif count_num ==0:
            print "没有找到待删除数据"
        else:
            print "查询结果有问题，未删除数据"
        count_num = link_db.exec_count(self,count_sql)
        if count_num == 0:
            print "删除成功"
        else:
            print "删除失败"
        #################################################################
        
            
        self.assertTrue(success)
        
    def test_02_gx(self):
        '''语文-国学美文-国学'''
        print u"开始测试！语文-国学美文-国学"
        wd = self.wd
        success = True
        
        #进入国学
        topmenu_t.top_menu_gx(self)
        #验证国学页面
        if not ("国学" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-国学初始化失败")
        else:
            print(u"PASS-国学初始化成功")
        
        #切换窗口进入文章详情页面
        #多窗口操作开始
        #print wd.window_handles
        #获得当前窗口句柄
        articlelistpage_window = wd.current_window_handle
        #点击文章
        wd.find_element_by_xpath(".//*[@id='c_CataList']/li[2]/a/span[1]").click()
        time.sleep(2) 
        #获得当前所有打开的窗口的句柄
        all_handles = wd.window_handles
        #进入《幼学琼林》选读页面
        for handle in all_handles:
            if handle != articlelistpage_window:
                #print wd.title
                wd.switch_to_window(handle)
                #print 'now 《幼学琼林》选读 page!'
                #print wd.title
                if not ("《幼学琼林》选读" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print(u"FAILED-文章《幼学琼林》选读展示失败")
                else:
                    print(u"PASS-文章《幼学琼林》选读展示成功")
                #print wd.window_handles
                #wd.find_element_by_xpath(".//*[@id='moveDiv']/span[2]").click()
                wd.close()
                #print wd.window_handles
                wd.switch_to_window(articlelistpage_window)
                #print wd.window_handles
                #print wd.title
            
        self.assertTrue(success)
        
    def test_03_qk(self):
        '''语文-国学美文-期刊'''
        print u"开始测试！语文-国学美文-期刊"
        wd = self.wd
        success = True
        
        #进入期刊
        topmenu_t.top_menu_qk(self)
        #验证期刊页面
        if not ("期刊" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-期刊初始化失败")
        else:
            print(u"PASS-期刊初始化成功")
        
        #切换窗口进入文章详情页面
        #多窗口操作开始
        #print wd.window_handles
        #获得当前窗口句柄
        articlelistpage_window = wd.current_window_handle
        
        #定位到期刊图片        
        article = wd.find_element_by_xpath(".//*[@id='img_New']")  
        #鼠标悬浮在期刊图片上方
        ActionChains(wd).move_to_element(article).perform()
        #等待3秒
        time.sleep(1)
        #定位到五年真题元素
        mouse = wd.find_element_by_xpath(".//*[@id='c_MenuList']/li[3]/a")  
        #鼠标移动至五年真题上方悬浮
        ActionChains(wd).move_to_element(mouse).perform()
        time.sleep(1)
        #点击文章
        wd.find_element_by_xpath(".//*[@id='c_MenuList']/li[3]/a").click()
        time.sleep(1) 
        #获得当前所有打开的窗口的句柄
        all_handles = wd.window_handles
        #进入爱在心里页面
        for handle in all_handles:
            if handle != articlelistpage_window:
                #print wd.title
                wd.switch_to_window(handle)
                #print 'now 爱在心里 page!'
                #print wd.title
                if not ("爱在心里" in wd.find_element_by_tag_name("html").text):
                    success = False
                    print(u"FAILED-文章爱在心里展示失败")
                else:
                    print(u"PASS-文章爱在心里展示成功")
                #print wd.window_handles
                #wd.find_element_by_xpath(".//*[@id='moveDiv']/span[2]").click()
                wd.close()
                #print wd.window_handles
                wd.switch_to_window(articlelistpage_window)
                #print wd.window_handles
                #print wd.title
        
        self.assertTrue(success)
    
    def tearDown(self):
        logout.logout(self)
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()

        