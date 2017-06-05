#!/usr/bin/env python2.7
#coding:utf-8

def outer(fun):
    def wrapper(arg):
        print "验证"
        res = fun(arg)
        return res
    return wrapper
@outer
def func1(arg):
    print "func1",arg
    return "hello"
    
result = func1("alex")
print result
'''
@outer    
def func1():
    print "func2"
@outer    
def func3():
    print "func3"
    
func1()
func1()
func3()
'''