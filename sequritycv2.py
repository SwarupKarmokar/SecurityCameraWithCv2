import cv2
import winsound

cam = cv2.VideoCapture(0)
while cam.isOpened():
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()
    diff = cv2.absdiff(frame1,frame2)

    gray = cv2.cvtColor(diff,cv2.COLOR_RGB2BGR)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _,thresh = cv2.threshold(blur, 20,255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    boundary, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(frame1, contours=boundary,contourIdx=-1, color=(0,0,255), thickness=2)
    for i in boundary:
        if cv2.contourArea(i) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(i)
        cv2.rectangle(frame1, (x,y), (x+w, y+h), (0,0,255), 2)
        winsound.Beep(500,200)

    cv2.imshow('image',frame1)
    if cv2.waitKey(2) & 0xFF == 27:
        break
cv2.destroyAllWindows()