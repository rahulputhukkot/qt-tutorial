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

        spinbox = QSpinBox()
        # doblespinbox = QDoubleSpinBox()

        spinbox.lineEdit().setReadOnly(True)

        spinbox.setMinimum(-10)
        spinbox.setMaximum(3)
        # doublespinbox.setRange(-10, 3)

        spinbox.setPrefix("£")
        spinbox.setSuffix("c")
        spinbox.setSingleStep(3)
        # Or e.g. 0.5 for QDoublespinbox

        spinbox.valueChanged.connect(self.value_changed)
        spinbox.textChanged.connect(self.text_changed)

        self.setCentralWidget(spinbox)
    
    def value_changed(self, value):
        print("Value:", value)
    
    def text_changed(self, text):
        print("Text:", text)
    
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()