from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
# from .api import get_mars_rovers

def home(request):
    return render(request, 'home.html')

### View for job application





