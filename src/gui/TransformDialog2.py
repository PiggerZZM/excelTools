import logging

from PySide2.QtCore import Slot
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QDialog

from src.gui.UI_file.Ui_TransformDialog2 import Ui_TransformDialog2
from src.transform_tools.transform_tool2 import TransformTool2
from src.utils.exist_util import ExistUtil
from src.utils.excel_loader import ExcelLoader


class TransformDialog2(QDialog):
    """
    "只转换表头"功能窗口
    """
    def __init__(self, father_window, success_window):
        super().__init__()
        self.setWindowIcon(QIcon("./gui/ZZM.ico"))
        self.father_window = father_window
        self.success_window = success_window

        # 应用UI
        self.ui = Ui_TransformDialog2()
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
            begin_row = int(self.ui.rowBegin.text())
            end_row = int(self.ui.rowEnd.text())

            transform_tool2 = TransformTool2(workbook, worksheet, begin_row, end_row)
            transform_tool2.excute()
            workbook.save(filename.split('/')[-1].replace(".xlsx", "_" + sheetname + "(只合并上表头).xlsx"))
            logging.info("转换上表头成功！")
            self.father_window.widget.show_text("转换上表头成功！")
            self.father_window.widget.show_text("--------------------")
            self.success_window.show()
        self.close()
