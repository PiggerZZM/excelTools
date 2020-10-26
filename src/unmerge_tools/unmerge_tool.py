import logging
from copy import deepcopy

from openpyxl import load_workbook, Workbook

'''
    在实例化前需要先判断excel文件以及工作表是否存在
'''


class UnmergeTool:

    def __init__(self, filename: str, sheetname: str):
        self.filename = filename
        self.sheetname = sheetname
        self.workbook = load_workbook(self.filename)  # 读取excel
        self.worksheet = self.workbook[self.sheetname]  # 读取工作表

    def excute(self) -> Workbook:
        logging.info("正在拆分合并单元格，请稍等……")
        self.unmerge()
        return self.workbook

    def unmerge(self):
        # 获取所有 合并单元格的 位置信息
        # 是个可迭代对象，单个对象类型：openpyxl.worksheet.cell_range.MultiCellRange
        merged_list = deepcopy(self.worksheet.merged_cells)  # 深拷贝，进行拆分单元格的同时会改变worksheet.merged_cells
        logging.info("检测到{}_{}中合并单元格如下：".format(self.filename, self.sheetname))
        logging.info(merged_list)

        # 拆分合并的单元格 并填充内容
        for merged_area in merged_list:
            r1, r2, c1, c2 = merged_area.min_row, merged_area.max_row, merged_area.min_col, merged_area.max_col
            self.worksheet.unmerge_cells(start_row=r1, end_row=r2, start_column=c1, end_column=c2)
            # 获取左上角单元格的内容
            first_value = str(self.worksheet.cell(r1, c1).value).strip()
            # 数据填充
            for row in range(r1, r2 + 1):  # 遍历行
                for col in range(c1, c2 + 1):
                    self.worksheet.cell(row, col).value = first_value


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    filename = input('请输入excel文件名.后缀名: \n')
    sheetname = input("请输入工作表名：\n")
    unmerge_tool = UnmergeTool(filename, sheetname)
    new_workbook = unmerge_tool.excute()
    new_workbook.save(filename.replace('.xlsx', "_" + sheetname + '_unmerged.xlsx'))
    logging.info("解除合并单元格成功！")
