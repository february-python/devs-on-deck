from django.shortcuts import render, redirect
from apps.orgs.models import Org
from django.contrib import messages

# Create your views here.
def org_register_page(request):
    return render(request, "orgs/org_reg.html")

def org_register(request):
    errors = Org.objects.validate(request.POST)
    if errors:
        for error in errors:
            messages.error(request, error)
    else:
        Org.objects.create_user(request.POST)
    return redirect('/orgs/register/')

def org_login_page(request):
    return render(request, "orgs/org_login.html")

def org_login(request):
    errors = Org.objects.login.validate(request.POST)
    if errors:
        for error in errors:
            messages.error(request, error)
    return redirect('/orgs/login/')

def org_logoff(request):
    request.session.clear()
    return redirect('/orgs/login')