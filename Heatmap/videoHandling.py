import cv2
import os
import shutil
import glob
import imageHandling


cwd = os.getcwd()
temp_dir = "" + cwd +"/temp_frames"
os.mkdir(temp_dir)

fps = 0
count = 1


def read_video(vid_path):
    global fps
    global count
    # Creating a VideoCapture object to read the video
    cap = cv2.VideoCapture(vid_path)
    count = 1
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Loop until the end of the video
    while (cap.isOpened()):

        # Capture frame-by-frame
        ret, frame = cap.read()

        if ret:
            name = "" + temp_dir + "/frame" + str(count) + ".png"
            cv2.imwrite(name.format(count), frame)
            #optional resizing
            '''
            cv2.imwrite(name.format(count), frame)
            count += 5
            cap.set(cv2.CAP_PROP_POS_FRAMES, count)
            
                try:
                frame = cv2.resize(frame, (540, 380), fx=0, fy=0, interpolation=cv2.INTER_CUBIC)
            except:
                break
            '''
            # Display the resulting frame
            cv2.imshow('Frame', frame)
            count += 1
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


def get_fps():
    global fps
    fps = int(fps)
    return fps


def get_num_frames():
    global count
    return count


def analyze_frames(csv_path):
    frame_size = imageHandling.get_specs("temp/frame1.png")

    out = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, frame_size)

    for filename in sorted(glob.glob('temp/*.png'), key=os.path.getmtime):
        name = filename[5:-4]
        imageHandling.analyze_image(filename, csv_path, name)

    for f in sorted(glob.glob('*.png'), key=os.path.getmtime):
        img = cv2.imread(f)
        out.write(img)

    out.release()