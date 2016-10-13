#!/usr/bin/python
#coding=utf-8
# Filename: test2.py
# def sayHello():
#     print 'Hello World!' # block belonging to the function
#
# sayHello() # call the function
#
# f = open('H:/11.txt','r')
# print f.read()
# f.close()
#
#
# try:
#     fff = open('H:/11.txt','r')
#     print fff.read()
# finally:
#     if f:
#         f.close()
#
# with open("H:/11.txt",'r') as ff:
#     print ff.read()

# f2 = open('H:/11.txt','r')
# for line in f2.readline():
#     print(line.strip())
# f2.close()
# f3 = open('H:/11.txt', 'w')
# f3.write("huhuhuhu")
# f3.close()

import os
print os.name

# print os.uname() win7 no

print os.environ

print os.getenv('PATH')

print os.path.abspath('.')

# os.path.join('.','sbsb')
# os.mkdir('./sbsb2')
#
# os.rmdir('./sbsb')

# print os.path.split('H:/11.txt')
#
# print os.path.splitext('H:/11.txt')


# os.rename('H:/11.txt','22.txt')
# os.remove('22.txt')

import shutil

print [x for x in os.listdir('.') if os.path.isdir(x)]

print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']



try:
    import cPickle as pickle
except ImportError:
    import pickle


d = dict(anme='liumin',age=11)
print pickle.dumps(d)

f = open("H:/1231.txt",'wb')
pickle.dump(d,f)
f.close()

f = open("H:/1231.txt",'rb')
d = pickle.load(f)
f.close()
print 'result:',d



import json

dd  = dict(name='name',age=23)
print json.dumps(dd) #dump

print '------------------'

json_str = '{"age": 20, "score": 88, "name": "Bob"}'

print  json.loads(json_str) # 序列化字符串的反序列化






