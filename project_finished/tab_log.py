from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QCursor
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, 
    QLabel, QHBoxLayout, QVBoxLayout, QCalendarWidget, 
    QWidget, QStackedLayout, QSizePolicy, QSpacerItem,
    QTabWidget, QLineEdit, QScrollArea, QComboBox
)

class Schedule_editor_item(QWidget):
    # This class creates an "exercise" that can be placed in a scroll view area. The "exercise"
    # contains one text field for a name and three for various other things (examples: sets, reps, weight).
    # The parameter "fields" should be a list of strings.
    # Note: any text can be written in the fields. 
    def __init__(self, fields):
        super().__init__()
        
        self.fields = fields
        # set a fixed size 
        self.setMaximumHeight(70)

        layout_main = QHBoxLayout()
        layout_sub = QVBoxLayout()
        layout_sub_sub = QHBoxLayout()
        self.setLayout(layout_main)
        
        self.entry_name = QLabel(self.fields[0])

        layout_sub.addWidget(self.entry_name)
        layout_main.setDirection(QHBoxLayout.RightToLeft)
        layout_main.addLayout(layout_sub)
        layout_sub.addLayout(layout_sub_sub)

        self.entry_list = []
        for field in self.fields[1]:
            entry_field = QLineEdit(field)
            layout_sub_sub.addWidget(entry_field)
            self.entry_list.append(entry_field)

    def collect(self):
        # Method for collecting text input written in the text fields. 
        list_text = [input_text.text() for input_text in self.entry_list]
        return list_text


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
        # Add an item to the scroll area.
        self.items.append(item)
        self.vbox.addWidget(item)
    
    def clear(self):
        # Remove all items from the scroll area. 
        for item in self.items: 
            self.vbox.removeWidget(item)
            item.deleteLater()
        
        self.items = []
    
    def collect(self):
        # Collect text from all fields in all widgets.
        collection = []
        for item in self.items:
            collection.append(item.collect())

        return collection

class tab_log(QWidget):
    def __init__(self, schedule, user_performance_data, widget_parent):
        super().__init__()

        # Attributes for parameters
        self.user_performance_data = user_performance_data
        self.widget_parent = widget_parent

        # Layout
        layout_main = QVBoxLayout()
        layout_sub = QHBoxLayout()
        

        # Widgets
        exercises = self.create_items(schedule)
        self.scroll_area = Schedule_scroll_area(exercises) 
        button_save = QPushButton("Spara")
        button_clear = QPushButton("Återställ prestation")
        self.label_date = QLabel(self.widget_parent.get_current_date())

        # Signals
        button_save.clicked.connect(self.functionality_save)

        # Adding layouts and widgets to main_layout
        layout_sub.addWidget(self.label_date)
        layout_sub.addWidget(button_save)
        layout_sub.addWidget(button_clear)

        layout_main.addLayout(layout_sub)
        layout_main.addWidget(self.scroll_area.scroll)

        self.setLayout(layout_main)

    def create_items(self, schedule):
        item_list = []
        for exercise in schedule:
            item = Schedule_editor_item(exercise)
            item_list.append(item)
        
        return item_list 


    def view_set(self, schedule):
        item_list = self.create_items(schedule)

        for item in item_list:
            self.scroll_area.add(item)

    def view_update(self, schedule):
        self.scroll_area.clear()
        self.label_date.setText(self.widget_parent.get_current_date())
        if schedule != None:
            self.view_set(schedule)

    def input_collect(self):
        return self.scroll_area.collect()

    def input_append(self, user_input):
        date = self.widget_parent.get_current_date()
        self.user_performance_data[date] = user_input

    def functionality_save(self):
        user_input = self.input_collect()
        self.input_append(user_input)


