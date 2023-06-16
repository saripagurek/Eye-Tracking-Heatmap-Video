from tkinter import *
from tkinter import filedialog
import os

csv_data = []
video_data = []

# Create tk window
win = Tk()
win.geometry("750x550")
win.title("Eye Tracking Heatmap")

def run():
   print(csv_data)
   print(video_data)


def open_csv():
    types = [('csv files', '*.csv')]
    file = filedialog.askopenfile(mode='r', filetypes=types)
    if file:
        csv_path = str(os.path.abspath(file.name))
        Label(win, text="Input Data : " + csv_path, font=('Helvetica 14')).pack()
        csv_data.append(csv_path)


def open_vid():
    types = [('video files', '*.mp4')]
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



