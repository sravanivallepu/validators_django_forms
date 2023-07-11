from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse
def sf(request):
    SFO=StudentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            return HttpResponse(str(SFD.cleaned_data))
        else:
            return HttpResponse('Invalid data')
    return render(request,'sf.html',d)