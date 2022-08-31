import requests

API_KEY = "4ad70550be784679f2059e87a5c0fc47"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
city= input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather =data['weather'][0]["description"]
    temp = round(data["main"]["temp"] -273.15,1)
    print("Weather:",weather)
    print("Temperature:",temp,"c")
else:
    print("An error occurred.")