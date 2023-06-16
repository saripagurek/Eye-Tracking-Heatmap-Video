import csv
import random

rows = []

for i in range(5):
    col = random.randint(0, 400)
    row = random.randint(0, 400)
    rows.append([col, row])

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    writer.writerows(rows)