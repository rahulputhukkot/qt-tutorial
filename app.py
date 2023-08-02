import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QContextMenuEvent
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QMenu

class MainWindow(QMainWindow):
    def  __init__(self):
        super().__init__()
        self.show()

        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_context_menu)

    def on_context_menu(self, pos) -> None:
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.addAction(QAction("test 4", self))
        context.exec(self.mapToGlobal(pos))


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()