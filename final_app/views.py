from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
# from .api import get_mars_rovers

def home(request):
    return render(request, 'home.html')

<<<<<<< HEAD
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
=======
def results(request):
    query = request.GET.get('q', '')
    context = {'q': query}
    return render(request, 'results.html', context)

### View for job application





>>>>>>> jayden_branch
