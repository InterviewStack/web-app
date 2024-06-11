from django.shortcuts import render
from .models import *

def userFeed(request):
    if request.user.is_authenticated:
        return render(request, 'core/base.html')


