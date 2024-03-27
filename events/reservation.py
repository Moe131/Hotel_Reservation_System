from events.room import Room
class Reservation:
    """ Represents a reservation of a room"""

    def __init__(self, room, first, last, email , phone , startDate, endDate):
        self._room = room
        self._first = first
        self._last = last
        self._email = email
        self._phone = phone
        self._startDate = startDate
        self._endDate = endDate

    def guest(self):
        return self._guest

    def room(self):
        return self.room

    def first(self):
        return self._first

    def last(self):
        return self._last

    def email(self):
        return self._email

    def phone(self):
        return self._phone

    def startDate(self):
        return self._startDate

    def endDate(self):
        return self._endDate