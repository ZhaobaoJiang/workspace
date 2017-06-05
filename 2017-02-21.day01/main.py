#!/usr/bin/env python2.7
#coding:utf-8
#create date: 2017-02-21
#author: jiang.zhaobao
#function: user login and register.

import os
print "===================welcome==================="

#打开被锁定的用户文件
#file_lock = file("lock.txt","r+")
#file_user = file("user.txt","r")

#检查用户是否被锁定
def lock_user():
    file_lock = file("lock.txt","r+")
    for line in file_lock.readlines():
        if user_name == line.strip():
            file_lock.close()
            return 1
        else:
            file_lock.close()
            return 0

#检查用户名密码是否正确
def check_user():
    file_user = file("user.txt","r")
    for line in file_user.readlines():
        msg = line.strip().split()
        if user_name == msg[0] and password == msg[1]:
            print "login sucess."
            file_user.close()
            break
        else:
            "username or password error."
            file_user.close()

if __name__ == "__main__":
    while True:
        user_name = raw_input("USERNAME:")
        res = lock_user()
        print res
        if res == 0:
            password = raw_input("PASSWORD:")
            check_user()
        else:
            print "You have been locked." 
            
