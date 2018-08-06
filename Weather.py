import requests
api='https://api.openweathermap.org/data/2.5/weather?appid=a4342b3980a47277be0dc1f82e800b70&q='
city=input("Enter the City name")
url=api+city
data=requests.get(url).json()
mod_data=data['weather'][0]['main']
moddata=data['wind']['speed']
print("Weather",mod_data)
print("Wind Speed=",moddata)