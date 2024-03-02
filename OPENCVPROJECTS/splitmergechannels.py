import cv2 as cv
import numpy as np

img=cv.imread('Photos/park.jpg')
cv.imshow('Park',img)

# Splitting BGR to Blue, Green And Red Channels
b,g,r=cv.split(img)

# Displayed as Grayscale Images. Lighter Shade shows more concentration of that color in that area. 
cv.imshow('Blue',b)
cv.imshow('Green',g)
cv.imshow('Red',r)

print(img.shape) #3 Color Channels
print(b.shape) # No Color channel number means channels=1 therefore it is depicted as grayscale as grayscale has color channel as 1
print(g.shape)
print(r.shape)

# Merging B,G,R
merged = cv.merge([b,g,r])
cv.imshow('Merged',merged)

# Depicting B,G,R in their own colours rather than grayscale
blank=np.zeros(img.shape[:2],dtype='uint8')
blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])

cv.imshow('BLUE',blue)# Same rule as before.. Lighter=More
cv.imshow('GREEN',green)
cv.imshow('RED',red)

cv.waitKey(0)