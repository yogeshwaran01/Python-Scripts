def convert_bytes_to(bytes: int, convert_to: str) -> int:
    """
    Function convert bytes to kb, mb, gb and tb

    >>> convert_bytes_to(1024, convert_to="kb")
    1
    >>> convert_bytes_to(123456789, convert_to="mb")
    118
    >>> convert_bytes_to(1073741824, convert_to="gb")
    1
    """

    data = {"kb": 1, "mb": 2, "gb": 3, "tb": 4}
    res = float(bytes)
    for _ in range(data[convert_to]):
        res = res / 1024

    return round(res)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
