from django.shortcuts import render, redirect
from base.models import *


def home(request):
    return render(request, 'base.html')
