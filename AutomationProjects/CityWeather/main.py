# Import the required libraries
import requests

# Initialize the API_KEY and BASE_URL
API_KEY = "57890a95dc0d2268742e3ffea4b2f00b"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather" 

#A function to call the api for the city that is passed as a param
def weatherData(city):
    apiRequest = f"{BASE_URL}?q={city}&appid={API_KEY}"
    response = requests.get(apiRequest)
    if response.status_code == 200:
        return response.json()['weather'][0]['main']
    else:
        return "ERROR"
    

print("Weather: " + weatherData(input("Enter the city: ")))