#!/usr/bin/env python2.7
#coding:utf-8
'''
   @author:jiang.zhaobao
'''
import pickle 
#检查用户登录
def user_login():
    #记录用户输入错误的次数
    count = 0 
    #打开被锁定的用户文件
    user_locked = open("user_locked.txt","a+")
    #打开记录用户名和密码的文件
    user_info_file = open("user_passwd.txt","r")
    while count < 3:
        #提示输入用户名、密码
        user_name = raw_input("username:")
        user_password = raw_input("password:")
        #检查用户是否被锁定,如果被锁定跳出整个循环，否则继续向下执行
        for lock in user_locked.readlines():
            if user_name == lock.strip("\n"):
                break
        #关闭锁定用户的文件
        user_locked.seek(0)
        flag = '' 
        #遍历文件每一行
        for line in user_info_file.readlines():
            #去除换行符“\n”并分割。
            name_pwd = line.strip("\n").split()
            #如果用户名密码匹配则跳出循环，flag = True
            if user_name == name_pwd[0] and user_password == name_pwd[1]:
                flag = True
                return 0
                break
        user_info_file.seek(0) #重新指向文件开头
        
        #用户名密码正确输出并跳出整个循环，否则登录失败次数count+1
        if flag:
            print "============login success==========="
            return 0
        else:
            print "User or password error! You have %d chance!" % (2-count)
            count += 1
        
        #连续输入错误3次，把用户名写入锁定文件
        if count == 3:
            user_locked.write(user_name+"\n")
            return 1
            
# user_login()
#用户登录成功后，提示用户选择具体的操作入口。
def user_action_select():
    #用户的选择行为
    user_select = ["shopping","cash","transfer","reimbursement","query","exit"]
    for index,item in enumerate(user_select,1):
        print index,":",item
    #提示用户选择具体的操作
    select_number = raw_input("Your select No.!")
    #返回用户的选择
    return select_number
        
#user_action_select()
    