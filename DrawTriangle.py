import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
pts1 = np.array([[80,340], [370,340],[220,70]], np.int32)
pts2 = np.array([[80,125], [370,125],[215,390]], np.int32)




cv2.polylines(img, [pts1], True, (0,0,255), 3)
cv2.polylines(img, [pts2], True, (255,0,0), 3)
cv2.imshow('Polygon',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
