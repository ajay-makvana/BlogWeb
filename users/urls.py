from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'users'

urlpatterns = [
    # Login Page
    path('login/',views.login,name='login'),
    # Registration page.
    path('signup/', views.signup, name='signup'),
    #Logout Page
    path('logout/', views.logout, name='logout'),
    #User Home Page
    path('home/', views.home, name='home'),
    #New Article
    path('new-article/', views.newArticle, name='newArticle'),
    #User's Own Article
    path('my-articles/', views.userAllArticles, name='userAllArticles'),
    #Comment
    path('<str:slugOfArticle>', views.comment, name='comment'),
    #User's Specific Article
    path('my-articles/<str:slugOfArticle>', views.specific_article, name='specific_article'),
    #EditArticles
    path('my-articles/edit/<str:slugOfArticle>', views.editArticle, name='editArticle'),
]