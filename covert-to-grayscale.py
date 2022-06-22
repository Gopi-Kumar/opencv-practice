import cv2
path = input("Enter the path and name of image==")

print("Provided img path is ", path)
img1 = cv2.imread(path,0)
cv2.imshow("converted image ==", img1)
cv2.waitKey();
cv2.distroyAllWindows()