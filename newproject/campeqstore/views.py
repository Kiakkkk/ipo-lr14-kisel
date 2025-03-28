from django.shortcuts import render

def hello_world(request):
    return render(request, 'index.html')

def about_shop(request):
    return render(request, 'about_shop.html')    