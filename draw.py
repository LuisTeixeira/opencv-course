import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

# 1. Paint the image
blank[200:300, 300:400] = 0, 255, 0
cv.imshow('Green', blank)

# Draw a rectangle
cv.rectangle(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (255, 0, 0), thickness=cv.FILLED)
cv.imshow("Rectangle", blank)

# Draw a circle
cv.circle(blank, (blank.shape[1] // 2, blank.shape[0] // 2), 40, (0, 0, 255), thickness=cv.FILLED)
cv.imshow("Circle", blank)

# Draw a line
cv.line(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255), thickness=3)
cv.imshow("Line", blank)

# Write text on an image
cv.putText(blank, 'Hello', (225, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255, 255, 255), 2)
cv.imshow("Text", blank)


cv.waitKey(0)
