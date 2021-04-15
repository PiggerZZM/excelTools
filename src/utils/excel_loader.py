from openpyxl import load_workbook


class ExcelLoader:

    def __init__(self, filename, sheetname):
        self.filename = filename
        self.sheetname = sheetname

    def load_excel(self):
        workbook = load_workbook(self.filename)
        worksheet = workbook[self.sheetname]
        return workbook, worksheet