#!/usr/bin/env python2.7
#coding:utf-8
from django.shortcuts import render,render_to_response
from django.http.response import HttpResponse
import json
# Create your views here.

def ajax(request):
    
    if request.method == "POST":
        
        print request.POST
        data = {'status':0,'msg':'请求成功','data':[11,22,33]}  
        #return HttpResponse('ok')
        return HttpResponse(json.dumps(data))
    else:
        return render_to_response('app04/ajax.html')