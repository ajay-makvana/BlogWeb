from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from blog.models import Post

def index(request):
    most3recentadded = Post.objects.filter(status=1).order_by('-created_on')[:3]
    most3liked = Post.objects.filter(status=1).order_by('-likes')[:3]
    context = {'most3recentadded':most3recentadded,'most3liked':most3liked}
    return render(request,'home/index.html',context)