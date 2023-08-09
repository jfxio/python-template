"""An example module with a couple of simple functions."""
from collections.abc import Iterator


def total(integers: Iterator[int]) -> int:
    """
    Sum the provided integers.

    Args:
        integers (Iterator[int]): the integers to sum

    Returns:
        int: the sum of integers (0 if integers is empty)
    """
    return sum(integers)


def total_squares(integers: Iterator[int]) -> int:
    """
    Sum the squares of the given integers.

    Args:
        integers (Iterator[int]): Integers to square and sum.__annotations__

    Returns:
        int: The sume of the squared integers or 0 if integers is empty
    """
    return sum(n**2 for n in integers)
