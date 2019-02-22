# +--------------------------------------------------------+
# |                                                        |
# | Get the weather for my home weather station.           |
# | Written by: Brad Buskey                                |
# | Written in: Python 3                                   |
# | Contact: deckyon@gmail.com                             |
# |                                                        |
# +--------------------------------------------------------+

#! python

# Lets import some required libraries that will be used to gather and display the information.
import urllib
from urllib.request import urlopen
import json

# Get and load the weather data from my house weather station.
weatherdata = urllib.request.urlopen("http://api.wunderground.com/api/<Use Your API Key Here>/conditions/q/pws:<Get Your Location Code from WeatherUnderground>.json")
weatherinfo = json.loads(weatherdata.read())

# This gets the data regarding the sun and moon phases and rises/sets.
astrodata = urllib.request.urlopen("http://api.wunderground.com/api/<Use Your API Key Here>/astronomy/q/pws:<Get Your Location Code from WeatherUnderground>.json")
astroinfo = json.loads(astrodata.read())

# Get information on any active alerts in the area.
alertdata = urllib.request.urlopen("http://api.wunderground.com/api/<Use Your API Key Here>/alerts/q/pws:<Get Your Location Code from WeatherUnderground>.json")
alertinfo = json.loads(alertdata.read())


# Here we start to display the different information gathered from the above three URLS.
print ("+-----------------------------------------------------------------------------+")
print ("| Current Weather at my house: " + weatherinfo['current_observation']['observation_location']['full'])
print ("| " + weatherinfo['current_observation']['observation_time'])
print ("+-----------------------------------------------------------------------------+")
print ("| Conditions        : " + weatherinfo['current_observation']['weather'])
print ("| Temperature       : " + weatherinfo['current_observation']['temperature_string'])
print ("| Feels Like        : " + weatherinfo['current_observation']['feelslike_string'])
print ("| Windchill         : " + weatherinfo['current_observation']['windchill_string'])
print ("| Heat Index        : " + weatherinfo['current_observation']['heat_index_string'])
print ("| Dewpoint          : " + weatherinfo['current_observation']['dewpoint_string'])
print ("| Relative Humidity : " + weatherinfo['current_observation']['relative_humidity'])
if weatherinfo['current_observation']['pressure_trend'] == '+':
	trendinfo = 'upwards'
elif weatherinfo['current_observation']['pressure_trend'] == '-':
	trendinfo = 'downwards'
elif weatherinfo['current_observation']['pressure_trend'] == '0':
	trendinfo = 'constant'
elif weatherinfo['current_observation']['pressure_trend'] == '':
	trendinfo = 'N/C'
print ("| Pressure          : " + weatherinfo['current_observation']['pressure_in'] + ", trending: " + trendinfo)
print ("| Rainfall          : " + weatherinfo['current_observation']['precip_today_string'])
print ("| Wind              : " + weatherinfo['current_observation']['wind_string'])
print ("| Visability        : " + weatherinfo['current_observation']['visibility_mi'] + " miles.")
print ("+-----------------------------------------------------------------------------+")
print ("| Moon Phase        : " + astroinfo['moon_phase']['phaseofMoon'])
print ("| Illumination      : " + astroinfo['moon_phase']['percentIlluminated'] + " %")
print ("| Moon Rise         : " + astroinfo['moon_phase']['moonrise']['hour'] + ":" + astroinfo['moon_phase']['moonrise']['minute'])
print ("| Moon Set          : " + astroinfo['moon_phase']['moonset']['hour'] + ":" + astroinfo['moon_phase']['moonset']['minute'])
print ("+-----------------------------------------------------------------------------+")
print ("| Sun Rise          : " + astroinfo['sun_phase']['sunrise']['hour'] + ":" + astroinfo['sun_phase']['sunrise']['minute'])
print ("| Sun Set           : " + astroinfo['sun_phase']['sunset']['hour'] + ":" + astroinfo['sun_phase']['sunset']['minute'])
print ("+-----------------------------------------------------------------------------+")
if 'type' in alertinfo:
	print ("| Alert           : " + alertinfo['alerts']['description'])
	print ("| Expires         : " + alertinfo['alerts']['expires'])
	print ("| Message         : " + alertinfo['alerts']['message'])
else:
	print ("| No weather alerts or special notices for this region at this time.")
print ("+-----------------------------------------------------------------------------+")
print ()

# Prompt to hit Enter to exit the script.
wait = input("Press the 'Enter' key to exit.")

# And lets go ahead and exit the script.
exit()
