import threading

from tkinter import *
from tkinter import ttk, messagebox
import global_variables as my_var
import pandas as pd
import my_table_connection
import xlwings as xw
import os
import datetime

def retrieve_my_data(self):
    pass
    # my_data = []
    # my_table = []
    # if len(self.entry_search.get()) > 10:
    #     my_data.append(get_my_data_from_total_cormer.get_my_team_first_page_link(self.entry_search.get()))
    # else:
    #     # print(my_var.list_league())
    #     for my_link in my_var.list_league():
    #         # print(my_link)
    #         for link in sql_connections.get_my_team_first_page_link(my_link):
    #             for i in range(1, my_var.my_pages_to_collect_data):
    #                 my_data.append(get_my_data_from_total_cormer.get_my_team_first_page_link(link + str(i)))
    #
    # for page in my_data:
    #     # print(page)
    #     if page is not None:
    #         for row in page:
    #             my_table.append(row)
    # my_table = duplicate_or_already_exist_in_sql(my_table)
    #
    # sql_connections.insert_data_of_the_games(my_table)


def create_database(self):
    answer = messagebox.askyesno('Warning!!!','You will delete all Data!!!\nDo you want to continue?', icon='warning')
    # print(answer)
    if answer:
        my_table_connection.drop_create_table()


def live_page(self):

    print("live page data")

    #getting a list with lists. for each link league, each team and their links on main paig
    list_teams_links=[]
    for my_link in my_var.link_main_page:
        print(my_link)
        list_teams_links.append(my_table_connection.get_first_page_data(my_link))
        # print(list_teams_links)

    # for each team I am getting all the games
    for league in list_teams_links:
        for team in league:
            team_detail_games = (my_table_connection.get_detail_team_games(team[2]))
            print("---------------------------------------")
            print(team[2])
            print(team_detail_games)
        # team_detail_games = (my_table_connection.get_detail_team_games(league[0][2]))



def show_detailed_data():
    pass
    #Show_data.show_detailed_data()

def create_excell_all_data():
    pass


class DesignMainWindow:

    def __init__(self, root):
        self.root = root
        # create all the frames
        self.frame_top = Frame(self.root, height=50)
        self.frame_buttom = Frame(self.root, height=500)

        self.my_button_live_page_data = Button(self.frame_top, text="get data from live page", command=lambda: live_page(self),width=30, padx=50, pady=30)
        self.my_button_create_database_and_tables = Button(self.frame_top, text="create database and tables", command=lambda: create_database(self),width=30, padx=50, pady=30)
        self.my_button_show_data_details = Button(self.frame_top, text="Show detailed data", command=show_detailed_data,width=30, padx=50, pady=30)
        self.my_button_create_excell_all_data = Button(self.frame_top, text="Create excell all data", command=create_excell_all_data,width=30, padx=50, pady=30)


        self.frame_top.pack(side=TOP, expand=False, fill=BOTH)
        self.frame_buttom.pack(side=BOTTOM, expand=True, fill=BOTH)
        self.my_button_live_page_data.pack(pady=5)
        self.my_button_create_database_and_tables.pack(pady=5)
        self.my_button_show_data_details.pack(pady=5)
        self.my_button_create_excell_all_data.pack(pady=5)

        # Bind the Escape key to a function that does nothing
        self.root.bind('<Escape>', self.do_nothing)

    def do_nothing(self, event):
        print("escape")


class Start:
    def __init__(self):
        self.root = Tk()
        self.root.title("Main!!!")
        self.root.geometry("800x400")

        self.main_window = DesignMainWindow(self.root)

        mainloop()


if __name__ == "__main__":
    Start()
