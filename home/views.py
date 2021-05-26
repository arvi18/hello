from django.contrib import messages
from django.shortcuts import render, HttpResponse
from datetime import date, datetime
from home.models import Contact
# Create your views here.


def index(request):
    context = {
        'var': "thljejgjgkg sent"
    }
    return render(request, 'index.html', context)


def material(request):
    return render(request, 'material.html')


def about(request):
    return HttpResponse("this is about page")


def links(request):
    return render(request, 'links.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        query = request.POST.get('query')
        contact=Contact(name=name, email=email, query=query, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')


    return render(request, 'contact.html')

    # python manage.py runserver
