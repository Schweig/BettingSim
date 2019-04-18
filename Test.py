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
                elif text == "Preview":
                    response = requests.get(base_url + link.attrs['href'])
                    print("Guess Game")
                else:
                    if text not in teams:
                        teams[link.text] = Team(link.text)
                        teams[link.text].played_game('home')
                    print("Team")

    else:
        date = datetext.split(" ")
        month = date[1]
        daynum = date[2][:-1]
        year = date[3]
        games = day.find_all("div", {"class": "game"})
    # for game in games:
    #     links = game.find_all("a")
    #     for link in links:
    #         if link.text is "Boxscore":
    #             print("Read Data")
    #         elif link.text is "Preview":
    #             print("Guess Game")
    #         else:
    #             print("Team")



# for i in range(1,currentday+1):
#     print (i)
#
# x = Team("Mets")
# x.allowed_run_home()
# x.scored_run_home()
#
# print(x)

