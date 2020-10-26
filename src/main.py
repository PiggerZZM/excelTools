import logging
import time

from src.transform_tools.transform_tool1 import TransformTool1, str_to_int
from src.transform_tools.transform_tool2 import TransformTool2
from src.unmerge_tools.unmerge_tool import UnmergeTool
from src.utils.exist_util import ExistUtil
from src.utils.file_loader import FileLoader

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    print("--------------------------------------------")
    print("1. 解除合并单元格并填充")
    print("2. 中式表头处理(转置)")
    print("3. 中式表头处理(只合并上表头)")
    print("--------------------------------------------")
    choice = int(input("选择使用的功能：\n"))

    logging.info("开始处理!")
    filename = input("输入excel文件名.xlsx: \n")
    sheetname = input("输入工作表名称：\n")

    if ExistUtil.check_exists(filename, sheetname):
        file_loader = FileLoader(filename, sheetname)
        workbook, worksheet = file_loader.load_file()
        logging.info("读取Excel成功！")
        if choice == 1:
            unmerge_tool = UnmergeTool(workbook, worksheet)
            new_workbook, new_worksheet = unmerge_tool.excute()
            new_workbook.save(filename.replace(".xlsx", "_" + sheetname + "unmerged.xlsx"))
            logging.info("转换成功！")
        elif choice == 2:
            print("输入数据集的行列范围")
            data_row_begin = int(input('数据集起始行号：\n'))
            data_row_end = int(input('数据集结束行号：\n'))
            data_col_begin = str_to_int(input('数据集起始列号(英文字母或数字)：\n'))
            data_col_end = str_to_int(input('数据集结束列号(英文字母或数字)：\n'))
            transformTool1 = TransformTool1(workbook, worksheet, data_row_begin, data_row_end, data_col_begin,
                                            data_col_end)
            new_workbook = transformTool1.excete()
            new_workbook.save(filename.replace(".xlsx", "_" + sheetname + "(转置).xlsx"))
            logging.info("转换成功！")
        elif choice == 3:
            print("输入表头的行号范围")
            begin_row = int(input("输入表头起始行："))
            end_row = int(input("输入表头结束行："))

            transformTool2 = TransformTool2(workbook, worksheet, begin_row, end_row)
            new_workbook = transformTool2.excute()
            new_workbook.save(filename.replace(".xlsx", "_" + sheetname + "(只合并上表头).xlsx"))
            logging.info("转换成功！")
    print("完成！")
    time.sleep(5)
