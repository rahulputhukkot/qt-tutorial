import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QContextMenuEvent
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QMenu

class MainWindow(QMainWindow):
    def  __init__(self):
        super().__init__()
        self.show()

    def contextMenuEvent(self, event: QContextMenuEvent) -> None:
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.addAction(QAction("test 4", self))
        context.exec_(event.globalPos())


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()