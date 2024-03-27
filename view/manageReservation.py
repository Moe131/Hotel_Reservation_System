import tkinter as tk

HEIGHT = 300
WIDTH = 400

class ManageReservation :

    def __init__(self, database):
        self._database = database
        self._root = tk.Tk()
        self._root.title("Guest Information")
        self._root.minsize(WIDTH,HEIGHT)

        headerLabel = tk.Label(self._root, text = "Manage Reservation", font= "Times 20")
        lineLabel = tk.Label(self._root, text = "_"*50)
        lineLabe2 = tk.Label(self._root, text = "")


        reservationEmailLabel = tk.Label(self._root, text= "Email Associated with Reservation: ")
        roomNumberEntry = tk.Entry(self._root, width = 20)
        button = tk.Button(self._root, text = "Retrieve")
        firstNameLabel = tk.Label(self._root, text = "First Name: ")
        firstNameLabel2 = tk.Label(self._root, text = "-")
        lastNameLabel = tk.Label(self._root, text = "Last Name: ")
        lastNameLabel2 = tk.Label(self._root, text = "-")
        emailLabel = tk.Label(self._root, text = "Email: ")
        emailLabel2 = tk.Label(self._root, text = "-")
        phoneLabel = tk.Label(self._root, text = "Phone Number: ")
        phoneLabel2 = tk.Label(self._root, text = "-")
        roomTypeLabel = tk.Label(self._root, text = "Room Type: ")
        roomTypeLabel2 = tk.Label(self._root, text = "-")

        headerLabel.grid(row= 0, column = 0, columnspan = 2)
        lineLabel.grid(row= 1, column = 0, columnspan = 2)
        reservationEmailLabel.grid(row= 2, column = 0 ,columnspan = 2)
        roomNumberEntry.grid(row= 3, column = 0, columnspan = 2)
        button.grid(row = 4, column = 0, columnspan = 2)
        lineLabe2.grid(row= 5, column = 0)
        firstNameLabel.grid(row= 6, column = 0)
        firstNameLabel2.grid(row= 6, column = 1)
        lastNameLabel.grid(row= 7, column = 0)
        lastNameLabel2.grid(row= 7, column = 1)
        emailLabel.grid(row= 8, column = 0)
        emailLabel2.grid(row= 8, column = 1)
        phoneLabel.grid(row= 9 , column = 0)
        phoneLabel2.grid(row= 9 , column = 1)
        roomTypeLabel.grid(row=10, column = 0)
        roomTypeLabel2.grid(row=10, column = 1)



    def run(self):
        self._root.mainloop()

if __name__ == "__main__":
    pass