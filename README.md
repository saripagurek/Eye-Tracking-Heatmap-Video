# Eye-Tracking-Heatmap

Python program to overlay heatmap of eye tracking data on a video.

Dependencies:
- numpy
  $ pip install numpy
- matplotlib
  $ pip install matplotlib
- tkinter
  $ pip install tk
- cv2 (opencv)
  $ pip install opencv-python
- pillow
  $ pip install Pillow

To run: 
1. From project directory, run main.py $ python main.py
2. Use the tkinter GUI to import one or more csv data files and one mp4 video file. The input data must be of the format:
 ![Example CSV Image](exampleCSV.png "Example CSV")
** Note that the headings DO matter **
4. Click 'Run'. The imported video will play as the program reads in the its individual frames. When the video playback window closes, you are free to exit the program.
5. The resulting video named 'output.mp4' will be located in the project directory.

