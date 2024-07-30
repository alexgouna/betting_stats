

def drop_table(table_name):
    my_sql_string = f"""
    DROP TABLE {table_name}
    """
    return my_sql_string

def create_table(table_name):
    if table_name == "table_team_games":
        my_sql_string = f"""
       CREATE TABLE "table_team_games" (
                "game_id"	INTEGER UNIQUE,
                "game_date"	TEXT,
                "game_homeplayername"	TEXT,
                "game_hometeamname"	TEXT,
                "game_homegoal"	TEXT,
                "game_awaygoal"	TEXT,
                "game_awayplayername"	TEXT,
                "game_awayteamname"	TEXT,
                PRIMARY KEY("game_id" AUTOINCREMENT)
            );
        """
    else: my_sql_string=""
    return my_sql_string



def import_data_to_table(my_data):
    my_sql_string = f"""
     INSERT INTO table_team_games(
    game_date, game_homeplayername, game_hometeamname,
    game_homegoal, game_awaygoal, game_awayplayername, game_awayteamname)
SELECT '{my_data[0]}', '{my_data[1]}', '{my_data[2]}', '{my_data[3]}', '{my_data[4]}', '{my_data[5]}', '{my_data[6]}'
WHERE NOT EXISTS (
    SELECT 1
    FROM table_team_games
    WHERE game_date = '{my_data[0]}'
      AND game_homeplayername = '{my_data[1]}'
      AND game_hometeamname = '{my_data[2]}'
      AND game_homegoal = '{my_data[3]}'
      AND game_awaygoal = '{my_data[4]}'
      AND game_awayplayername = '{my_data[5]}'
      AND game_awayteamname = '{my_data[6]}')
    """
    return my_sql_string



def excel_extract_data():
    my_sql_string = f"""
         SELECT * FROM
        """
    return my_sql_string

