from django.contrib import admin,auth
from django.urls import path,include
from . import views

app_name = 'users'

urlpatterns = [
    # User Registration
    path('register/',views.register ,name='register'),
    # User Inbuilt
    path('',include('django.contrib.auth.urls')),
    #User Home Page
    path('home/', views.home, name='home'),
    #New Article
    path('new-article/', views.newArticle, name='newArticle'),
    #User's Own Article
    path('my-articles/', views.userAllArticles, name='userAllArticles'),
    #User's Specific Article
    path('my-articles/<str:slugOfArticle>', views.specific_article, name='specific_article'),
    #EditArticles
    path('my-articles/edit/<str:slugOfArticle>', views.editArticle, name='editArticle'),
    #DeleteArticle
    path('<str:slugOfArticle>', views.deleteArticle, name='deleteArticle'),
]