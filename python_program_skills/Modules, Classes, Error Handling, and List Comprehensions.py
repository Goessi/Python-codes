## 2. Introduction to the Data ##

import csv
file = open('nfl_suspensions_data.csv')
nfl = csv.reader(file)
nfl_suspensions = list(nfl)
nfl_suspensions = nfl_suspensions[1:] # to avoid header
years = {}
for item in nfl_suspensions:
    row_year = item[5]
    if row_year in years:
        years[row_year] = years[row_year] + 1
    else:
        years[row_year] = 1
print(years)

## 3. Unique Values ##

import csv
file = open('nfl_suspensions_data.csv')
nfl = list(csv.reader(file))
nfl = nfl[1:]
teams = []
games = []
for item in nfl:
    teams.append(item[1])
    games.append(item[2])
unique_teams = set(teams) # will return only unique values
unique_games = set(games)
    
    

## 4. Suspension Class ##

class Suspension:
    def __init__(self,a_list_row):
        self.name = a_list_row[0]
        self.team = a_list_row[1]
        self.games = a_list_row[2]
        self.years = a_list_row[5]
third_suspension = Suspension(nfl_suspensions[2])

## 5. Tweaking the Suspension Class ##

class Suspension():
    def __init__(self,row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]
        try:
            self.year = int(row[5])
        except Exception:
            self.year = 0
    def get_year(self):
        return(self.year)
      
missing_year = Suspension(nfl_suspensions[22])
twenty_third_year = missing_year.get_year()
        
