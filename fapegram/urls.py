from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from base.views import *
from base.sitemap import *
from django.contrib.sitemaps.views import sitemap

sitemaps={
	'post': PostSitemap,
        'model' : ModelSitemap,
        'page' : PageSitemap,
}

urlpatterns = [
    path("robots.txt", robots_txt),
    path('admin/', admin.site.urls),
    path('',home),
    path(
    'sitemap.xml', sitemap, { 'sitemaps':sitemaps}, name="django.contrib.sites.views.sitemap"
    ),
   
    path('<username>/<id>/', view, name='view'),
    path('search/', search, name='search'),
    path('comment/', comment, name='comment'),
    path('like/', like, name='like'),
    path('popular/', popu, name='popular'),
    path('random/', rand, name='random'),
    path('contact/', contact, name='contact'),
    path('dmca/', dmca, name='dmca'),
   
    path("model/", include("base.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Fapegram Admin"
admin.site.site_title = "Fapegram Admin Portal"
admin.site.index_title = "Welcome to Fapegram Head Quarter"
