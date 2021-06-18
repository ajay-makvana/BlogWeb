from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from blog.models import Post,Comment
from users.forms import PostForm,CommentForm

# Create your views here.

def register(request):
    if request.method == 'GET':
        return render(request,'registration/user_register.html')
    else:
        form_user_creation = UserCreationForm(data=request.POST)
        messages.info(request, form_user_creation.errors)
        if form_user_creation.is_valid():
            new_user = form_user_creation.save();
            login(request,new_user)
            return redirect('home:index')
        else:
            form_user_creation = UserCreationForm(data=request.POST)
            return render(request,'registration/user_register.html',{'form_user_creation':form_user_creation})

@login_required(login_url='users:login')
def home(request):
    user = request.user
    blogposts = Post.objects.filter(author=user).order_by('-created_on')
    context = {'blogposts': blogposts}
    return render(request,'users/userHome.html',context)

@login_required(login_url= 'users:login')
def userAllArticles(request):
    user = request.user
    blogposts = Post.objects.filter(author = user).order_by('-created_on')
    context = {'blogposts':blogposts}
    return render(request,'users/userAllArticles.html',context)

@login_required(login_url= 'users:login')
def specific_article(request,slugOfArticle):
    article = Post.objects.filter(slug=slugOfArticle)
    comments = Comment.objects.filter(postid=article[0].id).order_by('-created_on')
    print(article[0].id)
    context = {'post': article[0], 'comments': comments}
    return render(request, 'users/article.html', context)


@login_required(login_url= 'users:login')
def editArticle(request,slugOfArticle):
    article = Post.objects.get(slug=slugOfArticle)
    if request.method == 'POST':
        form = PostForm(instance=article, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:userAllArticles')
    form = PostForm(instance=article)
    return render(request, 'users/editArticle.html',{'form':form,'post':article})


@login_required(login_url= 'users:login')
def newArticle(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_article = form.save(commit=False)
            new_article.author = request.user
            new_article.save()
            return redirect('users:userAllArticles')
        else:
            messages.info(request,'Plase all add details carefull there is error')
            return render(request, 'users/newArticle.html', {'form': form})
    form = PostForm()
    return render(request, 'users/newArticle.html',{'form':form})
