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

        self.lineedit = QLineEdit()
        self.lineedit.setMaxLength(15)
        self.lineedit.setPlaceholderText("Enter your text")
        
        self.lineedit.returnPressed.connect(self.return_pressed)
        self.lineedit.selectionChanged.connect(self.selection_changed)
        self.lineedit.textChanged.connect(self.text_changed)
        self.lineedit.textEdited.connect(self.text_edited)
        # validation only numbers 4 sets of 3 numbers seperated by . and blanks are shown as _
        # https://doc.qt.io/qt-6/qlineedit.html#inputMask-prop
        self.lineedit.setInputMask('000.000.000.000;_')

        self.setCentralWidget(self.lineedit)
    
    def return_pressed(self):
        print("Return pressed")
        self.lineedit.setText("KABOOOMM!!!")
    
    def selection_changed(self):
        print("Selection changed")
        print(self.lineedit.selectedText())

    def text_changed(self, text):
        print("Text changed")
        print(text)

    def text_edited(self, text):
        print("Text edited")
        print(text)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()