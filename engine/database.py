import sqlite3

class Database:

    def __init__(self, path:str):
        self._path = path
        self._connection = None

    def open(self):
        self._connection = sqlite3.connect(self._path)
        cursor = self._connection.execute(""" PRAGMA foreign_keys = ON; """)
        cursor.close()

    def close(self):
        self._connection.close()

    def createDatabaseFile(self):
        """ This is only used once to create the database"""
        cursor = self._connection.cursor()
        cursor.execute("""
            CREATE TABLE guest (
                guestID INTEGER PRIMARY KEY ,
                firstName text NOT NULL ,
                lastName text NOT NULL ,
                email text NOT NULL ,
                phone text NOT NULL
            ); 
        """)
        cursor.execute("""
            CREATE TABLE room (
                roomNumber INTEGER PRIMARY KEY ,
                guestID INTEGER NOT NULL,
                type text NOT NULL,
                FOREIGN KEY(guestID)  REFERENCES guest(guestID)   
            ); 
        """)
        cursor.execute("""
            CREATE TABLE reservation (
                roomNumber INTEGER NOT NULL ,
                guestID INTEGER NOT NULL,
                startDate date NOT NULL,  
                EndDate date NOT NULL , 
                FOREIGN KEY (roomNumber) REFERENCES room(roomNumber),
                FOREIGN KEY (guestID) REFERENCES guest(guestID)
            );
        """)

if __name__ == "__main__":
    d = Database("databaseFile.db")
    d.open()
    d.close()