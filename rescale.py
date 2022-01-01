import cv2 as cv

#img = cv.imread('Photos/cat_large.jpeg')
#cv.imshow("Cat", img)


def rescaleFrame(frame, scale=0.75):
    # Images, Video and Live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def changeRes(width, height):
    # Live video
    cap.set(3, width)
    cap.set(4, height)


cap = cv.VideoCapture('Videos/dog.mp4')
while True:
    isTrue, frame = cap.read()

    frame_resized = rescaleFrame(frame, scale=.2)

    cv.imshow("Video Resized", frame_resized)
    cv.imshow("Video", frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

cap.release()
cv.destroyAllWindows()

cv.waitKey(0)