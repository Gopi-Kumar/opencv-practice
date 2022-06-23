# from asyncio import locks
# 0putChecker
import cv2
# program for chaging image or video to grayscale
cap = cv2.VideoCapture(0)

#saving video 
fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("output.avi", fourcc, 20.0,(640,480),0)

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
output.release() 
cv2.destroyAllWindows() 

# cap = cv2.VideoCapture("file://home/kali/Videos/video.mkv")

# while True:
#     ret,frame = cap.read()
#     frame = cv2.resize(frame, (700,450))
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     cv2.imshow("frame", frame)
#     cv2.imshow("gray", gray)
#     k = cv2.waitKey(500)
#     if k == ord("q") & 0xFF:
#        break
    


# cap.release()
# cv2.destroyAllWindows() 







# path = input("Enter the path and name of image==")

# print("Provided img path is ", path)
# img1 = cv2.imread(path,0)
# cv2.imshow("converted image ==", img1)
# cv2.resize(img1, (506,700))

# k = cv2.waitKey(0);
# if k==ord("s"):
#     cv2.imwrite("/home/kali/Downloads/output.jpeg",img1)
# else:
#     cv2.destroyAllWindows()
# cv2.distroyAllWindows()   0