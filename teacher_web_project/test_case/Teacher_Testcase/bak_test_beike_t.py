#coding=utf-8
'''
Created on 2017年8月18日
updated on 2017年8月30日 - 优化脚本输出及函数
updated on 2017年9月12日 - 添加视频推荐班级的数据库处理、课件点赞的数据库处理
五好导学网-教师web端-班级管理 自动化测试脚本
@author: 房立信
'''

from selenium import webdriver
import sys
#from robotide.widgets import dialog
#from pip._vendor.pkg_resources import msg
sys.path.append('\PubModule')
from test_case.PubModule import login
from test_case.PubModule import logout
from test_case.PubModule import topmenu_t
from test_case.PubModule import link_db
from test_case.PubModule import link_mongo
#from selenium.webdriver.firefox.webdriver import WebDriver
#from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time, unittest,os,datetime
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

#对异常弹窗的处理
def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_beike_t(unittest.TestCase):
    '''教师pc端-备课中心模块测试'''
    def setUp(self):
        #os.system("D:\\selenium_upfile\\changeprofile.bat")
        #定义浏览器下载配置
        profile = webdriver.FirefoxProfile("C:\\Users\\Administrator\\Application Data\\Mozilla\\Firefox\\Profiles\\nce5v0dx.default")  
        #关闭flash自动检查是否最新版本
        profile.set_preference("extensions.blocklist.enabled", "false")
        #激活flash插件
        profile.set_preference("plugin.state.flash", 2)
        #定义浏览器，打开测试网站
        self.wd=webdriver.Firefox(profile)
        self.wd.implicitly_wait(30)
        self.wd.get("http://www.wuhaodaoxue.com")
        #脚本运行时，错误的信息将被打印到这个列表中。
        self.verificationErrors = []
        #是否继续接受下一下警告
        self.accept_next_alert = True
        self.wd.maximize_window()

        wd = self.wd
        #登录
        login.login(self,"17200000071", "1qaz@WSX")
        #检查是否登录成功
        if not (len(wd.find_elements_by_id("User")) != 0):
            print(u"FAILED-登录失败！")
    
    def test_01_bkzxsp(self):
        '''备课中心-视频'''
        print u"开始测试！备课中心-视频"
        wd = self.wd
        success = True

        topmenu_t.top_menu_sp(self)
        if wd.title != "视频":
            success = False
            print(u"FAILED-视频列表页初始化失败")
        else:
            print(u"PASS-视频列表页初始化成功！")
            
        #点击切换章节目录
        wd.find_element_by_xpath("//article/div/div[2]/div[2]/div[1]/ul/li[1]").click()
        wd.find_element_by_xpath("//article/div/div[2]/div[2]/div[1]/ul/li[2]").click()
        wd.find_element_by_xpath("//article/div/div[2]/div[2]/div[2]/ul/li[2]").click()

        ###########################################
        #数据库操作1、获取页面中的a标签中的url
        element = wd.find_element_by_xpath("html/body/article/div/div[2]/div[3]/ul/li/a")
        #print element.get_attribute("href") 
        source_res_id = element.get_attribute("href") 
        #截取两次，获得res_id
        middle_res_id = source_res_id.split("html?id=")[1]
        final_res_id = middle_res_id.split("&categoryId=")[0]
        #print "res_id shi %s",final_res_id
        ###########################################
        
        if not ("6 散步" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-视频筛选验证失败")
        else:
            print(u"PASS-视频筛选验证成功！")
        #进入6散步，视频详情页面
        wd.find_element_by_xpath("//div[@class='videoBox']//p[.='6 散步']").click()
        #判断title是否是"视频播放"
        title = EC.title_is(u"视频播放")
        if title(wd):
            print(u"PASS-进入视频详情页成功！")
        else:
            print(u"FAILED-进入视频详情页失败！")
        
        if not ("6 散步" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-视频详情页初始化失败")
        else:
            print(u"PASS-视频详情页初始化成功！")
        time.sleep(1)  
        #调用 shipin.exe 测试视频操作
        os.system("D:\\selenium_upfile\\shipin_t.exe")
        print (u"Warning-视频播放完成，暂时无好办法检验！")

        time.sleep(2)
        
        #点击分享按钮
        wd.find_element_by_xpath("//div[@class='functions']/span[5]").click()
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
            if handle != oldpage_window:
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
                    #print wd.title
    
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
            if handle2 != oldpage_window:
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
            if handle3 != oldpage_window:
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

        #点击推荐按钮
        wd.find_element_by_id("recommend").click()
        time.sleep(1)
        ##########################################################
        #2、获取隐藏标签内的值
        element1 = wd.find_element_by_xpath("//article/div/div[2]/div[4]/div[1]/ul/li[3]/span[2]")
        final_class_id = element1.get_attribute("textContent")
        #print "class_id 是 %s",final_class_id
        ##########################################################
        #点击班级
        wd.find_element_by_xpath("//article/div/div[2]/div[4]/div[1]/ul/li[3]/span[1]").click()
        #输入备注信息
        wd.find_element_by_xpath(".//*[@id='c_Remark']").click()
        wd.find_element_by_xpath(".//*[@id='c_Remark']").clear()
        wd.find_element_by_xpath(".//*[@id='c_Remark']").send_keys(u"自动化测试推荐视频")
        #点击确定按钮
        wd.find_element_by_xpath(".//*[@id='c_RefBtn0']").click()

        ##############下面是数据库还原数据##################################
        #3、获取完相关ID后，链接数据库
        link_db.link_db(self)
        #final_class_id = '9692388d61c04e3ebe54b9e14201e5cc'
        #final_res_id = '3f22efcffaa549bc86536b2c4861c2d5'
        
        #4、组装统计结果sql、查询sql,判断如果查询出结果是1条，且查询的时间与系统当前时间相差不超过1分钟的，执行备份sql，删除sql，否则打印：删除试卷不成功。
        count_sql = "SELECT count(*) FROM res_paper_assign t WHERE t.`class_id` = '"+final_class_id+"' AND t.`type` = '300' AND t.`paper_res_id` = '"+final_res_id+"' AND t.`user_id` = (SELECT id FROM user_info a WHERE a.`mobile` = '17200000071') ORDER BY t.`assign_time` DESC;"
        #print count_sql
        select_sql = "SELECT * FROM res_paper_assign t WHERE t.`class_id` = '"+final_class_id+"' AND t.`type` = '300' AND t.`paper_res_id` = '"+final_res_id+"' AND t.`user_id` = (SELECT id FROM user_info a WHERE a.`mobile` = '17200000071') ORDER BY t.`assign_time` DESC;"
        #print select_sql
        #5、调用执行语句
        count_num = link_db.exec_count(self,count_sql)
        #print count_num
        ass_time = link_db.exec_select(self,select_sql,"assign_time")
        #print "布置时间为"
        #print ass_time,type(ass_time)
        #print "布置时间戳为"
        #print time.mktime(ass_time.timetuple())
        
        #获取到布置id
        assign_id = link_db.exec_select(self,select_sql,"id")
        #print "布置id",assign_id
        #6、获取当前系统时间
        sys_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        #print "系统时间为："
        #print sys_time,type(sys_time)
        #print "系统时间戳为"
        #print time.mktime(time.strptime(sys_time, '%Y-%m-%d %H:%M:%S'))

        #7、开始逻辑判断，如果统计条数为1条，且时间差不超过60秒，可以进行下面的步骤。
        #
        #time_dif = (sys_time - ass_time).seconds
        time_chuo =time.mktime(ass_time.timetuple())  - time.mktime(time.strptime(sys_time, '%Y-%m-%d %H:%M:%S'))
        #print sys_time - ass_time
        #print ccc.seconds
        #print time_dif
        #print time_chuo
        if count_num == 1:
            if time_chuo < 60:
                #组装备份sql-布置作业记录表
                #bak_sql = "SELECT * FROM res_paper_assign t WHERE t.`class_id` = '"+final_class_id+"' AND t.`type` = '300' AND t.`paper_res_id` = '"+final_res_id+"' AND t.`user_id` = (SELECT id FROM user_info a WHERE a.`mobile` = '17200000071')  into outfile '/tmp/flx/selenium/res_paper_assign"+sys_final_time+".txt'"
                bak_sql1 = "INSERT INTO res_paper_assign_autotest_bak SELECT * FROM res_paper_assign WHERE id = '"+assign_id+"';"
                #执行备份sql
                bak_result = link_db.exec_bak(self,bak_sql1)
                #print bak_result
                if bak_result:
                    print(u"备份mysql-布置作业记录表成功")
                else:
                    print(u"备份mysql-布置作业记录表失败")
                #组装备份sql-布置对象表
                #bak_sql = "SELECT * FROM res_paper_assign t WHERE t.`class_id` = '"+final_class_id+"' AND t.`type` = '300' AND t.`paper_res_id` = '"+final_res_id+"' AND t.`user_id` = (SELECT id FROM user_info a WHERE a.`mobile` = '17200000071')  into outfile '/tmp/flx/selenium/res_paper_assign"+sys_final_time+".txt'"
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
        
    def test_02_bkzxyp(self):
        '''备课中心-音频'''
        print u"开始测试！备课中心-音频"
        wd = self.wd
        success = True

        topmenu_t.top_menu_yp(self)
        if not ("音频" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-音频列表页初始化失败")
        else:
            print(u"PASS-音频列表页初始化成功！")        
        #点击第三单元    
        wd.find_element_by_id("daecadad4eba4d579b43b9bb5097a18f").click()
        #点击第10课
        wd.find_element_by_id("2f754d1cd9954960b4a768ec91916fc9").click()
        if not ("10.再塑生命的人" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-音频筛选验证失败")
        else:
            print(u"PASS-音频筛选验证成功！")
        #切换第二单元
        wd.find_element_by_id("2e0536cf123449d0a1f893423087300b").click()
        #点击播放
        wd.find_element_by_id("Isplay").click()
        #点击关闭音量
        wd.find_element_by_css_selector("div.ComPlayer-volume-button").click()
        #点击打开音量
        wd.find_element_by_css_selector("div.ComPlayer-volume-button").click()
        #点击暂停
        wd.find_element_by_id("Isplay").click()
        
        print (u"Warning-音频播放完成，暂时无好办法检验！")
        self.assertTrue(success)
    
    def test_03_bkzxkj(self):
        '''备课中心-课件'''
        print u"开始测试！备课中心-课件"
        wd = self.wd
        success = True

        topmenu_t.top_menu_kj(self)
        if wd.title != "课件":
            success = False
            print(u"FAILED-课件列表页初始化失败")
        else:
            print(u"PASS-课件列表页初始化成功！")
            
        #点击第一单元
        wd.find_element_by_id("eba02c26d0644e2cb12784f0c8a49604").click()
        #点击第三课
        wd.find_element_by_id("60054a669f5d4835bab14c763b0f1f17").click()
        #点击第四课
        wd.find_element_by_id("d6a6d4bf771349c59160e71b9a5feb51").click()
        #点击第二单元
        wd.find_element_by_id("2e0536cf123449d0a1f893423087300b").click()
        #点击第七课
        wd.find_element_by_id("9c33aba0ac694ab0b867f6026065eb74").click()
        if not ("7 散文诗二首（1）" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-课件筛选验证失败")
        else:
            print(u"PASS-课件筛选验证成功！")
        wd.find_element_by_link_text("7 散文诗二首（1）").click()
        if not ("课件播放" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-课件详情页初始化失败")
        else:
            print(u"PASS-课件详情页初始化成功！")
        #点击下载
        wd.find_element_by_css_selector("button.fr.c_CWDownLoadBtn").click()
        #点击分享
        wd.find_element_by_xpath("//div[@id='p_CWOperationWrap_div']/i").click()
        if not ("分享给好友" in wd.find_element_by_tag_name("html").text):
            success = False
            print(u"FAILED-分享给好友对话框打开失败")
        else:
            print(u"PASS-分享给好友对话框打开！")

        #获取老页面的窗口句柄
        oldpage_window = wd.current_window_handle
        #print oldpage_window
        #分享至QQ好友
        wd.find_element_by_css_selector("a.bds_sqq").click()
        #隐形等待30秒钟
        self.wd.implicitly_wait(30)
        #切换页面，验证新页面，关闭新页面
        all_handles = wd.window_handles
        #print all_handles
        for handle in all_handles:
            if handle != oldpage_window:
                #print wd.title
                wd.switch_to_window(handle) 
                #print handle
                time.sleep(3)
                #frame = wd.find_element_by_xpath(".//*[@id='login']")
                try:
                    wd.refresh()
                    #切入iframe对话框
                    wd.switch_to_frame("login_frame")
                except Exception,msg:
                    #print msg
                    print (u"FAILED-发送给好友控件跳转失败")
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
                    #print wd.title

                # 判断title包含
                #title2 = EC.title_contains(u'QQ好友')
                #print title2(wd)
                wd.close()
                wd.switch_to_window(oldpage_window)
        
        #获取老页面的窗口句柄
        oldpage_window = wd.current_window_handle
        #分享至QQ空间
        wd.find_element_by_css_selector("a.bds_qzone").click()
        time.sleep(3)
        all_handles = wd.window_handles
        for handle2 in all_handles:
            if handle2 != oldpage_window:
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
            if handle3 != oldpage_window:
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

        #下面开始点赞，先获取当前点赞数，点赞，然后再获取一次点赞数。
        old_like_num = wd.find_element_by_xpath(".//*[@id='p_CWOperationWrap_div']/p/span").text
        #print old_like_num
        try:
            #点赞记录
            wd.find_element_by_xpath("//div[@id='p_CWOperationWrap_div']/p/i").click()
        except Exception,msg:
            print msg
        new_like_num = wd.find_element_by_xpath(".//*[@id='p_CWOperationWrap_div']/p/span").text
        #print new_like_num
        if  (old_like_num == new_like_num):
            success = False
            print (u"FAILED-点赞失败")
        else:
            print (u"PASS-点赞成功")
        
        #获取当前页面URL
        now_url = wd.current_url
        #两次截取，获得资源编码，[1]代表切割右边部分，如果是[0]代表切割左边部分
        ppt_id = now_url.split('html?id=')[1]
        #print ppt_id
        #恢复数据库点赞数据
        link_db.link_db(self)
        count_sql = "SELECT count(*) FROM user_praise WHERE obj_id = '"+ppt_id+"' AND user_id = (SELECT id FROM user_info WHERE mobile = '17200000071');"
        #print count_sql
        count_num = link_db.exec_count(self,count_sql)
        #print count_num
        if count_num == 1:
            del_sql = "DELETE FROM user_praise WHERE obj_id = '"+ppt_id+"' AND user_id = (SELECT id FROM user_info WHERE mobile = '17200000071');"
            link_db.exec_del(self,del_sql)
            print u"PASS-数据库点赞数据还原成功"
        else:
            print u"数据异常：发现多个或0个同一用户对同一课件的点赞数据。"
        
        self.assertTrue(success)
    
    def tearDown(self):
        #滚动到最上方
        self.wd.execute_script("window.scrollTo(0, 0);")
        logout.logout(self)
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
