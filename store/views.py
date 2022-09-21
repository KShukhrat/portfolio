from django.shortcuts import redirect, render
from .models import *
from .forms import ContactForm
from django.http import HttpResponse


def index(request):
    cer = Certificate.objects.all()
    project = Project.objects.all()
    resume = Resume.objects.all()
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Habar junatildi')
    context = {'certificate': cer, 'project': project, 'form': form, 'resume': resume}
    return render(request, 'index.html', context)

def components(request):
    return render(request, 'components.html')
