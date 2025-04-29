import sys


def main():
    if len(sys.argv) != 2:
        print("AssertionError: the arguments are bad")
        return

    NESTED_MORSE = {
        " ": "/ ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "0": "----- ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "---. "
    }
    morse_code = ""
    message = sys.argv[1]
    for char in message:
        upper_char = char.upper()
        if upper_char in NESTED_MORSE:
            morse_code += NESTED_MORSE[upper_char]
        else:
            print("AssertionError: the arguments are bad")
            return

    print(morse_code[:-1])


if __name__ == "__main__":
    main()
