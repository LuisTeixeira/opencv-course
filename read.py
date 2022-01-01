import cv2 as cv

#img = cv.imread('Photos/cat_large.jpeg')
#cv.imshow("Cat", img)

# Reading Videos
cap = cv.VideoCapture('Videos/dog.mp4')
while True:
    isTrue, frame = cap.read()
    cv.imshow("Video", frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

cap.release()
cv.destroyAllWindows()