"""
There is an array with some numbers.
All numbers are equal except for one(imposter).

"""


def imposter(arr: list) -> str:
    """
    >>> imposter([1,2,1,1,1,1])
    2
    >>> imposter(["python", "java", "python", "python"])
    'java'

    """
    n = []
    s = set(arr)
    for e in s:
        if arr.count(e) == 1:
            n.append(e)
    return n[0]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
