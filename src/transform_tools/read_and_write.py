import logging

from src.transform_tools.int_to_upper_char import int_to_upper_char
import xlrd
import xlwt


def read_and_write(params: dict) -> xlwt.Workbook():
    filename_unmerged = params["filename_unmerged"]
    sheet_name = params["sheet_name"]
    data_row_end = params["data_row_end"]
    data_row_begin = params["data_row_begin"]
    data_col_end = params["data_col_end"]
    data_col_begin = params["data_col_begin"]
    logging.info("参数接收成功，开始处理" + filename_unmerged + ' ' + sheet_name)

    xlsx = xlrd.open_workbook(filename_unmerged)
    sheet = xlsx.sheet_by_name(sheet_name)
    total_rows = sheet.nrows
    total_cols = sheet.ncols
    top_attrs = total_rows - data_row_end + data_row_begin - 1
    left_attrs = total_cols - data_col_end + data_col_begin - 1

    # 创建新表格
    workbook = xlwt.Workbook()
    new_sheet = workbook.add_sheet(sheet_name)

    # 读取数据并写入到新表格
    new_row = 0
    count = 0
    for row in range(data_row_begin, data_row_end + 1):
        for col in range(data_col_begin, data_col_end + 1):
            data = str(sheet.cell_value(row, col)).strip()
            count += 1
            for top in range(data_row_begin):
                new_sheet.write(new_row, top, sheet.cell_value(top, col).strip())

            for left in range(data_col_begin):
                new_sheet.write(new_row, left + top_attrs, sheet.cell_value(row, left).strip())

            # 写入额外信息
            # write_extra(new_sheet, new_row, top_attrs, left_attrs, extra)

            # 写入数值
            new_sheet.write(new_row, top_attrs + left_attrs, data)

            logging.info("数据[{}, {}]写入成功".format(row, int_to_upper_char(col)))

            new_row += 1

    logging.info("数据集有效数据个数：{}".format(count))

    return workbook
