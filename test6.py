#!/usr/bin/python
#coding=utf-8


# 数据库
import MySQLdb

conn = MySQLdb.connect(
        host='101.200.145.47',
        port=3306,
        user='root',
        passwd='liumin110',
        db='liumin2',
        )
cur = conn.cursor()


#cur.execute("insert into sss values(111,'huhu')")

cur.execute("select * from sss")

result = cur.fetchall()

print result
# ((111L, 'huhu'), (223L, '2323'))





cur.close()
conn.commit()
conn.close()


# 学习ROM 框架

# 邮件


