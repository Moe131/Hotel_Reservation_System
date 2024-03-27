from view.home import *
from engine.database import Database
def main():
    database = Database("engine/databaseFile.db")
    mainWindow = Home(database)
    mainWindow.run()

if __name__ == "__main__":
    main()