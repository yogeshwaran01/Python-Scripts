"""
A pangram is a sentence that contains every single letter of the alphabet at least once.
For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram,
because it uses the letters A-Z at least once (case is irrelevant).
Given a string, detect whether or not it is a pangram. Return True if it is, False if not.
Ignore numbers and punctuation.

"""

from string import ascii_lowercase


def is_pangram(s: str) -> int:
    """
    >>> is_pangram("The quick, brown fox jumps over the lazy dog!")
    True

    >>> is_pangram("quick, brown jumps over the lazy dog")
    False
    """

    return set(ascii_lowercase) == set(s.lower()).intersection(set(ascii_lowercase))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
