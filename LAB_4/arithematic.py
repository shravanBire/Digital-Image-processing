import cv2
import numpy as np

img1 = cv2.imread('cat.jpg')
img2 = cv2.imread('dog.jpg')

img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

added = np.clip(img1 + img2, 0, 255).astype(np.uint8)
cv2.imwrite("added.jpg",added)

subtracted = np.clip(img1 - img2, 0, 255).astype(np.uint8)
cv2.imwrite("sub.jpg",subtracted)

multiplied = np.clip(img1 * img2, 0, 255).astype(np.uint8)
cv2.imwrite("mul.jpg",multiplied)

divided = np.clip(img1 / (img2 + 1), 0, 255).astype(np.uint8)
cv2.imwrite("div.jpg",divided)


print(img1.shape)
cv2.imshow("Image 1", img1)
cv2.imshow("Image 2", img2)
cv2.imshow("Added", added)
cv2.imshow("Subtracted", subtracted)
cv2.imshow("Multiplied", multiplied)
cv2.imshow("Divided", divided)
cv2.waitKey(0)
cv2.destroyAllWindows()