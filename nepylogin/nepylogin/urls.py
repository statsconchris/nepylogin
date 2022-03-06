from django.contrib import admin
from django.urls import path

#login
from django.views.generic.base import TemplateView
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='nepylogin/home.html'), name='home'),
    path('login/', views.LoginView.as_view(template_name= 'nepylogin/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name= 'nepylogin/logout.html'), name='logout'),
]

