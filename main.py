import sys
from PyQt6.QtWidgets import *
from PyQt6.QtSvg import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from util.fetch import weather

app = QApplication(sys.argv)
window = QMainWindow()

location = "Srinagar"

window.setWindowTitle(f"Weather in {location}")
window.setWindowIcon(QIcon("./assets/wLogo.png"))
window.setFixedSize(850, 500)

central_frame = QFrame(window)
central_frame.setFixedSize(850, 500)
central_frame.setStyleSheet("background :#6ba2c2;")

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

img = QLabel(parent=window)
img.setPixmap(QPixmap(f"./assets/{weather(location)['current']['condition']['text']}.png"))
img.move(600, 150) 
img.setFixedHeight(200)
img.setFixedWidth(200)

window.show()
sys.exit(app.exec())