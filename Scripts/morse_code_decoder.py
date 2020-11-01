MORSE_CODE = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
    "-----": "0",
    "--..--": ", ",
    ".-.-.-": ".",
    "..--..": "?",
    "-..-.": "/",
    "-....-": "-",
    "-.--.": "(",
    "-.--.-": ")",
}


def decodeMorse(morse_code: str) -> str:
    """
    >>> decodeMorse(".... . -.--   .--- ..- -.. .")
    'HEY JUDE'
    """

    list = morse_code.strip().split("   ")
    ans = []
    for i in list:
        final = []
        for j in i.split():
            final.append(MORSE_CODE.get(j))
        ans.append("".join(final))
    return " ".join(ans)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    sen = input("Enter the Morse code to decode: ")
    print(decodeMorse(sen))
