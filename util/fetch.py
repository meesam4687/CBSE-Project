import requests
import time
t = str(time.time()).split(".")[0]
def weather(location):
    url = f"https://api.weatherapi.com/v1/current.json?q={location.lower()}&key=5d7c3c1717bd4642979153713230206&t={t}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Request failed : {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
def forecast(location):
    url = f"https://api.weatherapi.com/v1/forecast.json?q={location.lower()}&key=5d7c3c1717bd4642979153713230206&t={t}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Request failed : {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")