from django.urls import path
from . import views
from .views import PostDetailView, PostSearchView

urlpatterns = [
    path('', views.home, name='blog_home'),
    path('landing/', views.landing, name='blog_landing'),
    path('create_post/', views.create_post, name='create_post'),
    path('post/<slug:slug>/update', views.update_post, name='update_post'),
    path('post/<slug:slug>/delete', views.delete_post, name='delete_post'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('search_post/', PostSearchView.as_view(), name='search_post'),
]