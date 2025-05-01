import sys
from ft_filter import ft_filter


def main():
    if len(sys.argv) != 3:
        print("AssertionError: the arguments are bad")
        return
    try:
        n = int(sys.argv[2])
        words = sys.argv[1].split()
        print(list(ft_filter(lambda word: len(word) > n, words)))
    except ValueError:
        print("AssertionError: the arguments are bad")
        return


if __name__ == "__main__":
    main()
