import cv2 as cv
import numpy as np
from numpy.lib.type_check import imag

img = cv.imread('Photos/cats 2.jpg')
cv.imshow('Cats', img)

# Size Of Mask should be same as image for it to work
blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank', blank)

circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
rectangle=cv.rectangle(blank.copy(),(30,30),(370,370), 255, -1)

weird_shape=cv.bitwise_and(circle,rectangle)
cv.imshow('Weird',weird_shape)


# masked_image = cv.bitwise_and(img, img, mask=mask)
# cv.imshow('Masked Image', masked_image)

masked_image = cv.bitwise_and(img, img, mask=weird_shape)
cv.imshow('WEird Masked Image', masked_image)


cv.waitKey(0)