from django.shortcuts import render, redirect, get_object_or_404
from .forms import BlogForm
from .models import Blog
import os
from django.conf import settings
from django.http import HttpResponse
# Create your views here.

from django.shortcuts import render

# Create your views here.
def segundo_item(request):
    blogs = Blog.objects.all()
    path = settings.MEDIA_ROOT
    img_list = os.listdir(path + '/images')
    context = {'blogs':blogs,'images' : img_list,}
    return render(request, 'segundo_item.html',context)

# def home(request):
#     blogs = Blog.objects.all()
#     context = {'blogs':blogs,}
#     return render(request, 'segundo_item.html',context)

def create_blog(request):
    if request.method == 'POST':
            form = BlogForm(request.POST,request.FILES)
            if form.is_valid():
                 form.save()
                 return redirect('segundo_item')
    else:
         form = BlogForm()
    return render(request,'create_blog.html',{'form':form})

def success(request):
    return HttpResponse('successfully uploaded')

def delete_data(request,pk):
    data  = get_object_or_404(Blog, pk=pk)
    blogs = Blog.objects.all()
    if request.method == 'POST':
        data.delete()
        return redirect('segundo_item')
    return render(request, 'segundo_item.html', {'blogs':blogs})