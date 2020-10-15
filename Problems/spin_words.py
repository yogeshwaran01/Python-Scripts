"""
Function that takes in a string of one or more words,
and returns the same string, but with all five or more
letter words reversed.
Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.
"""


def spin_words(sentence: str) -> str:
    """
    >>> spin_words("Hey wollef sroirraw")
    'Hey fellow warriors'
    """

    splited_sentence = sentence.split()
    lists_of_word_spined = []
    for i in splited_sentence:
        if len(i) >= 5:
            word = list(i)
            word.reverse()
            word = "".join(word)
        else:
            word = i
        lists_of_word_spined.append(word)

    return " ".join(lists_of_word_spined)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
