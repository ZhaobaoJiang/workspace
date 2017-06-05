#!/usr/bin/env python2.7
#coding:utf-8
'''
   @author:jiang.zhaobao
'''
from user_info import *

if __name__ == "__main__":
    res_login = user_login()
    if res_login == 0:
        user_action_select()
    else:
        pass