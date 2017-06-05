from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http.response import HttpResponse 
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
    return render_to_response('contact.html')

def customer(request):
    return render_to_response('customer.html')
    