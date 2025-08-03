import cv2
import numpy as np

image = cv2.imread(r"C:\Users\ASUS\OneDrive\Desktop\comding\DIP\LAB_1\Flower.jpg")

B, G, R = cv2.split(image)

zeros = np.zeros_like(B)

blue_frame = cv2.merge([B, zeros, zeros])
green_frame = cv2.merge([zeros, G, zeros])
red_frame = cv2.merge([zeros, zeros, R])

cv2.imshow("Blue Frame (Color)", blue_frame)
cv2.imshow("Green Frame (Color)", green_frame)
cv2.imshow("Red Frame (Color)", red_frame)

cv2.waitKey(0)
cv2.destroyAllWindows()
