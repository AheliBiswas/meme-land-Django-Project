from django.contrib import admin
from .models import imageUpload,Genre
from user.models import Profile
# Register your models here.
admin.site.register(imageUpload)
admin.site.register(Genre)
admin.site.register(Profile)