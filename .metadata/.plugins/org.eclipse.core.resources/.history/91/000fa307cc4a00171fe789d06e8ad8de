#!/usr/bin/env python2.7
#coding:utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from app01 import models
# Create your views here.

def index(request,page):
    #操作数据库进行分页
    page = int(page)
    per_item = 5
    start = (page-1)*5
    end = page*5
    count = models.Host.objects.all()[start:end].count()
    result = models.Host.objects.all()[start:end]
    ret = {'data':result,'count':count}
    return render_to_response('index.html',ret)