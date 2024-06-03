from tkinter import *
import sys
import Create_my_database_esoccer
import Esoccer_get_data
import Esoccer_views
import global_variables

root = Tk()
root.title("Main!!!")
root.geometry("400x270")

def database_update():
    try:
        global_variables.my_total_pages = int(my_entry_end_page.get())
    except:
        global_variables.my_total_pages=1
    try:
        global_variables.my_first_page = int(my_entry_start_page.get())
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

my_label_title = Label(root, text="Press the 'Submit' to update the database",font=(20))
my_label_start_page = Label(root, text="Pages to End search (recomend 20):")
my_entry_start_page=Entry(root)
my_label_end_page = Label(root, text="Pages to Start Search (recomend 1):")
my_entry_end_page=Entry(root)
my_label4 = Label(root, text="no use for the moment:")
pages_entry3=Entry(root)
button_submit = Button(root,text='Submit',command=database_update,font=(25))
my_label_select_if_first_use = Label(root, text="Select if is First Use")


my_label_title.grid(row=0,column=0,columnspan=3,pady=10,padx = 15)

my_label_start_page.grid(row=2,column=0,pady=5,padx = 15)
my_entry_start_page.grid(row=2,column=1,pady=5,padx = 15)

my_label_end_page.grid(row=1,column=0,pady=5,padx = 15)
my_entry_end_page.grid(row=1,column=1,pady=5,padx = 15)

my_label4.grid(row=3,column=0,pady=5,padx = 15)
pages_entry3.grid(row=3,column=1,pady=5,padx = 15)

my_label_select_if_first_use.grid(row=4,column=0,pady=5,padx = 15)
drop.grid(row=4,column=1,pady=5,padx = 15)

button_submit.grid(row=5,column=0,columnspan=2,pady=5,padx = 15)

print("----------------THE END-----------------")


root.mainloop()

