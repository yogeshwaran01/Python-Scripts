"""
Function, persistence, that takes
in a positive parameter num and returns
its multiplicative persistence,
which is the number of times you must multiply
the digits in num until you reach a single digit.
"""


def mul(lists: list) -> int:
    result = 1
    for x in lists:
        result = result * x
    return result


def persistence(n: int) -> int:
    """
    >>> persistence(243)
    2
    """
    a = list(str(n))
    count = 0
    while len(a) != 1:
        a = list(str(mul(map(int, a))))
        count = count + 1
    return count


if __name__ == "__main__":
    import doctest

    doctest.testmod()
