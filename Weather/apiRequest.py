import requests

#________________WEATHER API______________________________________________
url = "https://community-open-weather-map.p.rapidapi.com/weather"

querystring = {"q":"California,usa","lat":"0","lon":"0","callback":"test","id":"2172797","lang":"null","units":"imperial","mode":"xml"}

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "bb40ec7670mshde139a8c436226fp175544jsn658639525ad1"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
#_______________________END API 1__________________________________________

#_____________________US EAL ESTATEAPI______________________________________
#import requests
print("-----------------------------------------------------")
url = "https://us-real-estate.p.rapidapi.com/v2/property-detail"

querystring = {"property_id":"3199790641"}

headers = {
    'x-rapidapi-host': "us-real-estate.p.rapidapi.com",
    'x-rapidapi-key': "bb40ec7670mshde139a8c436226fp175544jsn658639525ad1"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)