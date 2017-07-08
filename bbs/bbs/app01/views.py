from django.shortcuts import render
from django.shortcuts import render_to_response
from app01 import models
from django.shortcuts import HttpResponse
#from app01.extensions import html
#from app01.extensions import global001
import json
from django.core import serializers
from django.db.models.query import QuerySet

# Create your views here.

def index(request):
    
    all_data = models.News.objects.all()
    return render_to_response('index.html',{'data':all_data })

def addfavor(request):
    id = request.POST.get('nid')
    newsObj = models.News.objects.get(id=id)
    temp = newsObj.favor_count + 1
    newsObj.favor_count = temp 
    newsObj.save()
    return HttpResponse(temp)