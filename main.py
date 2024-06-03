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
    global_variables.my_total_pages = int(pages_entry.get())

    # #Creat_my_database.create_my_tables() runs only on debug mode
    if sys.gettrace() is not None:
        Create_my_database_esoccer.create_my_tables()

    # esoccer get data
    Esoccer_get_data.esoccer_move_data()

    # esoccer create views sql strings
    Esoccer_views.create_my_views()


my_label1 = Label(root, text="press the 'Submit' to update the database")
my_label2 = Label(root, text="Pages to search(recomend 20):")
pages_entry=Entry(root)
button_submit = Button(root,text='Submit',command=database_update)

my_label1.grid(row=0,column=0,columnspan=2)
my_label2.grid(row=1,column=0)
pages_entry.grid(row=1,column=1)
button_submit.grid(row=2,column=0,columnspan=2)

print("----------------THE END-----------------")


root.mainloop()

