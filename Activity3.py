import cv2
import numpy as np

img1= cv2.imread("teletubbies.jpg")

height, width = img1.shape[:2]

start_row, start_col = int(height*0.1), int(width*0.1)

end_row, end_col = int(height*0.25), int(width*0.25)

cropped = img1[start_row:end_row, start_col:end_col]


start_row1, start_col1 = int(height*0.25), int(width*0.25)

end_row1, end_col1 = int(height*0.5), int(width*0.5)

cropped1 = img1[start_row1:end_row1, start_col1:end_col1]


start_row2, start_col2 = int(height*0.5), int(width*0.5)

end_row2, end_col2 = int(height*0.75), int(width*0.75)

cropped2 = img1[start_row2:end_row2, start_col2:end_col2]


start_row3, start_col3 = int(height*0.75), int(width*0.75)

end_row3, end_col3 = int(height*1.0), int(width*1.0)

cropped3 = img1[start_row3:end_row3, start_col3:end_col3]


cv2.imshow("Original",img1)
cv2.waitKey(0)


cv2.imshow("Cropped",cropped)
cv2.waitKey(0)


cv2.imshow("Cropped1",cropped1)
cv2.waitKey(0)


cv2.imshow("Cropped2",cropped2)
cv2.waitKey(0)


cv2.imshow("Cropped3",cropped3)
cv2.waitKey(0)

cv2.destroyAllWindows()
