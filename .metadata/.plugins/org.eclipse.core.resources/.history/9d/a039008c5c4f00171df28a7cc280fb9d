#!/usr/bin/env python2.7
#coding:utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.utils.safestring import mark_safe
from app01 import models
from app01 import common
from app01 import html_helper
# Create your views here.

def index(request,page):
    #操作数据库进行分页
    '''
    page = int(page)
    '''
    print request.COOKIES
    
    page = common.try_int(page,1)
    count = models.Host.objects.all().count()
    
    pageObj = html_helper.PageInfo(page,count,5)
    result = models.Host.objects.all()[pageObj.start:pageObj.end]
    
    page_string = html_helper.Pager(page,pageObj.all_page_count)
    ret = {'data':result,'count':count,'page':page_string}
    
    #return render_to_response('index.html',ret)
    response = render_to_response('index.html',ret)
    response.set_cookie('k1','v1')
    
    return response