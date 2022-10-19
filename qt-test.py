from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QCursor
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, 
    QLabel, QHBoxLayout, QVBoxLayout, QCalendarWidget, 
    QWidget, QStackedLayout, QSizePolicy, QSpacerItem,
    QTabWidget, QLineEdit, QScrollArea, QComboBox
)

import tab_schedule
import tab_calendar
import tab_log


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # State attributes

        # Lists
        self.schedules = [
            [("1name", ["a", "b", "c"]), ("name", ["reps", "b", "c"]), ("name", ["a", "b", "c"]), ("name", ["a", "b", "c"])],
            [("2name", ["a", "b", "c"]), ("name", ["a", "b", "c"]), ("name", ["a", "b", "c"]), ("name", ["a", "b", "c"])],
            [("3name", ["a", "b", "c"]), ("name", ["a", "b", "c"]), ("name", ["a", "b", "c"]), ("name", ["a", "b", "c"])]
        ]

        self.calendar_schedule = {}

        self.user_performance_data = {}

        # Set application title
        self.setWindowTitle("Exercise Calendar App")

        # Layouts
        self.layout_main = QStackedLayout()
        self.layout_calendar = QVBoxLayout()
        self.layout_schedule = QVBoxLayout()
        self.layout_log = QVBoxLayout()

        # Additional components

        # Widgets
        self.widget_main = QTabWidget()
        self.widget_calendar = tab_calendar.tab_calendar(self.schedules, self.calendar_schedule, self)
        self.widget_schedule = tab_schedule.tab_schedule(self.schedules)
        self.widget_log = tab_log.tab_log(self.schedules[0], self.user_performance_data, self)
        self.widget_results = QWidget()
        

        # set style options
        self.setStyleSheet("QLabel{font-size: 12pt;}")

        # set size options
        

        # Add layouts to widgets
        self.widget_main.setLayout(self.layout_main)

        # Add tabs to main widget
        self.widget_main.addTab(self.widget_calendar, "Kalender")
        self.widget_main.addTab(self.widget_schedule, "Schema")
        self.widget_main.addTab(self.widget_log, "Log")
        self.widget_main.addTab(self.widget_results, "Resultat")
        
        
        # Signals

        # Set important stuff!
        self.setCentralWidget(self.widget_main)
    
    def view_schedule(self):
        self.widget_main.setCurrentWidget(self.widget_schedule)
    
    def log_update(self, schedule_index):
        self.widget_log.view_update(self.schedules[schedule_index])
    
    def viewer_update(self, schedule_index):
        self.widget_schedule.viewer.schedule_index_set(schedule_index)
        self.widget_schedule.viewer.update_viewer_schedule()

    def get_current_date(self):
        date = self.widget_calendar.date_current.toString("yyyy, MM, dd")
        return date

app = QApplication([])

window = MainWindow()
window.show()

app.exec()


