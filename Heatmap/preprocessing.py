import csv
import os
#import videoHandling


cwd = os.getcwd()
temp_dir2 = "" + cwd +"/temp_data"
os.mkdir(temp_dir2)


def process_csv(file_path, fps):
    #filename = 'examples/input_data.csv'
    filename = file_path
    rows = []

    with open(filename, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        for row in datareader:
            duration = 1
            r = []
            for i in range(len(row)):
                row[i] = int(round(float(row[i])))
                if i <= 1:
                    r.append(row[i])
                elif i == 2:
                    duration = ((row[i] * fps) // 1000)
            for frame in range(duration):
                rows.append(r)

    with open('processed.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        writer.writerows(rows)


testlist = ['test1.csv', 'test2.csv', 'test3.csv']

def set_up(file_list):
    data = []

    for f in file_list:
        with open(f, 'r') as csvfile:
            datareader = list(csv.reader(csvfile))
            data.append(datareader)

    #num_frames = videoHandling.get_num_frames()
    num_frames = 20
    for x in range(num_frames):
        csv_name = "" + temp_dir2 + "/frame" + str(x)
        with open(csv_name, 'w', newline='') as file:
            writer = csv.writer(file)
            for f in data:
                row = f[x]
                writer.writerow(row)


test(testlist)

