from django.shortcuts import render

def index(request):
    return render(request, 'devs/index.html')


def success(request):
    return render(request, 'devs/success.html')

def devreg(request):
    return render(request, 'devs/register.html')

def languages(request):
    return render(request, 'devs/languages.html')

def frameworks(request):
    return render(request, 'devs/frameworks.html')

