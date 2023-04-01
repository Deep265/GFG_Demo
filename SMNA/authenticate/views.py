from django.shortcuts import render,HttpResponseRedirect,HttpResponse,get_object_or_404,reverse
# Login Imports
from django.contrib.auth import login,logout,authenticate
# Models Import
from .models import Signup
from django.contrib.auth.models import User
# Email
from django.conf import settings
from django.core.mail import send_mail

# OTP
import random

# Create your views here.

def user_signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        first_name = request.POST.get("fname")
        last_name = request.POST.get("lname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        phone = request.POST.get("phone")

        try:
            image = request.FILES.get("img")
            new_user = User(username=username,first_name=first_name,last_name=last_name,email=email)
            new_user.set_password(password)
            extra_info = Signup(user=new_user,image=image,phone=phone)
            extra_info.save()
            subject = 'Registration Message'
            message = f'Hi {first_name} {last_name}, thank you for registering in LoanVault.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, email_from, recipient_list)
        except:
            new_user = User(username=username, first_name=first_name, last_name=last_name, email=email)
            new_user.set_password(password)
            new_user.save()
            extra_info = Signup(user=new_user, phone=phone)
            extra_info.save()
            subject = 'Registration Message'
            message = f'Hi {first_name} {last_name}, thank you for registering in LoanVault.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email,]
            send_mail(subject, message, email_from, recipient_list)
        return HttpResponseRedirect('/authentication/login/')
    return render(request,'signup.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse("predict:home"))
            else:
                return HttpResponse("User is not active")
        else:
            return HttpResponse("No user found")
    return render(request,'login.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("authentication:login"))


