import sys

import pandas as pd
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

headers = {"UserAgent": UserAgent().random}


def merge_into_dict(list_1: list, list_2: list) -> dict:
    """
    Merge two lists into Dictionary
    """

    result_dict = {}
    for i in zip(list_1, list_2):
        result_dict[i[0]] = i[1]
    return result_dict


def ipl_points_table(year: str) -> list:
    """
    Funtion return the ipl points table
    """

    url = "https://www.iplt20.com/points-table/{}".format(year)
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, "html.parser")
    data = list(map(lambda x: x.text, soup.find_all("td")))
    teams = list(map(lambda x: " ".join(x.split()), data[1::12]))
    matches_played = data[2::12]
    won = data[3::12]
    lost = data[4::12]
    tied = data[5::12]
    not_rated = data[6::12]
    run_rate = data[7::12]
    points = data[10::12]
    heading = [
        "team",
        "matches_played",
        "won",
        "lost",
        "tied",
        "not_rated",
        "run_rate",
        "points",
    ]
    table = list(
        zip(teams, matches_played, won, lost, tied, not_rated, run_rate, points)
    )
    points_table = [merge_into_dict(heading, i) for i in table]

    return points_table


if __name__ == "__main__":
    try:
        season = sys.argv[1]
    except (IndexError, KeyError):
        season = input("Enter the Season Year: ")
    finally:
        print(pd.DataFrame(ipl_points_table(season)))
