from PySide6.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow)
from PySide6.QtCore import Qt, QSize
from PySide6 import QtWidgets
import sys

class scrollWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.scroll = QScrollArea()             # Scroll Area which contains the widgets, set as the centralWidget
        self.vbox = QVBoxLayout()               # The Vertical Box that contains the Horizontal Boxes of  labels and buttons

        for i in range(1,50):
            object = QLabel("TextLabel")
            self.vbox.addWidget(object)

        self.setLayout(self.vbox)

        #Scroll Area Properties
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self)

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        widget = scrollWidget()

        self.setCentralWidget(widget.scroll)

        self.setGeometry(600, 100, 1000, 900)
        self.setWindowTitle('Scroll Area Demonstration')
        self.show()


app = QtWidgets.QApplication(sys.argv)
main = MainWindow()
sys.exit(app.exec())