def generate_hashtag(s):
    """
    >>> generate_hashtag("Python Is Nice")
    '#PythonIsNice'
    >>> generate_hashtag("c i u")
    '#CIU'
    >>> generate_hashtag("python is  nice")
    '#PythonIsNice'
    """
    if s == "":
        return False
    elif len(s) > 140:
        return False
    else:
        res = "#"
        for i in s.split():
            res = res + i.capitalize()
    return res


if __name__ == "__main__":
    import doctest

    doctest.testmod()
