import csv
import os
import math
import videoHandling


cwd = os.getcwd()
temp_dir2 = "" + cwd +"/temp_data"
os.mkdir(temp_dir2)

#fill in frame by frame data by interpolating x,y coordinates for saccades/fixations with durations
def interpolate(dict_data, fps):
    #store fixations and saccades as [start, x,y] coordinates
    all_points = []
    fixations = []
    saccades = []
    num_fixations = len(dict_data["CURRENT_FIX_X"])
    num_saccades = len(dict_data["CURRENT_FIX_START"])

    for i in range(1, num_fixations):
        d = dict_data["CURRENT_FIX_DURATION"][i]
        duration = int(math.floor((d * fps) // 1000))
        for frame in range(duration):
            curr_start = dict_data["CURRENT_FIX_START"][i]
            curr_x = dict_data["CURRENT_FIX_X"][i]
            curr_y = dict_data["CURRENT_FIX_Y"][i]
            curr_fix = [curr_start, curr_x, curr_y]
            fixations.append(curr_fix)

    for i in range(0, num_saccades):
        start = dict_data["CURRENT_SAC_START_TIME"][i]
        x1 = dict_data["CURRENT_SAC_START_X"][i]
        y1 = dict_data["CURRENT_SAC_START_Y"][i]
        saccades.append([start, x1, y1])
        x2 = dict_data["CURRENT_SAC_END_X"][i]
        y2 = dict_data["CURRENT_SAC_END_Y"][i]
        dur = dict_data["CURRENT_SAC_DURATION"][i]
        rise = y2 - y1
        run = x2 - x1
        steps = int(math.floor((dur * fps) // 1000))

        if steps > 1:
            slope_step_x = run / (steps)
            slope_step_y = rise / (steps)
            prev_x = x1
            prev_y = y1
            for s in range(steps):
                new_point_x = prev_x + slope_step_x
                new_point_y = prev_y + slope_step_y
                saccades.append([start, new_point_x, new_point_y])
                prev_x = new_point_x
                prev_y = new_point_y
            end = dict_data["CURRENT_SAC_END_TIME"][i]
            saccades.append([end, x2, y2])

    for f in fixations:
        all_points.append(f)
    for s in saccades:
        all_points.append(s)
    #sort all points by time stamp, ie. start time
    all_points.sort(key=lambda x: x[0])
    all_points.pop(0)
    while len(all_points) > videoHandling.get_num_frames():
    #while len(all_points) > 948:
        all_points.pop()

    for point in all_points:
        point.pop(0)
    return all_points


def organize(file_path):
    data = {}
    with open(file_path, 'r') as csvfile:
        datareader = list(csv.reader(csvfile))
    num_rows = len(datareader)

    #expected 10 columns in inputted data file
    #read columns of csv and convert into numerical values in a dictionary where key == column title
    try:
        for i in range(10):
            title = datareader[0][i]
            col = []
            for j in range(1, num_rows):
                val = datareader[j][i]
                if val == '':
                    val = 0
                else:
                    val = float(val)
                col.append(val)
            data[title] = col
    except:
        print("inputted csv: " + file_path + " has an invalid number of columns. Please double check your inputted data.")
        exit()
    sac_dur = []
    #calculate saccade duration
    try:
        num_saccades = len(data["CURRENT_SAC_START_TIME"])
        for i in range(num_saccades):
            calc = data["CURRENT_SAC_END_TIME"][i] - data["CURRENT_SAC_START_TIME"][i]
            sac_dur.append(calc)
        data["CURRENT_SAC_DURATION"] = sac_dur
    except:
        print("inputted csv: " + file_path + " has invalid data. Check for naming of columns and missing rows.")
        exit()
    try:
        return interpolate(data, 29)
    except:
        print("Failed to interpolate coordinates in: " + file_path)
        print("Check for naming of columns and missing rows.")
        exit()


#organize('examples/complete_input.csv')


def set_up(file_list):
    file_data = []
    for f in file_list:
        file_data.append(organize(f))
    num_frames = videoHandling.get_num_frames() - 1
    #num_frames = 947
    for x in range(1, num_frames + 1):
        csv_name = "" + temp_dir2 + "/frame" + str(x)
        with open(csv_name, 'w', newline='') as file:
            writer = csv.writer(file)
            for i in range(len(file_data)):
                row = file_data[i][x]
                newrow = []
                for val in row:
                    new = int(float(val))
                    newrow.append(new)
                writer.writerow(newrow)



#set_up(['examples/complete_input.csv'])
