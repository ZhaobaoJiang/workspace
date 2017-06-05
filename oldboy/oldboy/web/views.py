from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http.response import HttpResponse
from web.models import Asset,UserInfo
# Create your views here.

def index(request):
    return HttpResponse("index")

def login(request,name):
    print name,id
    return HttpResponse('login')

def add(request,name):
    Asset.objects.create(hostname=name)
    return HttpResponse("ok")

def delete(request,id):
    Asset.objects.get(id=id).delete()
    return HttpResponse("ok")

def update(request,id,hostname):
    '''
    obj = Asset.objects.get(id=id)
    obj.hostname = hostname
    obj.save()  
    '''
    
    Asset.objects.filter(id__gt=id).update(hostname=hostname)  
    return HttpResponse('ok')

def get(request):
    '''
    obj = Asset.objects.get(id=id)
    obj.hostname = hostname
    obj.save()  
    '''
    alldata = Asset.objects.all().values('id','hostname')
    print alldata.query
    tmp = Asset.objects.all()[0:2]
    print tmp
    
    alldata = Asset.objects.all().order_by("-id")
    return HttpResponse(alldata)

def AssetList(request):
    asset_list = Asset.objects.all()
    return render_to_response('assetlist.html',{'data':asset_list,'user':'alex'})

def login(request):
    if request.method == "POST":
        user = request.POST.get('username',None)
        pwd = request.POST.get('password',None)
        print user,pwd
        result = UserInfo.objects.filter(username=user,password=pwd).count()
        if result == 1:
            return HttpResponse('login ok!')
        else:
            return render_to_response('login.html',{'status':'username/password error!'})
    else:
        return render_to_response('login.html')


def register(request):
    if request.method == "POST":
        user = request.POST.get('username',None)
        pwd = request.POST.get('password',None)
        print user,pwd
        result = UserInfo.objects.filter(username=user,password=pwd).count()
        if result == 1:
            return HttpResponse('login ok!')
        else:
            return render_to_response('login.html',{'status':'username/password error!'})
    else:
        return render_to_response('login.html')
