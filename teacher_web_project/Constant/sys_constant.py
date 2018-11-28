# -*- coding: utf-8 -*-
'''
Created on 2018年01月29日
自动化测试——常量文件，固定不变的数据维护在此处
@author: 房立信
'''
# constant/sys_constant.py

# 常量部分（固定不变使用频繁的参数维护在此处）
LOGIN_URL = 'http://www.wuhaodaoxue.cn/'

#浏览器配置目录
Firefox_Path = 'C:\\Users\\Administrator\\AppData\\Local\\Mozilla\\Firefox\\Profiles\\pl3wrsan.default'

#测试搜索自动化脚本的相对路径
test_path = '.\\test_case'

#autoIT的路径
autoitfile_path = 'D:\\auto_test\\WebAutoTest\\teacher_web_project\\AutoitFile\\'
#邮件相关配置
#发信邮箱
mail_from_user=u'fanglixin@bcbook.cn'
#收信邮箱
mail_to_user=[u'xiashudong@bcbook.cn',u'wanghaiyong@bcbook.cn',u'dongyunlou@bcbook.cn',u'hanlei@bcbook.cn',u'fanglixin@bcbook.cn',u'machunmiao@bcbook.cn',u'yanshuangshuang@bcbook.cn',u'yanenming@bcbook.cn',u'wangshuai@bcbook.cn']
#抄送邮箱
mail_cc_user=[u'machunmiao@bcbook.cn',u'yanshuangshuang@bcbook.cn',u'yanenming@bcbook.cn',u'wangshuai@bcbook.cn',u'zhangjianshu@bcbook.cn']
#发件人邮箱账号
mail_from_user_id = u'fanglixin@bcbook.cn'
#发件人邮箱密码
mail_from_user_passwd = "bc12345678"
#SMTP 服务器
mail_server = u'mail.bcbook.cn'

#报告相关
#报告文件存放目录
report_path = 'D:\\auto_test\\WebAutoTest\\teacher_web_project\\Report'
#报告标题
report_title = u'五好导学网-AutoTest-Report'
#报告描述
report_description = u'用例执行情况：'

