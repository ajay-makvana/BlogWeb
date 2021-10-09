from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.
from django.urls import reverse
from django.utils.text import slugify

STATUS = ((0,"Draft"),(1,"Publish"))

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100,unique=True)
    content = RichTextField()
    #content = models.TextField()
    slug = models.SlugField(max_length=100,unique=True,help_text="add your blog slug means short url")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)
    status = models.IntegerField(choices=STATUS,default=0)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    # views field for count views on blog post
    total_views = models.IntegerField(default=0)
    likes = models.ManyToManyField(User,related_name='like')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    postid = models.ForeignKey(Post,on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content[0:30] + "... by " + self.user.username



