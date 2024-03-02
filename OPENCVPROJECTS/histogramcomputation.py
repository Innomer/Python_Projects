import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img=cv.imread('Photos/cats.jpg')
cv.imshow('cats',img)

blank = np.zeros(img.shape[:2], dtype='uint8')

# Histogram gives graph of pixel density

# gray =cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('gray',gray)

circle=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)

# mask=cv.bitwise_and(gray,gray,mask=circle)
# cv.imshow('mask',mask)

# # Grayscale histogram
# gray_hist=cv.calcHist([gray],[0],mask,[256],[0,256])
# # Bins means intensity of pixels 0 is black and 256 is white

# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('No of Pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()


#Color Histogram
colors=('b','g','r')
plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('No of Pixels')

masked_image=cv.bitwise_and(img,img,mask=circle)
cv.imshow('mask',masked_image)

for i,col in enumerate(colors):
    hist=cv.calcHist([img],[i],circle,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
    
plt.show()



cv.waitKey(0)