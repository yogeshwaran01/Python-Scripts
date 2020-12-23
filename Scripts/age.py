from datetime import datetime
import time


class Age:
    """
    Class calculate the Age
    """

    def __init__(self, date: int, month: int, year: int):
        today = datetime.today()
        self.user_date = date
        self.user_month = month
        self.user_year = year
        self.today_year = today.year
        self.today_month = today.month
        self.today_date = today.day
        self.year_diff = self.today_year - self.user_year
        month_diff = self.today_month - self.user_month
        if month_diff < 0:
            self.month_diff = (12 + self.today_month) - self.user_month
        else:
            self.month_diff = month_diff
        date_diff = self.today_date - self.user_date
        if date_diff < 0:
            self.date_diff = (30 + self.today_date) - self.user_date
        else:
            self.date_diff = date_diff

    def as_years(self) -> int:
        return self.today_year - self.user_year

    def as_months(self) -> int:
        return (self.as_years() * 12) + self.month_diff

    def as_days(self) -> int:
        return (self.as_years() * 365) + self.date_diff


if __name__ == "__main__":
    day = int(input("Enter the date of you Birthday: "))
    month = int(input("Enter the month of you Birthday: "))
    year = int(input("Enter the year of you Birthday: "))
    age = Age(day, month, year)
    print(f"Your age is: {age.as_years()}")
    print(
        f"You are {age.year_diff} years {age.month_diff} months and {age.date_diff} days old!"
    )
