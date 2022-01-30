import sys
import random

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.do_paint = False
        self.setGeometry(100, 50, 800, 500)
        self.setWindowTitle('Git и случайные окружности')
        self.btn = QPushButton('Круги!', self)
        self.btn.resize(100, 20)
        self.btn.move(10, 10)
        self.btn.clicked.connect(self.run)
        self.show()
    
    def run(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            for i in range(random.randint(1, 15)):
                qp.setBrush(QColor(random.randint(0, 255), 
                                   random.randint(0, 255), 
                                   random.randint(0, 255)))
                d = random.randint(1, 200)
                qp.drawEllipse(random.randint(1, 800), 
                               random.randint(1, 500), d, d)
            qp.end()
  

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())