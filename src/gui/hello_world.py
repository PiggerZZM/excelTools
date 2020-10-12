import sys
# PySide2最重要的模块：QtWidgets
from PySide2.QtWidgets import QApplication, QLabel

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app = QApplication([]) 也可不传参数

    # QLabel是一个类，能够显示文本和图片（文本支持html）
    label = QLabel("<font color=red size=40>Hello World!</font>")
    # 调用show方法设置显示label
    label.show()
    # 只有调用了exec_()方法，才真正把所有控件显示到屏幕
    app.exec_()
