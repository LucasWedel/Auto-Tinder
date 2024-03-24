import cv2

# Load an image
image = cv2.imread('C:\\Users\\lucas\\Downloads\\Test5.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Initialize HOG descriptor
hog = cv2.HOGDescriptor()

# Compute HOG features
features = hog.compute(gray)

# 'features' contains the HOG descriptors for the image
print(features)
