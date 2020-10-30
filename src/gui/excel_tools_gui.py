import logging
import sys

from PySide2.QtWidgets import QApplication

from src.gui.Widget import Widget
from src.gui.Window import MainWindow

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    app = QApplication()

    widget = Widget()

    window = MainWindow(widget)
    window.resize(800, 600)
    window.show()

    sys.exit(app.exec_())
