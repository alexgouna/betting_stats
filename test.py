import tkinter as tk
class PageUpdateApp:
    def __init__(self, root):
        self.root = root
        self.root.
        self.root.title("Rather do...")

        self.label = tk.Label(root, text="You are going to update the database!!")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=10)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.cancel_button = tk.Button(self.button_frame, text="Cancel", command=self.cancel)
        self.cancel_button.pack(side=tk.LEFT, padx=5)

        self.submit_button = tk.Button(self.button_frame, text="Submit", command=self.submit)
        self.submit_button.pack(side=tk.LEFT, padx=5)

        self.result = None

    def cancel(self):
        self.result = False
        self.root.quit()

    def submit(self):
        entry_value = self.entry.get()
        if entry_value.strip() == "":
            self.result = True
        else:
            self.result = int(entry_value)
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = PageUpdateApp(root)
    root.mainloop()

    print(app.result)
