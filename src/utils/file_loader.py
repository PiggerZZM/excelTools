from openpyxl import load_workbook


class FileLoader:

    def __init__(self, filename, sheetname):
        self.filename = filename
        self.sheetname = sheetname

    def load_file(self):
        workbook = load_workbook(self.filename)
        worksheet = workbook[self.sheetname]
        return workbook, worksheet