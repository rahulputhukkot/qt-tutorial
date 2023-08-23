import sys

from PySide6.QtGui import QDoubleValidator, QIcon
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLayout,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.init_ui()

    def init_ui(self):
        num_buttons = [
            "7","8","9",
            "4","5","6",
            "1","2","3",
            "0","."
        ]
        operator_buttons = ["/", "*", "-", "+"]
        num_positions = [(row, column) for row in range(2, 6) for column in range(3)]
        operator_positions = [(row, 3) for row in range(2, 6)]
        print(operator_buttons, operator_positions)
        self.layout = QGridLayout()
        self.layout.setSizeConstraint(
            QLayout.SetFixedSize
        )  # The layout wont space out when the window is resized

        self.input_display = QLineEdit()
        self.input_display.setClearButtonEnabled(True)
        self.input_display.setValidator(
            QDoubleValidator()
        )  # Make it so that it accept only numbers (signed/unsigned decimals)

        self.backspace_btn = QPushButton()
        self.backspace_btn.setIcon(QIcon("qt-tutorial/icons/delete.png"))
        self.backspace_btn.clicked.connect(self.input_display.backspace)

        self.clear_btn = QPushButton("Clear")
        self.clear_btn.clicked.connect(self.input_display.clear)

        self.equels = QPushButton("=")

        self.layout.addWidget(self.backspace_btn, 1, 0)

        self.layout.addWidget(self.clear_btn, 1, 1)

        self.layout.addWidget(self.equels, 1, 2, 1, 2)

        self.layout.addWidget(self.input_display, 0, 0, 1, 4)

        for button, pos in zip(num_buttons, num_positions):
            num_btn = QPushButton(button)
            # if checked = False is not given it retains the last value stored after the whole iteration
            num_btn.clicked.connect(
                lambda checked=False, text=button: self.num_button_clicked(text)
            )
            self.layout.addWidget(num_btn, pos[0], pos[1])

        for button, pos in zip(operator_buttons, operator_positions):
            self.layout.addWidget(QPushButton(button), pos[0], pos[1])
        self.layout.addWidget(QPushButton("%"), 5,2)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

    def num_button_clicked(self, text):
        if not self.input_display.text() and (text == "0"):
            return
        self.input_display.insert(text)


# create the application object and show it
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
