import sqlite3

class Database:

    def __init__(self, path:str):
        self._path = path
        self._connection = None

    def open(self):
        self._connection = sqlite3.connect(self._path)
        cursor = self._connection.cursor()
        cursor = self._connection.execute(""" PRAGMA foreign_keys = ON; """)
        cursor.close()

    def close(self):
        self._connection.close()
