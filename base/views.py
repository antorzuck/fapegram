from django.shortcuts import render, redirect
from base.models import *


def home(request):
    img = Art.objects.all().order_by('-id')
    context = {'img': img}
    return render(request, 'home.html', context)

def profile(request):
    return render(request, 'profile.html')
