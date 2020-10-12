# 传入xlrd读入的workbook
import xlwt


def strip_util(workbook, name):
    new_workbook = xlwt.Workbook()
    sheet_names = workbook.sheet_names()
    for sheet_name in sheet_names:
        sheet = workbook[sheet_name]
        new_sheet = new_workbook.add_sheet(sheet)
        total_rows = sheet.nrows
        total_cols = sheet.ncols
        for row in total_rows:
            for col in total_cols:
                new_sheet.write(row, col, str(sheet.cell_value(row, col)).strip())
    new_workbook.save(name.replace(".xlsx", "_strip.xlsx"))
