import requests
from dotenv import load_dotenv
import os 
import boto3
import json
from botocore.exceptions import ClientError, BotoCoreError

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
    
    try:
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
        
        #Return Message Upload Success
        return {
            'statusCode': 200,
            'body': f"Weather data for {weather['city']} has been uploaded to S3 bucket {S3_BUCKET_NAME}"
        }
        
    #Return HTTPError from WeatherAPI
    except requests.exceptions.HTTPError as e:
        return {
            'statusCode': response.status_code,
            'body':f"Weather API HTTP error: {str(e)}"
        }
    
    #Return Requests Error
    except requests.exceptions.RequestException as e:
        return {
            'statusCode': 500,
            'body': f"Weather API request failed: {str(e)}"
        }
    
    #Return ClientError from S3
    except ClientError as e:
        return {
            'statusCode': 500,
            'body':f"S3 ClientError: {e.response['Error']['Message']}"
        }
    
    #Return low-level Boto3 SDK issues
    except BotoCoreError as e:
        return {
            'statusCode': 500,
            'body':f"S3 BotoCoreError: {str(e)}"
        }
    
    #Return other kinds of Error
    except Exception as e:
        return {
            'statusCode': 500,
            'body':f"Unexpected error: {str(e)}"
        }

    



print(lambda_handler(None, None))
