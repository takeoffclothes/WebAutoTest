import xlrd

def open_excel(file= 'file.xls'):
        try:
                data = xlrd.open_workbook(file)
                return data
        except Exception as e:
                print (str(e))

#����������ȡExcel����е����� ����:file��Excel�ļ�·�� ;colnameindex����ͷ���������е����� ��by_index���������
def excel_table_byindex(file= 'file.xls',colnameindex=0,by_index=0):
        data = open_excel(file)
        table = data.sheets()[by_index]
        nrows = table.nrows #����
        colnames = table.row_values(colnameindex) #ĳһ������ 
        list = []
        for rownum in range(1,nrows):
                row = table.row_values(rownum)
                if row:
                        app = {}
                        for i in range(len(colnames)):
                                app[colnames[i]] = row[i] 
                                list.append(app)
        return list
''' 
#�÷�ʾ��   
def Login():

        listdata = excel_table_byindex("E:\\data.xlsx" , 0)

        if (len(listdata) <= 0 ):
                assert 0 , u"Excel�����쳣"

        for i in range(0 , len(listdata) ):
                browser = webdriver.Firefox()
                browser.get("http://www.effevo.com")
                assert "effevo" in browser.title

                #�����¼��ť
                browser.find_element_by_xpath(".//*[@id='home']/div/div[2]/header/nav/div[3]/ul/li[2]/a").click()
                time.sleep(1)

                browser.find_element_by_id('passname').send_keys(listdata[i]['username'])
                browser.find_element_by_id('password').send_keys(listdata[i]['password'])
                browser.find_element_by_xpath(".//*[@id='content']/div/div[6]/input").click()

                time.sleep(2)
                try:
                        elem = browser.find_element_by_xpath(".//*[@id='ee-header']/div/div/div/ul[2]/li/a/img")
                except NoSuchElementException:
                        assert 0 , u"��¼ʧ�ܣ��Ҳ������Ͻ�ͷ��"
                browser.close()
'''