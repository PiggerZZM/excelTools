from datetime import datetime
from random import choices, randint
from string import digits

from src.utils.str_to_int import str_to_int


class DesensitizeUtil:

    @staticmethod
    def desensitive(worksheet, num_col_list: str, date_col_list: str):

        # 数值列脱敏处理
        # 空字符串split得到一个字符串的列表
        if num_col_list != '':
            hashtable = {}
            col_list = num_col_list.split(' ')
            if len(col_list) != 0:
                for col in col_list:
                    coln = str_to_int(col) - 1
                    # 枚举excel中的所有行
                    for row_index, row in enumerate(worksheet.rows, start=1):
                        # 跳过表头
                        if row_index == 1:
                            continue
                        id = row[coln].value
                        if id in hashtable:
                            random_id = hashtable[id]
                        else:
                            random_id = ''.join(choices(digits, k=len(str(row[coln].value))))
                            hashtable[id] = random_id
                        worksheet.cell(row_index, coln + 1, random_id)

        # 日期列脱敏处理
        if date_col_list != '':
            col_list = date_col_list.split(' ')
            for col in col_list:
                coln = str_to_int(col) - 1
                # 枚举excel中的所有行
                for row_index, row in enumerate(worksheet.rows, start=1):
                    # 跳过表头
                    if row_index == 1:
                        continue
                    random_date = datetime(randint(1940, 2020), randint(1, 12), randint(1, 28))
                    worksheet.cell(row_index, coln + 1, random_date)
