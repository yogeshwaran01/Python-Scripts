"""
The hiker first enters a valley units deep. Then they climb out and up onto a mountain
units high. Finally, the hiker returns to sea level and ends the hike.

countingValleys has the following parameter(s):

    int steps: the number of steps on the hike
    string path: a string describing the path

Returns

    int: the number of valleys traversed

"""


def countingValleys(path: str) -> int:
    L = 0
    no_of_valley = 0
    for s in path:
        if s == "U":
            L = L + 1
            if L == 0:
                no_of_valley = no_of_valley + 1
        else:
            L -= 1
    return no_of_valley
