from django.shortcuts import render, redirect, HttpResponseRedirect
from django.core.paginator import Paginator
from base.models import *
from django.http import  HttpResponse
import random



def robots_txt(request):
    lines = [
        "User-agent: *",
        "Disallow: /admin"
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")




def home(request):
    pro = Profile.objects.all().order_by('-id')
    paginator = Paginator(pro, 30)
    page_number = request.GET.get("page")
    pro = paginator.get_page(page_number)
    context = {'pro': pro}
    return render(request, 'home.html', context)

def profile(request, username):
    prof = Profile.objects.get(user__username=username)
    arts = Art.objects.filter(prof=prof).order_by('-id')
    paginator = Paginator(arts, 24)
    pagen = request.GET.get('page')
    arts = paginator.get_page(pagen)
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
        paginator = Paginator(prof, 24)
        page_number = request.GET.get("page")
        prof = paginator.get_page(page_number)
        context = {'q':q, 'prof':prof}
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
    pro = Profile.objects.get(user__username=request.POST.get('usr'))
    pro.likex += 1
    pro.save()
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))



def popu(request):
    prof = Profile.objects.all().order_by('-likex')
    paginator = Paginator(prof, 30)
    page_number = request.GET.get("page")
    prof = paginator.get_page(page_number)
    context = {'prof':prof}
    return render(request, 'popular.html', context)



def rand(request):
    prof = list(Profile.objects.all())
    random.shuffle(prof)
    paginator = Paginator(prof, 30)
    page_number = request.GET.get("page")
    prof = paginator.get_page(page_number)
    context = {'prof':prof}
    return render(request, 'random.html', context)


def contact(request):
   return render(request, 'contact.html')


def dmca(request):
   if request.method == 'POST':
      em = request.POST.get('e')
      ur = request.POST.get('u')
      re = request.POST.get('r')
      DMCA.objects.create(email=em, url=ur, reason=re)
      c = {'msg' : "Form submit successfully. We'll review into this asap!"}
      return render(request, 'dmca.html',context=c)
   return render(request, 'dmca.html')
