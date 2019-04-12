import gspread
import mlbgame
import calendar
import time
from oauth2client.service_account import ServiceAccountCredentials

def initMonth(month,numDays):
    # use creds to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    name = calendar.month_name[month]
    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    wb = client.open('BettingSim')
    for i in range(1,numDays+1):
        fullName = name+""+str(i)
        wb.add_worksheet(fullName,50,10)
def clearMonth(month,numDays):
    # use creds to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    name = calendar.month_name[month]
    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    wb = client.open('BettingSim')
    for i in range(1,numDays+1):
        fullName = name+""+str(i)
        wb.del_worksheet(wb.worksheet(fullName))
def addGames(month,numDays):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    name = calendar.month_name[month]
    wb = client.open('BettingSim')
    for i in range(1,numDays+1):
        fullName = name+""+str(i)
        sheet = wb.worksheet(fullName)
        sheet.append_row(['Home','Away','Game_ID','Wager','Line','Result'])
        games = mlbgame.day(2019, month, i)
        for game in games:
            sheet.append_row([game.home_team, game.away_team, game.game_id])
            time.sleep(1)
def evalGames(month,numDays):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    name = calendar.month_name[month]
    wb = client.open('BettingSim')
    for i in range(1, numDays + 1):
        fullName = name + "" + str(i)
        sheet = wb.worksheet(fullName)
        list_of_hashes = sheet.get_all_records()
        for row in list_of_hashes:
            evalGame(row['Game_ID'],sheet)


def evalGame(game_id,sheet):
    try:
        innings = mlbgame.box_score(game_id).innings
        if not innings:
            print('debug stmt')
        if innings[0]['home']+innings[0]['away'] is 0:
            id_cell = sheet.find(game_id)
            sheet.update_cell(id_cell.row+3,id_cell.col+3,'win')
            time.sleep(1)
    except:
        print("innings issues")
clearMonth(4,30)
initMonth(4,30)
addGames(4,30)
evalGames(4,30)