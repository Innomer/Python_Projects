import cv2 as cv
import numpy as np

#Two ways:- Draw on original or Make a dummy image

blank=np.zeros((500,500,3),dtype='uint8') #Dummy/Blank Image:- 500,500,3 is dimensions(height width no of colour channels) and uint8 is data type of image
#cv.imshow('Blank',blank)

#img = cv.imread('Photos/cat.jpg')
#cv.imshow('Cat',img)

#1. Paint the image a certain colour
#blank[:]=0,255,0 #Referencing all the pixels
#cv.imshow('Green',blank)

#blank[200:300,300:400]=0,0,255 #Only certain part as red
#cv.imshow('RED',blank)

#2. Rectangle
#cv.rectangle(blank,(0,0),(img.shape[1]//2,img.shape[0]//2),(0,250,0),thickness=2)
#cv.imshow('rect',blank)
#Filled Rectangle
#cv.rectangle(blank,(0,0),(250,500),(0,250,0),thickness=-1) #thickness=cv.Filled also works
#cv.imshow('rectFilled',blank)

#3. Circle
#cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=-1)
#cv.imshow('Circle',blank)

#4. Line
#cv.line(blank,(300,100),(blank.shape[1]//2,blank.shape[0]//2),(255,0,0),thickness=2)
#cv.imshow('Line',blank)

#5. Text
cv.putText(blank,'HELLO!',(250,250),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=2) #Larger text may overflow.. so no other way of adjusting other than arranging origin and stuff
cv.imshow('Text',blank)

cv.waitKey(0)