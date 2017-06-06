#!/usr/bin/env python2.7
#coding:utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http.response import HttpResponse 
import models
# Create your views here.

def login(request):
    return HttpResponse("index")

def index(request):
    return render_to_response('index.html')

def documents(request):
    return render_to_response('documents.html')

def epg(request):
    return render_to_response('epg.html')

def contact(request):
    ret = {'status':'','data':None}
    if request.method == "POST":
        username = request.POST.get('username',None)
        tel = request.POST.get('tel',None)
        email = request.POST.get('email',None)
        address = request.POST.get('address',None)
        
        is_empty = all([username,tel])
        if is_empty:
            models.contact.objects.create(username=username,
                                        tel=tel,
                                        email=email,
                                        address=address)
        else:
            ret['status'] = "联系人或电话不能为空！"    
    data = models.contact.objects.all()
    ret['data'] = data
     
    #跨表查数据   
    return render_to_response('contact.html',ret)

def customer(request):
    return render_to_response('customer.html')
    