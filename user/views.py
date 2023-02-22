from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Profile
# email imports 
from django.conf import settings
from django.core.mail import send_mail
import uuid
# Create your views here.
def loginPage(request):
    page='meme-land-login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exists')
    

        if user.profile.is_verified == True:
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,'Password is wrong')
        else:
            messages.error(request,'Your account has not been verified')
            return redirect('register')
    context = {'page':page}
    return render(request,'user/login.html',context)

def logoutPage(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    page='meme-land-register'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        email = request.POST.get('email')
        try:
            if User.objects.filter(username = username).first():
                messages.error(request,'username already exists')
                return redirect('register')
            if User.objects.filter(email=email).first():
                messages.error(request,'Email already exists')
                return redirect('register')

            user = User.objects.create(
            username = username,
            email = email
            )
            user.set_password(password)
            user.save()
            messages.success(request, 'A verification mail has been send to your email')
            # token and email function call
            token = str(user.profile.verification_id)
            registrationConfMail(email,token)
            return redirect('login')
        except Exception as e:
            print(e)
    context = {'page':page}
    return render(request,'user/register.html',context)


# email sending operation

def registrationConfMail(email,token):
    subject = 'Welcome to Meme-land.Thank you for being a beta-user UwU'
    messages = f'Hi, This is Aheli the creater of Meme-Land.As you are a beta-user and project is still in beta phase you may get the mail in spam.This is your account verification link http://127.0.0.1:8000/user/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject,messages,email_from,recipient_list)

def verify(request,token):
    user = Profile.objects.get(verification_id = token)
    if user:
        user.is_verified = True
        user.save()
        messages.success(request,'Your email has been successfully verified')
        return redirect('login')


# Password Recovery
def getEmail(request):
    page='meme-land-get-mail'
    if request.method == 'POST':
        email = request.POST.get('re_email')
        user = User.objects.get(email=email)
        if user is not None:
            token = user.profile.verification_id
            messages.success(request, 'Verification mail has been send to you')
            passwordRecoveryMail(email,token)
        else:
            messages.error(request,'email does not exists ')

    context = {'page':page}
    return render(request,'user/email_recovery.html',context)

def passwordRecoveryMail(email,token):
    subject = 'Password Recovery.Thank you for being a beta-user UwU'
    messages = f'Hi, This is Aheli the creater of Meme-Land.As you are a beta-user and project is still in beta phase you may get the mail in spam.This is your recovery password link http://127.0.0.1:8000/user/forget-password/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject,messages,email_from,recipient_list)   

def forgetPassword(request,token):
    page='meme-land-set-password'
    user = Profile.objects.get(verification_id = token)
    if request.method == 'POST':

        password = request.POST.get('password')
        if user:
            user.user.set_password(password)
            user.user.save()
            messages.success(request,'Your password have been succefully changed')
            return redirect('login')
    context = {'page':page}
    return render(request,'user/forget_password.html')