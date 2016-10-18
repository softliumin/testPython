#!/usr/bin/python
#coding=utf-8

import urllib2, cookielib
"""
这是爬虫的起始类
url管理器
网页下载器
requests
urllib2


"""

#创建cookie容器
cj = cookielib.CookieJar()
#创建opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
#安装opener
urllib2.install_opener(opener)
#带cookie访问网页

print '11111111111111111'
response2 = urllib2.urlopen("http://www.baidu.com")
print response2.getcode()






print '22222222222222222222'
request22 =  urllib2.Request("http://www.baidu.com")
request22.add_header("user-agent","Mozilla/5.0")
request222 = urllib2.urlopen(request22)

print request222.getcode()
print '333333333333333333333333333333333'
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3 = urllib2.urlopen("http://www.baidu.com")
#print response3.getcode()
print cj
#print response3.read()
