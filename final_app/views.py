from django.shortcuts import render, redirect
from typing import Dict, List, Any
from django.http import HttpResponse, HttpRequest
from .api import google_job_api
from django.urls import reverse
from .models import Job
from .forms import JobForm

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
        if not jobs:
            return redirect('error')
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
