#!/usr/bin/env python2.7
#coding:utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.utils.safestring import mark_safe
from app01 import models
from app01 import common
# Create your views here.

def index(request,page):
    #操作数据库进行分页
    '''
    page = int(page)
    '''
    page = common.try_int(page,1)
    per_item = 5
    start = (page-1)*per_item
    end = page*per_item
    count = models.Host.objects.all().count()
    result = models.Host.objects.all()[start:end]
    temp = divmod(count, per_item)
    if temp[1] == 0:
        all_page_count = temp[0]
    else:
        all_page_count = temp[0] + 1
    
    page_html = []
    first_html = "<a href='/index/%d'>首页</a>" %(1)
    page_html.append(first_html)
    
    for i in range(all_page_count):
        a_html = "<a href='/index/%d'>%d</a>" %(i+1,i+1)
        page_html.append(a_html)
    
    end_html = "<a href='/index/%d'>尾页</a>" %(all_page_count)
    page_html.append(end_html)
    page = mark_safe(''.join(page_html))
    ret = {'data':result,'count':count,'page':page}
    return render_to_response('index.html',ret)