import matplotlib.pyplot as plt
from load_image import ft_load


def main():
    try:
        image = ft_load("animal.jpeg")
        print(image)
        zoomed_image = image[100:500, 450:850, 0:1]
        print(f"New shape after slicing: {zoomed_image.shape}")
        print(zoomed_image)
        plt.figure()
        plt.imshow(zoomed_image, cmap='gray')
        plt.show()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
