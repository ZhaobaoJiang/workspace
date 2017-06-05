#!/usr/bin/env python2.7
#coding:utf-8
import time
import os
import pickle

#此函数用来记录用户的行为
def user_action_record(username,action):
    action_file = file(username+".txt","a")
    action_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    action_file.write(action_time+" "+username+" "+action)
    
user_action_record("tom", "login")