import logging
import sys

from PySide2.QtWidgets import QApplication

from src.gui.StripDialog import StripDialog
from src.gui.SuccessWindow import SuccessWindow
from src.gui.TransformDialog1 import TransformDialog1
from src.gui.TransformDialog2 import TransformDialog2
from src.gui.Widget import Widget
from src.gui.Window import MainWindow

if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    app = QApplication()

    success_window = SuccessWindow()
    widget = Widget(success_window)
    window = MainWindow(widget)
    transform_dialog1 = TransformDialog1(window, success_window)
    widget.transform_tool1_button.clicked.connect(transform_dialog1.show)
    transform_dialog2 = TransformDialog2(window, success_window)
    widget.transform_tool2_button.clicked.connect(transform_dialog2.show)
    strip_dialog = StripDialog(window, success_window)
    widget.strip_button.clicked.connect(strip_dialog.show)

    window.show()

    sys.exit(app.exec_())
