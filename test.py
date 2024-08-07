from tkinter import *
from tkinter import ttk
import config
import my_table_connection


class ResizableFramesApp:

    def __init__(self, root):

        self.root = root
        self.root.title("Resizable Frames")

        # my frames
        self.my_frame_top = Frame(root)
        self.my_frame_mid = Frame(root, bg='blue')
        self.my_frame_bot = Frame(root, bg='green')

        self.my_frame_top.pack(fill='both', expand=True)
        self.my_frame_mid.pack(fill='both', expand=True)
        self.my_frame_bot.pack(fill='both', expand=True)

        self.root.bind("<Configure>", self.on_resize)

        # ------------------SEARCH------------------
        Label(self.my_frame_top, text="Search : ", font='BOLD').grid(row=0, column=0, padx=5, pady=5, rowspan=6)
        self.my_search = Entry(self.my_frame_top, width=30)
        self.my_search.grid(row=0, column=1, padx=5, pady=5, rowspan=6)
        self.my_search.bind("<KeyRelease>", self.search_data)
        # checkpoints
        self.my_check_points()

        self.my_data = my_table_connection.get_all_data_from_table_team_games()

        # create and populate my tree
        my_headers = ('Date', 'Player home', 'Team home', 'Home', 'Away', 'Player away', 'Team away')
        self.tree = ttk.Treeview(self.my_frame_mid)
        self.tree['columns'] = (my_headers)
        for index, col in enumerate(my_headers):
            if index == 0:
                my_width = 100
            elif index == 3 or index == 4:
                my_width = 30
            else:
                my_width = 150
            self.tree.column(col, anchor=W, width=my_width)
            self.tree.heading(col, text=col, anchor=W)
        self.tree.bind('<Button-1>', self.on_header_click_order_by)
        self.tree.column('#0', width=0, stretch=NO)
        self.tree_populate()
        self.tree.pack(side=LEFT, fill='both', expand=True)

        self.scrollbar = Scrollbar(self.my_frame_mid, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=self.scrollbar.set)
        self.scrollbar.pack(side=LEFT, fill=Y)

    def my_check_points(self):
        self.var_all = BooleanVar(value=False)
        self.var_date = BooleanVar(value=False)
        self.var_homeplayername = BooleanVar(value=False)
        self.var_hometeamname = BooleanVar(value=False)
        self.var_homegoal = BooleanVar(value=False)
        self.var_awaygoal = BooleanVar(value=False)
        self.var_awayplayername = BooleanVar(value=False)
        self.var_awayteamname = BooleanVar(value=False)

        self.my_ckeck_all = Checkbutton(self.my_frame_top, text='All', variable=self.var_all, anchor="w",
                                        command=self.command_all)
        self.my_ckeck_date = Checkbutton(self.my_frame_top, text='Date', variable=self.var_date, anchor="w",
                                         command=self.command_one)
        self.my_ckeck_homeplayername = Checkbutton(self.my_frame_top, text='Home player name',
                                                   variable=self.var_homeplayername, anchor="w",
                                                   command=self.command_one)
        self.my_ckeck_hometeamname = Checkbutton(self.my_frame_top, text='Home team', variable=self.var_hometeamname,
                                                 anchor="w", command=self.command_one)
        self.my_ckeck_homegoal = Checkbutton(self.my_frame_top, text='Home', variable=self.var_homegoal, anchor="w",
                                             command=self.command_one)
        self.my_ckeck_awaygoal = Checkbutton(self.my_frame_top, text='Away', variable=self.var_awaygoal, anchor="w",
                                             command=self.command_one)
        self.my_ckeck_awayplayername = Checkbutton(self.my_frame_top, text='Away player name',
                                                   variable=self.var_awayplayername, anchor="w",
                                                   command=self.command_one)
        self.my_ckeck_awayteamname = Checkbutton(self.my_frame_top, text='Away team', variable=self.var_awayteamname,
                                                 anchor="w", command=self.command_one)

        self.my_ckeck_all.grid(row=0, column=2, padx=5, pady=5, rowspan=3, sticky=W + E)
        self.my_ckeck_date.grid(row=3, column=2, padx=5, pady=5, rowspan=3, sticky=W + E)
        self.my_ckeck_homeplayername.grid(row=0, column=3, padx=5, pady=5, rowspan=2, sticky=W + E)
        self.my_ckeck_hometeamname.grid(row=2, column=3, padx=5, pady=5, rowspan=2, sticky=W + E)
        self.my_ckeck_homegoal.grid(row=4, column=3, padx=5, pady=5, rowspan=2, sticky=W + E)
        self.my_ckeck_awaygoal.grid(row=4, column=4, padx=5, pady=5, rowspan=2, sticky=W + E)
        self.my_ckeck_awayplayername.grid(row=0, column=4, padx=5, pady=5, rowspan=2, sticky=W + E)
        self.my_ckeck_awayteamname.grid(row=2, column=4, padx=5, pady=5, rowspan=2, sticky=W + E)

        self.my_asc_desc = [0, 0, 0, 0, 0, 0, 0]

    def on_header_click_order_by(self, event):
        # Identify which column header was clicked
        my_column = self.tree.identify_column(event.x)
        region = self.tree.identify('region', event.x, event.y)

        def asc_desc(my_pos):
            print(self.my_asc_desc)
            if self.my_asc_desc[my_pos] == 0:
                self.my_asc_desc[my_pos] = 1
                return 'ASC'
            else:
                self.my_asc_desc[my_pos] = 0
                return 'DESC'

        if region == 'heading':
            if self.tree.heading(my_column)['text'] == 'Date':
                my_order_by = f"game_date {asc_desc(0)}"
            elif self.tree.heading(my_column)['text'] == 'Player home':
                my_order_by = f"game_homeplayername {asc_desc(1)}"
            elif self.tree.heading(my_column)['text'] == 'Team home':
                my_order_by = f"game_hometeamname {asc_desc(2)}"
            elif self.tree.heading(my_column)['text'] == 'Home':
                my_order_by = f"game_homegoal {asc_desc(3)}"
            elif self.tree.heading(my_column)['text'] == 'Away':
                my_order_by = f"game_awaygoal {asc_desc(4)}"
            elif self.tree.heading(my_column)['text'] == 'Player away':
                my_order_by = f"game_awayplayername {asc_desc(5)}"
            else:
                my_order_by = f"game_awayteamname {asc_desc(6)}"

            self.search_data(event, my_order_by)

    def tree_populate(self):
        for row in self.my_data:
            self.tree.insert('', 'end', values=row[1:])

    def command_all(self):
        if self.var_all.get():
            self.var_date.set(False)
            self.var_homeplayername.set(False)
            self.var_hometeamname.set(False)
            self.var_homegoal.set(False)
            self.var_awaygoal.set(False)
            self.var_awayplayername.set(False)
            self.var_awayteamname.set(False)

    def command_one(self):
        if self.var_date.get() and self.var_homeplayername.get() and self.var_hometeamname.get() and self.var_homegoal.get() and \
                self.var_awaygoal.get() and self.var_awayplayername.get() and self.var_awayteamname.get():
            self.var_all.set(True)
            self.var_date.set(False)
            self.var_homeplayername.set(False)
            self.var_hometeamname.set(False)
            self.var_homegoal.set(False)
            self.var_awaygoal.set(False)
            self.var_awayplayername.set(False)
            self.var_awayteamname.set(False)
        else:
            self.var_all.set(False)

    def search_areas(self):
        my_data = ""

        def my_text(my_data, search_field):
            if len(my_data) == 0:
                return f" {search_field} LIKE '%{self.my_search.get()}%' "
            else:
                return my_data + f" OR {search_field} LIKE '%{self.my_search.get()}%' "

        if self.var_date.get():
            my_data = " game_date LIKE '%{my_search_data}%' "
        if self.var_homeplayername.get():
            my_data = my_text(my_data, "game_homeplayername")
        if self.var_hometeamname.get():
            my_data = my_text(my_data, "game_hometeamname")
        if self.var_homegoal.get():
            my_data = my_text(my_data, "game_homegoal")
        if self.var_awaygoal.get():
            my_data = my_text(my_data, "game_awaygoal")
        if self.var_awayplayername.get():
            my_data = my_text(my_data, "game_awayplayername")
        if self.var_awayteamname.get():
            my_data = my_text(my_data, "game_awayteamname")
        return my_data

    def search_data(self, event, my_order_by=None):
        self.my_data = my_table_connection.get_all_data_from_table_team_games(self.my_search.get(), self.search_areas(),
                                                                              my_order_by)
        for row in self.tree.get_children():
            self.tree.delete(row)
        self.tree_populate()
        self.tree.pack(side=LEFT, fill='both', expand=True)

    def on_resize(self, event):
        # Get the new height of the window
        new_height = self.root.winfo_height()

        # Calculate the new height for each frame based on the ratio 2:6:2
        frame_height_top = new_height * 2 / 10
        frame_height_bot = new_height * 2 / 10
        if frame_height_top > 100:
            frame_height_top = 100
        elif frame_height_top < 50:
            frame_height_top = 50
        if frame_height_bot > 100:
            frame_height_bot = 100
        elif frame_height_bot < 50:
            frame_height_bot = 50
        frame_height_mid = new_height - frame_height_top - frame_height_bot

        # Set the new dimensions for each frame
        self.my_frame_top.config(height=frame_height_top)
        self.my_frame_mid.config(height=frame_height_mid)
        self.my_frame_bot.config(height=frame_height_bot)

        # Update the geometry to force the resize
        self.my_frame_top.pack_propagate(False)
        self.my_frame_mid.pack_propagate(False)
        self.my_frame_bot.pack_propagate(False)

def main():
    root = Tk()
    root.geometry("800x600")  # Initial window size
    app = ResizableFramesApp(root)
    root.mainloop()


main()
