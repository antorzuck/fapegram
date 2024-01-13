from django.contrib.sitemaps import Sitemap
from base.models import Art, Profile
from django.urls import reverse


class PostSitemap(Sitemap):
    changefreq = 'daily'
    priority = 1.0
    
    def items(self):
        return Art.objects.all().order_by('-id')
    
    def location(self,obj):
        return '/' + f'{obj.prof.user.username}/' + str(obj.id)




class ModelSitemap(Sitemap):
    changefreq = 'daily'
    priority = 1.0

    def items(self):
        return Profile.objects.all().order_by('-id')

    def location(self,obj):
        return '/' + 'model/' + obj.user.username



class PageSitemap(Sitemap):

    priority = 0.9
    changefreq = 'monthly'

    def items(self):
        return ['dmca','random','popular', 'contact']

    def location(self, item):
        return reverse(item)

