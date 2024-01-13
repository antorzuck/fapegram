from django.urls import path
from .views import profile, upload

urlpatterns = [
    path('<username>', profile, name='profile'),
    path('upload/<username>', upload, name='upload'),
]
