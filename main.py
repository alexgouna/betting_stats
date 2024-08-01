import multiprocessing
from tkinter import *
from tkinter import messagebox
import config

import my_table_connection


def retrieve_my_data():
    pass

def create_database():
    answer = messagebox.askyesno('Warning!!!', 'You will delete all Data!!!\nDo you want to continue?', icon='warning')
    if answer:
        my_table_connection.drop_create_table()

def live_page():
    print("live page data")
    list_teams_links = []
    for my_link in config.link_main_page:
        print(my_link)
        list_teams_links.append(my_table_connection.get_first_page_data(my_link))

    for league in list_teams_links:
        for team in league:
            team_detail_games = my_table_connection.get_detail_team_games(team[2])
            print("---------------------------------------")
            print(team[2])
            print(team_detail_games)




def show_detailed_data():
    my_table_connection.show_all_detailed_data()

def create_excell_all_data():
    pass

class DesignMainWindow:
    def __init__(self, root):
        self.root = root
        self.frame_top = Frame(self.root, height=50)
        self.frame_buttom = Frame(self.root, height=500)

        self.my_button_live_page_data = Button(self.frame_top, text="get data from live page", command=lambda: self.run_in_process_live_page(), width=30, padx=50, pady=30)
        self.my_button_create_database_and_tables = Button(self.frame_top, text="create database and tables", command=lambda: self.run_in_process(create_database), width=30, padx=50, pady=30)
        self.my_button_show_data_details = Button(self.frame_top, text="Show detailed data", command=show_detailed_data, width=30, padx=50, pady=30)
        # self.my_button_show_data_two_teams = Button(self.frame_top, text="Show data for two teams", command=show_data_two_teams, width=30, padx=50, pady=30)
        self.my_button_create_excell_all_data = Button(self.frame_top, text="Create excell all data", command=create_excell_all_data, width=30, padx=50, pady=30)

        self.frame_top.pack(side=TOP, expand=False, fill=BOTH)
        self.frame_buttom.pack(side=BOTTOM, expand=True, fill=BOTH)
        self.my_button_live_page_data.pack(pady=5)
        self.my_button_create_database_and_tables.pack(pady=5)
        self.my_button_show_data_details.pack(pady=5)
        # self.my_button_show_data_two_teams.pack(pady=5)
        self.my_button_create_excell_all_data.pack(pady=5)


    def run_in_process_live_page(self):
        def command_all():
            config.last_page_custom_bool = False
            self.run_in_process(live_page)
            self.my_button_live_page_data.config(state=DISABLED)
            self.child_root.destroy()

        def command_custom():

            try:
                config.last_page_custom_page = int(self.my_entry.get())
                config.last_page_custom_bool = True
                self.run_in_process(live_page)
                self.my_button_live_page_data.config(state=DISABLED)
                self.child_root.destroy()
            except:
                messagebox.showerror("ERROR!!!!", "Put a valid number in the box")


        def command_cansel():
            self.child_root.destroy()

        self.child_root = Toplevel(self.root)
        self.child_root.title("Last page!!!")
        self.child_root.geometry("300x180")

        self.child_frame_top = Frame(self.child_root)
        self.child_frame_bottom = Frame(self.child_root)

        self.child_frame_top.pack(fill='both', side='top', expand=True)
        self.child_frame_bottom.pack(fill='both', side='top', expand=True)

        self.my_label = Label(self.child_frame_top,text="* ALL for retrieving all the data\n* Custom for a number of pages",justify="left", font=('15'))
        self.my_label_pages = Label(self.child_frame_top,text="Pages :", justify="left", font=('15'))
        self.my_entry = Entry(self.child_frame_top)

        self.my_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        self.my_label_pages.grid(row=1, column=0, padx=10, pady=10)
        self.my_entry.grid(row=1, column=1, sticky=W, padx=5)


        self.my_button_all = Button(self.child_frame_bottom,text="ALL", command=command_all, width=10)
        self.my_button_custom = Button(self.child_frame_bottom, text="Custom", command=command_custom, width=10)
        self.my_button_cansel = Button(self.child_frame_bottom, text="Cansel", command=command_cansel, width=10)

        self.my_button_all.grid(row = 0, column= 0,padx=10)
        self.my_button_custom.grid(row = 0, column= 1,padx=10)
        self.my_button_cansel.grid(row = 0, column= 2,padx=10)

        self.child_root.mainloop()

        self.my_button_live_page_data.config(state=NORMAL)


    def run_in_process_show_all_detailed_data(self):
        self.run_in_process(show_detailed_data)

    def run_in_process(self, target):
        process = multiprocessing.Process(target=target)
        process.start()

class Start:
    def __init__(self):
        self.root = Tk()
        self.root.title("Main!!!")
        self.root.geometry("800x400")
        self.main_window = DesignMainWindow(self.root)
        mainloop()


if __name__ == "__main__":
    multiprocessing.freeze_support()  # For Windows support
    Start()
