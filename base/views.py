from django.shortcuts import render,redirect
from .models import imageUpload,Genre
from .form import ImageUploadForm
from django.contrib import messages
from django.db.models import Q
# Create your views here.

def home(request):
    page = 'gallery'
    search_item = request.GET.get('search_item') if request.GET.get('search_item') != None else ''
    
    images = imageUpload.objects.filter(
            Q(title__icontains = search_item)|
            Q(genre__title__icontains = search_item)
        ).order_by('-created')
    genres = Genre.objects.all()
    context = {'images':images,'genres':genres,'page':page}
    return render(request,'base/home.html',context)

def upload_image(request):
    page = 'Upload'
    genres = Genre.objects.all()
    form = ImageUploadForm()
    if request.method == 'POST':
        title = request.POST.get('title')
        genre_title = request.POST.get('genre_title')
        genre,created = Genre.objects.get_or_create(title=genre_title)
        image = request.FILES.get('image')
        obj = imageUpload.objects.create(
            user = request.user,
            title = title,
            genre = genre,
            image = image
        )
        obj.save()
        # form = ImageUploadForm(request.POST,request.FILES)
        # if form.is_valid():
        #     form.save()
        messages.success(request, 'Images has successfully uploaded.')
        return redirect('home')

    context = {'form':form,'page':page,'genres':genres}
    return render(request,'base/upload_image.html',context)

def homeFilter(request,pk):
    images = imageUpload.objects.filter(genre=pk)
    page = Genre.objects.get(id=pk)
    genres = Genre.objects.all()
    context = {'images':images,'genres':genres,'page':page}
    return render(request,'base/home.html',context)
