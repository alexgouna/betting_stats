import sqlite3


def sql(place, team):
    conn = sqlite3.connect("my_database_esoccer.db")
    c = conn.cursor()
    my_sql = "SELECT COUNT(*),SUM(goal_{0}) FROM total_info_detailed WHERE {0} = '{1}'".format(place, team)
    c.execute(my_sql)
    my_data = c.fetchall()
    conn.commit()
    conn.close()
    return (my_data)


def my_data(team):
    my_data = (team, sql("home", team)[0][0], sql("home", team)[0][1], sql("away", team)[0][0], sql("away", team)[0][1], 'wins_home', 'wins_away')

    return my_data


def compare(team1, team2):
    my_data_team_1 = my_data(team1)
    my_data_team_2 = my_data(team2)
    print(my_data_team_1)
    print(my_data_team_2)


compare('Bayern(BlackStar9)', 'Bayern(BlackStar9)')
