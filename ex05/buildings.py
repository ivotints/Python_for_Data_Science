import sys


def main():
    try:
        if len(sys.argv) > 2:
            print("AssertionError: Too many arguments")
            return
        elif len(sys.argv) == 2:
            text = sys.argv[1]
        else:
            print("What is the text to count?")
            try:
                text = input()
            except EOFError:
                text = ""
        upper = 0
        lower = 0
        punct = 0
        spaces = 0
        digits = 0
        punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

        for c in text:
            if c.isupper():
                upper += 1
            elif c.islower():
                lower += 1
            elif c in punctuation:
                punct += 1
            elif c.isdigit():
                digits += 1
            elif c.isspace():
                spaces += 1

        print(f"The text contains {len(text)} characters:")
        print(f"{upper} upper letters")
        print(f"{lower} lower letters")
        print(f"{punct} punctuation marks")
        print(f"{spaces} spaces")
        print(f"{digits} digits")
    except KeyboardInterrupt:
        print(" Quit")


if __name__ == "__main__":
    main()
