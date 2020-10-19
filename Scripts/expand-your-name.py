import random

A = [
    "active",
    "adorable",
    "afraid",
    "alert",
    "ambitous",
    "amusing",
    "angry",
    "attentive",
    "argumentative",
    "adventurous",
]
B = ["bashful", "boring", "bossy", "brainy", "brave", "bright", "busy", "brilliant"]
C = [
    "capable",
    "calm",
    "careful",
    "cautious",
    "charismatic",
    "cheerful",
    "eager",
    "clever",
    "clumsy",
    "confident",
    "curious",
]
D = [
    " daring",
    " decisive",
    "dedicated",
    "delightful",
    "demanding",
    "detailed",
    "determined",
    "dreamer",
]
E = ["eager", "easygoing", "efficient", "enchanting", "energetic", "enthusiastic"]
F = [
    "fun",
    "fearless",
    "fair",
    "foolish",
    "forgiving",
    "friendly",
    "forgetful",
    "fortunate",
    "flexible",
]
G = ["generous", "gentle ", "giving", "glamorous", "graceful", "greedy"]
H = [
    "happy",
    "hard working",
    "healthy",
    "helpful",
    "heroic",
    "honest",
    "helpful",
    "hilarious",
    "hungry",
    "humorous",
]
I = [
    "imaginative",
    "immature",
    "impatient",
    "impulsive",
    "inventive",
    "intelligent",
    "industrious",
    "independent",
]
J = ["jelous", "jolly", "joyful"]
K = ["kind", "knowledgeable"]
L = ["lazy", "leader", "likable", "lonely", "loud", "loving", "loyal", "lucky"]
M = ["mannerly", "mature", "mean", "mean", "messy", "moody", "mysterious"]
N = ["naughty", "neat", "nervous", "noisy", "nature lover"]
O = ["obedient", "anxious", "observant", "optimistic", "outgoing", "outstanding"]
P = [
    "polite",
    "perfect",
    "picky",
    "pleasant",
    "proud",
    "productive",
    "playful",
    "persistent",
]
Q = ["qualified"]
R = ["relaxed", "reliable", "respectful", "rude", "respectful", "responsible"]
S = [
    "secretive",
    "selfish",
    "sensitive",
    "shy",
    "sincere",
    "smart",
    "sweet",
    "successful",
    "silly",
    "sneaky",
    "studious",
    "stubborn",
]
T = [
    "talented",
    "talkative",
    "tall",
    "thankful",
    "timid",
    "tired",
    "tough",
    "tolerant",
    "thoughtful",
]
U = ["understanding", "ususual", "upset", "useful", "unselfish"]
V = ["valiant", "valuable", "vocal", "vivacious"]
W = ["welcoming", "willing", "wise", "witty"]
X = ["eXtreme"]
Y = ["young", "youthful"]
Z = ["zany", "zesty", "zippy"]


def string_to_list(strings: str) -> list:
    lists = []
    for i in strings:
        lists.append(i)
    return lists


def replace(lis: list, ini: int, fin: int) -> list:
    for letter in lis:
        if letter == ini:
            a = lis.index(ini)
            lis[a] = fin
    return lis


def expand(username: str) -> int:
    result = """{} \n""".format(username.upper())
    if len(username) > 1:
        t = string_to_list(username.lower().strip())
        for i in t:
            if i == "a":
                replace(t, i, random.choice(A))
            elif i == "b":
                replace(t, i, random.choice(B))
            elif i == "c":
                replace(t, i, random.choice(C))
            elif i == "d":
                replace(t, i, random.choice(D))
            elif i == "e":
                replace(t, i, random.choice(E))
            elif i == "f":
                replace(t, i, random.choice(F))
            elif i == "g":
                replace(t, i, random.choice(G))
            elif i == "h":
                replace(t, i, random.choice(H))
            elif i == "i":
                replace(t, i, random.choice(I))
            elif i == "j":
                replace(t, i, random.choice(J))
            elif i == "k":
                replace(t, i, random.choice(K))
            elif i == "l":
                replace(t, i, random.choice(L))
            elif i == "m":
                replace(t, i, random.choice(M))
            elif i == "n":
                replace(t, i, random.choice(N))
            elif i == "o":
                replace(t, i, random.choice(O))
            elif i == "p":
                replace(t, i, random.choice(P))
            elif i == "q":
                replace(t, i, random.choice(Q))
            elif i == "r":
                replace(t, i, random.choice(R))
            elif i == "s":
                replace(t, i, random.choice(S))
            elif i == "t":
                replace(t, i, random.choice(T))
            elif i == "u":
                replace(t, i, random.choice(U))
            elif i == "v":
                replace(t, i, random.choice(V))
            elif i == "w":
                replace(t, i, random.choice(W))
            elif i == "X":
                replace(t, i, random.choice(X))
            elif i == "y":
                replace(t, i, random.choice(Y))
            elif i == "z":
                replace(t, i, random.choice(Z))
            else:
                pass
        for g in t:
            a = g[0].capitalize() + " - " + g.capitalize()
            result = result + a + "\n"
    return result


if __name__ == "__main__":
    username = input("Enter your Name: ")
    print(expand(username))
