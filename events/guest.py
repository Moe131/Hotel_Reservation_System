class Guest:
    """ Represents a guest of the hotel"""

    def __init__(self, first, last, email, phone):
        self._first = first;
        self._last = last;
        self._email = email;
        self._phone = phone;

    def first(self):
        return self._first;

    def last(self):
        return self.last;

    def email(self):
        return self.email;

    def phone(self):
        return self.phone;