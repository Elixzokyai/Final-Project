from django.urls import path
from .views import register_view, login_view, logout_view, home_view
from blog.views import blog_list


urlpatterns = [
    path('', register_view, name='register'),
   path('login/', login_view, name='login'),
   path('home/', home_view, name='home'),
    path('logout/', logout_view, name='logout'),
    path('blog/', blog_list, name='blogapp'),

]