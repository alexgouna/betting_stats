import tkinter.ttk
from tkinter import *
import sqlite3
import my_tree as tree
# from main_program_helper import double_click_compare_teams
import main_program_helper


def my_view_list_select(my_view):
    if my_view=="total_info_detailed":
        my_view_list = ('Date', 'Hour', 'Home', 'Goal Home', 'Goal Away', 'Away', 'Corner Home',
                        'Corner Away', 'Shots Home',' Shots Away')
    elif my_view=="total_info":
        my_view_list = ('Date', 'Home', 'Score', 'Away', 'Corner', 'Shots')
    else:
        my_view_list = ('ID', 'Player', 'Team', 'Full Name')
    return my_view_list


def start():
    global my_tree

    def choose(*args):
        global my_tree

        my_tree[0].destroy()
        my_tree[1].destroy()

        if clicked.get() == "Players with teams":
            my_tree = tree.func_my_tree_view("team_player_with_names", my_view_list_select("team_player_with_names"),root_my_main_program)
        elif clicked.get() == "Total Info":
            my_tree = tree.func_my_tree_view("total_info", my_view_list_select("total_info"), root_my_main_program)
        elif clicked.get() == "Total Info details":
            my_tree = tree.func_my_tree_view("total_info_detailed", my_view_list_select("total_info_detailed"), root_my_main_program)
        my_tree[0].bind("<Double-1>", on_double_click)



    def on_double_click(event):
        # Get the item that was double-clicked
        item_id = my_tree[0].identify_row(event.y)
        if item_id:
            item = my_tree[0].item(item_id)
            item_text = item['values']

            if clicked.get() == "Players with teams":
                my_data = main_program_helper.func_double_click_player_info(item_text[1])
            elif clicked.get() == "Total Info":
                my_data = main_program_helper.func_double_click_compare_teams(item_text[2], item_text[5])
                my_data = "mot ready yet"
            elif clicked.get() == "Total Info details":
                my_data = main_program_helper.func_double_click_compare_teams(item_text[2], item_text[5])
            else:
                my_data = "No data for the current selection"

            tree.func_tree_on_double_click(my_data,clicked.get(),item_text[1])






    root_my_main_program = Tk()
    root_my_main_program.title("Bet stats!!!")
    root_my_main_program.geometry("1000x1000")

    start_view = "team_player_with_names"
    my_view_list = my_view_list_select(start_view)

    options = [
        "Players with teams",
        "Total Info",
        "Total Info details"
    ]


    clicked = StringVar(root_my_main_program)
    clicked.set(options[0])
    drop = OptionMenu(root_my_main_program, clicked, *options)
    drop.pack()
    clicked.trace('w',choose)

    #my_tree[0] is my_tree and my_tree[1] is my scrol bar
    my_tree = tree.func_my_tree_view(start_view, my_view_list, root_my_main_program)

    my_tree[0].bind("<Double-1>", on_double_click)


    root_my_main_program.mainloop()





