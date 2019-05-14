#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2019/3/29 1:28
# @Auth      :Administrator
# @Site      :
# @File      :connectMysqldb.py
# @SoftWare  :PyCharm Community Edition

import MySQLdb

class connectMysqldb():
    def __init__(self,server,user,passwd,dbName):
        self.server = server
        self.user = user
        self.passwd = passwd
        self.dbName = dbName
        self.db = MySQLdb.connect(self.server,self.user,self.passwd,self.dbName)

    def createdb(self):
        cur = self.db.cursor()
        cur.execute("SELECT VERSION()")
        data = cur.fetchone()

        print "Database version : %s " % data

        # 关闭数据库连接
        self.db.close()

if __name__ == "__main__":
    cn = connectMysqldb('192.168.0.130','root','smile146985','mysql')
    cn.createdb()