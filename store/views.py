from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def components(request):
    return render(request, 'components.html')
