import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load

def manual_transpose(array):
    """
    Manually transpose a 2D array without using library functions.

    Args:
        array: 2D NumPy array

    Returns:
        Transposed 2D array
    """
    # Get the dimensions of the input array
    height, width = array.shape

    # Create a new array with swapped dimensions
    transposed = np.zeros((width, height), dtype=array.dtype)

    # Manually copy each element to its transposed position
    for i in range(height):
        for j in range(width):
            transposed[j, i] = array[i, j]

    return transposed

def main():
    try:
        # Load the image
        image = ft_load("animal.jpeg")

        # Get image dimensions
        h, w, c = image.shape

        # Determine the size of the square to cut (using the smaller dimension)
        square_size = min(h, w)

        # Calculate starting coordinates for the square (centered in the image)
        start_row = (h - square_size) // 2
        start_col = (w - square_size) // 2

        # Cut the square portion from the image and take only the first channel
        square = image[start_row:start_row+square_size, start_col:start_col+square_size, 0:1]

        # Print square info
        print(f"The shape of image is: {square.shape}")
        print(square)

        # Get a 2D array by squeezing the single channel
        square_2d = square.squeeze()

        # Transpose the square
        transposed = manual_transpose(square_2d)

        # Print transposed info
        print(f"New shape after Transpose: {transposed.shape}")
        print(transposed)

        # Display transposed image
        plt.figure(figsize=(6, 6))
        plt.imshow(transposed, cmap='gray')
        plt.title("Transposed Image")
        plt.axis('off')
        plt.show()

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
