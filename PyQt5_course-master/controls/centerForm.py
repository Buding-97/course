# QDesktopWidget
import sys
from PyQt5.QtWidgets import QDesktopWidget,QMainWindow,QApplication
from PyQt5.QtGui import QIcon

class CenterForm(QMainWindow):
    def __init__(self,parent = None):
        super(CenterForm,self).__init__(parent)
        self.setWindowTitle('主窗口应用')
        self.resize(400,300)

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        newleft = (screen.width()-size.width())//2
        newright = (screen.height()-size.height())//2
        self.move(newleft,newright)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon('****.ico'))
    main = CenterForm()
    main.show()
    sys.exit(app.exec_())