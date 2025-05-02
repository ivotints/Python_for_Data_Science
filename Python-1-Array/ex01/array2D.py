def slice_me(family: list, start: int, end: int) -> list:
    """
    Prints the shape of a 2D array and returns a sliced version.

    Args:
        family: A 2D array (list of lists)
        start: Starting index for slicing
        end: Ending index for slicing (execlusive)

    Returns:
        A sliced version of the 2D array
    """
    if not isinstance(family, list):
        raise TypeError("Input must be a list")
    if len(family) == 0:
        raise ValueError("Input list cannot be empty")
    if not all(isinstance(row, list) for row in family):
        raise TypeError("All elements must be lists")
    row_lengths = [len(row) for row in family]
    if len(set(row_lengths)) > 1:
        raise ValueError("All rows must have the same length")

    print(f"My shape is : ({len(family)}, {len(family[0])})")
    family = family[start:end]
    print(f"My new shape is : ({len(family)}, {len(family[0])})")

    return family
