"""
What is an anagram?

Two words are anagrams of each other
if they both contain the same letters.

For example:

'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false

'abba' & 'abca' == false

"""


def is_anagram(a: str, b: str) -> bool:
    """
    >>> is_anagram("xyxyc", "xyc")
    False
    >>> is_anagram("abba", "ab")
    False
    >>> is_anagram("abba", "bbaa")
    True
    """

    return bool(len(a) == len(b) and set(a) == set(b))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
