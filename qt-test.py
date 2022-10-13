from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QCursor
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, 
    QLabel, QHBoxLayout, QVBoxLayout, QCalendarWidget, 
    QWidget, QStackedLayout, QSizePolicy, QSpacerItem,
    QTabWidget, QLineEdit, QScrollArea
)

# TODO: limit the number of characters that can be written, and which characters.
class Schedule_editor_item(QWidget):
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


class Schedule_viewer_item(QWidget):
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

class Schedule_scroll_area(QWidget):
    def __init__(self, schedule_items):
        super().__init__()
        
        self.scroll = QScrollArea()             # Scroll Area which contains the widgets, set as the centralWidget
        self.vbox = QVBoxLayout()               # The Vertical Box that contains the Horizontal Boxes of  labels and buttons
        self.vbox.setSpacing(0)
        self.vbox.setContentsMargins(0, 0, 0, 0)


        for item in schedule_items:
            self.vbox.addWidget(item)

        self.setLayout(self.vbox)

        #Scroll Area Properties
        
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self)

        




class schedule_viewer(QWidget):
    def __init__(self, exercises, widget_parent):
        super().__init__()

        # Layout of widget
        self.widget_parent = widget_parent
        self.layout_main = QVBoxLayout()
        layout_sub_menu = QHBoxLayout()
        layout_sub_items = QVBoxLayout()

        self.layout_main.addLayout(layout_sub_menu)
        self.layout_main.addLayout(layout_sub_items)
        self.setLayout(self.layout_main)

        # Menu
        layout_sub_menu_right = QHBoxLayout()
        layout_sub_menu_right.setDirection(QHBoxLayout.RightToLeft)
        layout_sub_menu_left = QHBoxLayout()

        layout_sub_menu.addLayout(layout_sub_menu_left)
        layout_sub_menu.addLayout(layout_sub_menu_right)

       
        menu_button_edit = QPushButton("redigera")
        menu_button_edit.clicked.connect(self.functionality_edit)
        menu_label_title = QLabel("Träning 1")

        layout_sub_menu_left.addWidget(menu_label_title)
        layout_sub_menu_right.addWidget(menu_button_edit)
        
        

        # Items
        schedule = [("name", ["a", "b", "c"]), ("name", ["a", "b", "c"]), ("name", ["a", "b", "c"]), ("name", ["a", "b", "c"])]
        schedule_items = [Schedule_viewer_item(item[0], item[1]) for item in schedule]
        widget_viewer_items = Schedule_scroll_area(schedule_items)

        layout_sub_items.addWidget(widget_viewer_items.scroll)

    
    def functionality_edit(self):
        self.widget_parent.layout_main.setCurrentIndex(1)
        



class Schedule_editor(QWidget):
    def __init__(self, exercises, widget_parent):
        super().__init__()

        # Layout of widget
        self.widget_parent = widget_parent
        self.layout_main = QVBoxLayout()
        layout_sub_menu = QHBoxLayout()
        layout_sub_items = QVBoxLayout()

        self.layout_main.addLayout(layout_sub_menu)
        self.layout_main.addLayout(layout_sub_items)
        self.setLayout(self.layout_main)

        # Menu
        layout_sub_menu_right = QHBoxLayout()
        layout_sub_menu_right.setDirection(QHBoxLayout.RightToLeft)
        layout_sub_menu_left = QHBoxLayout()

        layout_sub_menu.addLayout(layout_sub_menu_left)
        layout_sub_menu.addLayout(layout_sub_menu_right)
        
        menu_button_delete = QPushButton("Radera schema")
        menu_button_save = QPushButton("Spara")
        menu_button_cancel = QPushButton("Avbryt")
        
        menu_button_cancel.clicked.connect(self.functionality_edit)
        menu_label_title = QLabel("Träning 1")

        layout_sub_menu_left.addWidget(menu_label_title)
        layout_sub_menu_right.addWidget(menu_button_cancel)
        layout_sub_menu_right.addWidget(menu_button_save)
        layout_sub_menu_right.addWidget(menu_button_delete)
        

        # Items
        schedule = [("name", ["a", "b", "c"]), ("name", ["a", "b", "c"]), ("name", ["a", "b", "c"]), ("name", ["a", "b", "c"])]
        schedule_items = [Schedule_editor_item(item[1]) for item in schedule]
        widget_viewer_items = Schedule_scroll_area(schedule_items)

        layout_sub_items.addWidget(widget_viewer_items.scroll)

    
    def functionality_edit(self):
        self.widget_parent.layout_main.setCurrentIndex(0)

class tab_schedule(QWidget):
    def __init__(self):
        super().__init__()

        # Layout of tab
        self.layout_main = QStackedLayout()
        self.setLayout(self.layout_main)

        viewer = schedule_viewer([], self)
        editor = Schedule_editor([], self)

        self.layout_main.addWidget(viewer) # index 0
        self.layout_main.addWidget(editor) # index 1

        # Set default
        self.layout_main.setCurrentIndex(0)




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
        self.widget_schedule = tab_schedule()
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