from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMainWindow
import sys


class MyWindow(QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()

        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText('My first label')
        self.label.move(50, 50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText('Click Me')
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("you pressed the button")
        self.update()

    def update(self):
        self.label.adjustSize()

def window():
    app = QtWidgets.QApplication(sys.argv)
    win = MyWindow()
    win.setGeometry(200, 200, 300, 300)
    win.setWindowTitle('Tech With Tim!')
    win.show()
    sys.exit(app.exec())
    #win = uic.loadUi("main.ui")


window()
