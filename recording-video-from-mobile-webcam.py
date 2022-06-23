import cv2

camera = "https://192.168.43.1:8080/video"

cap = cv2.VideoCapture(0)
cap.open(camera)

fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("test.mp4", fourcc, 20.0, (640,400))

while cap.isOpened():
    ret,frame = cap.read()
    if ret == True:
        frame = cv2.resize(frame, (700,450))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame", frame)
        cv2.imshow("gray", gray)
        output.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


cap.release()
cv2.destroyAllWindows() 
