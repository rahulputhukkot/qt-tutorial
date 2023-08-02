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
        super().__init__()

        self.setWindowTitle("My App")
        
        slider = QSlider(Qt.Orientation.Horizontal)
        slider.setRange(-10,3)     
        slider.setSingleStep(3)

        slider.valueChanged.connect(self.value_changed)
        slider.sliderMoved.connect(self.slider_position)
        slider.sliderPressed.connect(self.slider_pressed)
        slider.sliderReleased.connect(self.slider_released)
    
        self.setCentralWidget(slider)
    
    def value_changed(self, value):
        print("Value:", value)
    
    def slider_position(self, position):
        print("Text:", position)
    
    def slider_pressed(self):
        print("Slider Pressed")

    def slider_released(self):
        print("Slider Released")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()