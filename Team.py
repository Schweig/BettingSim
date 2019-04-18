class Team:
    def __init__(self,name):
        self.name = name
        self.home_games = 0
        self.away_games = 0
        self.total_games = 0
        self.away_scored = 0
        self.home_scored =  0
        self.total_scored = 0
        self.away_allowed = 0
        self.home_allowed = 0
        self.total_allowed = 0

    def __str__(self):
        return str(self.__dict__)

    def set_name(self,name):
        self.name = name

    def allowed_run_home(self):
        self.home_allowed+=1

    def scored_run_home(self):
        self.home_scored+=1

    def allowed_run_away(self):
        self.away_allowed += 1

    def scored_run_away(self):
        self.away_scored += 1

    def played_game(self,type):
        if type is "home":
            self.home_games += 1
        elif type is "away":
            self.away_games += 1
        self.total_games +=1


