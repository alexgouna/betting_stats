import multiprocessing
import time
from tkinter import *
import Create_my_database_esoccer
import Esoccer_get_data
import Esoccer_views
import global_variables
import multiprocessing

def tesst():
    print("sssss")
    time.sleep(1)
    print("end of sleep 1...")

def tesst2():
    print("sssssssssss")
    time.sleep(1)
    print("end of ssssssleep 1...")

def database_update(drop):
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

def start_the_program():
    root1 = Tk()
    root1.title("Maasdfasdfin!!!")
    root1.geometry("400x270")

    my_label = Label(root1,text="asdfsadf")
    my_label.pack()
    root1.mainloop()

if __name__ == '__main__':
    def submit_button():

        # p1 = multiprocessing.Process(target=tesst)
        # p2 = multiprocessing.Process(target=tesst2)

        p1 = multiprocessing.Process(target=start_the_program)
        p2 = multiprocessing.Process(target=database_update(drop))
        p2 = multiprocessing.Process(target=start_the_program)

        p1.start()
        p2.start()

        p1.join()
        p2.join()



    root = Tk()
    root.title("Main!!!")
    root.geometry("400x270")

    options = [
        "Continue",
        "First Use"
    ]

    clicked = StringVar()
    clicked.set(options[0])
    drop = OptionMenu(root, clicked, *options)

    my_label_title = Label(root, text="Press the 'Submit' to update the database", font=(20))
    my_label_start_page = Label(root, text="Pages to Start search (recomend 1):")
    my_entry_start_page = Entry(root)
    my_label_end_page = Label(root, text="Pages to End Search (recomend 20):")
    my_entry_end_page = Entry(root)
    my_label4 = Label(root, text="no use for the moment:")
    pages_entry3 = Entry(root)
    button_submit = Button(root, text='Submit', command=submit_button, font=(25))
    my_label_select_if_first_use = Label(root, text="Select if is First Use")

    my_label_title.grid(row=0, column=0, columnspan=3, pady=10, padx=15)

    my_label_start_page.grid(row=1, column=0, pady=5, padx=15)
    my_entry_start_page.grid(row=1, column=1, pady=5, padx=15)

    my_label_end_page.grid(row=2, column=0, pady=5, padx=15)
    my_entry_end_page.grid(row=2, column=1, pady=5, padx=15)

    my_label4.grid(row=3, column=0, pady=5, padx=15)
    pages_entry3.grid(row=3, column=1, pady=5, padx=15)

    my_label_select_if_first_use.grid(row=4, column=0, pady=5, padx=15)
    drop.grid(row=4, column=1, pady=5, padx=15)

    button_submit.grid(row=5, column=0, columnspan=2, pady=5, padx=15)

    print("----------------THE END-----------------")

    root.mainloop()