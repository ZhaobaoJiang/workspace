from django.shortcuts import render
from django.shortcuts import render_to_response
from app03 import forms

# Create your views here.

def index(request):
    obj = forms.Alogin()
    ret = {'data':None,'error':""}
    ret['data'] = obj
    if request.method == 'POST':
        checkForm = forms.Alogin(request.POST)
        checkResult = checkForm.is_valid()
         
        if checkResult:
            pass
        else:
            errorObj = checkForm.errors
            ret['error'] = errorObj
            firstErrormsg = checkForm.errors.as_data().values()[0][0].message[0]
            ret['data'] = checkForm
        print checkResult
        print firstErrormsg
        
    #return render_to_response('app03/index.html',{'data':obj,'error':errorObj})
    return render_to_response('app03/index.html',ret)

