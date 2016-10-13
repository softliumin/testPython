#!/usr/bin/python
#coding=utf-8

class People(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_age(self):
        print '%s: %s' % (self.name, self.age)



liumin = People('liumin',22)

liumin.address = 'beijing'

liumin.print_age()

print  liumin.address

# 数据封装


# 访问限制  __ 双下划线的使用

class Car(object):
    def __init__(self, name, money):
        self.__name = name
        self.__money = money
    def print_money(self):
        print '%s : %s' % (self.__name,self.__money)

jieda = Car('jieda',200)

jieda.print_money()

print jieda._Car__name  # 这样可以使用了··但是一般不要使用

# print jieda.__name 直接访问私有属性 报错







# 继承 多态

# 高级面向对象







