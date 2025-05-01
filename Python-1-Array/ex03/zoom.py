import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load

def main():
    try:
        # Load the image
        image = ft_load("animal.jpeg")

        # Print image information
        print(image)  # This prints pixel content

        # Define the region to zoom (you can adjust these coordinates as needed)
        # Using coordinates that should work for most images
        # These are example coordinates - they can be modified
        h, w, c = image.shape
        center_h, center_w = h // 2, w // 2
        zoom_size = min(h, w) // 2

        y_start = center_h - zoom_size // 2
        y_end = center_h + zoom_size // 2
        x_start = center_w - zoom_size // 2
        x_end = center_w + zoom_size // 2

        # Ensure coordinates are valid
        y_start = max(0, y_start)
        y_end = min(h, y_end)
        x_start = max(0, x_start)
        x_end = min(w, x_end)

        # Slice the image to zoom in
        # Take only the first channel for grayscale effect
        zoomed_image = image[y_start:y_end, x_start:x_end, 0:1]

        # Print information about the zoomed image
        print(f"New shape after slicing: {zoomed_image.shape}")
        print(zoomed_image)

        # Create figure for plotting
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

        # Display original image with rectangle showing zoom area
        ax1.imshow(image)
        ax1.set_title("Original Image")
        ax1.add_patch(plt.Rectangle((x_start, y_start),
                                   x_end - x_start,
                                   y_end - y_start,
                                   edgecolor='r',
                                   facecolor='none',
                                   linewidth=2))

        # Display zoomed image
        zoomed_image_2d = zoomed_image.squeeze()  # Remove single-dimension axes if any
        ax2.imshow(zoomed_image_2d, cmap='gray')
        ax2.set_title("Zoomed Image")

        # Add scales to axes
        ax2.set_xticks(np.linspace(0, zoomed_image_2d.shape[1], 5))
        ax2.set_yticks(np.linspace(0, zoomed_image_2d.shape[0], 5))

        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
