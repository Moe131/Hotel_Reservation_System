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
        """ This is only used once to create the engine"""
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
        """ Can be used to add rooms the the engine"""
        self._connection.cursor().execute("""
            INSERT INTO room (roomNumber, type) VALUES(?,?) ;
        """, (room.roomNumber(), room.roomType()) )
        self._connection.commit()

    def addReservation(self, reservation):
        # Work on this
        cursor = self._connection.cursor()
        cursor.execute("""
            INSERT INTO reservation (roomNumber, firstName, lastName, email, phone, startDate,endDate) 
            VALUES(?,?,?,?,?,?,?) ;
            """, (reservation.room().roomNumber(), reservation.first(), reservation.last(),
                  reservation.email(), reservation.phone(), reservation.startDate(), reservation.endDate()) )
        self._connection.commit()



    def findRoom(self, roomType, startDate, endDate):
        """ Finds the roomNumber of the first available room | returns -1 if rooms are full """
        cursor = self._connection.cursor()
        cursor.execute("""
            SELECT room.roomNumber FROM room 
            LEFT JOIN reservation ON room.roomNumber = reservation.roomNumber
            WHERE room.type = ? AND (
                reservation.roomNumber IS NULL OR 
                NOT (reservation.startDate <= ? AND reservation.endDate >= ?)
            );
        """, (roomType, endDate, startDate))
        roomNumber = cursor.fetchone()
        return roomNumber[0]

if __name__ == "__main__":
    d = Database("databaseFile.db")
    d.open()



    d.close()