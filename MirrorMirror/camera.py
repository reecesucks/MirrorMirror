import os
import cv2
import pickle
import numpy as np
from PIL import Image, ImageTk


class Camera:
    def __init__(self):
        self.cfp = os.path.dirname(cv2.__file__) + "/data/haarcascade_frontalface_alt2.xml"
        fc = cv2.CascadeClassifier(self.cfp)
        self.cam = cv2.VideoCapture(0)

        # load the known faces and embeddings saved in last file
        self.data = pickle.loads(open('face_enc', "rb").read())

        self.frame = np.random.randint(0, 255, [100, 100, 3], dtype='uint8')
        #img = ImageTk.PhotoImage(Image.fromarray(frame))
        print('camera created')
    def get_img(self):
        ret, frame = self.cam.read()
        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #img = np.array(Image.fromarray(frame))
        return ret, frame
