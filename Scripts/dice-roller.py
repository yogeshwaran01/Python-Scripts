import random

def DiceRoll(no_of_dices: int) -> int:
    return random.choice([i for i in range(1, (no_of_dices * 6) + 1)])

if __name__ == "__main__":
    n = int(input("Enter the no.of Dices: "))
    while True:
        a = DiceRoll(n)
        input("----Press Any Key to Roll----")
        print(f'You go {a}')