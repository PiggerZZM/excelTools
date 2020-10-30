from PySide2 import QtCore
from PySide2.QtCore import Slot
from PySide2.QtWidgets import QApplication, QAction, QMainWindow


class MainWindow(QMainWindow):

    def __init__(self, widget):
        super().__init__()
        self.widget = widget
        self.setWindowTitle("Excel Tools")

        # 菜单按钮
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("文件")
        self.about_menu = self.menu.addMenu("关于")

        # 添加退出选项
        exit_action = QAction("退出", self)  # 实例化Exit选项
        exit_action.setShortcut("Ctrl+Q")  # 设置快捷键
        exit_action.triggered.connect(self.exit_app)

        # 添加读入文件选项
        open_file_action = QAction("打开文件", self)
        open_file_action.setShortcut("Ctrl+O")
        open_file_action.triggered.connect(self.widget.open_file)

        self.file_menu.addAction(exit_action)  # 向file菜单添加Exit选项
        self.file_menu.addAction(open_file_action)  # 添加打开文件选项
        self.setCentralWidget(self.widget)  # 将widget居中放置到窗体

        # 禁止最大化和拉伸窗口大小
        self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint)
        self.setFixedSize(self.width(), self.height())

    @Slot()
    def exit_app(self):
        QApplication.quit()
