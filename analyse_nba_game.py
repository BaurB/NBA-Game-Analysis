
def analyse_nba_game():
    # Get access to the play by play data of Oklahoma City Thunder vs Golden State Warriors. The encoding is required since some players have non-ASCII characters (e.g. D. SchrÃ¶der)
    with open ('mynba.txt', 'r', encoding='utf-8') as my_file:
        lines = my_file.readlines()
        
        list_of_lists = []
        
        # Split the data by '|' and organize it to the list of lists
        for line in lines:
            line = line.split('|')
            line[7] = line[7].replace('\n', '')
            list_of_lists += [line]  # Now we have list of lists
        
        My_dictlist = [] # This variable will store my results. It will store the return variable which is a list of dictionaries 

        # Before analysing the stats of a particular player, I need to include all the players to the list. One list is for Warriors players and other is for Oklahoma players.
        Warriors_players_list = ['K. Durant', 'S. Curry', 'K. Thompson', 'D. Green', 'D. Jones', 'K. Looney', 'S. Livingston', 'Q. Cook', 'A. Iguodala', 'J. Bell', 'J. Jerebko', 'A. McKinnie'] 

        Oklahoma_players_list = ['P. George', 'S. Adams', 'D. SchrÃ¶der', 'P. Patterson', 'T. Ferguson', 'J. Grant', 'Ã. Abrines', 'R. Felton', 'N. Noel', 'H. Diallo']
        
        # As can we see the number of Oklahoma players is less than the count of Warriors players. The for loop below is based on length of Warriors players list. When Oklahoma Players list is finished, the dictionary data for Warriors players will be still calculated. 
        for i in range (len(Warriors_players_list)):   
            # DATA dictionary
            Warriors_DATA =  {'players_name': Warriors_players_list[i], "FG": 0, "FGA": 0, "FG%": 0, "3P": 0, "3PA": 0, "3P%": 0, "FT": 0, "FTA": 0, "FT%": 0, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0}
                                    
            for j in range(len(list_of_lists)):
                Description = list_of_lists [j] [7] # (e.g. Turnover by K. Thompson)
                Home_Team = list_of_lists [j] [4] 
                Away_Team = list_of_lists [j] [3] 
                
                # A bunch of If statements are made to calculate data for the players.
                if ((Warriors_players_list[i] + ' makes 2-pt' in Description) or (Warriors_players_list[i] + ' makes 2-pt dunk' in Description) or (Warriors_players_list[i] + ' makes 2-pt hook shot' in Description) or (Warriors_players_list[i] + ' makes 3-pt jump shot' in Description)):
                    Warriors_DATA['FG'] += 1

                if ((Warriors_players_list[i] + ' makes 2-pt' in Description)or (Warriors_players_list[i] + ' makes 3-pt jump shot' in Description) or (Warriors_players_list[i] + ' misses 2-pt' in Description) or (Warriors_players_list[i] + ' misses 3-pt' in Description) ):
                    Warriors_DATA['FGA'] += 1

                if ('Defensive rebound by ' + Warriors_players_list[i] in Description):
                    Warriors_DATA['DRB'] += 1

                if (Warriors_players_list[i] + ' makes 3-pt' in Description):
                    Warriors_DATA['3P'] += 1

                if (Warriors_players_list[i] + ' misses 3-pt' in Description or Warriors_players_list[i] + ' makes 3-pt' in Description):
                    Warriors_DATA ['3PA'] += 1

                if (Warriors_players_list[i] + ' makes free throw' in Description):
                    Warriors_DATA ['FT'] += 1

                if (Warriors_players_list[i] + ' makes free throw' in Description or Warriors_players_list[i] + ' misses free throw' in Description ):
                    Warriors_DATA ['FTA'] += 1

                if ('Offensive rebound by ' + Warriors_players_list[i] in Description):
                    Warriors_DATA['ORB'] += 1

                if ('assist by ' + Warriors_players_list[i] in Description):
                    Warriors_DATA['AST'] += 1

                if ('steal by ' + Warriors_players_list[i] in Description):
                    Warriors_DATA['STL'] += 1

                if ('block by ' + Warriors_players_list[i] in Description):
                    Warriors_DATA['BLK'] += 1

                if ('Turnover by ' + Warriors_players_list[i] in Description):
                    Warriors_DATA['TOV'] += 1  

                if ('foul by ' + Warriors_players_list[i] in Description):
                    Warriors_DATA['PF'] += 1
            
            # Some players have zero integer for some activities. A try and except approach was used to avoid any error 
            try:
                Warriors_DATA ['FT%'] = round((Warriors_DATA['FT'] / Warriors_DATA['FTA']), 3) # If result is a float number, the round by 3 digits is made

            except:
                Warriors_DATA ['FT%'] = 0

            try:
                Warriors_DATA ['FG%'] = round((Warriors_DATA['FG'] / Warriors_DATA['FGA']), 3)

            except:
                Warriors_DATA ['FG%'] = 0

            try:
                Warriors_DATA ['3P%'] = round ((Warriors_DATA['3P'] / Warriors_DATA['3PA']) , 3)

            except:
                Warriors_DATA ['3P%'] = 0

            Warriors_DATA ['TRB'] = round((Warriors_DATA['ORB'] + Warriors_DATA['DRB']), 3)
            
            Warriors_DATA ['PTS'] = round((( Warriors_DATA['FG'] - Warriors_DATA['3P'] ) * 2 + Warriors_DATA['3P'] * 3 + Warriors_DATA['FT'] * 1), 3) 

            # Since list of Oklahoma player is smaller compared to Warriors players, I have used try and except method. I firstly calculate data until the list is finished. Then, I just leave the player name as blank and all result attributes (FG, FGA etc) as zero.
            try:
                Oklahoma_DATA =  {'players_name': Oklahoma_players_list[i], "FG":0, "FGA": 0, "FG%": 0, "3P": 0, "3PA": 0, "3P%": 0, "FT": 0, "FTA": 0, "FT%": 0, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0}

                for j in range(len(list_of_lists)):
                    Description = list_of_lists [j] [7]
                    Home_Team = list_of_lists [j] [4]
                    Away_Team = list_of_lists [j] [3]

                    if ((Oklahoma_players_list[i] + ' makes 2-pt' in Description) or (Oklahoma_players_list[i] + ' makes 2-pt dunk' in Description) or (Oklahoma_players_list[i] + ' makes 2-pt hook shot' in Description) or (Oklahoma_players_list[i] + ' makes 3-pt jump shot' in Description)):
                        Oklahoma_DATA['FG'] += 1

                    if ((Oklahoma_players_list[i] + ' makes 2-pt' in Description)or (Oklahoma_players_list[i] + ' makes 3-pt jump shot' in Description) or (Oklahoma_players_list[i] + ' misses 2-pt' in Description) or (Oklahoma_players_list[i] + ' misses 3-pt' in Description) ):
                        Oklahoma_DATA['FGA'] += 1

                    if ('Defensive rebound by ' + Oklahoma_players_list[i] in Description):
                        Oklahoma_DATA['DRB'] += 1

                    if (Oklahoma_players_list[i] + ' makes 3-pt' in Description):
                        Oklahoma_DATA['3P'] += 1

                    if (Oklahoma_players_list[i] + ' misses 3-pt' in Description or Oklahoma_players_list[i] + ' makes 3-pt' in Description):
                        Oklahoma_DATA ['3PA'] += 1

                    if (Oklahoma_players_list[i] + ' makes free throw' in Description):
                        Oklahoma_DATA ['FT'] += 1

                    if (Oklahoma_players_list[i] + ' makes free throw' in Description or Oklahoma_players_list[i] + ' misses free throw' in Description ):
                        Oklahoma_DATA ['FTA'] += 1

                    if ('Offensive rebound by ' + Oklahoma_players_list[i] in Description):
                        Oklahoma_DATA['ORB'] += 1

                    if ('assist by ' + Oklahoma_players_list[i] in Description):
                        Oklahoma_DATA['AST'] += 1

                    if ('steal by ' + Oklahoma_players_list[i] in Description):
                        Oklahoma_DATA['STL'] += 1

                    if ('block by ' + Oklahoma_players_list[i] in Description):
                        Oklahoma_DATA['BLK'] += 1

                    if ('Turnover by ' + Oklahoma_players_list[i] in Description):
                        Oklahoma_DATA['TOV'] += 1  

                    if ('foul by ' + Oklahoma_players_list[i] in Description):
                        Oklahoma_DATA['PF'] += 1

                try:
                    Oklahoma_DATA ['FT%'] = round((Oklahoma_DATA['FT'] / Oklahoma_DATA['FTA']), 3)

                except:
                    Oklahoma_DATA ['FT%'] = None

                try:
                    Oklahoma_DATA ['FG%'] = round((Oklahoma_DATA['FG'] / Oklahoma_DATA['FGA']), 3)

                except:
                    Oklahoma_DATA ['FG%'] = None

                try:
                    Oklahoma_DATA ['3P%'] = round ((Oklahoma_DATA['3P'] / Oklahoma_DATA['3PA']) , 3)
                except:
                    Oklahoma_DATA ['3P%'] = None

                Oklahoma_DATA ['TRB'] = round((Oklahoma_DATA['ORB'] + Oklahoma_DATA['DRB']), 3)

                Oklahoma_DATA ['PTS'] = round((( Oklahoma_DATA['FG'] - Oklahoma_DATA['3P'] ) * 2 + Oklahoma_DATA['3P'] * 3 + Oklahoma_DATA['FT'] * 1), 3) 
            
            except:
                
                Oklahoma_DATA =  {'players_name': None, "FG":0, "FGA": 0, "FG%": 0, "3P": 0, "3PA": 0, "3P%": 0, "FT": 0, "FTA": 0, "FT%": 0, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0}
                        
            # Now a single dictionary is composed out of variables presented before
            Dictionary = {"home_team": {"name": list_of_lists[0] [4], "players_data": Warriors_DATA}, "away_team": {"name": list_of_lists[0] [3], "players_data": Oklahoma_DATA}}

#             print (Dictionary) Print one Dictionary at a time
            
            My_dictlist += [Dictionary] # Add the dictionaries to one list of dictionaries
            
   
        return My_dictlist # List of dictionaries



