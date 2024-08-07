Write a Program to read a digital image. Split and display image into 4 quadrants, up, 
down, right and left
------------------------------------------------------------------------------------------------
import cv2

# Load the image using the full path
img = cv2.imread(r"C:\Users\Pallavi\OneDrive\CG PYTHON LAB\demo.png")
# Check if the image was loaded successfully
if img is None:
    print("Error: Image not found or unable to load.")
else:
    # Get the dimensions of the image
    h, w, channels = img.shape

    # Horizontal division: Split the image into left and right parts
    half_width = w // 2
    left_part = img[:, :half_width]  # All rows, columns up to half
    right_part = img[:, half_width:]  # All rows, columns from half to the end

    # Vertical division: Split the image into top and bottom parts
    half_height = h // 2
    top = img[:half_height, :]  # All rows up to half, all columns
    bottom = img[half_height:, :]  # All rows from half to the end, all columns

    # Display the images
    cv2.imshow('Left part', left_part)
    cv2.imshow('Right part', right_part)
    cv2.imshow('Top', top)
    cv2.imshow('Bottom', bottom)

    # Save the images with different filenames
    cv2.imwrite(r'C:\Users\Pallavi\OneDrive\CG PYTHON LAB\top.jpg', top)
    cv2.imwrite(r'C:\Users\Pallavi\OneDrive\CG PYTHON LAB\bottom.jpg', bottom)
    cv2.imwrite(r'C:\Users\Pallavi\OneDrive\CG PYTHON LAB\right.jpg', right_part)
    cv2.imwrite(r'C:\Users\Pallavi\OneDrive\CG PYTHON LAB\left.jpg', left_part)

    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
