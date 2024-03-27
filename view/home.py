import tkinter as tk
from view.Reservation import Reservation
from view.availableRooms import AvailableRooms
from view.manageReservation import ManageReservation

HEIGHT = 250
WIDTH = 400

class Home :

    def __init__(self):
        self._root = tk.Tk()
        self._root.title("Main")
        self._root.minsize(WIDTH,HEIGHT)

        welcomeLabel = tk.Label(self._root, text = "Welcome to Hotel Reservation System", font= "Times 20")
        checkInButton = tk.Button(self._root, text = "Reserve", command = self.ReserveClick, width = 30)
        availableRoomsButton  = tk.Button(self._root, text = "Check Available Rooms", command = self.availableRoomsClick, width = 30)
        getInfoButton = tk.Button(self._root, text = "Manage Reservation", command = self.manageReservationClick, width = 30)
        exitButton  = tk.Button(self._root, text = "Exit", command = self.exitClick, width = 30)

        welcomeLabel.pack()
        tk.Label(self._root, text = "_"*45).pack()
        checkInButton.pack()
        availableRoomsButton.pack()
        getInfoButton.pack()
        exitButton.pack()

    def run(self):
        self._root.mainloop()

    def ReserveClick(self):
        Reservation().run()

    def availableRoomsClick(self):
        AvailableRooms().run()

    def manageReservationClick(self):
        ManageReservation().run()

    def exitClick(self):
        self._root.destroy()


if __name__ == "__main__":
    pass