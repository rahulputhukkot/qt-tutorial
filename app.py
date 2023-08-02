import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit


class MainWindow(QMainWindow):
    def  __init__(self):
        super().__init__()
        
        self.label = QLabel()
        self.setCentralWidget(self.label)
    
    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        self.label.setText("mouseMoveEvent")

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            self.label.setText("mousePressEvent LEFT")
        elif event.button() == Qt.MiddleButton:
            self.label.setText("mousePressEvent MIDDLE")
        elif event.button() == Qt.RightButton:
            self.label.setText("mousePressEvent RIGHT")  

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            self.label.setText("mouseReleaseEvent LEFT")
        elif event.button() == Qt.MiddleButton:
            self.label.setText("mouseReleaseEvent MIDDLE")
        elif event.button() == Qt.RightButton:
            self.label.setText("mouseReleaseEvent RIGHT")
    
    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            self.label.setText("mouseDoubleClickEvent LEFT")
        elif event.button() == Qt.MiddleButton:
            self.label.setText("mouseDoubleClickEvent MIDDLE")
        elif event.button() == Qt.RightButton:
            self.label.setText("mouseDoubleClickEvent RIGHT")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()