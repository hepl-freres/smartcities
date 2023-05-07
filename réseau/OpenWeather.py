import network
import time
import urequests


wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('WiFi-2.4-9B4E', '*******')


while not wlan.isconnected() and wlan.status() >= 0:
    print("Connexion...")
    time.sleep(1)
time.sleep(0.5)
print("Connected")

    
print(wlan.ifconfig())

key = {'lat': '50.1324333',
       'lon': '5.7907691',
       'appid': '58241d13228b46dce218c022ecb531c4',
       'units': 'metric'}

url = 'https://api.openweathermap.org/data/2.5/weather?lat='+key['lat']+'&lon='+key['lon']+'&appid='+key['appid']+'&units='+key['units']
print(url)

r = urequests.get(url)
dict = r.json()

temp=float((dict["main"]["temp"]))
temp_min=float((dict["main"]["temp_min"]))
temp_max=float((dict["main"]["temp_max"]))
humidity=float((dict["main"]["humidity"]))
pressure=float((dict["main"]["pressure"]))


print("Location:",dict["name"])
print("Weather: ",dict["weather"][0]["main"])
print("Current temperature: ",round(temp,1),"°C")
print("Minimum temperature today: ",round(temp_min,1),"°C")
print("Maximum temperature today: ",round(temp_max,1),"°C")
print("Relative humidity: ",round(humidity),"%")
print("Atmospheric pressure:",round(pressure),"hPa")


#print (dict.json())
wlan.disconnect()