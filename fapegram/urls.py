from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from base.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Fapegram Admin"
admin.site.site_title = "Fapegram Admin Portal"
admin.site.index_title = "Welcome to Fapegram Head Quarter"
