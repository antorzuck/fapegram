from django.urls import path
from .views import profile

urlpatterns = [
    path('<username>', profile, name='profile')
]
