import sys

try:
    if len(sys.argv) == 1:
        pass
    elif len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")
    else:
        num = int(sys.argv[1])
        if num % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
except ValueError:
    print("AssertionError: argument is not an integer")
except AssertionError as e:
    print(f"AssertionError: {e}")
