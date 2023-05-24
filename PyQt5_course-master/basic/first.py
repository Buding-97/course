import sys
from PyQt5.QtWidgets import QApplication,QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(300,150)
    w.move(300,300)
    # 设置窗口标题
    w.setWindowTitle('第一个基于PyQt5的桌面应用')
    w.show()
    # 进入主循环，通过exit安全释放
    sys.exit(app.exec_())