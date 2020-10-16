"""
Funtion return the given number is square or not
"""


def is_square(n: int) -> bool:
    """
    >>> is_square(64)
    True
    >>> is_square(56)
    False
    """

    if n == 0:
        return True
    else:
        i = 1
        while i * i <= n:
            if (n % i == 0) and (n / i == i):
                return True
            i = i + 1
        return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
