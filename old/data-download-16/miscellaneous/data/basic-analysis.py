import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = 'rodnovery-poland.csv'
df = pd.read_csv(data)
countmen = df['Płeć:'].value_counts()['Mężczyzna']
countwomen = df['Płeć:'].value_counts()['Kobieta']
filename = 'data/rodnovery-poland.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

males, voivodeships = [], []
for row in reader:
    men = int(row[2])
    voivodeships = int(row[3])

plt.bar
plt.show()


