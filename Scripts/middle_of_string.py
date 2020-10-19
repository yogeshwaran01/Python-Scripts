"""
Funtion return the middle letter of the string
"""


def get_middle(s: str) -> str:
    """
    >>> get_middle("python")
    'th'
    >>> get_middle("cpython")
    't'
    """

    lists = list(s)
    if len(lists) % 2 == 0:
        return lists[len(lists) // 2 - 1] + lists[len(lists) // 2]
    return lists[len(lists) // 2]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
