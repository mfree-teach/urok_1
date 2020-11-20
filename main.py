import sys
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication
from random import random, randrange


class Window(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.fl = False

    def run(self):
        self.fl = True
        self.update()

    def paintEvent(self, event):
        if self.fl:
            d, x, y = round(random() * self.width()), round(random() * self.width() / 2), round(
                random() * self.width() / 2)
            l = [x, y, d, d]
            color = QColor(randrange(256), randrange(256), randrange(256))
            qp = QPainter()
            qp.begin(self)

            qp.setBrush(color)
            qp.drawEllipse(*l)

            qp.end()


app = QApplication(sys.argv)
w = Window()
w.show()
sys.exit(app.exec())