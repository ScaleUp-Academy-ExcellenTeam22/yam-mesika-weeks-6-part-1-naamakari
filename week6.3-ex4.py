from typing import List
from typing import Tuple


def create_full_name(first_name: str, last_name: str) -> str:
    return first_name[0].upper() + first_name[1:] + ' ' + last_name[0].upper() + last_name[1:]


def full_names(first_names: Tuple, last_names: Tuple, min_length: int = 0) -> List:
    """
    The function gets a list of first and last names and creates full names,
    and becomes a capital letter every first letter in the name.
    :param first_names: List of first names.
    :param last_names: List of last names
    :param min_length: Minimum length for full name, the default value is 0, meaning any length is obtained.
    :return: The list of full names.
    """
    return [create_full_name(first_name, last_name)
            for first_name in first_names
            for last_name in last_names
            if len(first_name) + len(last_name) + 1 >= min_length]


if __name__ == '__main__':
    first_names_list = ('avi', 'moshe', 'yaakov')
    last_names_list = ('cohen', 'levi', 'mizrahi')
    print(full_names(first_names_list, last_names_list, 10) ==
          ['Avi Mizrahi', 'Moshe Cohen', 'Moshe Levi', 'Moshe Mizrahi',
           'Yaakov Cohen', 'Yaakov Levi', 'Yaakov Mizrahi'])
    print(full_names(first_names_list, last_names_list) ==
          ['Avi Cohen', 'Avi Levi', 'Avi Mizrahi', 'Moshe Cohen', 'Moshe Levi', 'Moshe Mizrahi',
           'Yaakov Cohen', 'Yaakov Levi', 'Yaakov Mizrahi'])
