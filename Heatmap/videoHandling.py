import cv2
import os
import shutil
import glob
import imageHandling


cwd = os.getcwd()
temp_dir = "" + cwd +"/temp"
os.mkdir(temp_dir)


def read_video(vid_path):
    # Creating a VideoCapture object to read the video
    cap = cv2.VideoCapture(vid_path)
    count = 1

    # Loop until the end of the video
    while (cap.isOpened()):

        # Capture frame-by-frame
        ret, frame = cap.read()

        if ret:
            name = "" + temp_dir + "/frame" + str(count) + ".png"
            cv2.imwrite(name.format(count), frame)
            #optional resizing
            '''
                try:
                frame = cv2.resize(frame, (540, 380), fx=0, fy=0, interpolation=cv2.INTER_CUBIC)
            except:
                break
            '''
            # Display the resulting frame
            cv2.imshow('Frame', frame)
            count += 5
            cap.set(cv2.CAP_PROP_POS_FRAMES, count)

            # define q as the exit button
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            # release the video capture object
            cap.release()
            cv2.destroyAllWindows()


def clean_dir():
    shutil.rmtree(temp_dir)


def analyze_frames():
    frame_size = imageHandling.get_specs("temp/frame1.png")

    out = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 5, frame_size)

    for filename in glob.glob('temp/*.png'):
        img = cv2.imread(filename)
        out.write(img)

    out.release()