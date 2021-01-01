import os
from time import sleep
from datetime import datetime

def count_down():
    new_year = datetime(datetime.now().year + 1, 1, 1)
    today = datetime.now()

    day_diff = new_year.day - today.day
    if day_diff < 0:
        day_diff = 30 + new_year.day - today.day
    month_diff = 12 - today.month
    total_days = int(day_diff + ((month_diff/2) * 30) + ((month_diff / 2) * 31))


    hour_diff = new_year.hour - today.hour
    if hour_diff < 0:
        hour_diff = (new_year.hour - today.hour) + 23

    minute_diff = new_year.minute - today.minute
    if minute_diff < 0:
        minute_diff = 59 + new_year.minute - today.minute

    sec_diff = new_year.second - today.second
    if sec_diff < 0:
        sec_diff = 59 + (new_year.second - today.second)

    return f'{day_diff} Days {hour_diff} Hours {minute_diff} Minutes and {sec_diff} Seconds'

while True:
    os.system('clear')
    print(count_down())
    sleep(1)
    os.system('clear')
