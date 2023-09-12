# views.py
import asyncio
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.core.mail import send_mail
from .models import Message, Script, Website, API, Certificate


def home(request):
    scripts = Script.objects.all()
    websites = Website.objects.all()
    apis = API.objects.all()
    certificates = Certificate.objects.all()
    return render(request, 'index.html', {'scripts': scripts, 'websites': websites, 'apis': apis, 'certificates': certificates})


def info(request, model_name, pk):
    model = None
    if model_name == 'script':
        model = get_object_or_404(Script, id=pk)
    elif model_name == 'website':
        model = get_object_or_404(Website, id=pk)
    elif model_name == 'api':
        model = get_object_or_404(API, id=pk)
    elif model_name == 'certificate':
        model = get_object_or_404(Certificate, id=pk)

    context = {'model': model}
    return render(request, 'portfolio-details.html', context)


def details(request):
    return render(request, 'portfolio-details.html')
