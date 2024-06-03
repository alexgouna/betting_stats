import sqlite3
import global_variables

def my_sql_of_views(my_view):
    if my_view == 'team_player_with_names':
        sql = "CREATE VIEW team_player_with_names AS " \
              "SELECT player_team_id,player_name,team_name,(team_name || '('|| player_name || ')') as full_name  FROM player_team,player,team" \
              " WHERE player_team_player_id=player_id AND player_team_team_id=team_id"
    elif my_view == 'total_info':
        sql = "CREATE VIEW total_info AS " \
              "SELECT games_team_date_time,t1.full_name AS Home, (games_team_1_goal || ' - '|| games_team_2_goal) as goal, t2.full_name AS Away, " \
              "(games_team_1_corner || ' - '|| games_team_2_corner) as corner, (games_team_1_shots || ' - '|| games_team_2_shots) as shots " \
              "FROM games as g " \
              "JOIN team_player_with_names t1 ON g.games_team_1_player_team_id = t1.player_team_id " \
              "JOIN team_player_with_names t2 ON g.games_team_2_player_team_id = t2.player_team_id "
    elif my_view == 'total_info_detailed':
        sql = "CREATE VIEW total_info_detailed AS " \
              "SELECT (SUBSTR(games_team_date_time,7,4) || '/' || SUBSTR(games_team_date_time,4,2) || '/' ||SUBSTR(games_team_date_time,1,2)) as date, " \
              "SUBSTR(games_team_date_time,12,5) as hour, t1.full_name AS Home, games_team_1_goal as goal_home, games_team_2_goal as goal_away, " \
              "t2.full_name AS Away, games_team_1_corner  as corner_home, games_team_2_corner  as corner_home, " \
              "games_team_1_shots as shots_home, games_team_2_shots as shots_away " \
              "FROM games as g " \
              "JOIN team_player_with_names t1 ON g.games_team_1_player_team_id = t1.player_team_id " \
              "JOIN team_player_with_names t2 ON g.games_team_2_player_team_id = t2.player_team_id "
    else:
        sql =""
    return sql

def views_to_create():
    sql_list_to_create = []
    for my_view in global_variables.my_list_of_views:
        sql_list_to_create.append(my_sql_of_views(my_view))
    return sql_list_to_create


def views_to_drop():
    sql_list_to_drop=[]
    for my_view in global_variables.my_list_of_views:
        sql_list_to_drop.append('DROP VIEW IF EXISTS {0}'.format(my_view))
    return sql_list_to_drop

def create_my_views():


    conn = sqlite3.connect("my_database_esoccer.db")
    c = conn.cursor()

    #drop my_views
    for sql in views_to_drop():
        c.execute(sql)

    #create my_views
    for sql in views_to_create():
        c.execute(sql)


    conn.commit()
    conn.close()