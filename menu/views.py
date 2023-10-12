from django.shortcuts import render

def index(request):
    return render(request, 'menu/index.html')

def base(request, name):
    return render(request, 'menu/index.html', {'name': name})