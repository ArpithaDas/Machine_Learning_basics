import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
pts = np.array([[10,50], [400,50],[90,200],[50,350]], np.int32)




cv2.polylines(img, [pts], True, (0,0,255), 3) 
cv2.imshow('Polygon',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
