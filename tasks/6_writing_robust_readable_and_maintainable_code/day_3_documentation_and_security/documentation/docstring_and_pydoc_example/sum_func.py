"""This module includes few simple addition functions."""

# This function increments given argument `a` by 1.
def add_one(a):
    return a + 1


def add(a, b):
    """Returns sum of `a` and `b` arguments."""
    return a + b


def add_negative(a, b):
    """Function returning sum of `a` and `b` if both are negative, `None`
    otherwise.

    Parameters:
    a (int): First number to be included in the sum.
    b (int): Second number to be included in the sum.

    Returns:
    int: Sum of `a` and `b` if both are negative, `None` otherwise.
    """
    if a < 0 and b < 0:
        return add(a, b)
    else:
        pass


def add_positive(a, b):
    """Function returning sum of `a` and `b` if both are positive, `None`
    otherwise.

    :param a: First number to be included in the sum.
    :type a: int
    :param b: Second number to be included in the sum.
    :type b: int

    :return: Sum of `a` and `b` if both are positive, `None` otherwise.
    :rtype: int
    """
    if a > 0 and b > 0:
        return add(a, b)
    else:
        pass


def main():
    print(add_one.__doc__)
    print(add.__doc__)
    print(add_negative.__doc__)
    print(add_positive.__doc__)


if __name__ == "__main__":
    main()
