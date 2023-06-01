from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    context = {'variable': 'This is sent'}
    return render(request, 'index.html', context) # syntax: render(request, 'template_name.html')
    # return render(request, "index.html", {"today": datetime.today"})

    # return HttpResponse("This is the home page")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is the about page")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("This is the services page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your response has been submitted!')

    return render(request, 'contact.html')
    # return HttpResponse("This is the contact page")

# @login_required(login_url='/login') # This is the login page
# it will redirect to login page if user is not logged in and if user is logged in then it will redirect to the desired page