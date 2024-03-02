import cv2 as cv
import numpy as np

# 4 BITWSIE OPERATORS:- AND, OR, XOR and NOT
# BITWISE Operate in a binary manner. Pixel is turned off if value=0 and on if value=1

blank=np.zeros((400,400),dtype='uint8')

rectangle=cv.rectangle(blank.copy(),(30,30),(370,370), 255, -1)
circle=cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow('Rectangle',rectangle)
cv.imshow('Circle',circle)

# Bitwise And:- Takes Two images, puts one over other and returns intersection
bitwise_and=cv.bitwise_and(rectangle,circle) 
cv.imshow('BitAnd',bitwise_and)

# Bitwise OR:-Takes Two images, puts one over other and returns intersection as well as non intersection
bitwise_or=cv.bitwise_or(rectangle,circle) 
cv.imshow('BitOr',bitwise_or)

# Bitwise XOR:-Takes Two images, puts one over other and returns non intersection
bitwise_xor=cv.bitwise_xor(rectangle,circle) 
cv.imshow('BitXOr',bitwise_xor)

# Bitwise NOT:-Inverts Binary Color
bitwise_not=cv.bitwise_not(circle) 
cv.imshow('BitNOT',bitwise_not)


cv.waitKey(0)