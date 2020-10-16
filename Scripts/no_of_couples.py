"""
Funtion return no.of.couples(pairs)
in the list
"""

def couples(ar: list) -> int:
    """
    >>> couples([10, 20, 20, 10, 10, 30, 50, 10, 20])
    3
    """
    res = []
    couples = {}
    for i in ar:
        count = ar.count(i)
        couples["{}".format(i)] = count
    for i in couples:
        x = couples[i] // 2
        if x >= 1:
            res.append(x)
        else:
            pass
    return sum(res)
 
          
if __name__ == "__main__":
    import doctest
    
    doctest.testmod()
