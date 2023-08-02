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
       
        listwidget = QListWidget()
        listwidget.addItems(["One", "Two", "Three"])

        listwidget.currentItemChanged.connect(self.item_changed)
        listwidget.currentTextChanged.connect(self.text_changed)
        self.setCentralWidget(listwidget)
    
    def item_changed(self, item):
        # Here in this case the QListWidget item is sent instead of the index
        print('Item changed:', item.text())
    
    def text_changed(self, text):
        print('Text changed', text)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()