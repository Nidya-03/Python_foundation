import pyodbc

class DBConnection:
    con = None

    @staticmethod
    def getConnection():
        if DBConnection.con is None:
            try:
                DBConnection.con = pyodbc.connect(
                    'Driver={SQL Server};'
                    'Server=LAPTOP-1DU8L5I4\SQLEXPRESS;'
                    'Database=TicketBookingSystem;'
                )
                print("Database Connected Successfully!!")
            except pyodbc.Error as err:
                print(f"Error connecting DB: {err}")

        return DBConnection.con