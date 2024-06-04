import sqlite3

#CREATE TABLE match
def create_table_match():
    global c
    try:
        c.execute("""CREATE TABLE match (
                match_id integer,
                match_team1_team_id integer,
                match_team2_team_id integer,
                match_team1_goal integer,
                match_team2_goal integer,
                match_team1_corner integer,
                match_team2_corner integer,        
                match_league_id integer
                )""")
    except:
        print("Error with 'CREATE TABLE match' or table already exist")

#CREATE TABLE team
def create_table_team():
    global c
    try:
        c.execute("""CREATE TABLE team (
                team_id integer,
                team_name text
                )""")
    except:
        print("Error with 'CREATE TABLE team' or table already exist")

#CREATE TABLE player
def create_table_player():
    global c
    try:
        c.execute("""CREATE TABLE player (
                player_id integer,
                player_name text,
                player_team_id
                )""")
    except:
        print("Error with 'CREATE TABLE player' or table already exist")


#CREATE TABLE team_player
def create_table_team_player():
    global c
    try:
        c.execute("""CREATE TABLE team_player (
                team_player_id integer,
                team_player_team_id integer,
                team_player_player_id integer
                )""")
    except:
        print("Error with 'CREATE TABLE team_player' or table already exist")

#CREATE TABLE league
def create_table_league():
    global c
    try:
        c.execute("""CREATE TABLE league (
                league_id integer,
                league_name text,
                league_years text,
                )""")
    except:
        print("Error with 'CREATE TABLE league' or table already exist")

#CREATE TABLE league_teams
def create_table_league_teams():
    global c
    try:
        c.execute("""CREATE TABLE league_teams (
                league_teams_id integer,
                league_teams_team_id integer,
                league_teams_league_id integer
                )""")
    except:
        print("Error with 'CREATE TABLE league_teams' or table already exist")


#CREATE THE TABLES
def create_my_tables_start():
    global c
    conn = sqlite3.connect("my_database.db")
    c = conn.cursor()

    create_table_match()
    create_table_team()
    create_table_player()
    create_table_team_player()
    create_table_league()
    create_table_league_teams()


    conn.commit()
    conn.close()


