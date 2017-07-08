#!/usr/bin/env python
#coding:utf-8
'''
Created on Jun 6, 2017

@author: root
'''
 
def try_int(arg,default):
    try:
        arg = int(arg)
    except Exception,e:
        arg = default
    return arg