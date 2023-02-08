from django.shortcuts import render, redirect
from .forms import BlogForm
from .models import Blog
# Create your views here.

from django.shortcuts import render

# Create your views here.
def segundo_item(request):
    blogs = Blog.objects.all()
    context = {'blogs':blogs,}
    return render(request, 'segundo_item.html',context)

# def home(request):
#     blogs = Blog.objects.all()
#     context = {'blogs':blogs,}
#     return render(request, 'segundo_item.html',context)

def create_blog(request):
    if request.method == 'POST':
            form = BlogForm(request.POST)
            if form.is_valid():
                 form.save()
                 return redirect('segundo_item')
    else:
         form = BlogForm()
    return render(request,'create_blog.html',{'form':form})