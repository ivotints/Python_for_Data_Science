import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
    Calculate BMI values from lists of height (in meters) and weight (in kg).

    Args:
        height: List of heights in meters
        weight: List of weights in kilograms

    Returns:
        List of BMI values
    """
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must have the same length")

    bmi_values = []
    for h, w in zip(height, weight):
        if not (isinstance(h, (int, float)) and isinstance(w, (int, float))):
            raise ValueError("All values in height and weight lists must be integers or floats")
        bmi = w / (h * h)
        bmi_values.append(bmi)

    return bmi_values

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Compare BMI values to a limit.

    Args:
        bmi: List of BMI values
        limit: The BMI limit to compare against

    Returns:
        List of booleans (True if BMI value is above the limit)
    """
    result = []
    for value in bmi:
        if not isinstance(value, (int, float)):
            raise ValueError("All values in BMI list must be integers or floats")
        result.append(value > limit)

    return result
