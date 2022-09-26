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
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        subject = request.POST['subject']
        Contact.objects.create(name=name, email=email, number=number, subject=subject)
        return HttpResponse('Habar junatildi')
    context = {'certificate': cer, 'project': project, 'form': form, 'resume': resume}
    return render(request, 'index.html', context)

def components(request):
    message = Contact.objects.all()
    context = {'message': message}
    return render(request, 'components.html', context)
