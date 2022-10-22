from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QCursor
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, 
    QLabel, QHBoxLayout, QVBoxLayout, QCalendarWidget, 
    QWidget, QStackedLayout, QSizePolicy, QSpacerItem,
    QTabWidget, QLineEdit, QScrollArea, QComboBox
)

import pdb


# TODO: 
# limit the number of characters that can be written, and which characters.
# Add a method to the "schedule_viewer" class to show a schedule.

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
        
        self.entry_name = QLineEdit(self.fields[0])

        layout_sub.addWidget(self.entry_name)
        layout_main.setDirection(QHBoxLayout.RightToLeft)
        layout_main.addSpacing(600)
        layout_main.addLayout(layout_sub)
        layout_sub.addLayout(layout_sub_sub)

        self.entry_list = []
        for field in self.fields[1]:
            entry_field = QLineEdit(field)
            layout_sub_sub.addWidget(entry_field)
            self.entry_list.append(entry_field)

    def collect(self):
        # Method for collecting text input written in the text fields. 
        list_text = []
        list_text.append(self.entry_name.text())
        list_text.append(tuple([input_text.text() for input_text in self.entry_list]))
        return list_text



class Schedule_viewer_item(QWidget):
    # This class creates an "exercise" that can be placed in a scroll view area.
    # The "exercise" contains a label that can show any text. The parameter 
    # "fields" is a list that should contain strings.   
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
            self.add(item)

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
        self.items.remove(item)
        self.vbox.removeWidget(item)
        item.deleteLater()
    
    def remove_last(self):
        self.remove(self.items[-1])
    
    def remove_all(self):
        for i in range(0, len(self.items)):
            self.remove_last()         

    def collect(self):
        # Collect text from all fields in all widgets.
        collection = []
        for item in self.items:
            collection.append(item.collect())

        return collection



class schedule_viewer(QWidget):
    # This class creates a widget that shows an exercise schedule.
    # The parameter "schedule" should be a list of tuples, which 
    # contain a string and a list of three strings.
    def __init__(self, widget_parent, schedules, index):
        super().__init__()

        # State attributes
        self.index = index
        self.schedules = schedules

        self.schedule = []
        if len(schedules) != 0:
            self.schedule = schedules[index]
        

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
        self.menu_label_title = QLabel()

        if len(self.schedule) == 0:
            self.menu_label_title.setText("Inget schema")
        else:
            self.menu_label_title.setText(f"schema {index + 1}")

        layout_sub_menu_left.addWidget(self.menu_label_title)
        layout_sub_menu_right.addWidget(menu_button_edit)
        
        # Items
        
        self.widget_viewer_items = None
        self.show_viewer_schedule()

        layout_sub_items.addWidget(self.widget_viewer_items.scroll)

    def functionality_edit(self):
        self.widget_parent.layout_main.setCurrentIndex(1)

    def show_viewer_schedule(self):
        # Creates a scroll area with "exercises" (objects of class "Schedule_viewer_item"). 
        schedule_items = [Schedule_viewer_item(item[0], item[1]) for item in self.schedule]
        self.widget_viewer_items = Schedule_scroll_area(schedule_items)

    def remove_viewer_schedule_items(self):
        # Removes all "exercises" in the scroll area.
        self.widget_viewer_items.remove_all()

    def add_viewer_schedule_items(self):
        schedule_items = [Schedule_viewer_item(item[0], item[1]) for item in self.schedule]
        for item in schedule_items: 
            self.widget_viewer_items.add(item)

    def update_viewer_schedule(self):
        # This method removes the currently shown schedule and 
        # shows the schedule at index "index" in the list schedules.
        if self.index+1 > len(self.schedules):
            self.index = -1 

        if len(self.schedules) == 0 or self.index == -1:
            self.menu_label_title.setText("Inget schema")
            self.remove_viewer_schedule_items()
            return 

        self.menu_label_title.setText(f"Schema {self.index + 1}")
        
        self.schedule = []
        if len(self.schedules) != 0:
            self.schedule = self.schedules[self.index]

        self.remove_viewer_schedule_items()
        self.add_viewer_schedule_items()    

    def schedule_index_set(self, index):
        self.index = index



class Schedule_editor(QWidget):
    # This class creates a widget that lets a user edit an exercise schedule.
    # The parameter "schedules" should be a list of tuples, which 
    # contain a string and a list of three strings.
    def __init__(self, widget_parent, schedules, schedule_index_current):
        super().__init__()

        # State attributes
        self.schedules = schedules
        self.editor_exists = False
        self.schedule_index_current = 0

        # Layout of widget
        self.widget_parent = widget_parent
        self.layout_main = QVBoxLayout()
        layout_sub_menu = QHBoxLayout()
        self.layout_sub_items = QVBoxLayout()

        self.layout_main.addLayout(layout_sub_menu)
        self.layout_main.addLayout(self.layout_sub_items)
        self.setLayout(self.layout_main)

        # Menu
        layout_sub_menu_right = QHBoxLayout()
        layout_sub_menu_right.setDirection(QHBoxLayout.RightToLeft)
        layout_sub_menu_left = QHBoxLayout()

        layout_sub_menu.addLayout(layout_sub_menu_left)
        layout_sub_menu.addLayout(layout_sub_menu_right)
        
        menu_button_save_schedule = QPushButton("Spara")
        menu_button_delete_schedule = QPushButton("Radera schema")
        menu_button_delete_exercise = QPushButton("Radera övning")
        menu_button_add_exercise = QPushButton("Ny övning")
        menu_button_add_schedule = QPushButton("Nytt schema")
        menu_button_end = QPushButton("Avsluta")
        
        menu_button_end.clicked.connect(self.functionality_end)
        menu_button_add_exercise.clicked.connect(self.functionality_add_exercise)
        menu_button_add_schedule.clicked.connect(self.functionality_add_schedule)
        menu_button_delete_schedule.clicked.connect(self.functionality_remove_schedule)
        menu_button_delete_exercise.clicked.connect(self.functionality_remove_exercise)
        menu_button_save_schedule.clicked.connect(self.functionality_save)
        

        self.widget_viewer_items = None
        self.editor_schedule(schedule_index_current)
        self.layout_sub_items.addWidget(self.widget_viewer_items.scroll)

        self.menu_combo = QComboBox()
        self.menu_combo.currentIndexChanged.connect(self.update_editor_schedule)
        self.set_combo_items()
        layout_sub_menu_left.addWidget(self.menu_combo)
        layout_sub_menu_right.addWidget(menu_button_end)
        layout_sub_menu_right.addWidget(menu_button_delete_schedule)
        layout_sub_menu_right.addWidget(menu_button_add_schedule)
        layout_sub_menu_right.addWidget(menu_button_delete_exercise)
        layout_sub_menu_right.addWidget(menu_button_add_exercise)
        layout_sub_menu_right.addWidget(menu_button_save_schedule)
        
    def set_combo_items(self):
        # Adds strings to the combo box. 
        for i in range(1, len(self.schedules)+1):
            self.menu_combo.addItem(f"schema {i}")

    def update_editor_schedule(self, index):
        # Updates the scroll area to show the currently selected schedule
        self.schedule_index_current = index

        if self.editor_exists:
            self.layout_sub_items.removeWidget(self.widget_viewer_items.scroll)
            self.editor_schedule(index)
            self.layout_sub_items.addWidget(self.widget_viewer_items.scroll)
        else:
            self.editor_exists = True
            
    def editor_schedule(self, schedule_index):
        # Creates schedule items from a list of tuples containing
        # a string and a list of strings. Also creates and sets
        # a new scroll area which contains the schedule items. 
        
        schedule_current = schedule_current = []
        if len(self.schedules) != 0:
            schedule_current = self.schedules[schedule_index]

        schedule_items = [Schedule_editor_item(item) for item in schedule_current]
        self.widget_viewer_items = Schedule_scroll_area(schedule_items)
        
    def functionality_end(self):
        # Hides the schedule editor and shows the schedule viewer.
        self.widget_parent.update_other_tabs()
        self.widget_parent.viewer.update_viewer_schedule()
        self.widget_parent.layout_main.setCurrentIndex(0)
        
    def functionality_add_exercise(self):
        # Adds a new widget for an exercise and a new tuple in a list.
        # The list is the list of the list "schedules" with the current index. 
        if len(self.schedules) == 0:
            return 

        schedule_items = self.schedules[self.schedule_index_current] 

        item_new = ("name", ["a", "b", "c"])
        if len(schedule_items) == 0:
            schedule_items = [("name", ["a", "b", "c"])]

        widget_new = Schedule_editor_item(schedule_items[-1])
            
        self.schedules[self.schedule_index_current].append(item_new)
        self.widget_viewer_items.add(widget_new)

    def functionality_remove_exercise(self):
        # Deletes exercise widget object and removes data from schedules.
        if len(self.schedules) == 0:
            return 

        schedule_items = self.schedules[self.schedule_index_current] 
        list_sub = self.schedules[self.schedule_index_current]

        # Exit function if no exercise widget objects exist.
        if len(list_sub) == 0:
            return

        self.widget_viewer_items.remove_last()
        del list_sub[-1]
        
    def functionality_add_schedule(self):
        # Adds a new schedule to both the list containing all schedules
        # and the combo box.
        schedule_new_name = f"schema {len(self.schedules)+1}"
        self.schedules.append([])
        self.menu_combo.addItem(schedule_new_name)
    
    def functionality_remove_schedule(self):
        # Removes a schedule from both list and combo box.
        if len(self.schedules) < 1:
            return 

        del self.schedules[self.schedule_index_current]
        self.menu_combo.removeItem(self.schedule_index_current)
        

    def functionality_save(self):
        # Saves text written to fields.
        if len(self.schedules) == 0:
            return 

        self.schedules[self.schedule_index_current] = self.widget_viewer_items.collect()



class tab_schedule(QWidget):
    # Creates a "tab" (widget) in which the user can view and edit schedules. 
    def __init__(self, schedules, widget_parent):
        super().__init__()

        self.widget_parent = widget_parent

        # Layout of tab
        self.layout_main = QStackedLayout()
        self.setLayout(self.layout_main)

        self.viewer = schedule_viewer(self, schedules, 0)
        editor = Schedule_editor(self, schedules, 0)

        self.layout_main.addWidget(self.viewer) # index 0
        self.layout_main.addWidget(editor) # index 1

        # Set default
        self.layout_main.setCurrentIndex(0)
    
    def update_other_tabs(self):
        self.widget_parent.widget_calendar.update_combo_items()
        self.widget_parent.widget_log.view_update(None)
