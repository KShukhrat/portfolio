from django.shortcuts import render
from .models import *
from django.http import HttpResponse
def index(request):
    cer = Certificate.objects.all()
    project = Project.objects.all()
    context = {'certificate': cer, 'project': project}
    return render(request, 'index.html', context)

def components(request):
    return render(request, 'components.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        subject = request.POST['subject']
        Contact.objects.create(name=name, email=email, number=number, subject=subject)
        return HttpResponse('muvofiqiyatli amlga oshirildi!!!')
