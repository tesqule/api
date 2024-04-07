import requests

url = "https://api.citybik.es/v2/networks"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    for network in data['networks']:
        network_id = network['id']
        network_name = network['name']
        city = network['location']['city']

        print(f"Network ID: {network_id}")
        print(f"Network Name: {network_name}")
        print(f"City: {city}")
        print("----")

else:
    print("Failed to fetch network data")