import os
from time import sleep
from datetime import datetime

while True:
    os.system("clear")
    now = datetime.now()
    print('\033[93m' + f'{now.hour}:{now.minute}:{now.second}'.center(os.get_terminal_size().columns))
    sleep(1)
    os.system("clear")
