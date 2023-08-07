import sys
from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PySide6.QtGui import QPalette, QColor

class Color(QWidget):

    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")
        
        layout = QGridLayout()
        layout.addWidget(Color('red'), 0,0)
        layout.addWidget(Color('green'), 1,0)
        layout.addWidget(Color('blue'), 1,1)
        layout.addWidget(Color('purple'), 2,1)
        layout.addWidget(Color('yellow'), 0,3)
        layout.addWidget(Color('yellow'), 3, 0)
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()