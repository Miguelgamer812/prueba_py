# from django.shortcuts import render

# # Create your views here.
# def home(request):
#     return render(request, 'base.html')

from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request, 'base.html')