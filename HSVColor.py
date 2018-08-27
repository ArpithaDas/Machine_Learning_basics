import cv2
img = cv2.imread("teletubbies.jpg")

img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('HSV Imamge', img_HSV)

cv2.imshow('HUE CHANNEL',img_HSV[:, :, 0])
cv2.imshow('SATURATION',img_HSV[:, :, 1])
cv2.imshow('VALUE CHANNEL',img_HSV[:, :, 2])

cv2.waitKey(0)
cv2.destroyAllWindows()
