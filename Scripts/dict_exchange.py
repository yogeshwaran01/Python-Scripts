"""
Funtion convert dictionary keys into values
and values into keys
"""

def dict_exchange(dicts: dict) -> dict:
    """
    >>> dict_exchange({'a': 'b', 'c': 'd'})
    {'b': 'a', 'd': 'c'}
    """
    key = dicts.keys()
    valve = dicts.values()
    return dict(zip(valve, key))

if __name__ == "__main__":
    import doctest
    
    doctest.testmod()
    