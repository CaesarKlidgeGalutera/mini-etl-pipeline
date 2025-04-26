# 🌦️Mini ETL Pipeline with OpenWeather API and AWS S3

## 📌Introduction
This project demonstrates a lightweight ETL (Extract, Transform, Load) pipeline using Python and cloud technologies. The script fetches real-time weather data from the OpenWeatherMap API, processes it to extract key metrics, and uploads the results to an AWS S3 bucket in JSON format.

It’s designed to be deployable in a cloud function environment (e.g., AWS Lambda), showcasing key skills in API integration, cloud storage, and error handling.

## 🛠Technology Used
![Amazon S3](https://img.shields.io/badge/Amazon%20S3-FF9900?style=for-the-badge&logo=amazons3&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
![dotenv](https://img.shields.io/badge/dotenv-ECD53F.svg?style=for-the-badge&logo=dotenv&logoColor=black)

## ⚙️Architecture
![Data Architecture Diagram](Documentation/Architecture.jpg)
## 🔁ETL Flow
Extract – Fetch weather data for a specific city (Pasig by default).

Transform – Parse and format relevant weather attributes (e.g., temperature, humidity).

Load – Upload the structured JSON file to a specified AWS S3 bucket.

## 🚨 Error Handling
The script includes detailed error handling for reliability and traceability:

- HTTPError – Handles HTTP issues from the OpenWeather API.

- RequestException – Catches generic request-level errors (e.g., connection issues).

- ClientError – Handles AWS S3 operation failures (e.g., permissions, missing buckets).

- BotoCoreError – Catches low-level AWS SDK exceptions.

- Generic Exception – Catches all other unexpected issues gracefully.
