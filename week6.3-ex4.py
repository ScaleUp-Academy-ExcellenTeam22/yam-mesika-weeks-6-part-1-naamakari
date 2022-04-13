from typing import List
FIRST_NAMES = ['avi', 'moshe', 'yaakov']
LAST_NAMES = ['cohen', 'levi', 'mizrahi']


def full_names(first_names: List[str], last_names: List[str], min_length: int = 0) -> List:
    """
    The function gets a list of first and last names and creates full names, while upper each first letter in the name.
    :param first_names: List of first names.
    :param last_names: List of last names
    :param min_length: Minimum length for full name, the default value is 0, meaning any length is obtained.
    :return: The list of full names.
    """
    return [first_name[0].upper() + first_name[1:] + ' ' + last_name[0].upper() + last_name[1:]
            for first_name in first_names
            for last_name in last_names
            if len(first_name) + len(last_name) + 1 >= min_length]


if __name__ == '__main__':
    print(full_names(FIRST_NAMES, LAST_NAMES, 10) ==
          ['Avi Mizrahi', 'Moshe Cohen', 'Moshe Levi', 'Moshe Mizrahi',
           'Yaakov Cohen', 'Yaakov Levi', 'Yaakov Mizrahi'])
    print(full_names(FIRST_NAMES, LAST_NAMES) ==
          ['Avi Cohen', 'Avi Levi', 'Avi Mizrahi', 'Moshe Cohen', 'Moshe Levi', 'Moshe Mizrahi',
           'Yaakov Cohen', 'Yaakov Levi', 'Yaakov Mizrahi'])
