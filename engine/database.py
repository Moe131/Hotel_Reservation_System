import sqlite3
from events.room import Room
from events.reservation import Reservation

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
            CREATE TABLE room (
                roomNumber INTEGER PRIMARY KEY ,
                type text NOT NULL
            ); 
        """)
        cursor.execute("""
            CREATE TABLE reservation (
                roomNumber INTEGER NOT NULL ,
                firstName text NOT NULL ,
                lastName text NOT NULL ,
                email text NOT NULL ,
                phone text NOT NULL,
                startDate date NOT NULL,  
                EndDate date NOT NULL , 
                FOREIGN KEY (roomNumber) REFERENCES room(roomNumber)
            );
        """)

    def addRoom(self,room):
        """ Can be used to add rooms the the database"""
        self._connection.cursor().execute("""
            INSERT INTO room (roomNumber, type) VALUES(?,?) ;
        """, (room.roomNumber(), room.roomType()) )
        self._connection.commit()


if __name__ == "__main__":
    d = Database("databaseFile.db")
    d.open()



    d.close()