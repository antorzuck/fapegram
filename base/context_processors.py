from .models import Profile

def popular(request):
    return {'pop': Profile.objects.all().order_by('-likex')[0:1]}
