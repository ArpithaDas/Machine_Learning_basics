import cv2
img = cv2.imread("teletubbies.jpg")

img_H = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_HSV = cv2.cvtColor(img, cv2.COLOR_GRAYTOBGR)

cv2.imshow('HSV Imamge', img_HSV)

cv2.imshow('RED',img_HSV[:, :, 0])
cv2.imshow('GREEN',img_HSV[:, :, 1])
cv2.imshow('BLUE',img_HSV[:, :, 2])

cv2.waitKey(0)
cv2.destroyAllWindows()
