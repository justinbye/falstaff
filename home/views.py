from django.shortcuts import render

def index(request):
    return render(request, 'home/base.html')

def about(request):
    return render(request, 'home/about.html')