from view.home import *
from engine.database import Database

def main():
    database = Database("engine/databaseFile.db")
    database.open()
    mainWindow = Home(database)
    mainWindow.run()
    database.close()

if __name__ == "__main__":
    main()