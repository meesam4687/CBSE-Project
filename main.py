from util.fetch import weather
print(weather("srinagar")["current"]["condition"]["text"])