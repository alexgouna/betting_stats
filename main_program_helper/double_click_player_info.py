import sqlite3


def player_info_start(team):
    conn = sqlite3.connect("my_database_esoccer.db")
    c = conn.cursor()

    sql = "SELECT * FROM total_info WHERE Home LIKE '%{0}%' OR Away LIKE '%{0}%'".format(team)

    my_data = c.execute(sql).fetchall()

    conn.commit()
    conn.close()
    return my_data


