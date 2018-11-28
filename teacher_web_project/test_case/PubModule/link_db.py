#!coding:utf-8
#import pymysql
import pymysql.__init__
import pymysql.cursors
'''
Python3之后不再支持MySQLdb的方式进行访问mysql数据库；
可以采用pymysql的方式

连接方式：
    1、导包
        import pymysql
    2、打开数据库连接
        conn = pymysql.connect(host='10.*.*.*',user='root',password='123456',db='self_dev',charset='utf8',cursorclass=pymysql.cursors.DictCursor)
        备注：其中cursorclass=pymysql.cursors.DictCursor 可有可无，配置的是每个字段的展示方式，按照字典的形式进行展示（方便通过列名进行访问），默认元组形式。
    3、使用cursor()方法获取操作游标 
        cur = connection.cursor()
    4、SQL 查询语句
        sql = "SELECT * FROM table t where t.name='政协'"
    5、执行SQL语句
        cur.execute(sql)
    6、获取所有记录列表
        rows = cur.fetchall()
    7、输出

    8、关闭数据库连接
        connection.close()

'''
#class dbClection:
    
def link_db(self):
        self.connection = pymysql.__init__.connect(host='rm-2ze2qfkp1qkzk5691o.mysql.rds.aliyuncs.com',
                                                   port = 3307,
                                                   user='whdxadmin',
                                                   password='Whdx_2017',
                                                   db='whadmin',
                                                   charset='utf8',
                                                   cursorclass=pymysql.cursors.DictCursor)
        
def getOrgid(self):
        cur = self.connection.cursor()

        sql = "SELECT t.id FROM user_info t WHERE t.`mobile` = '18600000071'"
        try:
            cur.execute(sql)
            results = cur.fetchall()

            for row in results:
                org_id = row['id']
                return org_id
                print(org_id)
        except:
            print('Error:unable to fetch data')
        
        cur.close()
        self.connection.close()

def get_assignID(self,user_command,return_field):
        cur = self.connection.cursor()
        
        sql = user_command
        #sql = "SELECT t.password FROM user_info t WHERE t.`mobile` = '18600000071'"
        try:
            cur.execute(sql)
            results = cur.fetchall()

            for row in results:
                org_id = row[return_field]
                return org_id
                #print(row)
        except:
            print('Error:unable to fetch data')
        
        cur.close()
        self.connection.close()
    
def exec_select(self,user_command,return_field):
        cur = self.connection.cursor()
        
        sql = user_command
        #sql = "SELECT t.password FROM user_info t WHERE t.`mobile` = '18600000071'"
        try:
            cur.execute(sql)
            results = cur.fetchall()

            for row in results:
                org_id = row[return_field]
                return org_id
                #print(row)
        except:
            print('Error:unable to fetch data')
        
        cur.close()
        self.connection.close()

def exec_count(self,_sql):
        cur = self.connection.cursor()
        
        sql = _sql
        #sql = "SELECT t.password FROM user_info t WHERE t.`mobile` = '18600000071'"
        try:
            cur.execute(sql)
            results = cur.fetchall()

            for row in results:
                org_id = row["count(*)"]
                return org_id
                #print(row)
        except:
            print('Error:unable to fetch data')
         
        cur.close()
        self.connection.close()
def exec_bak(self,_sql):
        cur = self.connection.cursor()
        
        sql = _sql
        #sql = "SELECT t.password FROM user_info t WHERE t.`mobile` = '18600000071'"
        try:
            cur.execute(sql)
            self.connection.commit()
            return True
        except Exception,msg:
            print msg
            print('Error:备份失败')
            return False
        cur.close()
        self.connection.close()

def exec_del(self,_sql):
        cur = self.connection.cursor()
        
        sql = _sql
        #sql = "SELECT t.password FROM user_info t WHERE t.`mobile` = '18600000071'"
        try:
            cur.execute(sql)
            self.connection.commit()  
            return True
        except Exception,msg:
            print msg
            return False
            #print('Error:删除失败')
        
        cur.close()
        self.connection.close()
'''

#if __name__ == '__main__':
    #db = dbClection()
    #conn = db.link_db()
    #res = db.getOrgid()
    #res=db.getall()
    #print(res)
'''