from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('',            views.article_list, name='homepage'),
    path('create/', views.article_create, name='article_create'),
    path('<slug:slug>/', views.article_item, name='article_detail'),
]
