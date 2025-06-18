class calculator:
    """A calculator class that is able to do
    calculations of vector with a scalar."""
    def __init__(self, numbers):
        self.numbers = numbers

    def __add__(self, object) -> None:
        """addition"""
        for i, _ in enumerate(self.numbers):
            self.numbers[i] += object
        print(self.numbers)

    def __mul__(self, object) -> None:
        """multiplication"""
        for i, _ in enumerate(self.numbers):
            self.numbers[i] *= object
        print(self.numbers)

    def __sub__(self, object) -> None:
        """substraction"""
        for i, _ in enumerate(self.numbers):
            self.numbers[i] -= object
        print(self.numbers)

    def __truediv__(self, object) -> None:
        """devision"""
        if object == 0:
            raise ZeroDivisionError()
        for i, _ in enumerate(self.numbers):
            self.numbers[i] /= object
        print(self.numbers)
