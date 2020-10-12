import logging
import os
import time

from src.transform_tools.read_and_write import read_and_write
from src.transform_tools.upper_char_to_int import char_to_int

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    filename_unmerged = input('请输入excel文件名.后缀名: \n')
    if os.path.exists(filename_unmerged):
        while True:

            quit_flag = input("回车继续转换表格，按q退出程序。")
            if quit_flag == 'q' or quit_flag == 'Q':
                break

            sheet_name = input("请输入{}需要转换的工作表名称：\n".format(filename_unmerged))

            # 输入数据集的行列范围
            print("输入数据集的行列范围")
            data_row_begin = int(input('数据集起始行号：\n')) - 1
            data_row_end = int(input('数据集结束行号：\n')) - 1
            data_col_begin = char_to_int(input('数据集起始列号(英文字母)：\n'))
            data_col_end = char_to_int(input('数据集结束列号(英文字母)：\n'))

            params = {
                "filename_unmerged": filename_unmerged,
                "sheet_name": sheet_name,
                "data_row_begin": data_row_begin,
                "data_row_end": data_row_end,
                "data_col_begin": data_col_begin,
                "data_col_end": data_col_end,
            }

            # 读取数据并写入到新表格
            workbook = read_and_write(params)

            # 写入到excel
            workbook.save(filename_unmerged.replace('.xlsx', '_') + sheet_name + '.xls')
            logging.info(filename_unmerged.replace('.xlsx', '_') + sheet_name + '转换成功，写入到xls文件')
            time.sleep(1)
    else:
        logging.warning(filename_unmerged + "不存在!")
