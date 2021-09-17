import logging

from src.utils.excel_loader import ExcelLoader
from src.utils.exist_util import ExistUtil
from src.utils.pinyin import str_to_pinyin


class HeaderToPinyinTool:
    """
    "表头转拼音首字母"功能
    """
    def __init__(self, worksheet):
        self.worksheet = worksheet

    def excute(self):
        max_column = self.worksheet.max_column  # 最大列数
        for col in range(1, max_column + 1):
            pinyin = str_to_pinyin(str(self.worksheet.cell(1, col).value))
            self.worksheet.cell(1, col).value = pinyin


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    filename = input('请输入excel文件名.后缀名: \n')
    sheetname = input('输入工作表名：\n')

    if ExistUtil.check_exists(filename, sheetname):
        excel_loader = ExcelLoader(filename, sheetname)
        workbook, worksheet = excel_loader.load_excel()
        header_to_pinyin_tool = HeaderToPinyinTool(worksheet)
        header_to_pinyin_tool.excute()
        workbook.save(filename.replace(".xlsx", "_" + sheetname + "转拼音.xlsx"))
        logging.info("转换成功！")
