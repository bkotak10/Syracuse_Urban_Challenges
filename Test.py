import csv
import certifi
from geopy.geocoders import Nominatim
from time import sleep
import pandas as pd

geolocator = Nominatim(user_agent="harathod@syr.edu")

df = pd.read_csv('/Users/harshilrathod/Desktop/AML/Final_Project/Parking_Violations_-_2023_-_Present.csv')

def latlong_to_zip(lat, lon):
    try:
        location = geolocator.reverse((lat, lon), exactly_one=True)
        address = location.raw['address']
        zip_code = address.get('postcode', None)
        return zip_code
    except ValueError:
        pass
    

zipcode = []
count = 1
for i,j in df.iterrows():
    lat = j['LAT']
    long = j['LONG']
    zip = latlong_to_zip(lat,long)
    zipcode.append(zip)
    print(count)
    count += 1
    if count == 10 or count ==20 or count == 30:
        sleep(10)
    sleep(1)
print('Success')

# x = latlong_to_zip(43.043481,-76.1181975009999)
# print(x)

