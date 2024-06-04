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
    def sort_treeview(col):
        pass
        # global my_tree
        # # Determine if sorting in ascending or descending order
        # data = [(my_tree.set(child, col), child) for child in my_tree.get_children("")]
        # data.sort(reverse=col == my_tree.heading(col, "text")[-1] == "▲")
        # for i, (val, child) in enumerate(data):
        #     print(child)
        #     print(i)
        #     my_tree.move(child, "", i)
        # my_tree.heading(col, text=col + (" ▲" if col == my_tree.heading(col, "text")[-1] != "▲" else " ▼"))

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
        my_tree.heading(item, text=item, command=lambda: sort_treeview(item))


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
    root_main = Tk()
    root_main.title("Bet stats!!!")
    root_main.geometry("1000x1000")

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
            my_tree = my_tree_view("team_player_with_names", root_main)
        elif clicked.get() == "Total Info":
            my_tree = my_tree_view("total_info", root_main)
        elif clicked.get() == "Total Info details":
            my_tree = my_tree_view("total_info_detailed", root_main)

        vsb = Scrollbar(root_main, orient="vertical", command=my_tree.yview)
        my_tree.configure(yscrollcommand=vsb.set)
        my_tree.pack(side=LEFT, fill=BOTH, expand=True)
        vsb.pack(side=RIGHT, fill=Y)

    def on_double_click(event):
        pass
        # Get the item that was double-clicked
        item_id = my_tree.identify_row(event.y)
        if item_id:
            item = my_tree.item(item_id)
            item_text = item['values']
            my_data = my_main_program_compare_teams.compare(item_text[2], item_text[5])
            print(my_data)
            show(my_data)

    clicked = StringVar(root_main)
    clicked.set(options[0])
    drop = OptionMenu(root_main, clicked, *options)

    drop.pack()
    clicked.trace('w', choose)

    my_tree = my_tree_view("total_info_detailed", root_main)

    # Create a vertical scrollbar
    vsb = Scrollbar(root_main, orient="vertical", command=my_tree.yview)
    my_tree.configure(yscrollcommand=vsb.set)

    # Pack the Treeview and scrollbar into the frame
    my_tree.pack(side=LEFT, fill=BOTH, expand=True)
    vsb.pack(side=RIGHT, fill=Y)

    my_tree.bind("<Double-1>", on_double_click)

    root_main.mainloop()

