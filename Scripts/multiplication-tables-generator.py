"""
Funtion Generates the mutiplication tables
"""


def multiplication_tables_generator(times: int, min: int, max: int) -> list:
    """
    >>> multiplication_tables_generator(2, 1, 10)
    ['1 x 2 = 2', '2 x 2 = 4', '3 x 2 = 6', '4 x 2 = 8', '5 x 2 = 10', '6 x 2 = 12', '7 x 2 = 14', '8 x 2 = 16', '9 x 2 = 18', '10 x 2 = 20']
    """

    tables = []
    for number in range(min, max + 1):
        tables.append(f"{number} x {times} = {number * times}")
    return tables


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    for table in multiplication_tables_generator(5, 5, 25):
        print(table)
