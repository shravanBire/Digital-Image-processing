import cv2
import numpy as np

image = cv2.imread(r"C:\Users\ASUS\OneDrive\Desktop\comding\DIP\LAB_1\Flower.jpg")

def grayscale_average(image):
    gray = np.mean(image, axis=2).astype(np.uint8)
    return gray

def grayscale_weighted(image):
    gray = (0.5 * image[:, :, 2] +
            0.6 * image[:, :, 1] +
            0.7 * image[:, :, 0]).astype(np.uint8)
    return gray

while True:
    print("1. Display image\n")
    print("2. Grayscale using Average Method (R+G+B)/3\n")
    print("3. Grayscale using Weighted Method 0.5R+0.6G+0.7B\n")
    print("0. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        cv2.imshow("My Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif choice == '2':
        gray = grayscale_average(image)
        cv2.imshow("Grayscale - Average Method", gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif choice == '3':
        gray = grayscale_weighted(image)
        cv2.imshow("Grayscale - Weighted Method", gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif choice == '0':
        print("Exiting program.")
        break

    else:
        print("Invalid choice\n")
