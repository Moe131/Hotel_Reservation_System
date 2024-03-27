import tkinter as tk

HEIGHT = 150
WIDTH = 400

class CheckOutFrame :

    def __init__(self):
        self._root = tk.Tk()
        self._root.title("Check Out")
        self._root.minsize(WIDTH, HEIGHT)

        headerLabel = tk.Label(self._root, text = "Check Out", font= "Times 20")
        lineLabel = tk.Label(self._root, text = "_"*50)
        lineLabe2 = tk.Label(self._root, text = "")

        roomLabel = tk.Label(self._root, text = "Room Number: ")
        roomNumberEntry = tk.Entry(self._root, width = 20)
        button = tk.Button(self._root, text = "Check Out")
        messageLabel = tk.Label(self._root, text = " ")


        headerLabel.grid(row = 0, column = 0, columnspan = 2)
        lineLabel.grid(row = 1, column = 0, columnspan = 2)
        roomLabel.grid(row = 2, column = 0)
        roomNumberEntry.grid(row = 2, column = 1)
        button.grid(row = 3, column = 0, columnspan = 2)
        lineLabe2.grid(row = 4, column = 0)
        messageLabel.grid(row = 5, column = 0, columnspan = 2)


    def run(self):
        self._root.mainloop()

if __name__ == "__main__":
    pass