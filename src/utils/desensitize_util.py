from datetime import datetime
from random import choices
from string import digits


class DesensitizeUtil:

    @staticmethod
    def desensitive(worksheet, col, tp):
        id_set = set()
        coln = ord(col) - ord('A')
        # 枚举excel中的所有行
        for index, row in enumerate(worksheet.rows, start=1):
            # 跳过表头
            if index == 1:
                continue
            if tp == '数值':  # 修改id
                random_id = ''.join(choices(digits, k=len(row[coln].value)))
                while random_id in id_set:  # 避免产生重复id
                    random_id = ''.join(choices(digits, k=len(row[coln].value)))
                id_set.add(random_id)
                worksheet[col + str(index)] = random_id
            elif tp == '日期':  # 修改日期
                random_date = datetime(row[coln].value.year, 1, 1)
                worksheet[col + str(index)] = random_date
        return worksheet
