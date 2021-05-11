import logging

from PySide2.QtCore import Slot
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QDialog

from src.gui.UI.Ui_TransformDialog1 import Ui_TransformDialog1
from src.transform_tools.transform_tool1 import TransformTool1
from src.utils.exist_util import ExistUtil
from src.utils.excel_loader import ExcelLoader
from src.utils.str_to_int import str_to_int


class TransformDialog1(QDialog):
    """
    "行列转置"功能窗口
    """
    def __init__(self, father_window, success_window):
        super().__init__()
        self.setWindowIcon(QIcon("./gui/ZZM.ico"))
        self.setWindowTitle("行列转置")
        self.father_window = father_window
        self.success_window = success_window

        # 应用UI
        self.ui = Ui_TransformDialog1()
        self.ui.setupUi(self)

    @Slot()
    def on_okButton_clicked(self):
        filename = self.father_window.widget.file_path.text()
        sheetname = self.father_window.widget.sheet_name_box.currentText()
        if ExistUtil.check_exists(filename, sheetname):
            excel_loader = ExcelLoader(filename, sheetname)
            workbook, worksheet = excel_loader.load_excel()
            logging.info("读取{}成功！".format(filename))
            self.father_window.widget.show_text("读取{}成功！".format(filename))
            data_row_begin = int(self.ui.dataRowBegin.text())
            data_row_end = int(self.ui.dataRowEnd.text())
            data_col_begin = str_to_int(self.ui.dataColBegin.text())
            data_col_end = str_to_int(self.ui.dataColEnd.text())
            transform_tool1 = TransformTool1(workbook, worksheet, data_row_begin, data_row_end, data_col_begin,
                                            data_col_end)
            new_workbook = transform_tool1.excute()
            new_workbook.save(filename.split('/')[-1].replace(".xlsx", "_" + sheetname + "(转置).xlsx"))
            logging.info("转置成功！")
            self.father_window.widget.show_text("转置成功！")
            self.father_window.widget.show_text("--------------------")
            self.success_window.show()
        self.close()
