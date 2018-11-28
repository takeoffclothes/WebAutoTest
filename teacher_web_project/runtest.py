# coding:utf-8
import unittest,time,os
from test_case.PubModule import HTMLTestRunner  
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from dis import disco
from Constant.sys_constant import *
#from test_case.Teacher_Testcase import test_shiti
#from test_case.Teacher_Testcase import test_mycenter
#from test_case.Teacher_Testcase import test_shouye
#from test_case.Teacher_Testcase import test_yewei


#=============定义发送邮件==========
def send_mail(file_new):
    '''
    #发信邮箱
    mail_from=u'fanglixin@bcbook.cn'
    #收信邮箱
    mail_to=[u'fanglixin@bcbook.cn',u'1244891537@qq.cn',u'kenan2002flx@qq.com']
    #抄送邮箱
    mail_cc=[u'fanglixin@bcbook.cn',u'1244891537@qq.cn',u'kenan2002flx@qq.com']
    '''
    #发信邮箱
    mail_from=mail_from_user
    #收信邮箱
    mail_to=mail_to_user
    #抄送邮箱
    mail_cc=mail_cc_user
    #定义正文
    f= open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    #构造一个邮件，第一句是普通邮件，第二句是带附件的邮件
    #msg=MIMEText(mail_body,_subtype='html',_charset='utf-8')
    msg = MIMEMultipart()

    #加入附件
    with open(file_new,"rb") as f:
        part = MIMEApplication(f.read(),Name=os.path.basename(file_new))
        msg.attach(part)
    
    msg.attach(MIMEText(mail_body,_subtype='html',_charset='utf-8'))
    
    #定义标题
    msg['Subject']=u'自动化报告'
    msg['From'] = mail_from
    msg['To'] = ';'.join(mail_to)
    msg['CC']= ';'.join(mail_cc)
    #定义发送时间（不定义的可能有的邮件客户端会不显示发送时间）
    msg['date']=time.strftime('%a, %d %b %Y %H:%M:%S %z')
    smtp=smtplib.SMTP()
    #连接 SMTP 服务器，此处用的 公司自己 的 SMTP 服务器
    #smtp.connect(u'mail.bcbook.cn')
    smtp.connect(mail_server)
    #用户名密码
    #smtp.login(u'fanglixin@bcbook.cn',u'bc12345678')
    smtp.login(mail_from_user_id,mail_from_user_passwd)
    smtp.sendmail(mail_from,mail_to,msg.as_string())
    smtp.quit()
    print ('email has send out !')
#======查找测试报告目录，找到最新生成的测试报告文件====
def send_report(testreport):
    result_dir = testreport
    #获取目录下的所有文件
    lists=os.listdir(result_dir)
    #os.path.getmtime：返回在此path下最后一次修改的时间
    #重新按时间对目录下的文件进行排列
    lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn))
    #print (u'最新测试生成的报告： '+lists[-1])
    #找到最新生成的文件
    file_new = os.path.join(result_dir,lists[-1])
    print (file_new)
    #调用发邮件模块
    send_mail(file_new)
#================将用例添加到测试套件===========
def creatsuite():
    #测试套件
    #testunit = unittest.TestSuite()
    #加入测试用例
    #testunit.addTest(test_shiti.test_shiti('test_test_shiti'))
    #testunit.addTest(test_mycenter.test_mycenter('test_test_mycenter'))
    #testunit.addTest(test_shouye.test_shouye('test_test_shouye'))
    #testunit.addTest(test_yewei.test_yewei('test_test_yewei'))
    #return testunit
    
    testunit=unittest.TestSuite()
    #定义测试文件查找的目录
    #test_dir='.\\test_case'
    test_dir= test_path
    #定义 discover 方法的参数
    
    discover=unittest.defaultTestLoader.discover(test_dir,pattern ='test*.py',top_level_dir=None)
    #discover=unittest.defaultTestLoader.discover(test_dir,pattern ='test_login_t.py',top_level_dir=None)
    print (discover)
    #discover 方法筛选出来的用例，循环添加到测试套件中
    #for test_case in discover:
    #    print test_case
    #    testunit.addTests(test_case)
    return discover
    
if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    #testreport = 'D:\\project\\teacher_web_project\\report\\'
    testreport = report_path
    filename = testreport+'\\'+now+'result.html'
    print(filename)
    fp = open(filename, 'wb')
    runner =HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title = report_title,
        description = report_description)
#        title=u'五好导学网-AutoTest-Report',
#        description=u'用例执行情况：')
    alltestnames = creatsuite()
    runner.run(alltestnames)
    fp.close() #关闭生成的报告
    send_report(testreport) #发送报告

    '''    
    #测试套件
    suit1 = unittest.TestSuite()
    #加入测试用例
    suit1.addTest(test_shiti.test_shiti('test_test_shiti'))
    suit1.addTest(test_mycenter.test_mycenter('test_test_mycenter'))
    suit1.addTest(test_shouye.test_shouye('test_test_shouye'))
    suit1.addTest(test_yewei.test_yewei('test_test_yewei'))

if __name__ == "__main__":
    #取前面时间
    now = time.strftime("%Y-%m-%M-%H_%M_%S",time.localtime(time.time())) 
    #定义报告存放位置
    filename = r"F:\selenium_report\{0}result.html".format(now)
    print(filename)
    fp = file(filename,'wb')
     
    #定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream = fp, title = u'百川测试报告', description = u'测试执行情况') 
        
    #runner = unittest.TextTestRunner()
    #运行测试用例
    runner.run(suit1)
    #os.system("D:\\selenium_upfile\\changeprofile.bat")
    #关闭报告文件
    fp.close()  
    '''