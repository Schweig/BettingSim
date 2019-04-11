import mlbgame
def getAvgRunsInFirstHome(year,month,team):
    month = mlbgame.games(year, month, home=team)
    games = mlbgame.combine_games(month)
    firstInningRunsOppo = 0
    firstInningRunsHome = 0
    num_of_games = 0
    for game in games:
        innings = mlbgame.box_score(game.game_id).innings
        if innings:
            firstInningRunsOppo += innings[0]['away']
            firstInningRunsHome += innings[0]['home']
            num_of_games += 1
    return {"games_played":num_of_games,"opponent":firstInningRunsOppo/num_of_games,"home":firstInningRunsHome/num_of_games}

def getAvgRunsInFirstAway(year,month,team):
    month = mlbgame.games(year, month, away=team)
    games = mlbgame.combine_games(month)
    firstInningRunsOppo = 0
    firstInningRunsHome = 0
    num_of_games = 0
    for game in games:
        try:
            innings = mlbgame.box_score(game.game_id).innings
            if innings:
                firstInningRunsOppo += innings[0]['away']
                firstInningRunsHome += innings[0]['home']
                num_of_games += 1
        except:
            print("no data")
    return {"games_played":num_of_games,"opponent":firstInningRunsOppo/num_of_games,"home":firstInningRunsHome/num_of_games}

print(getAvgRunsInFirstHome(2019,4,'Mets'))
print(getAvgRunsInFirstAway(2019,4,'Mets'))