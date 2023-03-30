from django.shortcuts import render

# Create your views here.

from .models import Animals, Category


def index(request):
    return render('index.html')

def Animals(request):
    return render()

def Categoria(request):
    return render()