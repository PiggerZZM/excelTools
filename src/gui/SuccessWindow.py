from PySide2.QtCore import Slot
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QDialog, QPushButton, QLabel, QVBoxLayout


class SuccessWindow(QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("./gui/ZZM.ico"))
        self.setWindowTitle("转换成功")
        self.resize(250, 80)
        self.text = QLabel("转换成功！")
        self.button = QPushButton("确认")
        self.button.clicked.connect(self.button_clicked)

        layout = QVBoxLayout()
        layout.addWidget(self.text)
        layout.addWidget(self.button)
        self.setLayout(layout)

    @Slot()
    def button_clicked(self):
        self.close()
