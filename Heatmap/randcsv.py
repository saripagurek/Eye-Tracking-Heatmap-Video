import csv
import random

rows = []

for i in range(5):
    col = random.randint(0, 1400)
    row = random.randint(0, 600)
    rows.append([col, row])

with open('datatest2.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    writer.writerows(rows)