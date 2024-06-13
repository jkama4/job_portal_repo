from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def results(request):
    query = request.GET.get('q', '')
    context = {'q': query}
    return render(request, 'results.html', context)

def contact(request):
    return render(request, 'contact.html')
