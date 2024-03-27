class Room:
    """ Represents a room of the hotel"""

    def __init__(self, roomNumber, roomType):
        self._roomNumber = roomNumber;
        self._roomType = roomType;


    def roomNumber(self):
        return self._roomNumber;

    def roomType(self):
        return self._roomType;