from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QCursor
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, 
    QLabel, QHBoxLayout, QVBoxLayout, QCalendarWidget, 
    QWidget, QStackedLayout, QSizePolicy, QSpacerItem,
    QTabWidget, QLineEdit
)

# TODO: limit the number of characters that can be written, and which characters.
class schedule_editor_item(QWidget):
    def __init__(self, fields):
        super().__init__()
        
        # set a fixed size 
        self.setMaximumHeight(70)

        layout_main = QHBoxLayout()
        layout_sub = QVBoxLayout()
        layout_sub_sub = QHBoxLayout()
        self.setLayout(layout_main)
        
        entry_name = QLineEdit("Namn")

        layout_sub.addWidget(entry_name)
        layout_main.setDirection(QHBoxLayout.RightToLeft)
        layout_main.addSpacing(600)
        layout_main.addLayout(layout_sub)
        layout_sub.addLayout(layout_sub_sub)

        for field in fields:
            entry_field = QLineEdit(field)
            layout_sub_sub.addWidget(entry_field)


class schedule_viewer_item(QWidget):
    def __init__(self, name, fields):
        super().__init__()
        
        # set a fixed size 
        self.setMaximumHeight(70)

        layout_main = QHBoxLayout()
        layout_sub = QVBoxLayout()
        self.setLayout(layout_main)
        
        title = QLabel(name)

        description_string = ""
        for field in fields:
            description_string += field + "     "
        
        description = QLabel(description_string)

        layout_main.addLayout(layout_sub)
        layout_sub.addWidget(title)
        layout_sub.addWidget(description)
        layout_main.setDirection(QHBoxLayout.RightToLeft)
        #layout_main.addSpacing()
        


class schedule_viewer(QWidget):
    def __init__(self):
        super().__init__()

        


class schedule_editor(QWidget):
    def __init__(self):
        super().__init__()

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
        self.widget_schedule = QWidget()
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
        excercise1 = schedule_viewer_item("Pull-up med vikt", ["3 Sets", "5 Reps", "10 kg"])
        excercise2 = schedule_viewer_item("Plankan", ["3 Sets", "1 min, 20 sek"])
        excercise3 = schedule_editor_item(["Sets", "Reps", "Vikt"])

        self.layout_schedule.addWidget(excercise1)
        self.layout_schedule.addWidget(excercise2)
        self.layout_schedule.addWidget(excercise3)

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