from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QCursor
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, 
    QLabel, QHBoxLayout, QVBoxLayout, QCalendarWidget, 
    QWidget, QStackedLayout, QSizePolicy, QSpacerItem,
    QTabWidget, QLineEdit, QScrollArea, QComboBox
)

class Schedule_scroll_area(QWidget):
    # This class creates a scrollable window. 
    # schedule_items is a list containing objects of 
    # class "Schedule_viewer_item" or "Schedule_editor_item". 
    def __init__(self, schedule_items):
        super().__init__()
        
        self.scroll = QScrollArea()             
        self.vbox = QVBoxLayout()               
        self.vbox.setSpacing(0)
        self.vbox.setContentsMargins(0, 0, 0, 0)

        self.items = [] 

        for item in schedule_items:
            self.vbox.addWidget(item)
            self.items.append(item)

        self.setLayout(self.vbox)

        #Scroll Area Properties
        
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self)

    def add(self, item):
        self.items.append(item)
        self.vbox.addWidget(item)
    
    def remove(self, item):
        self.vbox.removeWidget(item)
        item.deleteLater()
    
    def collect(self):
        # Collect text from all fields in all widgets.
        collection = []
        for item in self.items:
            collection.append(item.collect())

        return collection

class tab_log(QWidget):
    def __init__(self):
        super().__init__()

