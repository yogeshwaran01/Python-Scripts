import os
import time


class Stopwatch:
    def __init__(self, hour: int, minute: int, seconds: int):
        self.a = hour
        self.b = minute
        self.c = seconds
        self.hour = 0
        self.min = 0
        self.sec = 0

    def run(self):
        while True:
            time.sleep(1)
            os.system("clear")
            self.sec = self.sec + 1
            if self.sec == 60:
                self.min = self.min + 1
                self.sec = 0
            if self.min == 60:
                self.hour = self.hour + 1
                self.min = 0
            print("\t\t" + "⌚ STOPWATCH ⌚")
            print("\n" + "\t\t" + f"  {self.hour} : {self.min} : {self.sec}" + "\n")
            if self.sec == self.c and self.min == self.b and self.hour == self.a:
                break
            continue
        return True


if __name__ == "__main__":
    stopwatch = Stopwatch(0, 1, 5)

    stopwatch.run()
