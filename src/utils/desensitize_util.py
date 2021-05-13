from datetime import datetime
from random import choices
from string import digits

from src.utils.str_to_int import str_to_int


class DesensitizeUtil:

    @staticmethod
    def desensitive(worksheet, num_col_list: str, date_col_list: str):

        # 数值列脱敏处理
        id_set = set()
        col_list = num_col_list.split(' ')
        if len(col_list) != 0:
            for col in col_list:
                coln = str_to_int(col) - 1
                # 枚举excel中的所有行
                for row_index, row in enumerate(worksheet.rows, start=1):
                    # 跳过表头
                    if row_index == 1:
                        continue
                    random_id = ''.join(choices(digits, k=len(row[coln].value)))
                    while random_id in id_set:  # 避免产生重复id
                        random_id = ''.join(choices(digits, k=len(row[coln].value)))
                    id_set.add(random_id)
                    worksheet.cell(row_index, coln + 1, random_id)
                    # worksheet[col + str(index)] = random_id

        # 日期列脱敏处理
        col_list = date_col_list.split(' ')
        if len(col_list) != 0:
            for col in col_list:
                coln = str_to_int(col) - 1
                # 枚举excel中的所有行
                for row_index, row in enumerate(worksheet.rows, start=1):
                    # 跳过表头
                    if row_index == 1:
                        continue
                    random_date = datetime(row[coln].value.year, 1, 1)
                    worksheet.cell(row_index, coln + 1, random_date)
                    # worksheet[col + str(index)] = random_date
