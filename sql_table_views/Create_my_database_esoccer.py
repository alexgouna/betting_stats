import sqlite3


# CREATE TABLE team
def create_table_team():
    global c
    try:
        #drop the table if exist to recreate
        c.execute("DROP TABLE team")
    except:
        pass
    try:
        c.execute("""CREATE TABLE team (
                team_id INTEGER NOT NULL,
                team_name TEXT,
                PRIMARY KEY(team_id AUTOINCREMENT)
                )""")
    except:
        print("Error with esoccer 'CREATE TABLE team'")


# CREATE TABLE player
def create_table_player():
    global c
    try:
        #drop the table if exist to recreate
        c.execute("DROP TABLE player")
    except:
        pass
    try:
        c.execute("""CREATE TABLE player (
                player_id INTEGER NOT NULL,
                player_name TEXT,
                PRIMARY KEY(player_id AUTOINCREMENT)
                )""")
    except:
        print("Error with esoccer 'CREATE TABLE player'")


# CREATE TABLE player_team CONNECT EACH PLAYER WITH A TEA
def create_table_player_team():
    global c
    try:
        #drop the table if exist to recreate
        c.execute("DROP TABLE player_team")
    except:
        pass
    try:
        c.execute("""CREATE TABLE player_team (
                player_team_id INTEGER NOT NULL,
                player_team_player_id INTEGER,
                player_team_team_id INTEGER,
                PRIMARY KEY(player_team_id AUTOINCREMENT)
                )""")
    except:
        print("Error with esoccer 'CREATE TABLE player_team'")


# CREATE TABLE league create a list with leagues
def create_table_league():
    global c
    try:
        #drop the table if exist to recreate
        c.execute("DROP TABLE league")
    except:
        pass
    try:
        c.execute("""CREATE TABLE league (
                league_id INTEGER NOT NULL,
                league_name TEXT,
                league_minutes INTEGER,
                PRIMARY KEY(league_id AUTOINCREMENT)
                )""")
    except:
        print("Error with esoccer 'CREATE TABLE league'")


# CREATE TABLE games
def create_table_games():
    global c

    try:
        #drop the table if exist to recreate
        c.execute("DROP TABLE games")
    except:
        pass
    try:
        c.execute("""CREATE TABLE games (
                games_id INTEGER NOT NULL ,
                games_team_1_player_team_id INTEGER,
                games_team_2_player_team_id INTEGER,
                games_team_1_goal INTEGER,
                games_team_2_goal INTEGER,
                games_team_1_corner INTEGER,
                games_team_2_corner INTEGER,
                games_team_1_shots INTEGER,
                games_team_2_shots INTEGER,
                games_team_date_time DATE,
                PRIMARY KEY(games_id AUTOINCREMENT)
                )""")


    except:
        print("Error with esoccer 'CREATE TABLE league'")


# CREATE THE TABLES
def create_my_tables_start():
    global c
    conn = sqlite3.connect("my_database_esoccer.db")
    c = conn.cursor()

    create_table_team()
    create_table_player()
    create_table_player_team()
    create_table_league()
    create_table_games()

    conn.commit()
    conn.close()
