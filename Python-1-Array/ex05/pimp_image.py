import numpy as np
import matplotlib.pyplot as plt


def ft_display(img):
    """ft_Display image on plot"""
    plt.figure()
    plt.imshow(img, cmap='gray')
    plt.axis('off')
    plt.show()
    return img


def ft_invert(array) -> np.ndarray:
    """Inverts the color of the image received."""
    inverted = 255 - array
    ft_display(inverted)
    return inverted


def ft_red(array) -> np.ndarray:
    """Keeps only the red channel of the image."""
    red = array.copy()
    red[:, :, 1:] = 0
    ft_display(red)
    return red


def ft_green(array) -> np.ndarray:
    """Keeps only the green channel of the image."""
    green = array.copy()
    green[:, :, 0] = 0
    green[:, :, 2] = 0
    ft_display(green)
    return green


def ft_blue(array) -> np.ndarray:
    """Keeps only the blue channel of the image."""
    blue = array.copy()
    blue[:, :, :2] = 0
    ft_display(blue)
    return blue


def ft_grey(array) -> np.ndarray:
    """Converts the image to grayscale."""
    grey = array.copy()
    grey = np.mean(grey, axis=2)
    ft_display(grey)
    return grey
