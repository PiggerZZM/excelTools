from PySide2.QtCore import Slot
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QDialog

from src.gui.UI_file.Ui_SuccessDialog import Ui_successDialog


class SuccessWindow(QDialog):
    """
    操作成功提示窗口：包含转换成功字样和一个确认按钮
    """
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("./gui/ZZM.ico"))

        # 应用UI
        self.ui = Ui_successDialog()
        self.ui.setupUi(self)

    @Slot()
    def on_successButton_clicked(self):
        self.close()
