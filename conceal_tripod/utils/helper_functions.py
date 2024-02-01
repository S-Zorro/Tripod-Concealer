import cv2
import numpy as np
from PIL import Image

def draw_circle(radius):
    # Create a black background with dimensions 500x500 pixels
    image = np.zeros((1024, 1024, 3), dtype="uint8")

    # Define the center of the image
    center_coordinates = (512, 512)

    # Define the color of the circle (white in this case)
    color = (255, 255, 255)

    # Draw the circle
    cv2.circle(image, center_coordinates, radius, color, -1)

    return Image.fromarray(image)
    # cv2.imwrite('image_mask.png', image)
