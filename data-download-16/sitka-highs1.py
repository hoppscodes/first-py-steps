#this file prints tmax values contained in row 5 of the file.
import csv
filename = 'chapter_16/the_csv_file_format/data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)
print(highs)