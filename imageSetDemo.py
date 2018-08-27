import cv2

img = cv2.imread("teletubbies.jpg")

cv2.imshow("Welcome",img)

cv2.waitKey(0)

cv2.destroyAllWindows()
