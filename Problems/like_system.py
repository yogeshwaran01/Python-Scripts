"""
You probably know the "like" system from Facebook and other pages.
People can "like" blog posts, pictures or other items.
We want to create the text that should be displayed next to such an item.

"""


def likes(list_of_names: list) -> str:
    """
    >>> likes([])
    'no one likes this'
    >>> likes(["Python"])
    'Python likes this'
    >>> likes(["Python", "JavaScript", "SQL"])
    'Python, JavaScript and SQL like this'
    >>> likes(["Python", "JavaScript", "SQL", "JAVA", "PHP", "Ruby"])
    'Python, JavaScript and 4 others like this'
    """

    if len(list_of_names) == 0:
        return f"no one likes this"
    elif len(list_of_names) == 1:
        return f"{list_of_names[0]} likes this"
    elif len(list_of_names) == 2:
        return f"{list_of_names[0]} and {list_of_names[1]} like this"
    elif len(list_of_names) == 3:
        return (
            f"{list_of_names[0]}, {list_of_names[1]} and {list_of_names[2]} like this"
        )
    else:
        return f"{list_of_names[0]}, {list_of_names[1]} and {len(list_of_names) - 2} others like this"


if __name__ == "__main__":
    import doctest

    doctest.testmod()
