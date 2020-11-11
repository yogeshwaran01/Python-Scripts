import re
import getpass


def strong_pass(Password):

    if re.match(r"([a-zA-Z0-9]).{8,}", Password) is not None:
        return "Strong Password"

    return "Weak Password"


passwd = getpass.getpass("Enter Your password: ")
print(strong_pass(passwd))
