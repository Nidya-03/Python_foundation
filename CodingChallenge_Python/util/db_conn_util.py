
import pyodbc

class DBUtil:
    @staticmethod
    def get_db_conn():
        """Establishes a connection to the database."""
        try:
            conn = pyodbc.connect('Driver={SQL Server};'
                                  'Server=LAPTOP-1DU8L5I4\\SQLEXPRESS;'  # Ensure double backslash for the server
                                  'Database=LoanManagementSystem;'
                                  'Trusted_Connection=yes;')
            print("Connection successful")
            return conn
        except pyodbc.Error as ex:
            print(f"Error: {ex}")
            return None

    @staticmethod
    def execute_query(query, params=None):
        """Executes a given SQL query using a cursor."""
        conn = DBUtil.get_db_conn()  
        if conn:
            try:
                cursor = conn.cursor()  # Create a cursor object
                if params:
                    cursor.execute(query, params)  # Execute with parameters
                else:
                    cursor.execute(query)  # Execute without parameters
                conn.commit()  
                print("Query executed successfully.")
            except pyodbc.Error as ex:
                print(f"Error executing query: {ex}")
            finally:
                cursor.close()  
                conn.close()   
        else:
            print("Unable to establish connection.")

if __name__ == "__main__":
    
    db = DBUtil()  
    connection=db.get_db_conn()
    
    