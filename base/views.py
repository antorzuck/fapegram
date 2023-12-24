from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from base.models import *


def home(request):
    pro = Profile.objects.all().order_by('-id')
    paginator = Paginator(pro, 15)
    page_number = request.GET.get("page")
    pro = paginator.get_page(page_number)
    context = {'pro': pro}
    return render(request, 'home.html', context)

def profile(request, username):
    prof = Profile.objects.get(user__username=username)
    context = {'prof': prof}
    return render(request, 'profile.html', context)
