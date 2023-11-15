import csv
filename = 'C:\Users\samue\first-py-steps\first-py-steps\data-download-16\chapter_16\the_csv_file_format\data\sitka_weather_07_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
