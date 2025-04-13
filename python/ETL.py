import requests
from dotenv import load_dotenv
import os 

load_dotenv()
API_KEY = os.getenv("OpenWeathetMap_API_KEY")

city = 'Pasig'
url =  f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

# Extract the data from the OpenWeatherMap API
response = requests.get(url)
json_data = response.json()
print(json_data)

#Transform the data

