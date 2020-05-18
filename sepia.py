import cv2
import numpy as np
from PIL import Image

img = cv2.imread("lena.jpg")
height, width, depth = np.shape(img)

for i in range(0,height):
    for j in range(0,width):
        r=g=b=0
        r = img[i][j][0]*0.393 + img[i][j][1]*0.769 + img[i][j][2]*0.189
        g = img[i][j][0]*0.349 + img[i][j][1]*0.686 + img[i][j][2]*0.168
        b = img[i][j][0]*0.272 + img[i][j][1]*0.534 + img[i][j][2]*0.131
        
        if(r>255):
           r=255
        elif(r<0):
           r = 0 
           
        if(g>255):
           g=255
        elif(g<0):
           g = 0 
           
        if(b>255):
           b=255
        elif(b<0):
           b = 0         
        
        img[i][j][0] = b
        img[i][j][1] = g
        img[i][j][2] = r
        
cv2.imshow('image',img)
cv2.waitKey(0) 
