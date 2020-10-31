from psutil import sensors_battery

battery = sensors_battery()

if __name__ == "__main__":
    print(f"Percentage: {battery.percent}")
    print(f"Power Plugged: {battery.power_plugged}")
    print(f"SecsLeft: {battery.secsleft}")
