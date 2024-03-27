import tkinter as tk
from tkcalendar import DateEntry

HEIGHT = 350
WIDTH = 400

class CheckInFrame :

    def __init__(self):
        self._root = tk.Tk()
        self._root.title("Check In")
        self._root.minsize(WIDTH,HEIGHT)

        headerLabel = tk.Label(self._root, text = "Check In", font= "Times 20")
        lineLabel = tk.Label(self._root, text = "_"*50)
        firstNameLabel = tk.Label(self._root, text = "First Name: ")
        lastNameLabel = tk.Label(self._root, text= "Last Name: ")
        firstNameEntry = tk.Entry(self._root, width = 20)
        lastNameEntry = tk.Entry(self._root, width = 20)
        emailLabel = tk.Label(self._root, text = "Email: ")
        emailEntry = tk.Entry(self._root, width = 20)
        phoneLabel = tk.Label(self._root, text = "Phone Number: ")
        phoneEntry = tk.Entry(self._root, width = 20)

        # Submit button
        button = tk.Button(self._root, text = "Submit")

        #Radio Buttons
        var = tk.StringVar()
        roomLabel = tk.Label(self._root, text = "Type of room: ")
        r1 = tk.Radiobutton(self._root, text = "Single", variable = var, value = "Single")
        r2 = tk.Radiobutton(self._root, text = "Double", variable = var, value = "Double")
        r3 = tk.Radiobutton(self._root, text = "Triple", variable = var, value = "Triple")
        r4 = tk.Radiobutton(self._root, text = "Family", variable = var, value = "Family")

        #Check In/Out Date
        checkInDateLabel = tk.Label(self._root, text = "Check In Date: ")
        checkInDate = DateEntry(self._root, background= "magenta3", foreground= "black",bd=2)
        checkOutDateLabel = tk.Label(self._root, text = "Check Out Date: ")
        checkOutDate = DateEntry(self._root, background= "magenta3", foreground= "black",bd=2)

        headerLabel.grid(row= 0, column = 0, columnspan = 2)
        lineLabel.grid(row= 1, column = 0, columnspan = 2)
        firstNameLabel.grid(row= 2, column = 0)
        firstNameEntry.grid(row= 2, column = 1)
        lastNameLabel.grid(row= 3, column = 0)
        lastNameEntry.grid(row= 3, column = 1)
        emailLabel.grid(row= 4, column = 0)
        emailEntry.grid(row= 4, column = 1)
        phoneLabel.grid(row= 5, column = 0)
        phoneEntry.grid(row= 5, column = 1)
        roomLabel.grid(row=6, column = 0)
        r1.grid(row= 7, column = 0)
        r2.grid(row= 7, column = 1)
        r3.grid(row= 8, column = 0)
        r4.grid(row= 8, column = 1)
        checkInDateLabel.grid(row=9, column = 0)
        checkInDate.grid(row=9, column = 1)
        checkOutDateLabel.grid(row=10, column = 0)
        checkOutDate.grid(row=10, column = 1)
        button.grid(row = 11, column = 0, columnspan = 2)
    def run(self):
        self._root.mainloop()

if __name__ == "__main__":
    pass