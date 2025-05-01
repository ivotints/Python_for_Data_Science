import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    """
    Prints the shape of a 2D array and returns a sliced version.

    Args:
        family: A 2D array (list of lists)
        start: Starting index for slicing
        end: Ending index for slicing (exclusive)

    Returns:
        A sliced version of the 2D array
    """
    # Validate input is a list
    if not isinstance(family, list):
        raise TypeError("Input must be a list")

    # Check if empty
    if len(family) == 0:
        raise ValueError("Input list cannot be empty")

    # Validate all elements are lists
    if not all(isinstance(row, list) for row in family):
        raise TypeError("All elements must be lists")

    # Ensure all rows have the same length
    row_lengths = [len(row) for row in family]
    if len(set(row_lengths)) > 1:
        raise ValueError("All rows must have the same length")

    # Calculate and print shape
    shape = (len(family), len(family[0]) if family else 0)
    print(f"My shape is : {shape}")

    # Slice the array
    sliced_family = family[start:end]

    # Calculate and print new shape
    new_shape = (len(sliced_family), len(sliced_family[0]) if sliced_family else 0)
    print(f"My new shape is : {new_shape}")

    return sliced_family
