from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
)
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('media/files/<int:pk>/', PostDeleteView.as_view(), name='media-post-delete'),
    path('search/', views.search, name='search'),
    path('about/', views.about, name='blog-about'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # no template → direct redirect
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
]