from django.shortcuts import render
from .models import *

def index(request):
    cer = Certificate.objects.all()
    context = {'certificate': cer}
    return render(request, 'index.html', context)

def components(request):
    return render(request, 'components.html')
