import logging
import os
import sys

from PySide2.QtWidgets import QApplication

from src.gui.DesensitizeDialog import DesensitizeDialog
from src.gui.EncryptDialog import EncryptDialog
from src.gui.StripDialog import StripDialog
from src.gui.SuccessDialog import SuccessWindow
from src.gui.TransformDialog1 import TransformDialog1
from src.gui.TransformDialog2 import TransformDialog2
from src.gui.Widget import Widget
from src.gui.MainWindow import MainWindow

if __name__ == '__main__':
    # 解决Mac OS下不运行的问题
    os.environ['QT_MAC_WANTS_LAYER'] = '1'

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    app = QApplication()

    # 实例化"操作成功"提示窗口
    success_window = SuccessWindow()

    # 实例化主窗口所有控件
    widget = Widget(success_window)

    # 实例化主窗口
    window = MainWindow(widget)

    # 实例化"行列转置"功能窗口
    transform_dialog1 = TransformDialog1(window, success_window)
    widget.transform_tool1_button.clicked.connect(transform_dialog1.show)

    # 实例化"转换上表头"功能窗口
    transform_dialog2 = TransformDialog2(window, success_window)
    widget.transform_tool2_button.clicked.connect(transform_dialog2.show)

    # 实例化"去除字符"功能窗口
    strip_dialog = StripDialog(window, success_window)
    widget.strip_button.clicked.connect(strip_dialog.show)

    # 实例化"加密文件"功能窗口
    encrypt_dialog = EncryptDialog(window, success_window)
    widget.encrypt_button.clicked.connect(encrypt_dialog.show)

    # 实例化"数据脱敏"功能窗口
    desensitizeDialog = DesensitizeDialog(window, success_window)
    widget.desensitize_button.clicked.connect(desensitizeDialog.show)

    # 显示主窗口
    window.show()

    # 退出程序
    sys.exit(app.exec_())
