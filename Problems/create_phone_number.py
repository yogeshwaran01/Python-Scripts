"""
Function convert lists of 10 elements
into in the format of phone number

Example,
    (123) 456-789
    
"""


def create_phone_number(n: list) -> str:
    """
    >>> create_phone_number([1,2,3,4,5,6,7,8,9,0])
    '(123) 456-7890'
    """
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
