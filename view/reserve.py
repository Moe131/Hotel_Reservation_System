import tkinter as tk
from tkcalendar import DateEntry
from engine.database import Database
from engine.room import Room
from engine.reservation import Reservation

HEIGHT = 360
WIDTH = 400

class Reserve :

    def __init__(self, database):
        self._database = database
        self._root = tk.Tk()
        self._root.title("Check In")
        self._root.minsize(WIDTH,HEIGHT)

        headerLabel = tk.Label(self._root, text = "Reserve a room", font= "Times 20")
        headerLabel.grid(row= 0, column = 0, columnspan = 2)

        self.createInformationEntry()
        self.createRadioButton()
        self.createDateInput()
        self.createSubmitButton()
        self.createMessageLabel()

    def run(self):
        self._root.mainloop()

    def createMessageLabel(self):
        self._messageLabel = tk.Label(self._root, text = "")
        self._messageLabel.grid(row = 12, column = 0, columnspan = 2)

    def createSubmitButton(self): ### work on this
        button = tk.Button(self._root, text = "Submit", command = self.submitClick)
        button.grid(row = 11, column = 0, columnspan = 2)

    def submitClick(self):
        first = self._firstNameEntry.get()
        last = self._lastNameEntry.get()
        email = self._emailEntry.get()
        phone = self._phoneEntry.get()
        checkIn = self._checkInDate.get_date()
        checkOut = self._checkOutDate.get_date()
        roomType = self._var.get()
        roomNumber = self._database.findRoom(roomType, checkIn, checkOut);
        if (roomNumber == -1):
            self._messageLabel['text'] = "All " + roomType + " Rooms are booked during the selected date.\nTry a different date"
            self.resetFields();
            return
        room = Room(roomNumber,roomType)
        self._database.addReservation(Reservation(room, first, last, email, phone, checkIn,checkOut ))
        self._messageLabel['text'] = "Your room has been successfully booked !"
        self.resetFields();

    def resetFields(self):
        self.setEntry(self._firstNameEntry, "" )
        self.setEntry(self._lastNameEntry, "" )
        self.setEntry(self._emailEntry, "" )
        self.setEntry(self._phoneEntry, "" )
        self._r1.deselect()
        self._r2.deselect()
        self._r3.deselect()
        self._r4.deselect()

    def setEntry(self, entry, text):
        entry.delete(0, tk.END)
        entry.insert(0, text)

    def createRadioButton(self):
        self._var = tk.StringVar(self._root)
        roomLabel = tk.Label(self._root, text = "Type of room: ")
        self._r1 = tk.Radiobutton(self._root, text = "Single", variable = self._var, value = "Single")
        self._r2 = tk.Radiobutton(self._root, text = "Double", variable = self._var, value = "Double")
        self._r3 = tk.Radiobutton(self._root, text = "Triple", variable = self._var, value = "Triple")
        self._r4 = tk.Radiobutton(self._root, text = "Family", variable = self._var, value = "Family")
        roomLabel.grid(row=6, column = 0)
        self._r1.grid(row= 7, column = 0)
        self._r2.grid(row= 7, column = 1)
        self._r3.grid(row= 8, column = 0)
        self._r4.grid(row= 8, column = 1)

    def createDateInput(self):
        checkInDateLabel = tk.Label(self._root, text = "Check In Date: ")
        self._checkInDate = DateEntry(self._root, background= "magenta3", foreground= "black",bd=2)
        checkOutDateLabel = tk.Label(self._root, text = "Check Out Date: ")
        self._checkOutDate = DateEntry(self._root, background= "magenta3", foreground= "black",bd=2)

        checkInDateLabel.grid(row=9, column = 0)
        self._checkInDate.grid(row=9, column = 1)
        checkOutDateLabel.grid(row=10, column = 0)
        self._checkOutDate.grid(row=10, column = 1)

    def createInformationEntry(self):
        lineLabel = tk.Label(self._root, text = "_"*50)
        firstNameLabel = tk.Label(self._root, text = "First Name: ")
        lastNameLabel = tk.Label(self._root, text= "Last Name: ")
        self._firstNameEntry = tk.Entry(self._root, width = 20)
        self._lastNameEntry = tk.Entry(self._root, width = 20)
        emailLabel = tk.Label(self._root, text = "Email: ")
        self._emailEntry = tk.Entry(self._root, width = 20)
        phoneLabel = tk.Label(self._root, text = "Phone Number: ")
        self._phoneEntry = tk.Entry(self._root, width = 20)

        lineLabel.grid(row= 1, column = 0, columnspan = 2)
        firstNameLabel.grid(row= 2, column = 0)
        self._firstNameEntry.grid(row= 2, column = 1)
        lastNameLabel.grid(row= 3, column = 0)
        self._lastNameEntry.grid(row= 3, column = 1)
        emailLabel.grid(row= 4, column = 0)
        self._emailEntry.grid(row= 4, column = 1)
        phoneLabel.grid(row= 5, column = 0)
        self._phoneEntry.grid(row= 5, column = 1)


if __name__ == "__main__":
    pass