import requests
import json
from typing import Dict, List, Any, Tuple

api_key = "D4kF9idgdyfKrEtg1UFX1UQMAw9GVe3F2aKW2RaW"

def get_mars_rovers(rover_name: str, page: int, api_key: str, sol=None, earth_date=None, camera=None) -> Dict[Any,Any]:
    """This function gathers info from an external API that contains imagery about Mars.
    parameters:
        api_key (str): Key to access the API data
        rover_name (str): Name of the rover
        sol (int): Martian day to query
        camera (str): Abbreviation of camera
        page: (int): Page number for results
    return: Dictionary with API data
    """
    base_url = "https://api.nasa.gov/mars-photos/api/v1/rovers/" + rover_name + "/photos"

    params: Dict[str,str] = {
        "api_key": api_key,
        "page": page, # Page number of results
        "sol": sol, # Martian solar day
        "earth_date": earth_date, # Earth data year-month-day
        "camera": camera # Camera name (see list)
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
    else:
        print(f"Error handling data: {response.status_code}")
        return None
    
    all_rovers: Dict[str,str] = {}

    photo_data: List[Dict[str,Any]] = data["photos"]
    counter = 1

    for photo in photo_data:
        rover = {}

        camera_name: str = photo["camera"]["name"]
        picture: str = photo["img_src"]
        landing_date = photo["rover"]["landing_date"]
        launch_date = photo["rover"]["launch_date"]
        photo_taken = photo["earth_date"]

        rover["camera_name"] = camera_name
        rover["img"] = picture
        rover["landing_date"] = landing_date
        rover["launch_date"] = launch_date
        rover["img_date"] = photo_taken

        all_rovers[f"rover{counter}"] = rover
        counter += 1
        

    print(all_rovers)

    return all_rovers

rover_name = "curiosity"
sol = 1000
page = 1

rovers = get_mars_rovers(rover_name=rover_name, sol=sol, api_key=api_key, page=page)

rovers: List[str] = [
    "curiosity",
    "opportunity",
    "spirit",
]

camera_names: List[str] = [
    "FHAZ",
    "RHAZ",
    "MAST",
    "CHEMCAM",
    "MAHLI",
    "MARDI",
    "NAVCAM",
    "PANCAM",
    "MINITES"
]