import pickle
import threading
import cv2
from sys import exit
from sqlHelper import sqlHelper
from audio_bank import AudioBank
from camera import Camera
import tkinter
from tkinter import *
import settings
import numpy as np
from PIL import Image, ImageTk
import face_recognition


def on_closing():
    root.destroy()
    sys.exit()


sql_Helper = sqlHelper(settings.host, settings.user, settings.password, settings.database)
audio_bank = AudioBank(sql_Helper)
data = pickle.loads(open('face_enc', "rb").read())
audio_bank.fill_bank()
print(len(audio_bank.message_bank))
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = Camera()
root = tkinter.Tk()
root.title("FaceReader")


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = screen_width
window_height = screen_height
# find the center point
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
panel = tkinter.Label(root) #, image=img)
panel.grid(row=0,column=0,columnspan=3,pady=1,padx=10)

def myloop():
    print('looop')
    def run():
    #count = 0
        count = 0
        while True:
            ret, frame = cam.get_img()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            new_img = np.array(Image.fromarray(frame))
            newer_img = ImageTk.PhotoImage(Image.fromarray(new_img))
            panel.configure(image=newer_img)
            panel.image = newer_img
            panel.update()
            count = count + 1
            if count == 25:
                check_faces(frame)
                count = 0
    print('starting thread')
    thread = threading.Thread(target=run)
    thread.start()

def check_faces(frame):
    print('check image')
    img = np.array(Image.fromarray(frame))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    faces = face_cascade.detectMultiScale(gray,
                                          scaleFactor=1.1,
                                          minNeighbors=6,
                                          minSize=(60, 60),
                                          flags=cv2.CASCADE_SCALE_IMAGE)
    encodings = face_recognition.face_encodings(rgb)
    names = []
    # loop over the facial embeddings incase
    # we have multiple embeddings for multiple fcaes
    for encoding in encodings:
        print('for encode', encoding)
        # Compare encodings with encodings in data["encodings"]
        # Matches contain array with boolean values True and False
        matches = face_recognition.compare_faces(data["encodings"], encoding)
        # set name =unknown if no encoding matches
        name = "Unknown"
        if True in matches:
            # Find positions at which we get True and store them
            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
            count = {}
            # loop over the matched indexes and maintain a count for
            # each recognized face face
        for i in matchedIdxs:
            # Check the names at respective indexes we stored in matchedIdxs
            name = data["names"][i]
            print("name ",name)
            # increase count for the name we got
            count[name] = count.get(name, 0) + 1
            # set name which has highest count
            name = max(count, key=count.get)
            # will update the list of names
            names.append(name)
            #img_update = ImageTk.PhotoImage(img)
            # if name == "Ming" and audio ==False:
            #     print('sound!!!!')
            #     audio =True
            #     os.system("mpg321 hello.mp3")
            # if name == "Reece" and audio == False:
            #     print('sound!!!!')
            #     audio = True
            #     os.system("mpg321 fuckyoureece.mp3")

            # do loop over the recognized faces
            # for ((x, y, w, h), name) in zip(faces, names):
            #     print('for')
                # rescale the face coordinates
                # draw the predicted face name on the image
               # cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                #cv2.putText(img, name, (x, y), cv2.FONT_HERSHEY_SIMPLEX,
                 #           0.75, (0, 255, 0), 2)

                # cv2.imshow("Frame", img_update)
                # cv2.waitKey(0)
           # new_img = ImageTk.PhotoImage(Image.fromarray(img))

            #panel.configure(image=new_img)
            #panel.image = new_img
            #panel.update()
            break
            k = cv2.waitKey(1)
            if cv2.waitKey(33) == ord('a'):
                # ESC pressed
                print("Escape hit, closing...")

                cam.release()
                cv2.destroyAllWindows()
                break

buttonLoop = Button(root, text="Start Loop", command=myloop)
buttonLoop.place(x=5, y=15)

# thread = threading.Thread(target=print)
# thread.start()

root.after(1, myloop)
root.mainloop()



