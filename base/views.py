from django.shortcuts import render, redirect
from base.models import *


def home(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')
