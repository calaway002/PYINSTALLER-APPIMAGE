import cv2
import numpy as np

# Function to add two numbers
def add_numbers(a, b):
    return a + b

# Example of addition
result = add_numbers(5, 10)
print(f"The result of addition is: {result}")

# Create a blank white image using NumPy
image = np.ones((300, 300, 3), np.uint8) * 255

# Draw the result of the addition on the image using OpenCV
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, f'Result: {result}', (50, 150), font, 1, (0, 0, 0), 2, cv2.LINE_AA)

# Save the image
cv2.imwrite('result_image.png', image)

print("Image with addition result has been created as result_image.png")
