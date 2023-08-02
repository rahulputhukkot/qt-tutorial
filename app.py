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
        self.show()

        self.setWindowTitle("My App")
        label = QLabel("Hello")
        font = label.font()
        font.setPointSize(30)
        label.setFont(font)
        label.setAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
        )
        self.setCentralWidget(label)
        # Setting an image as the label
        label.setPixmap(QPixmap('../logo.png'))


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()