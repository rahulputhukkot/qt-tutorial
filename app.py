"""
REF: https://www.pythonguis.com/tutorials/pyside6-creating-multiple-windows/
"""

import sys
from random import randint
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget


class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window % d" % randint(0,100))
        # This shows that each time the button is pressed the current window
        #  is destroyed and a new one is created
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.w = None
        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)

    def show_new_window(self, checked):
        """ if we dont use self.w the window would only be displayed for a fraction 
        of a second its due to the reason that the dialog exist only inside the 
        funciton as soon as the its exited from the funciton value is lost due
        to garbage collection so we need to save this in some variable
        """
        if self.w is None:
            # check if already a window exist then use that 
            # one instead of creating a new one
            self.w = AnotherWindow() 
            self.w.show()
        else: 
            self.w.close() # closes the window
            self.w = None # discard the reference


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()