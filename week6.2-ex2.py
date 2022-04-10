from typing import List


def get_positive_numbers() -> List:
    """
    The function asks the user for a series of numbers and returns all the positive numbers, as a list of int.
    :return: List of the positive numbers in the list.
    """
    numbers_series = input("Please enter a series of numbers separated by a comma:\n")
    numbers_series = numbers_series.split(",")
    return list(map(lambda item: int(item), filter(lambda number: int(number) > 0, numbers_series)))


if __name__ == '__main__':
    print(get_positive_numbers())
