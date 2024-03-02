import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('Parks', img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Gradients and edges are mathematically different but here you can consider same

# 1. Canny (already done)
canny=cv.Canny(gray,150,175)
cv.imshow('Canny',canny)

# 2. Laplacian (Looks like pencil shading of image and light smudge)
lap=cv.Laplacian(gray,cv.CV_64F) #ddepth=data depth
lap=np.uint8(np.absolute(lap))
cv.imshow('Laplacian',lap)

# 3. Sobel
# Computes in X and Y direction
sobelx=cv.Sobel(gray,cv.CV_64F,1,0)
sobely=cv.Sobel(gray,cv.CV_64F,0,1)
combined_sobel=cv.bitwise_or(sobelx,sobely)

cv.imshow('SobelX',sobelx)
cv.imshow('SobelY',sobely)
cv.imshow('CombinedSobel',combined_sobel)

cv.waitKey(0)