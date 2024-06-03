import tkinter as tk
from tkinter import ttk

class TreeViewApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Treeview Double-Click Example")

        # Sample data
        self.data = [
            ("Banana", 1),
            ("Apple", 3),
            ("Cherry", 2),
            ("Date", 5),
            ("Fig", 4),
            ("Grape", 6)
        ]

        # Treeview setup
        self.tree = ttk.Treeview(root, columns=("Item", "Value"), show="headings")
        self.tree.heading("Item", text="Item")
        self.tree.heading("Value", text="Value")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Insert data into the Treeview
        self.load_data(self.data)

        # Bind the double-click event
        # self.tree.bind("<Double-1>", self.on_double_click)

        # Label to display selected item details
        self.label = ttk.Label(root, text="Double-clicked Item: None")
        self.label.pack(pady=10)

    def load_data(self, data):
        # Clear the treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
        # Insert new data
        for item in data:
            self.tree.insert("", tk.END, values=item)

    def on_double_click(self, event):
        pass
        # Get the item that was double-clicked
        item_id = self.tree.identify_row(event.y)
        if item_id:
            item = self.tree.item(item_id)
            item_text = item['values']
            self.label.config(text=f"Double-clicked Item: {item_text}")
            # Perform the desired operation here
            self.start_operation(item_text)

    def start_operation(self, item_text):
        # Replace this with the desired operation
        print(f"Starting operation on: {item_text}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TreeViewApp(root)
    root.mainloop()
