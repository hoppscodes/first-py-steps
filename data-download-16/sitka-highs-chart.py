import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'chapter_16/the_csv_file_format/data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)
#chart data   
plt.style.use('seaborn-v0_8-dark')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

#chart format
ax.set_title("highest temp recorded, july 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temp (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()