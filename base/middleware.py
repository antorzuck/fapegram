# middleware.py
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.conf import settings



om = False


def maintenance_middleware(get_response):
    def middleware(request):
        if om:
            return render(request, 'down.html')
        else:
            response = get_response(request)
            return response

    return middleware
