import time
import csv


class CSVFile:

    def __init__(self, file_path, file_name):
        self.file_name = file_path + '\\' + file_name
        self.analysis_date = time.strftime("%d_%m_%Y")
        self.file_access_type = ''
        self.fid = ''
        self.row_data = []

    def open_csv(self,file_privilege):
        self.file_access_type = file_privilege
        self.fid = open(self.file_name, 'r')
        return self.fid

    def read_line(self):
        self.file_data = csv.reader(self.fid)
        self.row = next(self.file_data)
        return [self.file_data, self.row]

    def find_num_of_rows(self):
        row_number_array = []

        for row_numbers in self.file_data:
            row_number_array.append(self.file_data.line_num)

        num_of_rows = max(row_number_array)

        return num_of_rows
