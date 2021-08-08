# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
import os
from glob import glob

png = glob(r"C:\Users\yusuf\PycharmProjects\YOLO\yolo_pretrained_image\images\*.png") # bu halde tum pngleri,*.jpeg halde spegleri jpg cevırır

for j in png:
    print(j)
    img = cv2.imread(j)
    cv2.imwrite(j[:-3]+"jpg",img)
    os.remove(j)