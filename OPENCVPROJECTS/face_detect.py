import cv2 as cv
import numpy as np

img = cv.imread('Photos/group 1.jpg')
cv.imshow('Group', img)

# Face Detection is only presence of Face check. Doesnt identify who it is
# Haar Cascade uses edges to detect whether a face or not. 
# Haar Cascade is a classifier that has been trained to tell what a face is. Another classifier is Local Binarypatterns which is advanced for us now.



gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# Reading Haar_face.xml
haar_cascade=cv.CascadeClassifier('haar_face.xml') # Passing path of xml file. This reads the xml code n stores it in the variable

faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=1) # Returns list of rectangular coordinates of face

print(f'No of faces found = {len(faces_rect)}')

for(x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv.imshow('Face',img)

# Haar Cascade are really sensitive to noise. Therefore we get 7 faces while using group 2 image.
# Therefore we can increase minNeighbors to reduce noise

# Live Video Face Detection:
capture=cv.VideoCapture(0)

while True:
    isTrue,frame=capture.read()
    #cv.imshow('Live',frame)
    gray_frame=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    faces_rect_live=haar_cascade.detectMultiScale(gray_frame,scaleFactor=1.1,minNeighbors=3)
    for(x,y,w,h) in faces_rect_live:
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    cv.imshow('Face_Live',frame)

    if cv.waitKey(20) & 0xFF==ord('d'): #To Break and Stop Infinite Repeation of Video
        #0xFF says if d is pressed or not
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)