from urllib.request import Request, urlopen
import sqlite3
import global_variables
from datetime import datetime
import time
import pandas as pd



# get the data from site
def my_list_with_esoccer_data(site_page):
    my_list=[]
    try:
        url = global_variables.my_url + str(site_page)
        request = Request(url)
        request.add_header('user-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36')
        page = urlopen(request)
        html_content = page.read()
        tables = pd.read_html(html_content)
        for record in tables[0].values.tolist():
            my_list.append(record)

        # for i in my_list:
        #     print(site_page)
        #     print(i)
        #     print("--------------------------------")
    except Exception as error:
        print(error)
    return my_list

# check if the record is valid
def the_record_is_valid(my_record):
    global c
    try:
        if my_record.find("(")!=-1 and my_record.find(")")!=-1:
            return True
    except Exception:
        return False

# fill up the tables player  ----   team   -----    team_player
def my_team_name_player_name(my_record):
    global c
    global my_team_player_id
    #INSERT PLAYER AND TEAM NAMES to the tables
    try:
        my_team_name = my_record[:my_record.find("(")-1]
        my_player_name = my_record[my_record.find("(")+1:my_record.find(")")-1]
        sql = " INSERT INTO team (team_name) SELECT ('{0}') WHERE NOT EXISTS (SELECT * FROM team WHERE team_name='{0}')".format(my_team_name)
        c.execute(sql)
        sql = " INSERT INTO player (player_name) SELECT ('{0}') WHERE NOT EXISTS (SELECT * FROM player WHERE player_name='{0}')".format(my_player_name)
        c.execute(sql)

        # GET TEAM AND PLAYER ID
        sql = "SELECT team_id FROM team WHERE team_name='{0}'".format(my_team_name)
        c.execute(sql)
        my_team_id=c.fetchall()[0][0]
        sql = "SELECT player_id FROM player WHERE player_name='{0}'".format(my_player_name)
        c.execute(sql)
        my_payer_id=c.fetchall()[0][0]

        #CONNECT PLAYER WITH TEAM
        sql = """ INSERT INTO player_team (player_team_player_id,player_team_team_id) SELECT {0},{1}
                WHERE NOT EXISTS (SELECT * FROM player_team WHERE player_team_player_id ={0} AND player_team_team_id={1})
                """.format(my_payer_id,my_team_id)
        c.execute(sql)
        # get team_player_id for later use
        sql = """SELECT player_team_id FROM player_team WHERE player_team_player_id ={0} AND player_team_team_id={1}
                """.format(my_payer_id,my_team_id)
        c.execute(sql)
        my_team_player_id=c.fetchall()[0][0]
    except Exception:
        print(Exception)



#fill league table
def my_league(league,minutes):
    global c
    sql = """ INSERT INTO league (league_name,league_minutes) SELECT '{0}',{1} 
            WHERE NOT EXISTS (SELECT * FROM league WHERE league_name='{0}')""".format(league,minutes)
    c.execute(sql)


# prepare the record for game table with the values
def my_games_record(my_team_player_1_id,my_team_player_2_id,record):

    #seperates the numbers from the text. needs to be formated "2 - 5" to be correct
    #works for the goals, corners and shots.
    def find_my_number(record,player):
        my_number = record.find(" - ")
        if player == 1 :
            return int(record[0:my_number])
        else:
            return int(record[my_number+3:len(record)])

    def games_team_date_time(record):

        def my_year():
            if int(global_variables.month_previous)<int(global_variables.month_current):
                global_variables.current_year =global_variables.current_year-1
            return str(global_variables.current_year)


        def my_month(record):
            global_variables.month_previous = global_variables.month_current
            global_variables.month_current = record[:2]
            return global_variables.month_current


        def my_day(record):
            return record[3:5]


        def my_hour(record):
            return record[6:]

        my_date = my_day(record)+'/'+my_month(record)+'/'+my_year()+' '+ my_hour(record)
        return (my_date)

    my_record=(my_team_player_1_id,my_team_player_2_id,find_my_number(record[3],1),find_my_number(record[3],2),
               find_my_number(record[6],1),find_my_number(record[6],2),
               find_my_number(record[6],1),find_my_number(record[6],2),games_team_date_time(record[0]))
    return my_record

#fill the game table with the values
def my_games(my_team_player_1_id,my_team_player_2_id,record):
    global c
    my_record = my_games_record(my_team_player_1_id, my_team_player_2_id, record)
    sql = """ INSERT INTO games (games_team_1_player_team_id,games_team_2_player_team_id,games_team_1_goal,games_team_2_goal,
            games_team_1_corner,games_team_2_corner,games_team_1_shots,games_team_2_shots,games_team_date_time) 
            SELECT {0},{1},{2},{3},{4},{5},{6},{7},'{8}' WHERE NOT EXISTS
            (SELECT * FROM games WHERE games_team_1_player_team_id = '{0}' AND games_team_2_player_team_id = '{1}' AND games_team_1_goal = '{2}' AND
            games_team_2_goal = '{3}' AND games_team_1_corner = '{4}' AND games_team_2_corner = '{5}' AND
            games_team_1_shots = '{6}' AND games_team_2_shots = '{7}')
            """.format(my_record[0],my_record[1],my_record[2],my_record[3],my_record[4],my_record[5],my_record[6],my_record[7],my_record[8])
    c.execute(sql)

def esoccer_move_data():
    global c
    global my_team_player_id

    my_team_player_id=0

    for site_page in range(global_variables.my_first_page, global_variables.my_total_pages):
        conn = sqlite3.connect("my_database_esoccer.db")
        c = conn.cursor()
        if site_page%10 ==0 :
            time.sleep(global_variables.wait_time)

        for record in my_list_with_esoccer_data(site_page):
            if the_record_is_valid(record[2]):
                my_team_name_player_name(record[2])
                my_team_player_1_id = my_team_player_id
                my_team_name_player_name(record[4])
                my_team_player_2_id = my_team_player_id
                my_league('Esoccer Battle - 8 mins',8)
                my_games(my_team_player_1_id,my_team_player_2_id,record)
        print (site_page)
        conn.commit()
        conn.close()



