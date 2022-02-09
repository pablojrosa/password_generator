import imp
from re import template
from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')


def password(request):
    
    characters = list('abcdefghijklmnopqrstuvwxyz')
    lenght = int(request.GET.get('lenght', 12))

    if bool(request.GET.get('uppercase')):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    
    if bool(request.GET.get('numbers')):
        characters.extend('0123456789')
    
    if bool(request.GET.get('specialcharacters')):
        characters.extend('\!@#$%&/=')

    password = ''
    for i in range(lenght):
        password += random.choice(characters)

    return render(request, 'generator/password.html', {'password':password})


def about(request):
    return render(request, 'generator/about.html')
