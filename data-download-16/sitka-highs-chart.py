import csv
import matplotlib.pyplot as plt

filename = 'chapter_16/the_csv_file_format/data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)
#chart data   
plt.style.use('seaborn-v0_8-dark')
fig, ax = plt.subplots()
ax.plot(highs, c='red')

#chart format
ax.set_title("highest temp recorded, july 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Temp (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()