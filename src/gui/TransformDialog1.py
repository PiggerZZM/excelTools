import logging

from PySide2.QtCore import Slot
from PySide2.QtWidgets import QDialog, QLineEdit, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

from src.transform_tools.transform_tool1 import str_to_int, TransformTool1
from src.utils.exist_util import ExistUtil
from src.utils.file_loader import FileLoader


class TransformDialog1(QDialog):

    def __init__(self, father_window, success_window):
        super().__init__()
        self.setWindowTitle("转换工具1")
        self.father_window = father_window
        self.success_window = success_window

        self.data_row_begin = QLineEdit()
        self.data_row_end = QLineEdit()
        self.data_col_begin = QLineEdit()
        self.data_col_end = QLineEdit()

        self.data_row_begin_text = QLabel("数据集起始行号：")
        self.data_row_end_text = QLabel("数据集结束行号：")
        self.data_col_begin_text = QLabel("数据集起始列号：")
        self.data_col_end_text = QLabel("数据集结束列号：")

        self.button = QPushButton("确认")
        self.button.clicked.connect(self.button_clicked)

        # 布局
        layout = QVBoxLayout()
        up_layout = QHBoxLayout()
        down_layout = QHBoxLayout()
        up_layout.addWidget(self.data_row_begin_text)
        up_layout.addWidget(self.data_row_begin)
        up_layout.addWidget(self.data_row_end_text)
        up_layout.addWidget(self.data_row_end)
        down_layout.addWidget(self.data_col_begin_text)
        down_layout.addWidget(self.data_col_begin)
        down_layout.addWidget(self.data_col_end_text)
        down_layout.addWidget(self.data_col_end)
        layout.addLayout(up_layout)
        layout.addLayout(down_layout)
        layout.addWidget(self.button)
        self.setLayout(layout)

    @Slot()
    def button_clicked(self):
        filename = self.father_window.widget.file_path.text()
        sheetname = self.father_window.widget.sheet_name_box.currentText()
        if ExistUtil.check_exists(filename, sheetname):
            file_loader = FileLoader(filename, sheetname)
            workbook, worksheet = file_loader.load_file()
            logging.info("读取{}成功！".format(filename))
            self.father_window.widget.show_text("读取{}成功！".format(filename))
            data_row_begin = int(self.data_row_begin.text())
            data_row_end = int(self.data_row_end.text())
            data_col_begin = str_to_int(self.data_col_begin.text())
            data_col_end = str_to_int(self.data_col_end.text())
            transformTool1 = TransformTool1(workbook, worksheet, data_row_begin, data_row_end, data_col_begin,
                                            data_col_end)
            new_workbook = transformTool1.excete()
            new_workbook.save(filename.split('/')[-1].replace(".xlsx", "_" + sheetname + "(转置).xlsx"))
            logging.info("转置成功！")
            self.father_window.widget.show_text("转置成功！")
            self.father_window.widget.show_text("--------------------")
            self.success_window.show()
        self.close()
