import logging

from PySide2.QtCore import QRect, Slot, Qt
from PySide2.QtWidgets import QFileDialog, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QWidget, \
    QComboBox

from src.unmerge_tools.unmerge_tool import UnmergeTool
from src.utils.exist_util import ExistUtil
from src.utils.file_loader import FileLoader
from src.utils.show_sheetnames import show_sheetnames
from src.utils.strip_util import StripUtil


class Widget(QWidget):

    def __init__(self, success_window):
        super().__init__()
        self.success_window = success_window
        self.sheetnames = ""

        # 左上的软件说明
        self.description = QLabel(
            '''软件说明：
处理Excel表格工具合集(校务数据中心自家用)
已实现功能：
    1. 解除合并单元格并填充
    2. 中式表头表格转换(转置)
    3. 中式表头表格转换(只处理上表头)
    4. 去除前后特定字符''')
        self.description.setGeometry(QRect(328, 240, 329, 27 * 4))
        self.description.setWordWrap(True)
        self.description.setAlignment(Qt.AlignTop)

        # 右边的程序输出信息
        self.output_info = QTextEdit()
        self.output_info.setReadOnly(True)

        # 左下的文件读取路径
        self.file_path_text = QLabel("表格所在位置：")
        self.file_path = QLineEdit()
        self.file_path.setReadOnly(True)
        self.file_path_button = QPushButton("打开")
        self.file_path_button.clicked.connect(self.open_file)

        # 左下的工作表名称
        self.sheet_name_text = QLabel("工作表名称：")
        self.sheet_name_box = QComboBox()

        # 左下的工具按钮
        self.unmerge_tool_button = QPushButton("解除合并单元格")
        self.unmerge_tool_button.clicked.connect(self.unmerge)
        self.transform_tool1_button = QPushButton("行列转置")
        self.transform_tool2_button = QPushButton("只处理上表头")
        self.strip_button = QPushButton("去除前后特定字符")

        # 布局
        self.layout = QHBoxLayout()
        self.file_path_layout = QHBoxLayout()
        self.button_layout = QHBoxLayout()
        self.left_layout = QVBoxLayout()
        self.sheet_name_layout = QHBoxLayout()

        # 将工具加入到布局
        self.button_layout.addWidget(self.unmerge_tool_button)
        self.button_layout.addWidget(self.transform_tool1_button)
        self.button_layout.addWidget(self.transform_tool2_button)
        self.button_layout.addWidget(self.strip_button)
        self.file_path_layout.addWidget(self.file_path_text)
        self.file_path_layout.addWidget(self.file_path)
        self.file_path_layout.addWidget(self.file_path_button)
        self.sheet_name_layout.addWidget(self.sheet_name_text)
        self.sheet_name_layout.addWidget(self.sheet_name_box)
        self.left_layout.addWidget(self.description)
        self.left_layout.addLayout(self.file_path_layout)
        self.left_layout.addLayout(self.sheet_name_layout)
        self.left_layout.addLayout(self.button_layout)
        self.layout.addLayout(self.left_layout)
        self.layout.addWidget(self.output_info)

        # 应用layout
        self.setLayout(self.layout)

    @Slot()
    def open_file(self):
        excel_file, _ = QFileDialog.getOpenFileName(self, 'Open file', '.', 'Excel files (*.xlsx)')
        if excel_file != "":
            logging.info("打开" + excel_file)
            self.sheetnames = show_sheetnames(excel_file)
            self.sheet_name_box.clear()
            self.sheet_name_box.addItems(self.sheetnames)
            self.file_path.setText(excel_file)
            output = "{}\n工作表名称：\n".format(excel_file)
            for sheetname in self.sheetnames:
                output += sheetname + "\n"
            self.show_text(output)

    @Slot()
    def unmerge(self):
        filename = self.file_path.text()
        sheetname = self.sheet_name_box.currentText()
        if ExistUtil.check_exists(filename, sheetname):
            file_loader = FileLoader(filename, sheetname)
            workbook, worksheet = file_loader.load_file()
            logging.info("读取{}成功！".format(filename))
            self.show_text("读取{}成功！".format(filename))
            unmerge_tool = UnmergeTool(workbook, worksheet)
            new_workbook, new_worksheet = unmerge_tool.excute()
            new_workbook.save(filename.split('/')[-1].replace(".xlsx", "_" + sheetname + "_unmerged.xlsx"))
            logging.info("解除合并单元格成功！")
            self.show_text("解除合并单元格成功！")
            self.show_text("--------------------")
            self.success_window.show()

    def show_text(self, info: str):
        temp = self.output_info.toPlainText() + info + '\n'
        self.output_info.setPlainText(temp)
