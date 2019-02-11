from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages as error_messages

def register(req):
    return render(req, 'devs/register.html')

def create_dev(req):
    errors = Dev.objects.validate_registration(req.POST)
    if errors:
        for error in errors:
            error_messages.error(req, error)
        return redirect('devs:register')
    dev = Dev.objects.create_dev(req.POST)
    req.session['dev_id'] = dev.id
    return redirect('devs:languages')

def login(req):
    return render(req, 'devs/login.html')

def login_dev(req):
    errors = Dev.objects.validate_login(req.POST)
    if errors:
        for error in errors:
            error_messages.error(req, error)
        return redirect('devs:login')
    dev = Dev.objects.get(email=req.POST['email'])
    req.session['dev_id'] = dev.id
    req.session['first_name'] = dev.first_name
    return redirect('devs:success')


# added with templates
def dashboard(req):
    if 'dev_id' not in req.session:
        return redirect('devs:index')
    return render(req, 'devs/dashboard.html')

def index(req):
    return render(req, 'devs/index.html')


def success(req):
    return render(req, 'devs/success.html')

def addlanguages(req):
    # Adds language and bio to DB entry
    return redirect('devs:frameworks')

def languages(req):
    return render(req, 'devs/languages.html')

def frameworks(req):
    return render(req, 'devs/frameworks.html')

def addframeworks(req):
    # Adds frameworks to DB entry
    return redirect('devs:success')

def messages(req):
    return render(req, 'devs/messages.html')

def logout(req):
    req.session.clear()
    return redirect('devs:index')
