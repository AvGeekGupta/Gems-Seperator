# File Name - Image_Capture.py
# Created by Vanshaj Goel
##############################


import cv2
import extcolors
import numpy as np
from datetime import datetime


class ImageCapture:
    def click_image(self):
        now = datetime.now()
        dt_string = now.strftime("%d%m%Y%H%M%S")
        camera = cv2.VideoCapture(0)
        return_value, image = camera.read()
        cv2.imwrite('./Images/opencv' + dt_string + '.png', image)
        cv2.imwrite('./Images/default.jpg', image)
        del camera
        img = cv2.imread('./Images/opencv' + dt_string + '.png')
        img = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
        cv2.imwrite('./Images/opencv' + dt_string + '.png', img)
        colors, pixel_count = extcolors.extract('./Images/opencv' + dt_string + '.png')
        return np.array([[(colors[0])[0][0]],
                         [(colors[0])[0][1]],
                         [(colors[0])[0][2]]])
