from django.shortcuts import render, redirect
from typing import Dict, List
from django.http import HttpResponse, HttpRequest
from .api import google_job_api
from django.urls import reverse
from typing import List, Dict, Any
from .models import Job
from .forms import JobForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Job

def home(request: HttpRequest) -> HttpResponse:
    """View for home.html
    param: request (HttpRequest) : Makes a request to present the html
    return: renders the data
    """
    return render(request, "home.html")

def about(request: HttpRequest) -> HttpResponse:
    """View for about.html
    param: request (HttpRequest) : Makes a request to present the html
    return: renders the data
    """
    return render(request, "about.html")

def results(request: HttpRequest) -> HttpResponse:
    """View for results.html
    param: request (HttpRequest) : Makes a request to present the html
    return: renders the data
    """
    country: str = request.GET.get("country", "")
    city: str = request.GET.get("city", "")
    location: str = city if city else country
    query: str = request.GET.get("q", "")
    if not query:
        return redirect(reverse("home"))

    try:
        jobs: List[Dict[str,str]] = google_job_api(query=query, location=location)
    except KeyError:
        return redirect('error')
    
    context: Dict[str,Any] = {
        "q": query,
        "location": location,
        "jobs": jobs
    }
    
    return render(request, "results.html", context)

def contact(request: HttpRequest) -> HttpResponse:
    """View for contact.html
    param: request (HttpRequest) : Makes a request to present the html
    return: renders the data
    """
    return render(request, "contact.html")

def error(request: HttpRequest) -> HttpResponse:
    """View for error.html
    param: request (HttpRequest) : Makes a request to present the html
    return: renders the data
    """
    return render(request, "error.html")

def favourites(request: HttpRequest) -> HttpResponse:
    """View for favourites.html
    param: request (HttpRequest) : Makes a request to present the html
    return: renders the data
    """
    return render(request, "favourites.html")
