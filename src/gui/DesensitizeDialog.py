import logging

from PySide2.QtCore import Slot
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QDialog

from src.utils.desensitize_util import DesensitizeUtil
from src.gui.UI.Ui_DesensitizeDialog import Ui_desensitizeDialog
from src.utils.excel_loader import ExcelLoader
from src.utils.exist_util import ExistUtil


class DesensitizeDialog(QDialog):
    """
    数据脱敏功能窗口
    """
    def __init__(self, father_window, success_window):
        super().__init__()
        self.setWindowIcon(QIcon("./gui/ZZM.ico"))
        self.father_window = father_window
        self.success_window = success_window

        # 应用UI
        self.ui = Ui_desensitizeDialog()
        self.ui.setupUi(self)

    @Slot()
    def on_OKButton_clicked(self):
        filename = self.father_window.widget.file_path.text()
        sheetname = self.father_window.widget.sheet_name_box.currentText()
        if ExistUtil.check_exists(filename, sheetname):
            excel_loader = ExcelLoader(filename, sheetname)
            workbook, worksheet = excel_loader.load_excel()
            logging.info("读取{}成功！".format(filename))
            self.father_window.widget.show_text("读取{}成功！".format(filename))
            DesensitizeUtil.desensitive(worksheet, self.ui.columnEdit.text(), self.ui.choiceBox.currentText())
            logging.info("数据脱敏成功！")
            self.father_window.widget.show_text("数据脱敏成功")
            filename_desensitize = filename.split('/')[-1].replace(".xlsx", "_" + sheetname + "(数据脱敏).xlsx")
            workbook.save(filename_desensitize)
            logging.info("保存成功")
            self.father_window.widget.show_text("写入文件{}\n".format(filename_desensitize))
            self.success_window.show()
        self.close()
