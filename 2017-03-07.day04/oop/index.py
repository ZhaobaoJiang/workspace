#!/usr/bin/env python2.7
#coding:utf-8
'''
class Province:
    memo = "中国的23个省份之一"
    def __init__(self,name,captial,leader):
        self.Name = name
        self.Captial = captial
        self.Leader = leader
    
    def sport_meet(self):
        print self.Name + "正在开运动会"
        
    @staticmethod
    def foo():
        print "每个省要带头反腐。"
    
    @property
    def bar(self):
        print self.Name
    
    def __call__(self):
        print "hello"        
hb = Province('河北','石家庄','李阳')
sd = Province('山东','济南','Alex')
hb.sport_meet()
hb.foo()
'''

'''
print hb.Name
print hb.memo
print Province.memo
print Province.Leader
'''

class Father(object):
    def __init__(self):
        self.Fname = "ffff"
        
    def Bad(self):
        print "father"
        
class son(Father):
    def __init__(self):
         self.Sname = "ssss"
         
    def bar(self):
        print "son"
    
    def Bad(self):
        Father.Bad(self)
        print "lkasdjfldaf"
        
s = son()
s.bar()
s.Bad()