from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def register(req):
    return render(req, 'devs/register.html')

def create_dev(req):
    errors = Dev.objects.validate_registration
    if errors:
        for error in errors:
            messages.error(req, error)
        return redirect('devs:register')
    dev = Dev.objects.create_dev(req.POST)
    req.session['dev_id'] = dev.id
    return redirect('devs:dashboard')

def login(req):
    return render(req, 'devs/login.html')

def login_dev(req):
    errors = Dev.objects.validate_login
    if errors:
        for error in errors:
            message.error(req, error)
        return redirect('devs:login')
    dev = Dev.objects.get(email=req.POST['email'])
    req.session['dev_id'] = dev.id
    return redirect('devs:dashboard')

def dashboard(req):
    if 'dev_id' not in req.session:
        return redirect('devs:register')
    return render(req, 'devs/dashboard.html')