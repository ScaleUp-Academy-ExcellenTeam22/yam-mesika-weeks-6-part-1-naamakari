from typing import List


def get_positive_numbers() -> List:
    """
    The function asks the user for a sequence of numbers and returns all the positive numbers, as a list of int.
    :return: List of the positive numbers in the list.
    """
    numbers_sequence = input("Please enter a sequence of numbers separated by a comma:\n")
    return [int(item) for item in numbers_sequence.split(",") if int(item) > 0]


if __name__ == '__main__':
    print(get_positive_numbers())
