import cv2 as cv
import numpy as np

img=cv.imread('Photos/cats.jpg')
cv.imshow('Cats',img)

# Blurring is used for reducing noise in an image
# Kernal is a window you draw on a part of a image and something happens to pixels in this window.
# Kernal Size is number of rows n columns of a Kernal. Higher the size, more the Blur
# Blur is applied to a pixel due to effect of surrounding pixels.

# 1. Averaging:- Middle Pixel Intensity = Average of that of Surrounding Pixels
average=cv.blur(img,(3,3))
cv.imshow('Averaging',average)

# 2. Gaussian Blur:- Same as Averaging but instead of Averaging intensity, each surrounding pixel is given a weight and average of product of weights is given
# Less blurring than Averaging but more Natural
gauss=cv.GaussianBlur(img,(3,3),0) #sigmaX is standard deviation in X direction
cv.imshow('Gaussian',gauss)

# 3. Median Blur:- Same as Averaging but instead of average, it takes median of intensity of surrounding pixels. More effective in reducing noice than averaging and some extent of gaussian blur
median=cv.medianBlur(img,3) # Not meant for high KSizes
cv.imshow('Median',median)

# 4. Bilateral Blur:- 
bilateral=cv.bilateralFilter(img,5,15,15) # sigmaColor more means more colors in neighbourhood to be considered. SigmaSpace more means more pixels at a larger distance shall be considered while blurring
cv.imshow('Bilateral',bilateral)

cv.waitKey(0)