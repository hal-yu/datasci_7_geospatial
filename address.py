import requests 
import urllib.parse
import json
import pandas as pd
import os 
from dotenv import load_dotenv

load_dotenv()

API_Key = os.getenv('API_Key')

df = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/HHA_507_2023/main/WK7/assignment7_slim_hospital_addresses.csv')
df = df.sample(100)

df['complete_address'] = df['ADDRESS'] + ' ' + df['CITY'] + ' ' + df['STATE']

google_response = []

for address in df['complete_address']: 

    search = 'https://maps.googleapis.com/maps/api/geocode/json?address='

    location_raw = address
    location_clean = urllib.parse.quote(location_raw)

    url_request_part1 = search + location_clean + '&key=' + API_Key
    url_request_part1

    response = requests.get(url_request_part1)
    response_dictionary = response.json()

    lat_long = response_dictionary['results'][0]['geometry']['location']
    lat_response = lat_long['lat']
    lng_response = lat_long['lng']

    final = {'address': address, 'lat': lat_response, 'lon': lng_response}
    google_response.append(final)

    print(f'....finished with {address}')


df1 = pd.DataFrame(google_response)

df1.to_csv('sampled_100.csv')
