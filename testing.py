import cv2

img1 = cv2.imread("/home/kali/Downloads/img.jpeg",0)
print(img1)
cv2.imshow("original", img1)
cv2.waitKey()
cv2.destroyAllWindows()
