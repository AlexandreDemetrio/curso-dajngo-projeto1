from django.http import HttpResponse
from django.shortcuts import render



# Create your views here.
def home(request):
    return HttpResponse('EU AMO A JESSICA')

def contato(request):
    return HttpResponse('<3')

def sobre(request):
    return HttpResponse('EU AMO MUITO A JESSICA')