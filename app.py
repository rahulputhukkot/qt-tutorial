import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDial,
    QDoubleSpinBox,
    QLabel,
    QLineEdit,
    QListWidget,
    QMainWindow,
    QSlider,
    QSpinBox
)

class MainWindow(QMainWindow):
    def  __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")
       
        combobox = QComboBox()
        combobox.setEditable(True)
        combobox.addItems(["One", "Two", "Three"])
        combobox.setInsertPolicy(QComboBox.InsertAlphabetically)
        combobox.setMaxCount(10)

        # The default signal sent by the currentIndexChanged is the index
        combobox.currentIndexChanged.connect(self.index_changed)
        # The same signal can send a text string as well
        combobox.currentTextChanged.connect(self.text_changed)
        
        self.setCentralWidget(combobox)
    
    def index_changed(self, index):
        print('Index changed:', index)
    
    def text_changed(self, text):
        print('Text changed', text)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()