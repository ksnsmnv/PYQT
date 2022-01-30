import sys
import random

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('yellow_circles.ui', self)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.run)
        self.show()
    
    def run(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(200, 100, 0))
            for i in range(random.randint(1, 15)):
                d = random.randint(1, 200)
                qp.drawEllipse(random.randint(1, 800), random.randint(1, 500), d, d)
            qp.end()
  

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())