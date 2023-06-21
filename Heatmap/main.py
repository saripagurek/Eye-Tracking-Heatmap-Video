from tkinter import *
from tkinter import filedialog
import os
import imageHandling
import videoHandling
import preprocessing

csv_data = []
video_data = []

# Create tk window
win = Tk()
win.geometry("750x550")
win.title("Eye Tracking Heatmap")

def run():
   if (len(csv_data) >= 1) and (len(video_data) >= 1):
       csv_path = csv_data[0]
       vid_path = video_data[0]
       #print(csv_path)
       #print(vid_path)
       videoHandling.set_up()
       videoHandling.read_video(vid_path)
       preprocessing.set_up(csv_data)
       videoHandling.analyze_frames()
       print("num frames: " + str(videoHandling.get_num_frames()))
       videoHandling.clean_dir()


def open_csv():
    types = [('csv files', '*.csv')]
    file = filedialog.askopenfile(mode='r', filetypes=types)
    if file:
        csv_path = str(os.path.abspath(file.name))
        Label(win, text="Input Data : " + csv_path, font=('Helvetica 14')).pack()
        csv_data.append(csv_path)


def open_vid():
    types = [('video files', '*.mp4')]
    #types = [('image files', '*.png')]
    file = filedialog.askopenfile(mode='r', filetypes=types)
    if file:
        vid_path = str(os.path.abspath(file.name))
        Label(win, text="Input Video : " + vid_path, font=('Helvetica 14')).pack()
        video_data.append(vid_path)

# Label and buttons
Label(win, text="Import video and eye tracking data", font=('Helvetica 14 bold')).pack(pady=20)

Button(win, text="Load .csv", command=open_csv).pack(pady=10)
Button(win, text="Load .mp4", command=open_vid).pack(pady=10)
Button(win, text="Run", command=run).pack(pady=10)


win.mainloop()



