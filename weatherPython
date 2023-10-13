import requests

api_key = "your_api_key"
city = input("Enter the city name: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
response = requests.get(url)
data = response.json()

if data["cod"] == 200:
    weather = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    print(f"Weather in {city}: {weather}")
    print(f"Temperature: {temperature}°C")
else:
    print("City not found.")
