from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    #return HttpResponse('<h1>Okk Google</h1>')
    return render(request,'blog/index.html')