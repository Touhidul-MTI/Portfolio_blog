from django.shortcuts import render

def index(request):
    return render(request, 'portfolio/home.html')

def contact(request):
    return render(request, 'portfolio/contactinfo.html')
