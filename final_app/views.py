from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
# from .api import get_mars_rovers

def home(request):
    return render(request, 'home.html')

<<<<<<< Updated upstream
### View for job application


=======
from django.shortcuts import render
from .api import get_mars_rovers

def mars_images_view(request: HttpRequest) -> HttpResponse:
  """
  View function to display Mars images from the NASA API.

  Handles GET requests with optional query parameters for rover name, sol (Martian day), and page number.
  Renders the 'mars_images.html' template with context data containing retrieved images or error messages.
  """
  rover_name = request.GET.get('rover_name', 'curiosity')  # Default to Curiosity rover
  sol = request.GET.get('sol', None)  # Optional sol parameter
  page = request.GET.get('page', 1)  # Default to page 1

  try:
    # Call get_mars_rovers function with retrieved parameters
    rovers_data = get_mars_rovers(rover_name, sol, api_key="D4kF9idgdyfKrEtg1UFX1UQMAw9GVe3F2aKW2RaW", page=page)  # Replace with your API key 
    if rovers_data is None:
      # Handle error from get_mars_rovers (e.g., no data found)
      error_message = "No data available for your request."
    else:
      error_message = None
  except Exception as e:
    # Handle other potential exceptions during API call
    error_message = f"An error occurred: {str(e)}"

  context = {
    'rover_name': rover_name,
    'sol': sol,
    'page': page,
    'rovers_data': rovers_data,
    'error_message': error_message,
  }

  return render(request, 'mars_images.html', context)
>>>>>>> Stashed changes



