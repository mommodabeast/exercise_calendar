from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QCursor
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, 
    QLabel, QHBoxLayout, QVBoxLayout, QCalendarWidget, 
    QWidget, QStackedLayout, QSizePolicy, QSpacerItem,
    QTabWidget, QLineEdit, QScrollArea, QComboBox
)

import tab_schedule



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # State attributes
        self.calendar_popup_shown = False

        # Set application title
        self.setWindowTitle("Exercise Calendar App")

        # Layouts
        self.layout_main = QStackedLayout()
        self.layout_calendar = QVBoxLayout()
        self.layout_schedule = QVBoxLayout()

        # Additional components

        # Widgets
        self.widget_main = QTabWidget()
        self.widget_calendar = QCalendarWidget()
        self.widget_schedule = tab_schedule.tab_schedule()
        self.widget_results = QWidget()
        self.widget_log = QWidget()

        # set style options
        self.setStyleSheet("QLabel{font-size: 12pt;}")

        # set size options
        

        # Add layouts to widgets
        self.widget_main.setLayout(self.layout_main)
        self.widget_calendar.setLayout(self.layout_calendar)
        self.widget_schedule.setLayout(self.layout_schedule)
        
        # Add elements to widgets

        # Add tabs to main widget
        self.widget_main.addTab(self.widget_calendar, "Kalender")
        self.widget_main.addTab(self.widget_schedule, "Schema")
        self.widget_main.addTab(self.widget_results, "Resultat")
        self.widget_main.addTab(self.widget_log, "Log")
        
        # Signals
        self.widget_calendar.clicked.connect(self.clicked_date)

        # Set important stuff!
        self.setCentralWidget(self.widget_main)


    def clicked_date(self, date):
        cursorPos = QCursor.pos()

        print(self.mapFromGlobal(cursorPos))
        print(date)
        self.dateOptions()

    def dateOptions(self):
        self.widget_main.setCurrentIndex(1)
            

app = QApplication([])

window = MainWindow()
window.show()

app.exec()