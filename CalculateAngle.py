import os
from CSVFile import CSVFile

data_directory = 'C:\\Users\\Tim\\Dropbox\\Research\\AOSConference2017\\CentroidPositionData'

csv = CSVFile(data_directory, os.listdir(data_directory)[0])

csv.open_csv('r')

[file_data, row] = csv.read_line()

num_of_rows = csv.find_num_of_rows()

print(row)