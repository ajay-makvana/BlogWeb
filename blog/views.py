from django.shortcuts import render,redirect
from .models import Post,Comment
from users.forms import CommentForm
from django.contrib.auth.decorators import login_required


def blog(request):
    allBlogPost = Post.objects.filter(status=1).order_by('-created_on')
    blogposts = {'blogposts':allBlogPost}
    return render(request,'blog/blog.html',blogposts)

def article(request,slugOfArticle):
    # added .first() to get only first article of this QuerySet 
    article = Post.objects.filter(slug=slugOfArticle).first()
    article.total_views = article.total_views + 1
    article.save()
    form = CommentForm()
    comments = Comment.objects.filter(postid=article.id).order_by('-created_on')
    context = {'post':article,'comments':comments,'form':form}
    return render(request,'blog/article.html',context)

@login_required(login_url = 'users:login')
def comment(request,slugOfArticle):
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.postid = Post.objects.filter(slug=slugOfArticle)[0]
            new_comment.save()
            return redirect('blog:article', slugOfArticle)
        else:
            messages.info(request,'Plase all add details carefull there is error')
            return render('blog:article',slugOfArticle,{'form':form})
    else:
        article = Post.objects.filter(slug=slugOfArticle)
        form = CommentForm()
        comments = Comment.objects.filter(postid=article[0].id).order_by('-created_on')
        context = {'post':article[0],'comments':comments,'form':form}
        return render(request,'blog/article.html',context)