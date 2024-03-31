import tkinter as tk
from tkcalendar import DateEntry


HEIGHT = 360
WIDTH = 400

class AvailableRooms :

    def __init__(self, database):
        self._database = database
        self._root = tk.Tk()
        self._root.title("Available Rooms")
        self._root.minsize(WIDTH,HEIGHT)

        self.createHeader()
        self.createDateInput()
        self.createRoomList()

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

    def createRoomList(self):
        self._listbox = tk.Listbox(self._root , width = 30  )
        self._listbox.grid(row=8, column = 0, columnspan = 2)


    def onCheck(self):
        self._message = tk.Label(self._root, text = " Here are the available rooms in selected dates:")
        self._message.grid(row=7, column = 0, columnspan = 2)
        i=0;
        for room in self._database.searchRooms(self._checkInDate.get_date(),self._checkOutDate.get_date()):
            self._listbox.insert(i, "Room " + str(room[0]) + " - " + str(room[1]) )
            i+=1

if __name__ == "__main__":
    pass