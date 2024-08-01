from tkinter import *
from tkinter import ttk

import my_table_connection


class ResizableFramesApp:

    def __init__(self, root):


        self.root = root
        self.root.title("Resizable Frames")


        # my frames
        self.my_frame_top = Frame(root, bg='red')
        self.my_frame_mid = Frame(root, bg='blue')
        self.my_frame_bot = Frame(root, bg='green')

        self.my_frame_top.pack(fill='both', expand=True)
        self.my_frame_mid.pack(fill='both', expand=True)
        self.my_frame_bot.pack(fill='both', expand=True)

        self.root.bind("<Configure>", self.on_resize)

        self.my_data = my_table_connection.get_all_data_from_table_team_games()

        # create and populate my tree
        column_list = ('Date', 'Player home', 'Team home', 'Home', 'Away', 'Player away', 'Team away')
        self.tree = ttk.Treeview(self.my_frame_mid)
        self.tree['columns'] = (column_list)
        for index,col in enumerate(column_list):
            if index==0:
                my_width = 40
            elif index == 3 or index == 4:
                my_width=30
            else:
                my_width = 150
            self.tree.column(col, anchor=W, width=my_width)
            self.tree.heading(col, text=col, anchor=W)
        self.tree.column('#0', width=0, stretch=NO)
        self.tree_populate()
        self.tree.pack(side=LEFT, fill='both', expand=True)

        self.scrollbar = Scrollbar(self.my_frame_mid, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=self.scrollbar.set)
        self.scrollbar.pack(side=LEFT, fill=Y)
    def tree_populate(self):
        for row in self.my_data:
            self.tree.insert('', 'end', values=row[1:])
            # print(row)

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
        frame_height_mid= new_height - frame_height_top - frame_height_bot

        # Set the new dimensions for each frame
        self.my_frame_top.config(height=frame_height_top)
        self.my_frame_mid.config(height=frame_height_mid)
        self.my_frame_bot.config(height=frame_height_bot)

        # Update the geometry to force the resize
        self.my_frame_top.pack_propagate(False)
        self.my_frame_mid.pack_propagate(False)
        self.my_frame_bot.pack_propagate(False)












if __name__ == "__main__":
    root = Tk()
    root.geometry("800x600")  # Initial window size
    app = ResizableFramesApp(root)
    root.mainloop()
