from django.urls import path

from . import views

urlpatterns = [
    path('news/<int:news_id>/', views.news_page, name='news_page'),
    path('', views.main_page, name='main_page'),
    path('comments', views.comments, name='comments'),
    path('likes', views.likes, name='likes'),
    path('delete_like', views.delete_like, name='delete_like'),


]