from django.urls import path
from . import views

urlpatterns = [
    path('',            views.article_list, name='article_list'),
    path('<slug:slug>/', views.article_item, name='article_detail'),
]
