from prettytable import PrettyTable
from analyse_nba_game import analyse_nba_game

def print_nba_game_stats(team_dict):
    dataset = analyse_nba_game() # Get Data

    # Hardcode the headers into the table :)
    t = PrettyTable([ 'Players', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']) # Use Prettytable
   
    # Initialize all variables as zero
    sum_FG = sum_FGA = sum_FGpercent = sum_3P = sum_3PA = sum_3Ppercent = sum_FT = sum_FTA = sum_FTpercent = sum_ORB = sum_DRB = sum_TRB = sum_AST = sum_STL = sum_BLK = sum_TOV = sum_PF = sum_PTS = 0
   
    for i in range (len(dataset)):
        dictionary = dataset[i] # Go one by one through list of dictionaries
        team = (dictionary['home_team']) # Specify which team stats you want to printout (home_team - Warriors; away_team - Oklahoma)
        players_data = (team['players_data']) # Navigate into players stats

        data = []
        for key, value in players_data.items():
            data += [(value)]
        
        # Add to get sum of all stats    
        sum_FG += data[1]
        sum_FGA += data[2]
        sum_FGpercent += data[3]
        sum_3P += data[4]
        sum_3PA += data[5]
        sum_3Ppercent += data[6]
        sum_FT += data[7]
        sum_FTA += data[8]
        sum_FTpercent += data[9]
        sum_ORB += data[10]
        sum_DRB += data[11]
        sum_TRB += data[12]
        sum_AST += data[13]
        sum_STL += data[14]
        sum_BLK += data[15]
        sum_TOV += data[16]
        sum_PF += data[17]
        sum_PTS += data[18]
        
        # Add the Players data one by one
        t.add_row([data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12], data[13], data[14], data[15], data[16], data[17], data[18]])

    # For Certain headers, the average value is required 
    sum_FGpercent = sum_FGpercent/10
    sum_FGpercent = round(sum_FGpercent, 3)

    sum_3Ppercent = sum_3Ppercent/ 6
    sum_3Ppercent = round(sum_3Ppercent, 3)

    sum_FTpercent = sum_FTpercent/ 3
    sum_FTpercent = round(sum_FTpercent, 3)

    # Add a row with summed stats 
    t.add_row(['Team Totals', sum_FG, sum_FGA, sum_FGpercent, sum_3P, sum_3PA, sum_3Ppercent, sum_FT, sum_FTA, sum_FTpercent, sum_ORB, sum_DRB, sum_TRB, sum_AST, sum_STL, sum_BLK, sum_TOV, sum_PF, sum_PTS])
    
    print (t) # Finally Printout 


team_dict = analyse_nba_game()

# print(team_dict) # The return of first function - list of dictionaries.

print_nba_game_stats(team_dict)

