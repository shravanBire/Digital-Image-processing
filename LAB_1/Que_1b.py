import cv2
import numpy as np

image = cv2.imread(r"C:\Users\ASUS\OneDrive\Desktop\comding\DIP\LAB_1\Flower.jpg")

gray = np.mean(image, axis=2).astype(np.uint8)

threshold = 127

bw = np.zeros_like(gray)
bw[gray > threshold] = 255 


cv2.imshow("Original Image", image)
cv2.imshow("Black and White - Manual Method", bw)
cv2.waitKey(0)
cv2.destroyAllWindows()