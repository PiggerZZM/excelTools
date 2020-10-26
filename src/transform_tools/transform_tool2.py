import logging

from src.unmerge_tools.unmerge_tool import UnmergeTool
from openpyxl import Workbook


class TransformTool2:

    def __init__(self, filename: str, sheetname: str, begin_row: int, end_row: int):
        self.filename = filename
        self.sheetname = sheetname
        self.begin_row = begin_row
        self.end_row = end_row

    def excute(self) -> Workbook:
        logging.info("正在拆分合并单元格，请稍等……")
        unmerge_tool = UnmergeTool(self.filename, self.sheetname)
        workbook = unmerge_tool.excute()
        worksheet = workbook[sheetname]

        max_column = worksheet.max_column  # 最大列数
        previous = ""
        for col in range(1, max_column + 1):
            temp = ""
            for row in range(begin_row, end_row + 1):
                if previous != str(worksheet.cell(row, col).value):
                    previous = str(worksheet.cell(row, col).value)
                    temp += previous
            worksheet.cell(end_row, col).value = temp
        worksheet.delete_rows(1, end_row - begin_row)
        return workbook


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    filename = input('请输入excel文件名.后缀名: \n')
    sheetname = input('输入工作表名：\n')
    begin_row = int(input("输入表头起始行："))
    end_row = int(input("输入表头结束行："))

    transformTool2 = TransformTool2(filename, sheetname, begin_row, end_row)
    new_workbook = transformTool2.excute()
    new_workbook.save(filename.replace(".xlsx", "_" + sheetname + "转换2.xlsx"))
    logging.info("转换成功！")
