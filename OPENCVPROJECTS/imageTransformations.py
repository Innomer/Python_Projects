import cv2 as cv
import numpy as np

#BASIC TRANSFORMATIONS ONLY


img=cv.imread('Photos/park.jpg')
cv.imshow('Park',img)

#1. Translation of Image(shifting along x,y axes)
def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]]) #Creating a Matrix to shift the image
    dimension=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimension)
    #-x=Left, -y=UP, x=Right, y=Down

translated=translate(img,-100,100)
cv.imshow('Translated',translated)

#2. Rotation
def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]

    if rotPoint==None:
        rotPoint=(width//2,height//2)
    
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions=(width,height)
    
    return cv.warpAffine(img,rotMat,dimensions)

    #positive angle is counterClock

rotated=rotate(img,45)
cv.imshow('Rotated',rotated)

rotated_rotated=rotate(rotated,45)
cv.imshow('Rotated_rotated',rotated_rotated) #Black Triangles come as in prev rotation you erased the triangles in image

#3. Resizing
resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

#4. Flipping
flipped=cv.flip(img,flipCode=-1) #flipcode=0(over X axis) or 1(Over y axis) or -1(Over Both Axes)
cv.imshow('Flip',flipped)

#5. Cropping
cropped=img[200:400,300:400]
cv.imshow('Crop',cropped)


cv.waitKey(0)