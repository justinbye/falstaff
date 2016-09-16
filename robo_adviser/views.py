from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #context = {'Hello World!'}
    return render (request, 'robo_adviser/index.html')

# Create your views here.
