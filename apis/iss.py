#!/usr/bin/python3

import requests
import datetime
import reverse_geocoder as rg

URL = 'http://api.open-notify.org/iss-now.json'

def main():
    res = requests.get(URL).json()

    lat = res['iss_position']['latitude']
    lon = res['iss_position']['longitude']
    coords_tuple = (lat, lon)
    result = rg.search(coords_tuple, verbose=False)
    city = result[0]['name']
    country = result[0]['cc']

    epoch_time = res['timestamp']
    date_time = datetime.datetime.fromtimestamp(epoch_time)

    print(f'CURRENT LOCATION OF THE ISS:\nTimestamp: {date_time}\nLon: {lon}\nLat: {lat}\nCity/Country: {city}, {country}')

if __name__ == "__main__":
    main()

