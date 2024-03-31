import tkinter as tk

HEIGHT = 400
WIDTH = 400

class ManageReservation :

    def __init__(self, database):
        self._database = database
        self._root = tk.Tk()
        self._root.title("Manage Reservation")
        self._root.minsize(WIDTH,HEIGHT)

        headerLabel = tk.Label(self._root, text = "Manage Reservation", font= "Times 20")
        lineLabel = tk.Label(self._root, text = "_"*50)
        lineLabe2 = tk.Label(self._root, text = "")


        reservationEmailLabel = tk.Label(self._root, text= "Email Associated with Reservation: ")
        self._reservationEmailEntry = tk.Entry(self._root, width = 20)
        button = tk.Button(self._root, text = "Retrieve", command = self.onRetrieve)
        self._messageLabel = tk.Label(self._root, text= "")
        firstNameLabel = tk.Label(self._root, text = "First Name: ")
        self._firstNameLabel2 = tk.Label(self._root, text = "-")
        lastNameLabel = tk.Label(self._root, text = "Last Name: ")
        self._lastNameLabel2 = tk.Label(self._root, text = "-")
        emailLabel = tk.Label(self._root, text = "Email: ")
        self._emailLabel2 = tk.Label(self._root, text = "-")
        phoneLabel = tk.Label(self._root, text = "Phone Number: ")
        self._phoneLabel2 = tk.Label(self._root, text = "-")
        roomNumberLabel = tk.Label(self._root, text = "Room Number: ")
        self._roomNumberLabel2 = tk.Label(self._root, text = "-")
        StartDateLabel = tk.Label(self._root, text = "Start Date: ")
        self._StartDateLabel2 = tk.Label(self._root, text = "-")
        EndDateLabel = tk.Label(self._root, text = "End Date: ")
        self._EndDateLabel2 = tk.Label(self._root, text = "-")
        self._cancelButton = tk.Button(self._root, text = "Cancel Reservation", state = "disabled", command = self.onCancel)
        self._cancelMessageLabel = tk.Label(self._root, text= "")



        headerLabel.grid(row= 0, column = 0, columnspan = 2)
        lineLabel.grid(row= 1, column = 0, columnspan = 2)
        reservationEmailLabel.grid(row= 2, column = 0 ,columnspan = 2)
        self._reservationEmailEntry.grid(row= 3, column = 0, columnspan = 2)
        button.grid(row = 4, column = 0, columnspan = 2)
        self._messageLabel.grid(row = 5, column = 0, columnspan = 2)
        lineLabe2.grid(row= 6, column = 0)
        firstNameLabel.grid(row= 7, column = 0)
        self._firstNameLabel2.grid(row= 7, column = 1)
        lastNameLabel.grid(row= 8, column = 0)
        self._lastNameLabel2.grid(row= 8, column = 1)
        emailLabel.grid(row= 9, column = 0)
        self._emailLabel2.grid(row= 9, column = 1)
        phoneLabel.grid(row= 10 , column = 0)
        self._phoneLabel2.grid(row= 10 , column = 1)
        roomNumberLabel.grid(row=11, column = 0)
        self._roomNumberLabel2.grid(row=11, column = 1)
        StartDateLabel.grid(row=12, column = 0)
        self._StartDateLabel2.grid(row=12, column = 1)
        EndDateLabel.grid(row=13, column = 0)
        self._EndDateLabel2.grid(row=13, column = 1)
        self._cancelButton.grid(row = 14, column = 0, columnspan = 2)
        self._cancelMessageLabel.grid(row = 15, column = 0, columnspan = 2)

    def run(self):
        self._root.mainloop()

    def onRetrieve(self):
        email = self._reservationEmailEntry.get()
        reservation = self._database.findReservation(email)
        self._cancelMessageLabel["text"] = ""
        if reservation is None:
            self.resetFields()
            self._messageLabel["text"] = "No reservation was found with the provided email."
            return;
        self._messageLabel["text"] = ""
        self._roomNumberLabel2["text"] = reservation[0]
        self._firstNameLabel2["text"] = reservation[1]
        self._lastNameLabel2["text"] = reservation[2]
        self._emailLabel2["text"] = reservation[3]
        self._phoneLabel2["text"] = reservation[4]
        self._StartDateLabel2["text"] = reservation[5]
        self._EndDateLabel2["text"] = reservation[6]
        self._cancelButton["state"] = "normal"




    def onCancel(self):

        self._database.cancelReservation( self._reservationEmailEntry.get(),self._StartDateLabel2.cget("text"), self._EndDateLabel2.cget("text"))
        self._cancelMessageLabel["text"] = "Your reservation was successfully cancelled."
        self._cancelButton["state"] = "disabled"
        self.resetFields()


    def resetFields(self):
        self._roomNumberLabel2["text"] = ""
        self._firstNameLabel2["text"] = ""
        self._lastNameLabel2["text"] = ""
        self._emailLabel2["text"] = ""
        self._phoneLabel2["text"] = ""
        self._StartDateLabel2["text"] = ""
        self._EndDateLabel2["text"] = ""


if __name__ == "__main__":
    pass