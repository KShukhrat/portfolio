from django.shortcuts import render
from .models import *

def index(request):
    cer = Certificate.objects.all()
    project = Project.objects.all()
    context = {'certificate': cer, 'project': project}
    return render(request, 'index.html', context)

def components(request):
    return render(request, 'components.html')
