import cv2 as cv
import numpy as np

img=cv.imread('Photos/cats.jpg')
cv.imshow('cats',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#Creating binary image from standalone image

# 1. Simple THresholding
threshold,thres=cv.threshold(gray,225,255,cv.THRESH_BINARY) #maxVal is if pixel>150 then set it to maxVal
cv.imshow('Thresh',thres)

threshold,thres_inverse=cv.threshold(gray,225,255,cv.THRESH_BINARY_INV) # maxval is if pixel<150 thenset it to maxval
cv.imshow('Thresh Inv',thres_inverse)

# 2. Adaptive Thresholding (becoz in 1. we have to specify threshod value. Here optimal value is automatically found)
adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,9)#blockSize is kSize, C value is integer subtracted from mean to fine tune thresholding
cv.imshow('Adaptive',adaptive_thresh)


cv.waitKey(0)