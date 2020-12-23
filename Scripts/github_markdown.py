import requests


def markdown(text: str) -> str:
    """ Function convert markdown to HTML """
    return requests.post("https://api.github.com/markdown", json={"text": text}).text

if __name__ == "__main__":
    import sys
    i_file = sys.argv[1]
    o_file = sys.argv[2]
    with open(i_file, 'r') as file:
        text = file.read()
    with open(o_file, 'w') as file:
        file.write(markdown(text))
