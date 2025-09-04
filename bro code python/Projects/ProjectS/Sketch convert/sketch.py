import numpy as np
import imageio
import scipy.ndimage
import cv2

img = "car.jpg"

def rgb2gray(rgb):
    # Corrected to ensure the formula uses consistent indentation and the correct output
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])
    # It's a 2D array formula to convert an image to grayscale

def dodge(front, back):
    # Added a small epsilon value to prevent division by zero errors
    epsilon = 1e-6
    final_sketch = front * 255 / (255 - back + epsilon)
    # Clip values to the valid range
    final_sketch[final_sketch > 255] = 255
    final_sketch[back == 255] = 255  # To convert any suitable column to categorical type
    return final_sketch.astype('uint8')  # Corrected the datatype to 'uint8'

# Read the image using imageio
ss = imageio.imread(img)
# Convert the image to grayscale
gray = rgb2gray(ss)

# Invert the grayscale image
i = 255 - gray
# 0, 0, 0 is for the darkest color, 255, 255, 255 is for the brightest color (probably white)

# Apply a Gaussian filter for blurring
blur = scipy.ndimage.gaussian_filter(i, sigma=15)  # Updated to avoid deprecated API usage
# `scipy.ndimage.filters` is deprecated; use `scipy.ndimage` directly

# Convert the image to a sketch
r = dodge(blur, gray)

# Save the final sketch
cv2.imwrite('car-sketch.png', r)
