from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exists')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Password is wrong')
    return render(request,'user/login.html')

def logoutPage(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
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
            messages.success(request, f'{username} has been successfully created')
            return redirect('login')
        except Exception as e:
            print(e)
    return render(request,'user/register.html')