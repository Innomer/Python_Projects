import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Default Colour Space for OPENCV is BGR and for matplotlib is RGB

img=cv.imread('Photos/park.jpg')
cv.imshow('Park',img)

#BGR TO GRAYSCALE
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#BGR TO HSV (Hue Saturation Value)
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

#BGR TO L*A*B
lab=cv.cvtColor(img,cv.COLOR_BGR2Lab)
cv.imshow('LAB',lab)

#Displaying using Matplotlib
# plt.imshow(img)
# plt.show() #Different Color seen as Colors are inversed due to openCv using BGR scale and Matplotlib using RGB scale

#BGR to RGB
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb) #INVERSED COLORS AS CV IS BGR AND THIS IMAGE IS RGB
plt.imshow(rgb)
plt.show()

#HSV TO BGR POSSIBLE.. GRAY TO BGR YES, LAB TO BGR AND RGB TO BGR yes.. GRAY TO HSV DIRECTLY NOT POSSIBLE
hsvtobgr=cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
graytobgr=cv.cvtColor(gray,cv.COLOR_GRAY2BGR)
labtobgr=cv.cvtColor(lab,cv.COLOR_Lab2BGR)
rgbtobgr=cv.cvtColor(rgb,cv.COLOR_RGB2BGR)



cv.waitKey(0)