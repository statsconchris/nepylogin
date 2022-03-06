from django.shortcuts import render
from django.contrib.auth.views import LogoutView


def home(request):
    return render(request,'home.html')


def logout(request):
    return LogoutView.as_view(template_name='logout.html')(request)


