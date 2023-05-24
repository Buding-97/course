# .ui transform to .py
```text
1. python -m PyQt5.uic.pyuic ***.ui -o ***.py

or

2. pyuic5 ***.ui -o ***.py
```
# 窗口类型

* QMainWindow、QDialog、QWidget
* QMainWindow:包含菜单栏、工具栏、状态栏和标题栏。
* QDialog:对话窗口的基类。
* QWidget:其他窗口。


# 对话框：QDialog

* QMessageBox
* QColorDialog
* QFileDialog
* QFontDialog
* QInputDialog


# 绘图API:QPainter
```
1. 文本
2. 各种图形（直线，点，椭圆，弧，扇形，多边形等）
3. 图像
```
**必须在paintEvent事件方法中绘制各种元素**

# 使用Pyinstaller打包PyQt5应用

```
pip3 install pyinstaller

pyinstaller -Fw Calc.py
```
**-w：不显示终端
-F：将所有的库打包成一个单独的文件**


