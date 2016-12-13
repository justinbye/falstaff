from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #context = {'Hello World!'}
    return render (request, 'home/base.html')

# Create your views here.
