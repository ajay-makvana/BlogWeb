from django.contrib import admin
from django.urls import path,include
from blog import views

app_name='blog'

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<str:slugOfArticle>', views.article, name='article'),
]
