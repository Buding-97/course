import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon

class FirstMainWin(QMainWindow):
    def __init__(self,parent = None):
        super(FirstMainWin,self).__init__(parent)

        self.setWindowTitle('主窗口应用')
        self.resize(400,300)
        self.status = self.statusBar()
        self.status.showMessage('存在5秒',5000)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon('****.ico'))
    main = FirstMainWin()
    main.show()
    sys.exit(app.exec_())