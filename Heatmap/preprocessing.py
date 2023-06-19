import csv
import videoHandling

#fps = videoHandling.get_fps()
fps = 30

filename = 'examples/input_data.csv'
rows = []

with open(filename, 'r') as csvfile:
    duration = 1
    datareader = csv.reader(csvfile)
    for row in datareader:
        r = []
        for i in range(len(row)):
            row[i] = int(round(float(row[i])))
            if i <= 1:
                r.append(row[i])
            elif i == 2:
                duration = ((row[i] * 30) // 1000)
        for frame in range(duration):
            rows.append(r)

with open('processed.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    writer.writerows(rows)