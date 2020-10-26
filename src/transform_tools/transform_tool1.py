import logging

from openpyxl import Workbook

from src.unmerge_tools.unmerge_tool import UnmergeTool


def str_to_int(chs: str) -> int:
    if chs[0].isdigit():
        return int(chs)
    else:
        num = 0
        for ch in chs:
            num *= 26
            if ord('A') <= ord(ch) <= ord('Z'):
                num += ord(ch) - ord('A') + 1
            elif ord('a') <= ord(ch) <= ord('z'):
                num += ord(ch) - ord('a') + 1
    return num


class TransformTool1:

    def __init__(self, filename: str, sheetname: str, data_row_begin: int,
                 data_row_end: int, data_col_begin: int, data_col_end: int):
        self.filename = filename
        self.sheetname = sheetname
        self.data_row_begin = data_row_begin
        self.data_row_end = data_row_end
        self.data_col_begin = data_col_begin
        self.data_col_end = data_col_end

    def read_and_write(self, worksheet) -> Workbook():
        total_rows = worksheet.max_row
        total_cols = worksheet.max_column
        top_attrs = total_rows - self.data_row_end + self.data_row_begin - 1
        left_attrs = total_cols - self.data_col_end + self.data_col_begin - 1
        logging.info(top_attrs)
        logging.info(left_attrs)
        # 创建新表格
        new_workbook = Workbook()
        new_sheet = new_workbook.create_sheet(self.sheetname)

        # 读取数据并写入到新表格
        new_row = 1
        count = 0
        for row in range(self.data_row_begin, self.data_row_end + 1):
            for col in range(self.data_col_begin, self.data_col_end + 1):
                data = str(worksheet.cell(row, col).value).strip()
                count += 1
                for top in range(1, self.data_row_begin):
                    new_sheet.cell(new_row, top, worksheet.cell(top, col).value.strip())
                for left in range(1, self.data_col_begin):
                    new_sheet.cell(new_row, left + top_attrs, worksheet.cell(row, left).value.strip())

                # 写入数值
                new_sheet.cell(new_row, top_attrs + left_attrs + 1, data)
                logging.info("数据[{}, {}]写入成功".format(row, col))
                new_row += 1

        logging.info("数据集有效数据个数：{}".format(count))

        return new_workbook

    def excete(self) -> Workbook:
        unmerge_tool = UnmergeTool(self.filename, self.sheetname)
        workbook = unmerge_tool.excute()
        worksheet = workbook[sheetname]
        new_workbook = self.read_and_write(worksheet)
        return new_workbook


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    filename = input('请输入excel文件名.后缀名: \n')
    sheetname = input("请输入{}需要转换的工作表名称：\n".format(filename))
    print("输入数据集的行列范围")
    data_row_begin = int(input('数据集起始行号：\n'))
    data_row_end = int(input('数据集结束行号：\n'))
    data_col_begin = str_to_int(input('数据集起始列号(英文字母或数字)：\n'))
    data_col_end = str_to_int(input('数据集结束列号(英文字母或数字)：\n'))

    transformTool1 = TransformTool1(filename, sheetname, data_row_begin, data_row_end, data_col_begin,
                                    data_col_end)
    new_workbook = transformTool1.excete()
    new_workbook.save(filename.replace(".xlsx", "_" + sheetname + "转换1.xlsx"))
    logging.info("转换成功！")
