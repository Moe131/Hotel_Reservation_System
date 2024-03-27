from guest import Guest
from room import Room
class Reservation:
    """ Represents a reservation of a room"""

    def __init__(self, guest, room, startDate, endDate):
        self._guest = guest;
        self._room = room;
        self._startDate = startDate;
        self._endDate = endDate;

    def guest(self):
        return self._guest;

    def room(self):
        return self.room;

    def startDate(self):
        return self.startDate;

    def endDate(self):
        return self.endDate;