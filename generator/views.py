from django.shortcuts import render
from django.http import HttpResponse
import random
import datetime


# Create your views here.

def home(request):
    return render(request, 'gen/home.html')

def password(request):
    chars =list('abcdefghIjklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        chars.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        chars.extend(list('!@#$%^&*()?~'))
    if request.GET.get('numbers'):
        chars.extend(list('1234567890'))

    l = int(request.GET.get('length',7))
    newpass = ""
    for i  in range(l):
        newpass += random.choice(chars)
    return render(request, 'gen/pass.html', {'password': newpass})

def about(request):
    x = datetime.datetime.now()
    year = x.year
    return render(request, 'gen/about.html', {'date': year})
