# Custom filter
from collections.abc import Iterable
from typing import List


def is_positive(number: int) -> bool:
    """
    The function checks if the received number is positive.
    :param number: The number to check if is positive.
    :return: If the number is positive or not.
    """
    return number > 0


def my_filter(filter_function: any, iterable: Iterable) -> List:
    """
    The function filters the received iterable according to the received filter function.
    :param filter_function: A function to filter according to.
    :param iterable: The iterable that needs to be filtered according to the function received.
    :return: A list with the elements that passed the filter.
    """
    if filter_function is None:
        return [item for item in iterable if bool(item)]
    return [item for item in iterable if filter_function(item)]


if __name__ == "__main__":
    numbers = [-2, -1, 0, 1, 2]
    none_elements = [0, "", None, 0.0, True, False, "Hello"]
    to_sum = [(1, -1), (2, 5), (5, -3, -2), (1, 2, 3)]
    print(my_filter(lambda n: n > 0, numbers))
    print(my_filter(is_positive, numbers))
    print(my_filter(None, none_elements))
    print(tuple(my_filter(sum, to_sum)))
