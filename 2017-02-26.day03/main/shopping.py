#!/usr/bin/env python2.7
#coding:utf-8
'''
   @author:jiang.zhaobao
'''

def show_goods():
    #用户可购买的商品列表
    goods = {"MacBook Air":7000,
             'Iphone':5000,
             'Iwatch':3000,
             'Bike':1699,
             'Cup':30,
             'Swiss army knife':79,
             'Router':109,
             'Bag':399,
             }
    '''格式化输出商品列表'''
    print '''No.  Name                Price'''
    print '''=============================================='''
    for index,item in enumerate(goods,1):
        print "%-5d%-20s%-10d" % (index,item,goods[item])
    print '''=============================================='''
    #提示用户选择商品
    select_goods = raw_input("What do you want to buy!")
    #返回用户选择的商品序号
    return select_goods
show_goods()