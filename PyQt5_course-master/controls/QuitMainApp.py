import sys
from PyQt5.QtWidgets import QHBoxLayout,QDesktopWidget,QMainWindow,QApplication,QPushButton,QWidget

class QuitMainApp(QMainWindow):
    def __init__(self):
        super(QuitMainApp,self).__init__()
        self.resize(400,300)
        self.setWindowTitle('退出应用程序')
        self.button1 = QPushButton('退出')
        self.button1.clicked.connect(self.onClick_Button)
        layout = QHBoxLayout()
        layout.addWidget(self.button1)
        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

    def onClick_Button(self):
        sender =self.sender()
        app  = QApplication.instance()
        app.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon('****.ico'))
    main = QuitMainApp()
    main.show()
    sys.exit(app.exec_())