import tkinter as tk

HEIGHT = 500
WIDTH = 600

class AvailableRooms :

    def __init__(self, database):
        self._database = database
        self._root = tk.Tk()
        self._root.title("Available Rooms")
        self._root.minsize(WIDTH,HEIGHT)

        welcomeLabel = tk.Label(self._root, text = "Available Rooms", font= "Times 20")
        welcomeLabel.pack()
        tk.Label(self._root, text = "_"*45).pack()

    def run(self):
        self._root.mainloop()

if __name__ == "__main__":
    pass