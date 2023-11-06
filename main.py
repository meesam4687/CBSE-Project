import sys
from PyQt6.QtWidgets import *
from PyQt6.QtSvg import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from util.fetch import weather, forecast

app = QApplication(sys.argv)
window = QMainWindow()

location = "Srinagar"

window.setWindowTitle(f"Weather in {location}")
window.setWindowIcon(QIcon("./assets/wLogo.png"))
window.setFixedSize(850, 500)

central_frame = QFrame(window)
central_frame.setFixedSize(850, 500)
central_frame.setStyleSheet("background :#4568a1;")

txt = QLabel(f"<h1>Weather in {location}</h1>", parent=window)
txt.setFixedWidth(850)
txt.setAlignment(Qt.AlignmentFlag.AlignCenter)
txt.setFont(QFont("Times", 10))

status = QLabel(f"<p>{weather(location)['current']['condition']['text']}</p>", parent=window)
status.setFont(QFont("Times", 30))
status.move(80, 180)
status.setFixedHeight(100)

temp = QLabel(f"<p>{str(weather(location)['current']['temp_c']).split('.')[0]}°C</p>", parent=window)
temp.setFont(QFont("Times", 20))
temp.move(82, 250)
temp.setStyleSheet("color: black")

curCondition = weather(location)['current']['condition']['text']
clears = ['Clear', 'Sunny']
cloudys = ['Cloudy', 'Overcast']
partlyCloudys = ['Partly cloudy', 'Mist', 'Fog', 'Freezing fog']
rains = ['Patchy rain possible', 'Patchy light rain', 'Light rain', 'Moderate rain at times', 'Moderate rain', 'Heavy rain at times', 'Heavy rain', 'Light freezing rain', 'Moderate or heavy freezing rain', 'Light rain shower', 'Moderate or heavy rain shower', 'Torrential rain shower', 'Light rain shower', 'Moderate or heavy rain shower', 'Torrential rain shower', 'Light sleet showers', 'Moderate or heavy sleet showers', 'Light snow showers', 'Moderate or heavy snow showers', 'Light showers of ice pellets', 'Moderate or heavy showers of ice pellets', 'Patchy light rain with thunder', 'Moderate or heavy rain with thunder', 'Patchy light snow with thunder', 'Moderate or heavy snow with thunder']
snows = ['Patchy light snow', 'Light snow', 'Patchy moderate snow', 'Moderate snow', 'Patchy heavy snow', 'Heavy snow', 'Ice pellets', 'Light snow showers', 'Moderate or heavy snow showers', 'Light showers of ice pellets', 'Moderate or heavy showers of ice pellets', 'Patchy light snow with thunder', 'Moderate or heavy snow with thunder']
if curCondition in clears:
    cImage = "clear"
if curCondition in cloudys:
    cImage = "cloudy"
if curCondition in partlyCloudys:
    cImage = "partlycloudy"
if curCondition in rains:
    cImage = "rain"
if curCondition in snows:
    cImage = "snow"

img = QLabel(parent=window)
img.setPixmap(QPixmap(f"./assets/{cImage}.png"))
img.move(600, 150) 
img.setFixedHeight(200)
img.setFixedWidth(200)

minTempText = QLabel(f"<p>Min Temp<br> &nbsp;&nbsp;&nbsp;{str(forecast(location)['forecast']['forecastday'][0]['day']['mintemp_c']).split('.')[0]}°C</p>", parent=window)
minTempText.setFont(QFont("Times", 15))
minTempText.move(125, 350)
minTempText.setFixedHeight(100)

maxTempText = QLabel(f"<p>Max Temp<br> &nbsp;&nbsp;&nbsp;{str(forecast(location)['forecast']['forecastday'][0]['day']['maxtemp_c']).split('.')[0]}°C</p>", parent=window)
maxTempText.setFont(QFont("Times", 15))
maxTempText.move(295, 350)
maxTempText.setFixedHeight(100)

humidityText = QLabel(f"<p>Humidity<br> &nbsp;&nbsp;{forecast(location)['forecast']['forecastday'][0]['day']['avghumidity']}%</p>", parent=window)
humidityText.setFont(QFont("Times", 15))
humidityText.move(475, 350)
humidityText.setFixedHeight(100)

windText = QLabel(f"<p>&nbsp;&nbsp;Wind<br> {forecast(location)['forecast']['forecastday'][0]['day']['maxwind_kph']}km/h</p>", parent=window)
windText.setFont(QFont("Times", 15))
windText.move(625, 350)
windText.setFixedHeight(100)

window.show()
sys.exit(app.exec())