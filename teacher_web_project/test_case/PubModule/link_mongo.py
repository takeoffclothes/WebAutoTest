#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymongo
import datetime


def link_mongo(coll_name):
    # 建立连接
    client = pymongo.MongoClient(host='47.93.21.81', port=2017)
    db = client['whadmin']
    #认证用户名密码
    db.authenticate("whadmin","Whdxmongodb_2017")
    #或者 db = client.example
    # 选择集合（mongo中collection和database都是延时创建的）
    coll = db[coll_name]
    return coll

def insert_multi_docs(coll,bak_data):
    # 批量插入documents,插入一个数组
    #information = [{"name": "xiaoming", "age": "25"}, {"name": "xiaoqiang", "age": "24"}]
    try:
        for i in range(0, len(bak_data)):
            coll.insert(bak_data[i])
    except Exception:
        return False
    else:
        return True
    #print information_id

def select_many_docs(coll,select_sql):
    # mongo中提供了过滤查找的方法，可以通过各种条件筛选来获取数据集，还可以对数据进行计数，排序等处理
    #coll = db['PaperSnapshotDataAutoTestBak']
    #ASCENDING = 1 升序;DESCENDING = -1降序;default is ASCENDING
    #for item in coll.find().sort("age", pymongo.DESCENDING):
    #    print item
    item = []
    for i in coll.find(select_sql):
        item.append(i)
        #print item
    return item

def get_counts(coll,select_sql):
    #count = coll.count(select_sql)
    #print "集合符合条件的数据共 %s个" % int(count)
    #条件查询
    count = coll.find({select_sql}).count()
    print "集合符合条件的数据共 %s个" % int(count)

def delete_datas(coll,select_sql):
    try:
        #删除数据
        coll.remove(select_sql)
    except Exception:
        return False
    else:
        return True

if __name__ == '__main__':
    
    mon_select_str_sql = "{\"paperAssignIds\":\"69ccf1f9dead4492b49ff1b11b0e62bb\"}"
    print mon_select_str_sql
    #将字符串类型转换为字典类型
    mon_select_list_sql = eval(mon_select_str_sql)
    print mon_select_list_sql
    my_collection = link_mongo("PaperSnapshotData")
    bak_data = select_many_docs(my_collection,mon_select_list_sql)

    my_collection = link_mongo("PaperSnapshotDataAutoTestBak")
    insert_multi_docs(my_collection,bak_data)
    delete_datas(my_collection,mon_select_list_sql)
    
