'''
QPainter
painter = QPainter()
painter.begin()
painter.drawText(...)
painter.end()
必须在paintEvent事件方法中绘制各种元素
'''

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QDialog
from PyQt5.QtGui import QPainter,QColor,QFont
from PyQt5.QtCore import Qt

class DrawText(QWidget):
    def __init__(self):
        super(DrawText,self).__init__()
        self.setWindowTitle('在窗口上绘制文本')
        self.resize(300,200)
        self.text = "Python从菜鸟到高手"

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)
        painter.setPen(QColor(150,43,125))
        painter.setFont(QFont('SimSun',15))
        painter.drawText(event.rect(),Qt.AlignCenter,self.text)
        painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrawText()
    main.show()
    sys.exit(app.exec_())