

def drop_table(table_name):
    my_sql_string = f"""
    DROP TABLE {table_name}
    """
    return my_sql_string

def create_table(table_name):
    if table_name == "game":
        my_sql_string = f"""
       CREATE TABLE "table_team_games" (
                "game_id"	INTEGER UNIQUE,
                "game_date"	TEXT,
                "game_home"	TEXT,
                "game_homelink"	TEXT,
                "game_away"	TEXT,
                "game_awaylink"	TEXT,
                "game_homegoal"	TEXT,
                "game_awaygoal"	TEXT,
                "game_homecorner"	TEXT,
                "game_awaycorner"	TEXT,
                "game_homeshots"	TEXT,
                "game_awayshots"	TEXT,
                PRIMARY KEY("game_id" AUTOINCREMENT)
            );
        """
    else: my_sql_string=""
    return my_sql_string

def first_page(my_link):
    my_sql_string = """
    DROP TABLE 
    """
    return my_sql_string








