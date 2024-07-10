import cv2

def image_to_sketch(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Invert the grayscale image
    inverted_image = cv2.bitwise_not(gray_image)

    # Apply Gaussian blur
    blurred_image = cv2.GaussianBlur(inverted_image, (21, 21), 0)

    # Invert the blurred image
    inverted_blurred_image = cv2.bitwise_not(blurred_image)

    # Create the final sketch by blending the grayscale image with the inverted blurred image
    sketch = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)

    return sketch

# Example usage
image_path = "C:\\Users\Gmini\Downloads\Get-Sketch-from-image-main\saman.jpeg"
sketch = image_to_sketch(image_path)
cv2.imshow('Sketch', sketch)
cv2.waitKey(0)
cv2.destroyAllWindows()
