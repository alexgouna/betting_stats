from tkinter import *
import sys
import Create_my_database_esoccer
import Esoccer_get_data
import Esoccer_views
import global_variables

root = Tk()
root.title("Main!!!")
root.geometry("300x300")

def database_update():
    try:
        global_variables.my_total_pages = int(pages_entry1.get())
    except:
        global_variables.my_total_pages=1
    try:
        global_variables.my_first_page = int(pages_entry2.get())
    except:
        global_variables.my_first_page=1

    # #Creat_my_database.create_my_tables() runs only on debug mode
    if drop =="First Use":
        Create_my_database_esoccer.create_my_tables()

    # esoccer get data
    Esoccer_get_data.esoccer_move_data()

    # esoccer create views sql strings
    Esoccer_views.create_my_views()


options = [
    "Continue",
    "First Use"
]
clicked = StringVar()
clicked.set(options[0])
drop = OptionMenu(root, clicked, *options)

my_label1 = Label(root, text="press the 'Submit' to update the database")
my_label2 = Label(root, text="Pages to search(recomend 20):")
pages_entry1=Entry(root)
my_label3 = Label(root, text="Pages to Start (recomend 1):")
pages_entry2=Entry(root)
my_label4 = Label(root, text="no use for the momment:")
pages_entry3=Entry(root)
button_submit = Button(root,text='Submit',command=database_update)

my_label1.grid(row=0,column=0,columnspan=2)

my_label2.grid(row=2,column=0)
pages_entry1.grid(row=2,column=1)

my_label3.grid(row=1,column=0)
pages_entry2.grid(row=1,column=1)

my_label4.grid(row=3,column=0)
pages_entry3.grid(row=3,column=1)

button_submit.grid(row=4,column=0,columnspan=2)

drop.grid(row=5,column=0,columnspan=2)

print("----------------THE END-----------------")


root.mainloop()

