import random


def Toss() -> str:
    """
    Funtion return random toss
    """

    COIN = ["Heads", "Tails"]
    return random.choice(COIN)


if __name__ == "__main__":
    while True:
        input("\n----Enter any key to Toss---\n")
        print(f"You Tossed - {Toss()}")
