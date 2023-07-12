from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.

def sf(request):
    SFO=studentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        SFD=studentForm(request.POST)
        if SFD.is_valid():
            return HttpResponse('valid data')
        else:
            return HttpResponse('invalid data')

    return render(request,'sf.html',d)

