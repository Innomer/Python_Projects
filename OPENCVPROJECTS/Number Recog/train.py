import sys
import cv2 as cv
import numpy as np
import sys

img=cv.imread(r'E:\OLD PC FILES\Mann Files\Game Dev\GIT REPO\OPENCVFILES\OPENCVPROJECTS\Number Recog\image.png')
img_copy=img.copy()

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
blur=cv.GaussianBlur(gray,(5,5),0)
thresh=cv.adaptiveThreshold(blur,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,5)



contours,hierarchy=cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)

samples=np.empty((0,100))
responses=[]
keys=[i for i in range(48,58)]


for cnt in contours:
    if cv.contourArea(cnt) > 50:
        [x,y,w,h]=cv.boundingRect(cnt)

        if h>28:
            cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            roi=thresh[y:y+h,x:x+w]
            roi_small=cv.resize(roi,(10,10))
            cv.imshow('norm',img)
            key=cv.waitKey(0)

            if key==27:
                sys.exit()
            elif key in keys:
                responses.append(int(chr(key)))
                sample = roi_small.reshape((1,100))
                samples = np.append(samples,sample,0)

responses = np.array(responses,np.float32)
responses = responses.reshape((responses.size,1))
print("training complete")

np.savetxt('generalsamples.data',samples)
np.savetxt('generalresponses.data',responses)