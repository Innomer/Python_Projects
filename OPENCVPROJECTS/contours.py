import cv2 as cv
import numpy as np

#CONTOURS ARE BOUNDARIES OF OBJECTS,LINE OR CURVE THAT JOINS POINTS ALONG BOUNDARIES
#MATHEMATICALLY CONTOURS!=EDGES
#USEFUL FOR SHAPE ANALYSIS AND OBJECT DETECTION/RECOGNITION

img=cv.imread('Photos/cats.jpg')
cv.imshow('Cats',img)

blank=np.zeros(img.shape,dtype='uint8')
cv.imshow('Blank',blank)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)
# METHOD 1: 

# blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
# cv.imshow('Blur',blur)

# canny=cv.Canny(blur,125,175)
# cv.imshow('Canny',canny)

# contours,hierarchies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)

# cv.findContours looks at the structural image and returns two values. 
# RETRLIST returns all contours, External only external contours, Tree only hierarchial contours
# Chain_none returns all... Simple compresses all into simple ones(EG:- None on a line gives all points of line while Simple on a line gives only endpoints as they are the simplest)

# print(f'{len(contours)} contours found')

# METHOD 2:Thresholding

# ret,thresh=cv.threshold(gray,125,255,cv.THRESH_BINARY) #gives only pixels with value betwenn 125 and 255.. Binary for 0 and 1 Pixel valuing only
# cv.imshow('Thresh',thresh)

# contours,hierarchies=cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
# print(f'{len(contours)} contours found')

# DRAWING CONTOURS ON BLANK IMAGE

# cv.drawContours(blank,contours, -1,(0,0,255),thickness=1) #-1 for all contours.. otherwise specify how many to draw
# cv.imshow('Contours Drawn', blank)

# USING CANNY FOR CONTOURS DRAWING
# canny=cv.Canny(img,125,175)
# contours,hierarchies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
# cv.drawContours(blank,contours, -1,(0,0,255),thickness=1)
# cv.imshow('Contours Drawn', blank)

#ADVICE:- USE CANNY FOR CONTOURING. AS SIMPLE THRESHOLDING HAS DISADVANTAGES


cv.waitKey(0)