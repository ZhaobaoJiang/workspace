#!/usr/bin/env python2.7
#coding:utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import redirect
# Create your views here.

def login(request):
    if request.method == 'POST':
        user = request.POST.get('username',None)
        pwd = request.POST.get('password',None)

        if user == 'alex' and pwd =='123':
            #request.session['is_login'] = True
            request.session['is_login'] = {'user':user} 
            return redirect('/app02/index/')
        else:
            return render_to_response('app02/login.html/',{'msg':'用户名或密码错误！'})
    return render_to_response('app02/login.html')

def index(request):
    #is_login = request.session.get('is_login',None)
    user_dict = request.session.get('is_login',None)
    if user_dict:
        return render_to_response('app02/index.html',{'username':user_dict['user']})
    else:
        return redirect('/app02/login/')
    
def logout(request):
    #销毁session
    del request.session['is_login']
    return redirect('/app02/login/ ')    
    
    