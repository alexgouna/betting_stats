from tkinter import *
import my_tree
from tkinter import ttk

style = ttk.Style()

def check_score(score):

    team_goal = int(score[:score.find("-")-1])
    opponent_goal = int(score[score.find("-")+2:])
    if team_goal>opponent_goal:
        return "win"
    elif team_goal<opponent_goal:
        return "lose"
    else:
        return "draw"

def color_cells(my_tree,my_extra_value):

    for child in my_tree.get_children():
        home = my_tree.item(child, 'values')[1]
        away = my_tree.item(child, 'values')[3]
        score = my_tree.item(child, 'values')[2]
        if home.find(my_extra_value)>0 or away.find(my_extra_value)>0:
            if check_score(score)=="win":
                my_tree.tag_configure('win', background='green')
                my_tree.item(child, tags='win')
            elif check_score(score)=="lose":
                my_tree.tag_configure('lose', background='red')
                my_tree.item(child, tags='lose')
            elif check_score(score)=="draw":
                my_tree.tag_configure('draw', background='yellow')
                my_tree.item(child, tags='draw')

#open a new window with the data included
def tree_on_double_click_start(my_data,selection,my_extra_value):
    root_tree_on_double_click = Tk()
    root_tree_on_double_click.title("root_tree_on_double_click!!!")
    root_tree_on_double_click.geometry("1000x1000")



    if selection == "Players with teams":
        my_view_list=("Date","Home","Score","Away")
    elif selection == "Total Info":
        my_view_list=("sdf","sdf")
    elif selection == "Total Info details":
        my_view_list=("Team","Total Games","Home Games","Home Goals","Home Wins","Home Draw","Home Loses","Away Games","Away Goals","Away Wins","Away Draw","Away Loses" )
    else:
        my_view_list = ("Emptyyyy!!!")

    treeview= my_tree.my_tree_view.my_tree_view_start(None, my_view_list, root_tree_on_double_click,my_data)

    if selection == "Players with teams":
        color_cells(treeview[0],my_extra_value)

    label = Label(root_tree_on_double_click,text="asdfasdf").pack()

    root_tree_on_double_click.mainloop()
    return my_data




