from load_image import ft_load
from pimp_image import ft_blue, ft_green, ft_grey, ft_invert, ft_red


def main():
    try:
        array = ft_load("landscape.jpg")
        print(array)
        ft_invert(array)
        ft_red(array)
        ft_green(array)
        ft_blue(array)
        ft_grey(array)
        print(ft_invert.__doc__)
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
