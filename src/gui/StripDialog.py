import logging

from PySide2.QtCore import Slot
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QDialog, QLineEdit, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

from src.utils.exist_util import ExistUtil
from src.utils.excel_loader import ExcelLoader
from src.utils.strip_util import StripUtil


class StripDialog(QDialog):

    def __init__(self, father_window, success_window):
        super().__init__()
        self.setWindowIcon(QIcon("./gui/ZZM.ico"))
        self.setWindowTitle("去除字符")
        self.father_window = father_window
        self.success_window = success_window

        self.strip_ch = QLineEdit()
        self.strip_ch_text = QLabel("要去除的字符：")

        self.button = QPushButton("确认")
        self.button.clicked.connect(self.button_clicked)

        # 布局
        layout = QVBoxLayout()
        up_layout = QHBoxLayout()
        up_layout.addWidget(self.strip_ch_text)
        up_layout.addWidget(self.strip_ch)
        layout.addLayout(up_layout)
        layout.addWidget(self.button)
        self.setLayout(layout)

    @Slot()
    def button_clicked(self):
        filename = self.father_window.widget.file_path.text()
        sheetname = self.father_window.widget.sheet_name_box.currentText()
        if ExistUtil.check_exists(filename, sheetname):
            excel_loader = ExcelLoader(filename, sheetname)
            workbook, _ = excel_loader.load_excel()
            logging.info("读取{}成功！".format(filename))
            self.father_window.widget.show_text("读取{}成功！".format(filename))
            letter = self.strip_ch.text()
            new_workbook = StripUtil.strip(workbook, letter)
            new_workbook.save(filename.split('/')[-1].replace(".xlsx", "_" + sheetname + "_stripped.xlsx"))
            logging.info("去除{}成功！".format(letter))
            self.father_window.widget.show_text("去除{}成功！".format(letter))
            self.father_window.widget.show_text("--------------------")
            self.success_window.show()
        self.close()
