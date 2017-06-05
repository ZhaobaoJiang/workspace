from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from app02 import models

# Create your views here.

def index(request):
    
    return HttpResponse('index')
    
