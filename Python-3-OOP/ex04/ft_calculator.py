class calculator:
    """calculator of vectors"""
    @staticmethod
    def dotproduct(V1: list[float | int], V2: list[float | int]) -> None:
        """Calc dot product"""
        if len(V1) == len(V2):
            print(f"Dot product is: {sum(x * y for x, y in zip(V1, V2))}")

    @staticmethod
    def add_vec(V1: list[float | int], V2: list[float | int]) -> None:
        """Calc sum"""
        if len(V1) == len(V2):
            print(f"Add Vector is : {list(x + y for x, y in zip(V1, V2))}")

    @staticmethod
    def sous_vec(V1: list[float | int], V2: list[float | int]) -> None:
        """Calc substaction"""
        if len(V1) == len(V2):
            print(f"Sous Vector is: {list(x - y for x, y in zip(V1, V2))}")
