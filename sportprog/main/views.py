from django.shortcuts import render
# from django.http import HttpResponse

def sh1(request):
    return render(request, 'main/sh1.html')

def legs(request):
    return render(request, 'main/legs.html')

def pres(request):
    return render(request, 'main/pres.html')

def bis1(request):
    return render(request, 'main/bis1.html')
def fore(request):
    return render(request, 'main/fore.html')
def tric(request):
    return render(request, 'main/tric.html')

def contact1(request):
    return render(request, 'main/contact1.html')


def index(request):
    return render(request, 'main/index.html')



def about(request):
    return render(request, 'main/about.html')



