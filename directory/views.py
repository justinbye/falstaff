from django.shortcuts import import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

def index(request):
    return HttpResponse("Hello world - directory index!")


