from PySide6.QtCore import Qt, QDate
from PySide6.QtGui import QAction, QCursor
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, 
    QLabel, QHBoxLayout, QVBoxLayout, QCalendarWidget, 
    QWidget, QStackedLayout, QSizePolicy, QSpacerItem,
    QTabWidget, QLineEdit, QScrollArea, QComboBox
)


class tab_calendar(QWidget):
    # Creates a "tab" (widget) in which the user can view and edit schedules. 
    def __init__(self, schedules, calendar_schedule, widget_parent):
        super().__init__()

        self.widget_parent = widget_parent
        self.calendar_schedule = calendar_schedule
        self.schedules = schedules
        self.date_current = QDate.currentDate()
        self.combo_index = 0

        # Widgets
        calendar = QCalendarWidget()
        button_add = QPushButton("Sätt schema")
        button_show = QPushButton("Visa schema")
        self.menu_combo = QComboBox()        

        # Signals
        calendar.clicked.connect(self.clicked_date)
        button_add.clicked.connect(self.functionality_set)
        button_show.clicked.connect(self.functionality_show)
        self.menu_combo.currentIndexChanged.connect(self.functionality_update_combo_index)

        # Widget setup
        self.set_combo_items()

        # Layout
        layout_main = QVBoxLayout()
        layout_sub = QHBoxLayout()

        layout_main.addLayout(layout_sub)
        layout_main.addWidget(calendar)

        layout_sub.addWidget(self.menu_combo)
        layout_sub.addWidget(button_add)
        layout_sub.addWidget(button_show)
        
        self.setLayout(layout_main)

    def set_combo_items(self):
        # Adds strings to the combo box. 
        for i in range(1, len(self.schedules)+1):
            self.menu_combo.addItem(f"schema {i}")

    def clear_combo_items(self):
        self.menu_combo.clear()
    
    def update_combo_items(self):
        self.clear_combo_items()
        self.set_combo_items()

    def clicked_date(self, date):
        self.date_current = date
        self.update_other_tabs()

    def functionality_set(self):
        # Adds a new key and value to the calendar_schedule dictionary or 
        # sets the value of an existing key. 
        date_string = self.date_current.toString("yyyy, MM, dd")
        self.calendar_schedule[date_string] = self.combo_index
        self.update_other_tabs()

    def functionality_show(self):
        # Show schedule tab
        self.widget_parent.view_schedule()

    def functionality_update_combo_index(self, index):
        self.combo_index = index
        
    
    def update_other_tabs(self):
        # Get schedule index for the current date.
        date_string = self.date_current.toString("yyyy, MM, dd")
        index = 0

        if date_string in self.calendar_schedule:
            index = self.calendar_schedule[date_string]
        else:
            index = -1

        self.widget_parent.log_update(index)
        self.widget_parent.viewer_update(index)
        self.menu_combo.setCurrentIndex(index)

        

        