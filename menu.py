import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('espresso.ui', self)
        self.run()

    def run(self):
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        self.tableWidget.clear()
        self.tableWidget.setHorizontalHeaderLabels(
            ('id', 'название', 'степень обжарки', 'молотый/в зернах', 
             'описание вкуса', 'цена', 'объем упаковки'))
        result = [i[0] for i in
                  cur.execute('''SELECT id FROM list''').fetchall()]
        result1 = [i[0] for i in
                   cur.execute('''SELECT title FROM list''').fetchall()]
        result2 = [i[0] for i in
                   cur.execute('''SELECT fried FROM list''').fetchall()]
        result3 = [i[0] for i in
                   cur.execute('''SELECT sells FROM list''').fetchall()]
        result4 = [i[0] for i in
                   cur.execute('''SELECT flavour FROM list''').fetchall()]
        result5 = [i[0] for i in
                   cur.execute('''SELECT price FROM list''').fetchall()]
        result6 = [i[0] for i in
                   cur.execute('''SELECT size FROM list''').fetchall()]
        for i in range(len(result)):
            result[i] = [str(result[i]), result1[i], result2[i], result3[i], 
                         result4[i], str(result5[i]), str(result6[i])]
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(len(result))
        row = 0
        for tup in result:
            col = 0
            print(tup)
            for item in tup:
                cellinfo = QTableWidgetItem(item)
                self.tableWidget.setItem(row, col, cellinfo)
                col += 1
 
            row += 1
        con.close()
  

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())