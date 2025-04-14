import requests
from dotenv import load_dotenv
import os 
import boto3
import json

load_dotenv()
API_KEY = os.getenv("OpenWeatherMap_API_KEY")

S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Extract the data from the OpenWeatherMap API
    city = 'Pasig'
    url =  f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    
    # Extract the data from the OpenWeatherMap API
    response = requests.get(url)
    json_data = response.json()
    
    # Transform the data
    weather = {
        'city': json_data['name'],
        'country': json_data['sys']['country'],
        'temperature': json_data['main']['temp'],
        'humidity': json_data['main']['humidity'],
        'pressure': json_data['main']['pressure'],
        'wind_speed': json_data['wind']['speed'],
        }
    
    file_name = f"{weather['city']}_{weather['country']}.json"
    
    #Load the data into S3 bucket
    s3.put_object(
        Bucket=S3_BUCKET_NAME,
        Key=file_name,
        Body=json.dumps(weather),
        ContentType='application/json'
    )
    
    return {
        'statusCode': 200,
        'body': f"Weather data for {weather['city']} has been uploaded to S3 bucket {S3_BUCKET_NAME}"
    }

print(lambda_handler(None, None))
