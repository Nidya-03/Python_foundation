import pyodbc

class DBConn:
    @staticmethod
    def get_db_conn():
        try:
            conn = pyodbc.connect('Driver={SQL Server};'
                                  'Server=LAPTOP-1DU8L5I4\\SQLEXPRESS;' 
                                  'Database=PayXpert;'
                                  'Trusted_Connection=yes;')
            print("Connection successful")
            return conn
        except pyodbc.Error as ex:
            print(f"Error: {ex}")
            return None

    @staticmethod
    def execute_query(query, params=None):
        conn = DBConn.get_db_conn() 
        if conn:
            try:
                cursor = conn.cursor() 
                if params:
                    cursor.execute(query, params) 
                else:
                    cursor.execute(query)  
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
    
    db = DBConn()  
    connection=db.get_db_conn()
    