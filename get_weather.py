import requests
def get_weather(city_name):
    API_key='af661f33945c2671187ee15a2eccff83'
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'

    response = requests.get(url)
    if response.status_code == 200:
      data= response.json()
      
      print(f'weather is',city_name,data['weather'][0]['description'])
      print(f'current temprature is ',data['main']['temp'])
      print(f'current temprature is Feels_like ',data['main']['feels_like'])
      print(f'humidity is ',data['main']['humidity'])
    else:
      print("city not found")    
city_name=input("city name ")
get_weather(city_name)  
