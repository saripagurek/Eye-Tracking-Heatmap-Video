import csv
import random

rows = []

for i in range(20):
    col = random.randint(0, 400)
    row = random.randint(0, 400)
    rows.append([col, row])

#with open('test3.csv', 'w', newline='') as file:
    #writer = csv.writer(file)

    #writer.writerows(rows)

#for i in range(79):
    #print(random.randint(700, 900))