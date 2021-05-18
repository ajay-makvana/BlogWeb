from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.contrib import messages
from blog.models import Post,Comment
from users.forms import PostForm,CommentForm

# Create your views here.

def signup(request):
    if request.method == 'POST':
        print(request.POST)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'UserName Already Taken')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Registered')
            else:
                new_user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
                new_user.save()
                print(new_user)
                auth.login(request, new_user)
                return redirect('home:index')
        else:
            messages.info(request,'Password Not Matched')

    return render(request,'users/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("home:index")
        else:
            messages.info(request,'Invalid Username or Password')
    return render(request,'users/login.html')

def logout(request):
    auth.logout(request)
    return redirect("home:index")

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

@login_required(login_url= 'users:login')
def comment(request,slugOfArticle):
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.postid = Post.objects.filter(slug=slugOfArticle)[0]
            new_comment.save()
            return redirect('blog:article',slugOfArticle)
        else:
            messages.info(request,'Plase all add details carefull there is error')
            return redirect('blog:article',slugOfArticle,{'form':form})
