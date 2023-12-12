import requests
import json
data = str(input("Do you want to learn random fact about cat?\n"))
data = data.lower()
print(data)
a = 100
while data != "no" or 'n':
    while a != 0:
        print("Here is random fact for you!\n")
        url = f"https://catfact.ninja/fact"
        info = requests.get(url)
        conversion = json.loads(info.text)
        print(conversion["fact"])
        a = int(input("Do you want to learn more! Press 0 to exit \n"))
