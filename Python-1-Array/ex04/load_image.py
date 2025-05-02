import numpy as np
from PIL import Image
import os


def ft_load(path: str) -> np.ndarray:
    """
    Load an image from the given path, print its shape,
    and return its pixel content in RGB format.

    Args:
        path: Path to the image file

    Returns:
        NumPy array containing the image's pixel values in RGB format
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"File '{path}' not found")
    with Image.open(path) as img:
        if img.format not in ['JPEG', 'JPG']:
            raise ValueError(f"Unsupported image format '{img.format}'. "
                             f"Only JPG/JPEG formats are supported.")
        if img.mode != 'RGB':
            img = img.convert('RGB')
        img_array = np.array(img)
        return img_array
