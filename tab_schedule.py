import pdb
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QCursor
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, 
    QLabel, QHBoxLayout, QVBoxLayout, QCalendarWidget, 
    QWidget, QStackedLayout, QSizePolicy, QSpacerItem,
    QTabWidget, QLineEdit, QScrollArea, QComboBox
)



# TODO: 
# limit the number of characters that can be written, and which characters.
# Fix bug that makes elements in self.items in the class Schedule_scroll_area disappear.
# Add saving to end button in schedule editor.

class Schedule_editor_item(QWidget):
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
        list_text = []
        list_text.append(self.entry_name.text())
        list_text.append(tuple([input_text.text() for input_text in self.entry_list]))
         
        return list_text




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
        

class Schedule_scroll_area(QWidget):
    def __init__(self, schedule_items):
        super().__init__()
        
        self.scroll = QScrollArea()             # Scroll Area which contains the widgets, set as the centralWidget
        self.vbox = QVBoxLayout()               # The Vertical Box that contains the Horizontal Boxes of  labels and buttons
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
        self.vbox.addWidget(item)
    
    def remove(self, item):
        self.vbox.removeWidget(item)
        item.deleteLater()
    
    def collect(self):
        collection = []
        print(len(self.items))
        for item in self.items:
            print("Hey")
            collection.append(item.collect())

        print(collection)
        return collection




class schedule_viewer(QWidget):
    def __init__(self, widget_parent, schedule):
        super().__init__()

        self.schedule = schedule

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
        
        self.widget_viewer_items = None
        self.viewer_schedule()

        layout_sub_items.addWidget(self.widget_viewer_items.scroll)

    
    def functionality_edit(self):
        self.widget_parent.layout_main.setCurrentIndex(1)

    def viewer_schedule(self):
        schedule_items = [Schedule_viewer_item(item[0], item[1]) for item in self.schedule]
        self.widget_viewer_items = Schedule_scroll_area(schedule_items)

        



class Schedule_editor(QWidget):
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
        

        

        # Items
        
               

    def set_combo_items(self):
        for schedule in self.schedules:
            self.menu_combo.addItem(schedule[0])

    def update_editor_schedule(self, index):
        # Save data of old schedule
        self.schedules[self.schedule_index_current] = self.widget_viewer_items.collect()

        # Update index
        self.schedule_index_current = index

        if self.editor_exists:
            self.layout_sub_items.removeWidget(self.widget_viewer_items.scroll)
            self.editor_schedule(index)
            self.layout_sub_items.addWidget(self.widget_viewer_items.scroll)
        else:
            self.editor_exists = True
            
    def editor_schedule(self, schedule_index):
        if (len(self.schedules) == 0):
            return 

        schedule_current = self.schedules[schedule_index]
        schedule_current = schedule_current[1:len(schedule_current)]

        schedule_items = [Schedule_editor_item(item) for item in schedule_current]
        self.widget_viewer_items = Schedule_scroll_area(schedule_items)
        
    
    def functionality_end(self):
        self.widget_parent.layout_main.setCurrentIndex(0)
        
    def functionality_add_exercise(self):
        schedule_items = self.schedules[self.schedule_index_current] 

        # Add exercise widget object and data to schedules.
        item_new = ("name", ["a", "b", "c"])
        widget_new = Schedule_editor_item(schedule_items[-1])

        self.widget_viewer_items.items.append(widget_new)
        self.schedules[self.schedule_index_current].append(item_new)
        self.widget_viewer_items.add(widget_new)

    def functionality_remove_exercise(self):
        schedule_items = self.schedules[self.schedule_index_current] 
        list_sub = self.schedules[self.schedule_index_current]

        # Exit function if no exercise widget objects exist.
        if len(list_sub) == 1:
            return

        # Delete exercise widget object and remove data from schedules.
        self.widget_viewer_items.remove(self.widget_viewer_items.items[-1])
        del list_sub[-1]
        del self.widget_viewer_items.items[-1]
        

    def functionality_add_schedule(self):
        schedule_new_name = f"schema {len(self.schedules)+1}"
        self.schedules.append([(schedule_new_name)])
        self.menu_combo.addItem(schedule_new_name)
    
    def functionality_remove_schedule(self):
        del self.schedules[self.schedule_index_current]
        self.menu_combo.removeItem(self.schedule_index_current)




class tab_schedule(QWidget):
    def __init__(self):
        super().__init__()

        # Test variables and attributes
        schedules = [
            [("schema 1"), ("name1", ["a", "b", "c"]), ("name", ["a", "b", "c"]), ("name", ["a", "b", "c"]), ("name", ["a", "b", "c"])],
            [("schema 2"), ("name2", ["a", "b", "c"]), ("name", ["a", "b", "c"]), ("name", ["a", "b", "c"]), ("name", ["a", "b", "c"])],
            [("schema 3"), ("name3", ["a", "b", "c"]), ("name", ["a", "b", "c"]), ("name", ["a", "b", "c"]), ("name", ["a", "b", "c"])]
        ]

        # Layout of tab
        self.layout_main = QStackedLayout()
        self.setLayout(self.layout_main)

        viewer = schedule_viewer(self, [("name", ["a", "b", "c"]), ("name", ["a", "b", "c"]), ("name", ["a", "b", "c"]), ("name", ["a", "b", "c"])])
        editor = Schedule_editor(self, schedules, 0)

        self.layout_main.addWidget(viewer) # index 0
        self.layout_main.addWidget(editor) # index 1

        # Set default
        self.layout_main.setCurrentIndex(0)

    def set_current_schedule(self, schedule):
        pass