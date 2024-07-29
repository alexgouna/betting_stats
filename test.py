
def last_page(my_link):
    def start_all_pages():
        global_variables.get_last_page(my_link) + 1

    def start_custom_pages():
        try:
            if (int(main_entry.get())) > 1:
                return int(main_entry.get()) + 1
        except:
            messagebox.Message("The value should be number")

    root = Tk()
    root.title("Last page")
    root.geometry("350x150")

    main_frame = Frame(root)
    button_frame = Frame(root)

    main_frame.pack(fill='both', side='top', expand=True)
    button_frame.pack(fill='both', side='top', expand=True)

    main_label_1 = Label(main_frame,
                         text="* Press 'ALL' to start redering all data  or\n* Press Custom to render the selected pages",
                         justify="left", font=('15'))
    main_label_2 = Label(main_frame, text="Pages:", justify="left", font=('15'))
    main_entry = Entry(main_frame)

    main_label_1.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    main_label_2.grid(row=1, column=0, padx=10, pady=10)
    main_entry.grid(row=1, column=1, sticky=W, padx=5)

    button_all = Button(button_frame, text="ALL", command=start_all_pages, width=10)
    button_custom = Button(button_frame, text="Custom", command=start_custom_pages, width=10)

    button_all.pack(side=LEFT, padx=50)
    button_custom.pack(side=RIGHT, padx=50)

    mainloop()


    return global_variables.get_last_page(my_link) + 1
