from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def about_shop(request):
    return render(request, 'about_shop.html')    
    
def author(request):
    return render(request, 'author.html')   

def specialties(request):
    return render(request, 'spec.html')

def spec_id(request, id):
    return HttpResponse(f"id:{id}")    