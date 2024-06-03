import tkinter.ttk
from tkinter import *
import sqlite3




def get_my_tree_data(my_view):
    conn = sqlite3.connect("my_database_esoccer.db")
    c = conn.cursor()
    c.execute("SELECT * FROM {0}".format(my_view))
    my_data = c.fetchall()
    conn.commit()
    conn.close()
    return my_data


def my_tree_view(my_view,root):
    my_tree = tkinter.ttk.Treeview(root)

    if my_view=="total_info_detailed":
        my_view_list = ('Date', 'Hour', 'Home', 'Goal Home', 'Goal Away', 'Away', 'Corner Home',
                        'Corner Away', 'Shots Home',' Shots Away')
    elif my_view=="total_info":
        my_view_list = ('Date', 'Home', 'Score', 'Away', 'Corner', 'Shots')
    else:
        my_view_list = ('ID', 'Player', 'Team', 'Full Name')


    my_tree['columns'] = my_view_list

    my_tree.column("#0", width=0, minwidth=0)
    for item in my_view_list:
        my_tree.column(item, anchor=W, width=100)

    my_tree.heading("#0", text="Label")
    for item in my_view_list:
        my_tree.heading(item, text=item)


    my_tree_data = get_my_tree_data(my_view)
    counter = 0
    for data in my_tree_data:
        my_tree.insert(parent='', index='end', iid=str(counter), text='', values=data)
        counter = counter + 1
    return my_tree
    # my_tree.grid(row=1, column=0, columnspan=3, pady=5, padx=15)


def start():
    global my_tree
    global vsb
    root = Tk()
    root.title("Bet stats!!!")
    root.geometry("1000x1000")

    options = [
        "Players with teams",
        "Total Info",
        "Total Info details"
    ]

    def choose(*args):
        global my_tree
        global vsb
        vsb.destroy()
        my_tree.destroy()
        if clicked.get() == "Players with teams":
            my_tree=my_tree_view("team_player_with_names",root)
        elif clicked.get() == "Total Info":
            my_tree=my_tree_view("total_info",root)
        elif clicked.get() == "Total Info details":
            my_tree=my_tree_view("total_info_detailed",root)

        vsb = Scrollbar(root, orient="vertical", command=my_tree.yview)
        my_tree.configure(yscrollcommand=vsb.set)
        my_tree.pack(side=LEFT, fill=BOTH, expand=True)
        vsb.pack(side=RIGHT, fill=Y)

    clicked = StringVar(root)
    clicked.set(options[0])
    drop = OptionMenu(root, clicked, *options)

    drop.pack()
    clicked.trace('w',choose)

    my_tree = my_tree_view("total_info_detailed", root)

    # Create a vertical scrollbar
    vsb = Scrollbar(root, orient="vertical", command=my_tree.yview)
    my_tree.configure(yscrollcommand=vsb.set)

    # Pack the Treeview and scrollbar into the frame
    my_tree.pack(side=LEFT, fill=BOTH, expand=True)
    vsb.pack(side=RIGHT, fill=Y)

    root.mainloop()


start()