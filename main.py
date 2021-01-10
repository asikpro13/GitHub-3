from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor
from PyQt5.QtCore import *
import sys
import random


class yellow_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        self.setupUi()
        self.pushButton.clicked.connect(self.run)

    def setupUi(self):
        self.setObjectName("Form")
        self.resize(607, 571)
        self.pushButton = QPushButton(self)
        self.pushButton.setGeometry(QRect(250, 10, 75, 23))
        self.retranslateUi()

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Git и случайные окружности"))
        self.pushButton.setText(_translate("Form", "Начать"))

    def run(self):
        self.paint()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)

            self.draw_flag(qp)
            qp.end()

    def draw_flag(self, qp):
        self.do_paint = False
        for i in range(100):
            qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            x = random.randint(0, self.width())
            y = random.randint(0, self.height())
            r = random.randint(0, 150)
            qp.drawEllipse(x, y, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = yellow_Window()
    ex.show()
    sys.exit(app.exec_())
