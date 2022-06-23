import cv2
import pafy


url = "https://www.youtube.com/watch?v=uts50CzLa6I"
data = pafy.new(url)
data = data.getbest(preftype='mp4')

cap = cv2.VideoCapture(0)

cap.open(data.url)

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.resize(frame, (700, 450))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame", frame)
        cv2.imshow("gray", gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


cap.release()
cv2.destroyAllWindows()
