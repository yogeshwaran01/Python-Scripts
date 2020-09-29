import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys

try:
    year = sys.argv[1]
except:
    year = input("Enter the season year: ")

def merge_into_dict(list_1,list_2):
    result_dict = {}
    for i in zip(list_1,list_2):
      result_dict[i[0]] = i[1]
    return result_dict

url = "https://www.iplt20.com/points-table/{}".format(year)
res = requests.get(url)

soup = BeautifulSoup(res.text,'html.parser')
data = list(map(lambda x: x.text ,soup.find_all('td')))
teams = list(map(lambda x: " ".join(x.split()),data[1::12]))
matches_played = data[2::12]
won = data[3::12]
lost = data[4::12]
tied = data[5::12]
not_rated = data[6::12]
run_rate = data[7::12]
points = data[10::12]

heading = ["team","matches_played","won","lost","tied","not_rated",'run_rate','points']
table = list(zip(teams,matches_played,won,lost,tied,not_rated,run_rate,points))

points_table = [merge_into_dict(heading, i) for i in table]

df = pd.DataFrame(points_table)

print(df)
