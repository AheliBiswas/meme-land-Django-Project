from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.loginPage,name='login'),
    path('register/',views.registerPage,name='register'),
    path('logout/',views.logoutPage,name='logout'),
    path('recover/',views.getEmail,name='get-email'),
    path('forget-password/<token>/',views.forgetPassword,name='forget-password'),
    path('verify/<token>/',views.verify,name='verify')
]