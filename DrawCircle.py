import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)


cv2.imshow('Original Image',img)
cv2.circle(img, (300, 300), (100),(0,0,255), -1)

cv2.imshow('Circle',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
