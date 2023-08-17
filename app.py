import sys
from PySide6.QtWidgets import (
    QMainWindow, QApplication, QCheckBox,
    QLabel, QToolBar, QStatusBar
)
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt, QSize

class MainWindow(QMainWindow):

  def __init__(self):
    super(MainWindow, self).__init__()

    self.setWindowTitle("My Awesome App")

    label = QLabel("Hello")
    label.setAlignment(Qt.AlignCenter)

    self.setCentralWidget(label)

    toolbar = QToolBar("My main toolbar")
    toolbar.setIconSize(QSize(16, 16))
    self.addToolBar(toolbar)

    #NOTE: QAction needs a QObject passed as a parameter to act as the parent for the action
    # in this case we pass self to have the QMainWindow as its parent
    button_action = QAction(QIcon("icons/acorn.png"),"Your Button", self)
    button_action.setStatusTip( "This is your button")
    button_action.triggered.connect(self.onMyToolBarButtonCLick)
    button_action.setCheckable(True) # This makes the button in the toolbar togglable 
    toolbar.addAction(button_action)

    toolbar.addSeparator()

    button_action_2 = QAction(QIcon("icons/android.png"), "Second Button", self)
    button_action_2.setStatusTip("This is the second button")
    button_action_2.triggered.connect(self.onMyToolBarButtonCLick)
    button_action_2.setCheckable(True)
    toolbar.addAction(button_action_2)

    toolbar.addWidget(QLabel("Hello"))
    toolbar.addWidget(QCheckBox())

    self.setStatusBar(QStatusBar(self))

  def onMyToolBarButtonCLick(self, s):
    print('onMyToolbarButtonClick',s)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()