import numpy as np
from PIL import Image
import os

def ft_load(path: str) -> np.ndarray:
    """
    Load an image from the given path, print its shape, and return its pixel content in RGB format.

    Args:
        path: Path to the image file

    Returns:
        NumPy array containing the image's pixel values in RGB format
    """
    # Check if the file exists
    if not os.path.exists(path):
        raise FileNotFoundError(f"Error: File '{path}' not found")

    try:
        # Attempt to open the image
        with Image.open(path) as img:
            # Check if the image format is supported
            if img.format not in ['JPEG', 'JPG']:
                # Convert format to uppercase for comparison
                if img.format.upper() not in ['JPEG', 'JPG']:
                    raise ValueError(f"Error: Unsupported image format '{img.format}'. Only JPG/JPEG formats are supported.")

            # Convert image to RGB mode if it's not already
            if img.mode != 'RGB':
                img = img.convert('RGB')

            # Convert image to numpy array
            img_array = np.array(img)

            # Print the shape of the image
            print(f"The shape of image is: {img_array.shape}")

            # Return the numpy array
            return img_array

    except Exception as e:
        if isinstance(e, ValueError):
            # Re-raise ValueError for format issues
            raise
        else:
            # Handle other exceptions
            raise RuntimeError(f"Error loading image: {str(e)}")
