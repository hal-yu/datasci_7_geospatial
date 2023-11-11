import requests 
import urllib.parse
import json
import pandas as pd
import os 
from dotenv import load_dotenv

load_dotenv()

API_Key = os.getenv('API_Key')

df = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/HHA_507_2023/main/WK7/assignment7_slim_hospital_coordinates.csv')
df = df.sample(100)

df['coordinates'] = df['X'].astype('str') + ',' + df['Y'].astype('str')

google_response = []

for coordinates in df['coordinates']: 

    search = 'https://maps.googleapis.com/maps/api/geocode/json?latlng='
    
    location_raw = coordinates

    url_request_part1 = search + location_raw + '&key=' + API_Key
    url_request_part1

    
    response = requests.get(url_request_part1)
    response_dictionary = response.json()

    lat_long = response_dictionary['results'][0]['formatted_address']

    final = {'address': lat_long, 'coordinates': coordinates}
    google_response.append(final)

    print(f'....finished with {coordinates}')


df1 = pd.DataFrame(google_response)

df1.to_csv('address_100.csv')
