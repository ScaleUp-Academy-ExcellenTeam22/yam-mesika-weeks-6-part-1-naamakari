from time import time


def timer(f, *parameters: any, **parameters2: any) -> float:
    """
    The function receives a function and parameters and calculates how long it takes to perform
     the function obtained with the obtained parameters.
    :param f: The received function.
    :param parameters: The received parameters, zero or more.
    :param parameters2: The received parameters, zero or more, with the name of the each parameter.
    :return: The time it takes to perform the obtained function with the obtained parameters.
    """
    start_time = time()
    f.__call__(*parameters, **parameters2)
    return time() - start_time


if __name__ == "__main__":
    print(timer(print, "Hello"))
    print(timer(zip, [1, 2, 3], [4, 5, 6]))
    print(timer("Hi {name}".format, name="Bug"))
