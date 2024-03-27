import tkinter as tk
from view.checkInFrame import CheckInFrame
from view.checkOutFrame import CheckOutFrame
from view.availableRoomsFrame import AvailableRoomsFrame
from view.getInfoFrame import GetInfoFrame




HEIGHT = 250
WIDTH = 400

class HomeFrame :

    def __init__(self):
        self._root = tk.Tk()
        self._root.title("Main")
        self._root.minsize(WIDTH,HEIGHT)

        welcomeLabel = tk.Label(self._root, text = "Welcome to Hotel Reservation System", font= "Times 20")
        checkInButton = tk.Button(self._root, text = "Check In", command = self.checkInClick, width = 30)
        checkOutButton  = tk.Button(self._root, text = "Check Out", command = self.checkOutClick, width = 30)
        availableRoomsButton  = tk.Button(self._root, text = "Check Available Rooms", command = self.availableRoomsClick, width = 30)
        getInfoButton = tk.Button(self._root, text = "Get Guest Information", command = self.getInfoClick, width = 30)
        exitButton  = tk.Button(self._root, text = "Exit", command = self.exitClick, width = 30)

        welcomeLabel.pack()
        tk.Label(self._root, text = "_"*45).pack()
        checkInButton.pack()
        checkOutButton.pack()
        availableRoomsButton.pack()
        getInfoButton.pack()
        exitButton.pack()

    def run(self):
        self._root.mainloop()

    def checkInClick(self):
        CheckInFrame().run()

    def  checkOutClick(self):
        CheckOutFrame().run()

    def availableRoomsClick(self):
        AvailableRoomsFrame().run()

    def getInfoClick(self):
        GetInfoFrame().run()

    def exitClick(self):
        self._root.destroy()


if __name__ == "__main__":
    pass