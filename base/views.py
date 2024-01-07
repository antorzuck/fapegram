from django.shortcuts import render, redirect, HttpResponseRedirect
from django.core.paginator import Paginator
from base.models import *
from django.http import  HttpResponse
import random


def home(request):
    pro = Profile.objects.all().order_by('-id')
    paginator = Paginator(pro, 15)
    page_number = request.GET.get("page")
    pro = paginator.get_page(page_number)
    context = {'pro': pro}
    return render(request, 'home.html', context)

def profile(request, username):
    prof = Profile.objects.get(user__username=username)
    arts = Art.objects.filter(prof=prof).order_by('-id')

    context = {'prof': prof, 'arts':arts}
    return render(request, 'profile.html', context)


def view(request, username, id):
    prof = Profile.objects.get(user__username=username)
    art = Art.objects.get(
          prof=prof,
          id=id)
    like = len(Like.objects.filter(art=art))
    com = Comment.objects.filter(photo=art).order_by('-id')
    
   
    context = {'com':com, 'art':art, 'like':like}
    return render(request, 'view.html', context)

def search(request):
    q = request.GET.get('q')
    prof = None
    if q:
        prof = Profile.objects.filter(name__icontains=q)
        context = {'prof':prof}
        return render(request, 'searchres.html', context)
    return render(request, 'search.html')



def comment(request):
    name = random.randint(100000000,999999999)
    id = request.POST.get('pid')
    bod = request.POST.get('bod')
    art = Art.objects.get(id=id)
    like = Comment.objects.create(photo=art, name=name, comm=bod)
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


def like(request):
    ip = None
    pid = request.POST.get('pid')
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    exi = Like.objects.filter(ip=ip, art=Art.objects.get(id=pid))
    if len(exi) > 0:
        exi.delete()
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    lk = Like.objects.create(ip=ip)
    lk.art.add(Art.objects.get(id=pid))
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
