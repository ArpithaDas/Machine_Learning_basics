import cv2
#import numpy as np
img = cv2.imread("teletubbies.jpg")

smaller = cv2.pyrDown(img)
larger = cv2.pyrUp(img)

cv2.imshow('original', img)
cv2.imshow('Smaller', smaller)
cv2.imshow('Larger', larger)

cv2.waitKey(0)
cv2.destroyAllWindows()

