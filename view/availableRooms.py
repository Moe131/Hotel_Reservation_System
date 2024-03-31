import tkinter as tk
from tkcalendar import DateEntry


HEIGHT = 350
WIDTH = 400

class AvailableRooms :

    def __init__(self, database):
        self._database = database
        self._root = tk.Tk()
        self._root.title("Available Rooms")
        self._root.minsize(WIDTH,HEIGHT)

        self.createHeader()
        self.createDateInput()

    def run(self):
        self._root.mainloop()

    def createHeader(self):
        headerLabel = tk.Label(self._root, text = "Available Rooms", font= "Times 20")
        headerLabel.grid(row = 0, column = 0, columnspan = 2)
        headerLabel = tk.Label(self._root, text = "_"*50)
        headerLabel.grid(row = 1, column = 0, columnspan = 2)

    def createDateInput(self):
        reservationEmailLabel = tk.Label(self._root, text = "Enter the timeframe to check the available rooms: ")
        checkInDateLabel = tk.Label(self._root, text = "Check In Date: ")
        self._checkInDate = DateEntry(self._root, background= "magenta3", foreground= "black",bd=2)
        checkOutDateLabel = tk.Label(self._root, text = "Check Out Date: ")
        self._checkOutDate = DateEntry(self._root, background= "magenta3", foreground= "black",bd=2)
        button = tk.Button(self._root, text = "Check", command = self.onCheck)


        reservationEmailLabel.grid(row=3, column = 0, columnspan = 2)
        checkInDateLabel.grid(row=4, column = 0)
        self._checkInDate.grid(row=4, column = 1)
        checkOutDateLabel.grid(row=5, column = 0)
        self._checkOutDate.grid(row=5, column = 1)
        button.grid(row=6, column = 0, columnspan = 2)

    def onCheck(self):
        pass

if __name__ == "__main__":
    pass