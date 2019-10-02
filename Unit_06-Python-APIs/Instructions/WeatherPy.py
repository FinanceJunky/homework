#!/usr/bin/env python
# coding: utf-8

# # WeatherPy
# ----
# 
# #### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[1]:


# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import time
import json
from pprint import pprint

# Import API key
from api_keys import api_key

# Incorporated citipy to determine city based on latitude and longitude
from citipy import citipy

# Output File (CSV)
output_data_file = "output_data/cities.csv"

# Range of latitudes and longitudes
lat_range = (-90, 90)
lng_range = (-180, 180)


# ## Generate Cities List

# In[2]:


# List for holding lat_lngs and cities
lat_lngs = []
cities = []

# Create a set of random lat and lng combinations
lats = np.random.uniform(low=-90.000, high=90.000, size=1500)
lngs = np.random.uniform(low=-180.000, high=180.000, size=1500)
lat_lngs = zip(lats, lngs)

# Identify nearest city for each lat, lng combination
for lat_lng in lat_lngs:
    city = citipy.nearest_city(lat_lng[0], lat_lng[1]).city_name
    
    # If the city is unique, then add it to a our cities list
    if city not in cities:
        cities.append(city)

# Print the city count to confirm sufficient count
len(cities)


# ### Perform API Calls
# * Perform a weather check on each city using a series of successive API calls.
# * Include a print log of each city as it'sbeing processed (with the city number and city name).
# 

# In[5]:


url = "http://api.openweathermap.org/data/2.5/weather?"
units = "Fahrenheit"

# Build partial query URL
query_url = f"{url}appid={api_key}&units={units}&q="

# Set up lists to hold reponse info, & loop variables
lat = []
lon = []
temp = []
cloud = []
country = []
humidity = []
date = []
wind = []
name = []
set_number = 1
count = 0

# Loop through the list of cities and perform a request for data on each
print('Beginning Data Retrieval\n------------------------------')
for city in cities:
    try:
        response = requests.get(query_url+city).json()
        print(f'Processing Record {count} of {set_number} | {city}')
        lat.append(response['coord']['lat'])
        lon.append(response['coord']['lon'])
        temp.append(response['main']['temp_max'])
        humidity.append(response['main']['humidity'])
        cloud.append(response['clouds']['all'])
        name.append(response['name'])
        country.append(response['sys']['country'])
        wind.append(response['wind']['speed'])
        date.append(response['dt'])
        time.sleep(.25)
        if count > 49:
            count = 1
            set_number = set_number + 1
        else:
            count = count + 1
        print(f"Processing record {count} of set {current_set} | {city}")
    except Exception:
        print("City not found. Skipping...")
print("--------------------_--------\nData Retrieval Complete\n-----------------------------")


# ### Convert Raw Data to DataFrame
# * Export the city data into a .csv.
# * Display the DataFrame

# In[10]:


weather_data ={"City":name, "Cloudiness": cloud, "Country": country,
     "Date": date, "Humidity": humidity, "Latitude": lat,
     "Longitude":lon, "Max Temperature": temp, "Wind Speed": wind}
# Convert to dataframe
weather_data = pd.DataFrame(weather_data)
# Save dataframe to csv
weather_data.to_csv("weather_output.csv")


# In[11]:


weather_data.count()


# In[9]:


weather_data.head()


# ### Plotting the Data
# * Use proper labeling of the plots using plot titles (including date of analysis) and axes labels.
# * Save the plotted figures as .pngs.

# #### Latitude vs. Temperature Plot

# In[42]:


#create a plot based on latitude and max temp
fig, ax = plt.subplots(figsize=(12,9))
ax.scatter(x=weather_data['Latitude'], y=weather_data['Max Temperature'])
ax.tick_params(axis='both', which='major', labelsize=12)
ax.tick_params(axis='both', which='minor', labelsize=12)
#labels
plt.title('Latitude vs Maximum Temp', size = 25)
plt.xlabel('Latitude', size = 20)
plt.ylabel('Maximum Temperature (Fahrenheit)', size = 20)
plt.grid()
#save as png
plt.savefig('fig1.png')
plt.show


# #### Latitude vs. Humidity Plot

# In[44]:


#create a plot based on latitude and humidity
fig, ax = plt.subplots(figsize=(12,9))
ax.scatter(x=weather_data['Latitude'], y=weather_data['Humidity'])
ax.tick_params(axis='both', which='major', labelsize=15)
ax.tick_params(axis='both', which='minor', labelsize=15)
#labels
plt.title('City Latitude vs. Humidity', size = 25)
plt.xlabel('Latitude', size = 20)
plt.ylabel('Humidity', size = 20)
plt.grid()
#save as png
plt.savefig('fig2.png')
plt.show


# #### Latitude vs. Cloudiness Plot

# In[45]:


#create a plot based on latitude and cloudiness
fig, ax = plt.subplots(figsize=(12,9))
ax.scatter(x=weather_data['Latitude'], y=weather_data['Cloudiness'])
ax.tick_params(axis='both', which='major', labelsize=15)
ax.tick_params(axis='both', which='minor', labelsize=15)
#labels
plt.title('City Latitude vs. Cloudiness', size = 25)
plt.xlabel('Latitude', size = 20)
plt.ylabel('Cloudiness', size = 20)
plt.grid()
#save as png
plt.savefig('fig3.png')
plt.show


# #### Latitude vs. Wind Speed Plot

# In[47]:


#create a plot based on latitude and wind speed
fig, ax = plt.subplots(figsize=(12,9))
ax.scatter(x=weather_data['Latitude'], y=weather_data['Wind Speed'])
ax.tick_params(axis='both', which='major', labelsize=15)
ax.tick_params(axis='both', which='minor', labelsize=15)
#labels
plt.title('City Latitude vs. Wind Speed', size = 25)
plt.xlabel('Latitude', size = 20)
plt.ylabel('Wind Speed (mph)', size = 20)
plt.grid()
#save as png
plt.savefig('fig4.png')
plt.show


# In[ ]:


# Temperatures are indeed warmer near the equator the scatter plot
# -  for latitude vs temp show a ^ or inverted V pattern peaking near
#    the Tropic of cancer. Since it is summer in the northern hemisphere,
#    this result from the dataplot proves the expected outcome on this point.
#
# This dataset shows an even distribution of wind speed at nearly all latitudes.
#
# There were lots of cities with 100% cloudiness and an almost equal amount
#  with no clouds for every latitude. An uncorrelatteable scatter of cloudiness
#  also resulted for the cities inbetween these extremes.

