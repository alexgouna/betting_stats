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


def get_my_vertical_scrolbar(my_tree,my_root):

    # Create a vertical scrollbar
    vsb = Scrollbar(my_root, orient="vertical", command=my_tree.yview)
    my_tree.configure(yscrollcommand=vsb.set)
    # Pack the Treeview and scrollbar into the frame
    my_tree.pack(side=LEFT, fill=BOTH, expand=True)
    vsb.pack(side=RIGHT, fill=Y)
    return vsb




# create my tree
def my_tree_view_start(my_view=None,my_view_list=None,my_root=None,my_data=None):

    my_tree = tkinter.ttk.Treeview(my_root)
    my_tree['columns'] = my_view_list

    my_tree.column("#0", width=0, minwidth=0)
    for item in my_view_list:
        my_tree.column(item, anchor=W, width=100)

    my_tree.heading("#0", text="Label")
    for item in my_view_list:
        my_tree.heading(item,text=item)

    if my_data is None:
        my_tree_data = get_my_tree_data(my_view)
    else:
        my_tree_data = my_data
        print(my_data)

    counter = 0
    for data in my_tree_data:
        my_tree.insert(parent='', index='end', iid=str(counter), text='', values=data)
        counter = counter + 1

    vsb = get_my_vertical_scrolbar(my_tree,my_root)


    return my_tree,vsb

