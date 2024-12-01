from django.urls import path, include
from .import views

# There is the route directories for all the paths of the applications forms


urlpatterns = [
    path('', views.application_view, name='application_view'),
    path('application/applied/', views.application_form, name='application_form'),
]