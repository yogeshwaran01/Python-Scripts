import os

os.chdir(os.getcwd() + "/Scripts")

main = "https://github.com/yogeshwaran01/Python-Scripts/blob/master/Scripts/"

l = []

for i in os.listdir():
    s = f"| [{i}]({main + i}) |" + "\n"
    l.append(s)

file = open("README.md", "w")
file.write("# Python-Scripts" + "\n" + "\n")
file.write("Some python scripts" + "\n" + "\n")
file.write(f"| **Scripts - {len(l)}**|" + "\n")
file.write("|--------------|" + "\n")
file.writelines(sorted(l))
