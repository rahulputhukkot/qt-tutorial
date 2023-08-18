import sys

from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QMainWindow,
    QMessageBox,
    QPushButton,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, s):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("I have a question!")
        dlg.setText("This is a simple dialog")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Question)
        
        # button = dlg.exec()
        
        # if button == QMessageBox.Yes:
        #     print("Yes!")
        # else:
        #     print("No!")

        # button = QMessageBox.question(self, "Question dialog", "The longer message")
        button = QMessageBox.critical(
            self,
            "Oh dear!",
            "Something went wrong",
            buttons = QMessageBox.Discard | QMessageBox.NoToAll | QMessageBox.Ignore,
            defaultButton=QMessageBox.Discard,
        )
        if button == QMessageBox.Discard:
            print("Discard!")
        elif button == QMessageBox.NoToAll:
            print("No to All")
        else:
            print("Ignored.")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
