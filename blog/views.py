from django.shortcuts import render
from .models import Post,Comment
from users.forms import CommentForm
from django.contrib.auth.decorators import login_required

def blog(request):
    allBlogPost = Post.objects.filter(status=1).order_by('-created_on')
    blogposts = {'blogposts':allBlogPost}
    return render(request,'blog/blog.html',blogposts)

def article(request,slugOfArticle):
    if request.method == "POST":
        pass
    else:
        article = Post.objects.filter(slug=slugOfArticle)
        form = CommentForm()
        comments = Comment.objects.filter(postid=article[0].id).order_by('-created_on')
        context = {'post':article[0],'comments':comments,'form':form}
        return render(request,'blog/article.html',context)