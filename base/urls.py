from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('home/<str:pk>/',views.homeFilter,name='homefilter'),
    path('upload-image/',views.upload_image,name='upload-image'),
    path('about/',views.about,name='about'),
]