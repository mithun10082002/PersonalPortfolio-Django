from django.shortcuts import render

def home(request):
    return render(request, 'portfolio/home.html')

def bio(request):
    return render(request, 'portfolio/bio.html')


