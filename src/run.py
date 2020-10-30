import logging
import sys

from PySide2.QtWidgets import QApplication

from src.gui.SuccessWindow import SuccessWindow
from src.gui.TransformDialog1 import TransformDialog1
from src.gui.TransformDialog2 import TransformDialog2
from src.gui.excel_tools_gui import Widget, MainWindow

if __name__ == '__main__':
    
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    app = QApplication()

    success_window = SuccessWindow()
    widget = Widget(success_window)
    window = MainWindow(widget)
    window.resize(800, 600)

    transform_dialog1 = TransformDialog1(window, success_window)
    widget.transform_tool1_button.clicked.connect(transform_dialog1.show)
    transform_dialog2 = TransformDialog2(window, success_window)
    widget.transform_tool2_button.clicked.connect(transform_dialog2.show)
    window.show()

    sys.exit(app.exec_())
