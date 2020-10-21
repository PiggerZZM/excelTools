import logging

from src.unmerge_tools.unmerge_tool import UnmergeTool
from openpyxl import Workbook


class TransformTool2:

    def __init__(self, filename: str, sheetname: str):
        self.filename = filename
        self.sheetname = sheetname

    def excute(self) -> Workbook:
        logging.info("正在拆分合并单元格，请稍等……")
        unmerge_tool = UnmergeTool(filename, sheetname)
        workbook = unmerge_tool.excute()
        worksheet = workbook[sheetname]
        begin_row = int(input("输入表头起始行："))
        end_row = int(input("输入表头结束行："))
        max_column = worksheet.max_column  # 最大列数
        for col in range(1, max_column + 1):
            temp = ""
            for row in range(begin_row, end_row + 1):
                if temp != str(worksheet.cell(row, col).value):
                    temp += str(worksheet.cell(row, col).value)
            worksheet.cell(end_row, col).value = temp
        worksheet.delete_rows(1, end_row - begin_row)
        return workbook


if __name__ == '__main__':

    filename = input('请输入excel文件名.后缀名: \n')
    sheetname = input('输入工作表名：\n')
    transformTool2 = TransformTool2(filename, sheetname)
    new_workbook = transformTool2.excute()
    new_workbook.save(filename.replace(".xlsx", "_" + sheetname + "转换2.xlsx"))
    logging.info("转换成功！")
