from django.urls import path
from .import views




urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('blog/post/', views.blog_apply, name='blog_apply'),
    path('blog/delete/<int:pk>', views.blog_delete, name='blog_delete'),
    path('blog/update/<int:pk>', views.blog_update, name='blog_update'),
]

