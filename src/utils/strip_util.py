from openpyxl import Workbook


class StripUtil:

    @staticmethod
    def strip(workbook: Workbook, letter=' '):
        sheet_names = workbook.sheetnames
        new_workbook = Workbook()
        for sheet_name in sheet_names:
            sheet = workbook[sheet_name]
            new_sheet = new_workbook.create_sheet(sheet_name)
            total_rows = sheet.max_row
            total_cols = sheet.max_column
            for row in range(1, total_rows + 1):
                for col in range(1, total_cols + 1):
                    temp = sheet.cell(row, col).value
                    if temp is not None:
                        new_sheet.cell(row, col, str(temp).strip(letter))
        return new_workbook
