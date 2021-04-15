import logging

from PySide2.QtCore import Slot
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QDialog, QLineEdit, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

from src.transform_tools.transform_tool2 import TransformTool2
from src.utils.exist_util import ExistUtil
from src.utils.excel_loader import ExcelLoader


class TransformDialog2(QDialog):

    def __init__(self, father_window, success_window):
        super().__init__()
        self.setWindowIcon(QIcon("./gui/ZZM.ico"))
        self.setWindowTitle("转换上表头")
        self.father_window = father_window
        self.success_window = success_window

        self.row_begin = QLineEdit()
        self.row_end = QLineEdit()
        self.row_begin_text = QLabel("表头起始行号：")
        self.row_end_text = QLabel("表头结束行号：")

        self.button = QPushButton("确认")
        self.button.clicked.connect(self.button_clicked)

        # 布局
        layout = QVBoxLayout()
        up_layout = QHBoxLayout()
        down_layout = QHBoxLayout()
        up_layout.addWidget(self.row_begin_text)
        up_layout.addWidget(self.row_begin)
        down_layout.addWidget(self.row_end_text)
        down_layout.addWidget(self.row_end)
        layout.addLayout(up_layout)
        layout.addLayout(down_layout)
        layout.addWidget(self.button)
        self.setLayout(layout)

    @Slot()
    def button_clicked(self):
        filename = self.father_window.widget.file_path.text()
        sheetname = self.father_window.widget.sheet_name_box.currentText()
        if ExistUtil.check_exists(filename, sheetname):
            excel_loader = ExcelLoader(filename, sheetname)
            workbook, worksheet = excel_loader.load_excel()
            logging.info("读取{}成功！".format(filename))
            self.father_window.widget.show_text("读取{}成功！".format(filename))
            begin_row = int(self.row_begin.text())
            end_row = int(self.row_end.text())

            transformTool2 = TransformTool2(workbook, worksheet, begin_row, end_row)
            new_workbook = transformTool2.excute()
            new_workbook.save(filename.split('/')[-1].replace(".xlsx", "_" + sheetname + "(只合并上表头).xlsx"))
            logging.info("转换上表头成功！")
            self.father_window.widget.show_text("转换上表头成功！")
            self.father_window.widget.show_text("--------------------")
            self.success_window.show()
        self.close()
