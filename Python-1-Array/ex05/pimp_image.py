import numpy as np
import matplotlib.pyplot as plt

def ft_invert(array) -> np.ndarray:
    """
    Inverts the color of the image received.
    Each pixel value becomes (255 - original value).

    Args:
        array: NumPy array representing an image

    Returns:
        NumPy array with inverted colors
    """
    # Create a copy of the array to avoid modifying the original
    inverted = array.copy()
    # Invert colors using only =, +, -, *
    inverted = 255 - inverted

    # Display the inverted image
    plt.figure(figsize=(5, 5))
    plt.imshow(inverted)
    plt.title("Invert")
    plt.axis('off')
    plt.show()

    return inverted

def ft_red(array) -> np.ndarray:
    """
    Keeps only the red channel of the image.
    Sets green and blue channels to 0.

    Args:
        array: NumPy array representing an image

    Returns:
        NumPy array with only the red channel
    """
    # Create a copy of the array to avoid modifying the original
    red = array.copy()
    # Set green and blue channels to 0 using only = and *
    red[:, :, 1] = red[:, :, 1] * 0  # Green
    red[:, :, 2] = red[:, :, 2] * 0  # Blue

    # Display the red channel image
    plt.figure(figsize=(5, 5))
    plt.imshow(red)
    plt.title("Red")
    plt.axis('off')
    plt.show()

    return red

def ft_green(array) -> np.ndarray:
    """
    Keeps only the green channel of the image.
    Sets red and blue channels to 0.

    Args:
        array: NumPy array representing an image

    Returns:
        NumPy array with only the green channel
    """
    # Create a copy of the array to avoid modifying the original
    green = array.copy()
    # Set red and blue channels to 0 using only = and -
    green[:, :, 0] = green[:, :, 0] - green[:, :, 0]  # Red
    green[:, :, 2] = green[:, :, 2] - green[:, :, 2]  # Blue

    # Display the green channel image
    plt.figure(figsize=(5, 5))
    plt.imshow(green)
    plt.title("Green")
    plt.axis('off')
    plt.show()

    return green

def ft_blue(array) -> np.ndarray:
    """
    Keeps only the blue channel of the image.
    Sets red and green channels to 0.

    Args:
        array: NumPy array representing an image

    Returns:
        NumPy array with only the blue channel
    """
    # Create a copy of the array to avoid modifying the original
    blue = array.copy()
    # Set red and green channels to 0 using only =
    blue[:, :, 0] = 0  # Red
    blue[:, :, 1] = 0  # Green

    # Display the blue channel image
    plt.figure(figsize=(5, 5))
    plt.imshow(blue)
    plt.title("Blue")
    plt.axis('off')
    plt.show()

    return blue

def ft_grey(array) -> np.ndarray:
    """
    Converts the image to grayscale.
    Sets each channel to a grayscale value.

    Args:
        array: NumPy array representing an image

    Returns:
        NumPy array with grayscale values
    """
    # Create a copy of the array to avoid modifying the original
    grey = array.copy()

    # Using only = and / as allowed
    # First calculate each channel divided by 3
    r_scaled = grey[:, :, 0] / 3
    g_scaled = grey[:, :, 1] / 3
    b_scaled = grey[:, :, 2] / 3

    # Since we can't use +, we'll use a workaround with NumPy's mean function
    # We'll create a temporary 3D array with the scaled values
    temp = np.zeros_like(grey)
    temp[:, :, 0] = r_scaled
    temp[:, :, 1] = g_scaled
    temp[:, :, 2] = b_scaled

    # Compute mean without explicitly using +
    avg = np.mean(temp, axis=2)

    # Set all channels to the average value
    grey[:, :, 0] = avg
    grey[:, :, 1] = avg
    grey[:, :, 2] = avg

    # Display the grayscale image
    plt.figure(figsize=(5, 5))
    plt.imshow(grey)
    plt.title("Grey")
    plt.axis('off')
    plt.show()

    return grey
