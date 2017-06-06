#!/usr/bin/env python2.7
#coding:utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.http.response import HttpResponse
from app01 import models
# Create your views here.

def login(request):
    ret = {'status':''}
    if request.method == "POST":
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        is_empty = all([username,password])
        if is_empty:
            count = models.UserInfo.objects.filter(username=username,password=password).count()
            if count == 1:
                return redirect('/app01/index/')
            else:
                ret['status'] = '用户名或密码错误'
        else:
            ret['status'] = '用户名或密码不能为空'
        
    return render_to_response('app01/login.html',ret)
def register(request):
    t1 = models.UserType.objects.create(name="超级管理员")
    t2 = models.UserType.objects.create(name="普通管理员")
    u1 = models.UserInfo.objects.create(
                                        username="alex",
                                        password="123",
                                        email="1@qq.com",
                                        user_type=t1
                                        )
    u2 = models.UserInfo.objects.create(
                                        username="tom",
                                        password="123",
                                        email="2@qq.com",
                                        user_type=t2
                                        )
    groupObjA = models.UserGroup.objects.create(GroupName='主机A')
    groupObjB = models.UserGroup.objects.create(GroupName='主机B')
    
    groupObjA.user.add(u1)
    groupObjB.user.add(u1)
    return HttpResponse("注册成功！")
    
    
def index(request):
    return render_to_response('app01/index.html')

def host(request):
    ret = {'status':'','data':None,'group':None}
    usergroup = models.UserGroup.objects.all()
    ret['group'] = usergroup
    if request.method == "POST":
        hostname = request.POST.get('hostname',None)
        ip = request.POST.get('ip',None)
        groupId = request.POST.get('group',None)
        
        is_empty = all([hostname,ip])
        if is_empty:
            groupObj = models.UserGroup.objects.get(id=groupId)
            models.Asset.objects.create(hostname=hostname,
                                        ip=ip,
                                        user_group=groupObj)
        else:
            ret['status'] = "hostname或ip不能为空"    
    data = models.Asset.objects.all()
    ret['data'] = data
    for item in data:
        print item.hostname
        print item.ip
        #挎表取数据
        print item.user_group.GroupName
     
    #跨表查数据   
    obj = models.Asset.objects.filter(user_group__GroupName="用户组A")    
    return render_to_response('app01/host.html',ret)