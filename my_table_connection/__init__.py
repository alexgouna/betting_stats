import sqlite3
import my_table_connection.sql_string as sql_string
import global_variables
import requests
from bs4 import BeautifulSoup


def drop_create_table():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    for table_name in global_variables.list_tables:
        try:
            c.execute(sql_string.drop_table(table_name))
        except:
            pass
        try:
            c.execute(sql_string.create_table(table_name))
        except:
            pass
    conn.commit()
    conn.close()


# def get_first_page_data(my_link):
#     conn = sqlite3.connect('database.db')
#     c = conn.cursor()
#     c.execute(sql_string.first_page(my_link))
#     my_table = c.fetchall()
#     conn.commit()
#     conn.close()
#     return my_table


#  returning the team names and the links for each.
def get_first_page_data(my_link):
    def name_player(my_string):
        return my_string[my_string.find('(') + 1:len(my_string) - 1]

    def name_team(my_string):
        return my_string[:my_string.find('(') - 1]

    my_table=[]

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(my_link, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')

    # find all tables
    soup.findAll("table")

    # find the table I need and use my_raw_table to store it. raw data in my_raw_table. each row is the data of a game
    my_raw_table = []
    for table in soup.findAll("table"):
        if "start time" in str(table):
            for row in table.findAll("tr"):
                my_raw_table.append(str(row))
            my_raw_table = my_raw_table[1:21]

    # breakdown the data from my_raw_table and find the links of the first 20 games
    for row in my_raw_table:
        home_link_start = row.find('/team/view/')
        home_link_end = row.find('">', home_link_start)

        home_name_start = home_link_end + 2
        home_name_end = row.find('Esports', home_name_start) - 1

        away_link_start = row.find('/team/view/', home_name_end)
        away_link_end = row.find('">', away_link_start)

        away_name_start = away_link_end + 2
        away_name_end = row.find('Esports', away_name_start) - 1

        home_link = "https://www.totalcorner.com/" + row[home_link_start:home_link_end] + "/page:"
        home_name_player = name_player(row[home_name_start:home_name_end])
        home_name_team = name_team(row[home_name_start:home_name_end])

        away_link = "https://www.totalcorner.com/" + row[away_link_start:away_link_end] + "/page:"
        away_name_player = name_player(row[away_name_start:away_name_end])
        away_name_team = name_team(row[away_name_start:away_name_end])

        my_table.append((home_name_player,home_name_team,home_link))
        my_table.append((away_name_player,away_name_team,away_link))

    return(my_table)

