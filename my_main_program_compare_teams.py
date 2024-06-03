import sqlite3


def sql(place, team):
    global c
    other_place = 'home'
    if place=="home":
        other_place='away'

    my_sql = "SELECT COUNT(*),SUM(goal_{0}),SUM(CASE WHEN goal_{0} > goal_{1} THEN 1 ELSE 0 END), " \
             "SUM(CASE WHEN goal_{0} = goal_{1} THEN 1 ELSE 0 END), SUM(CASE WHEN goal_{0} < goal_{1} THEN 1 ELSE 0 END) " \
             "FROM total_info_detailed WHERE {0} = '{2}'".format(place,  other_place, team)
    c.execute(my_sql)
    my_data = c.fetchall()

    return my_data[0]


def my_data(team):

    #my_data = (team, TOTAL GAMES        , HOME  GAMES         , HOME  GOAL          , HOME WINS           , HOME DRAW           , HOME LOSES
    my_data = (team, sql("home", team)[0] + sql("away", team)[0], sql("home", team)[0], sql("home", team)[1], sql("home", team)[2], sql("home", team)[3], sql("home", team)[4],
    sql("away", team)[0], sql("away", team)[1], sql("away", team)[2],  sql("away", team)[3], sql("away", team)[4])
    #AWAY  GAMES        , AWAY  GOAL          , AWAY WINS            , AWAY DRAW            ,          , AWAY LOSES

    return my_data


def compare(team1, team2):
    global c
    conn = sqlite3.connect("my_database_esoccer.db")
    c = conn.cursor()
    my_data_team_1 = my_data(team1)
    my_data_team_2 = my_data(team2)

    conn.commit()
    conn.close()
    return my_data_team_1,my_data_team_2

