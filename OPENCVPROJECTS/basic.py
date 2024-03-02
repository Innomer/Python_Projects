import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)

# 1. Converting Colour Channels
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('GRAYSCALE', gray)

# 2. Blurring
# kSize is (odd,odd) tuple and says how much to blur
blur = cv.GaussianBlur(img, (3, 7), cv.BORDER_DEFAULT)
cv.imshow('BLUR', blur)

# 3. Edge Cascade (Finding edges)
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)

# Blurred passing helps in reducing detected edges
cannyBlurred = cv.Canny(blur, 125, 175)
cv.imshow('CannyBlur', cannyBlurred)

# 4. Dilate Image using specific structuring elements(in this case a canny)
# more iterations=more dilations
dilated = cv.dilate(cannyBlurred, (7, 7), iterations=3)
cv.imshow('Dilated', dilated)

# 5. Eroding Image (Finding Original image from dilated image (not perfect always))
eroded = cv.erode(dilated, (7, 7), iterations=3)
cv.imshow('Eroded', eroded)

# 6. Resizing
# resizes ignoring aspect ration
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
# INter_AREA is for reszing to smaller version while Inter_Linear or Cubic is for enlarging. Cubic is slowest but highest Res
cv.imshow('Resized', resized)

# 7. Cropping
# Since Images are Arrays of Pixels, you can slice them to crop them
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
