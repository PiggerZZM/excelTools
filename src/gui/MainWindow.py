from PySide2.QtCore import Slot
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication, QAction, QMainWindow
from PySide2.QtCore import Qt


class MainWindow(QMainWindow):
    """
    主窗口
    """
    def __init__(self, widget):
        super().__init__()
        self.widget = widget
        self.resize(800, 600)
        self.setWindowTitle("Excel表格处理工具合集")
        self.setWindowIcon(QIcon("./gui/ZZM.ico"))

        # 菜单按钮
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("文件")

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
        self.setWindowFlag(Qt.WindowMaximizeButtonHint)
        self.setFixedSize(self.width(), self.height())

    @Slot()
    def exit_app(self):
        QApplication.quit()
