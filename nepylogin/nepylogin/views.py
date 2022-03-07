from django.shortcuts import render, redirect
from django.contrib.auth.views import LogoutView


def home(request):
    if request.user.is_verified():
        return render(request,'home.html')
    else:
        return redirect("two_factor:setup")


def logout(request):
    return LogoutView.as_view(template_name='logout.html')(request)


