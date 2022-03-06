from django.contrib import admin
from django.urls import path
from django.conf.urls import include

#login
from django.views.generic.base import TemplateView
from django.contrib.auth import views

#2fa
from two_factor.urls import urlpatterns as tf_urls

#views
from nepylogin import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    #path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('', include(tf_urls)),
    #path('login/', views.LoginView.as_view(template_name= 'login.html'), name='login'),
    path('account/logout/', views.logout, name='logout'),
    #path('account/logout/', views.LogoutView.as_view(template_name= 'logout.html'), name='logout'),
]

