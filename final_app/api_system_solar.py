import requests

# Define the API endpoint
url = "https://api.le-systeme-solaire.net/rest/bodies/"

# Fetch the data from the API
response = requests.get(url)
data = response.json()

# Print the data
for body in data['bodies']:
    print(f"Name: {body['englishName']}")
    print(f"Body type: {body['bodyType']}")
    print(f"Discovered by: {body['discoveredBy']}")
    print(f"Discovery date: {body['discoveryDate']}")
    print(f"Mass: {body.get('mass', {}).get('massValue', 'Unknown')} kg")
    print(f"Gravity: {body.get('gravity', 'Unknown')} m/s²")
    print(f"Density: {body.get('density', 'Unknown')} g/cm³")
    print(f"Dimension: {body['dimension']}")
    print(f"Mean temperature: {body['avgTemp', 'Unknown']} K")
    print()

