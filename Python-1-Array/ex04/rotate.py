import matplotlib.pyplot as plt
from load_image import ft_load


def main():
    try:
        image = ft_load("animal.jpeg")
        zoomed_image = image[100:500, 450:850, 0:1]
        print(f"The shape of image is: {zoomed_image.shape}")
        print(zoomed_image)
        zoomed_image = zoomed_image.squeeze()

        transposed = zoomed_image.copy()
        for i in range(400):
            for j in range(400):
                transposed[j, i] = zoomed_image[i, j]

        print(f"New shape after Transpose: {transposed.shape}")
        print(transposed)
        plt.figure()
        plt.imshow(transposed, cmap='gray')
        plt.show()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
