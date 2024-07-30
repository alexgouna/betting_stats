import sqlite3
from tkinter import *
from tkinter import messagebox
import my_table_connection
import my_table_connection.sql_string as sql_string
import config
import requests
from bs4 import BeautifulSoup
import time


def name_player(my_string):
    return my_string[my_string.find('(') + 1:len(my_string) - 1]


def name_team(my_string):
    if 'me">' in my_string:
        return my_string[4:my_string.find('(') - 1]
    return my_string[:my_string.find('(') - 1]


#  returning the team names and the links for each.
def get_first_page_data(my_link):
    my_table = []

    try:
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

            my_table.append((home_name_player, home_name_team, home_link))
            my_table.append((away_name_player, away_name_team, away_link))
    except Exception as error:
        print("'def get_first_page_data(my_link)")
        print(error.args)
        time.sleep(20)
        get_first_page_data(my_link)

    return (my_table)


# all data from 1 page of the team
def break_down_all_data(all_data_from_page):
    global my_year
    global my_month_old
    my_month_old = '12'
    my_year = 2024

    def custom_date(my_date):
        global my_year
        global my_month_old
        my_month = my_date[:2]
        my_day = my_date[3:5]
        my_hour = my_date[6:]
        if int(my_month_old) < int(my_month):
            my_year = my_year - 1
        my_month_old = my_month
        return str(my_year) + '/' + my_month + '/' + my_day + ' ' + my_hour

    my_table = []
    while True:

        date_start = all_data_from_page.find('<td class="text-center">') + 24
        date_end = date_start + 11

        home_name_start = all_data_from_page.find('target="_blank">', date_end) + 31
        home_name_end = all_data_from_page.find('Esports', home_name_start) - 1

        score_start = all_data_from_page.find('text-center match_goal', home_name_end) + 24
        score_end = all_data_from_page.find('</td>', score_start)

        away_name_start = all_data_from_page.find('target="_blank">', score_end) + 31
        away_name_end = all_data_from_page.find('Esports', away_name_start) - 1

        my_date = custom_date(all_data_from_page[date_start:date_end])
        home_name_player = name_player(all_data_from_page[home_name_start:home_name_end])
        home_name_team = name_team(all_data_from_page[home_name_start:home_name_end])
        home_goal = all_data_from_page[score_start:score_start + 1]
        away_goal = all_data_from_page[score_end - 1:score_end]
        away_name_player = name_player(all_data_from_page[away_name_start:away_name_end])
        away_name_team = name_team(all_data_from_page[away_name_start:away_name_end])

        my_table.append(
            (my_date, home_name_player, home_name_team, home_goal, away_goal, away_name_player, away_name_team))
        all_data_from_page = all_data_from_page[away_name_end:]
        if all_data_from_page.find('<td class="text-center">') == -1:
            break
    return my_table


def get_detail_team_games_for_each_page(my_link):
    my_page_data = []
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(my_link, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # find all tables
        for all_data_from_page in soup.findAll("table"):

            my_page_data.append(break_down_all_data(str(all_data_from_page)))
    except Exception as error:
        print("'def get_detail_team_games_for_each_page(my_link)'")
        print(error.args)
        if not  'invalid literal for int()' in str(error.args):
            time.sleep(20)
            get_detail_team_games_for_each_page(my_link)
    return my_page_data[0]



def last_page(my_link):
    return config.get_last_page(my_link)


def get_detail_team_games(my_link):
    my_table = []
    for page in range(1, last_page(my_link)):
        time.sleep(2)
        my_data = get_detail_team_games_for_each_page(my_link + str(page))

        # import data to database
        my_table_connection.import_my_data_to_database(my_data)

        my_table.append(my_data)
    return (my_table)
