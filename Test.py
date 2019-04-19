from Team import Team
import calendar
import datetime
from bs4 import BeautifulSoup as soup
import requests
teams = {}
response = requests.get("https://www.baseball-reference.com/leagues/MLB-schedule.shtml")
content  = response.content
parsed = soup(content,"lxml")
base_url = "https://www.baseball-reference.com"
schedule = parsed.find_all("div", {"class":"section_content"})[0].find_all("div")
for day in schedule:
    datetext = day.find("h3").text
    if "Today" in datetext:
        date = datetime.datetime.today()
        games = day.find_all("p",{"class":"game"})
        for game in games:
            links = game.find_all("a")
            for link in links:
                text = link.get_text()
                print(text)
                if text == "Boxscore":
                    response = requests.get(base_url+link.attrs['href'])
                    content = response.content
                    parsed = soup(content,"lxml")
                    rows = parsed.find("table",{"class":"linescore"}).find("tbody").find_all("tr")
                    for row in rows:
                        elms = row.find_all("td")
                        for elm in elms:
                            print (elm.text)
                elif text == "Preview":
                    response = requests.get(base_url + link.attrs['href'])
                    print("Guess Game")
                else:
                    if text not in teams:
                        if text != "Arizona D'Backs":
                            teams[link.text] = Team(link.text)
                        else:
                            teams["Arizona Diamondbacks"] = Team(link.text)

    else:
        date = datetext.split(" ")
        month = date[1]
        daynum = date[2][:-1]
        year = date[3]
        games = day.find_all("p", {"class": "game"})
        for game in games:
            links = game.find_all("a")
            for link in links:
                text = link.get_text()
                print(text)
                if text == "Boxscore":
                    response = requests.get(base_url + link.attrs['href'])
                    content = response.content
                    parsed = soup(content, "lxml")
                    rows = parsed.find("table", {"class": "linescore"}).find("tbody").find_all("tr")
                    away =rows[0].find_all("td")
                    home = rows[1].find_all("td")
                    home_team = home[1].string
                    away_team = away[1].string
                    teams[home_team].played_game("home")
                    teams[away_team].played_game("away")
                    if home[2].string != '0':
                        teams[home_team].scored_run_home()
                        teams[away_team].allowed_run_away()
                    elif away[2].string !=0:
                        teams[home_team].allowed_run_home()
                        teams[away_team].scored_run_home
                elif text == "Preview":
                    #response = requests.get(base_url + link.attrs['href'])
                    print("Guess Game")
                else:
                    if text not in teams:
                        if text != "Arizona D'Backs" :
                            teams[link.text] = Team(link.text)
                        else:
                            teams["Arizona Diamondbacks"] = Team(link.text)


print(teams)


# for i in range(1,currentday+1):
#     print (i)
#
# x = Team("Mets")
# x.allowed_run_home()
# x.scored_run_home()
#
# print(x)

