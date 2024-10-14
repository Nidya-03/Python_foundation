import sys
sys.path.append(r"C:\Users\Thirshala\OneDrive\Documents\python foundation-hexaware\casestudy_PayXpert")
import pyodbc
from dao.FinancialRecordService import FinancialRecordService
from entity.FinancialRecord import FinancialRecord
from exception.Customexceptions import FinancialRecordException,InvalidInputException
from exception.Customexceptions import DatabaseConnectionException
from util.DBConn import DBConn

class IFinancialRecordService(FinancialRecordService):
    def __init__(self):
        self.conn = DBConn.get_db_conn()
        self.financial_records = {}

    def AddFinancialRecord(self, Financialrecord:FinancialRecord):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                INSERT INTO FinancialRecord (employee_id,Recorddate,Description,Amount,Recordtype)
                VALUES (?, ?, ?, ?,?)
            """, (
                Financialrecord.employee_id,
                Financialrecord.RecordDate,
                Financialrecord.Description,
                Financialrecord.Amount,
                Financialrecord.RecordType
                
            ))
            self.conn.commit()
            print("Finanacial Record added successfully")
        except pyodbc.IntegrityError as e:
            raise InvalidInputException(f"Integrity error: {e}")
        except pyodbc.Error as e:
            raise DatabaseConnectionException(f"Database error: {e}")

    def GetFinancialRecordById(self, record_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM FinancialRecord WHERE record_id = ?", record_id)
            row = cursor.fetchone()
            if row:
                print(f"Record id :{row[0]},Employee id:{row[1]},Record date:{row[2]},Description:{row[3]},Amount:{row[4]},Record type:{row[5]}")
                
            else:
                raise FinancialRecordException(f"Record with ID {record_id} not found.")
            
        except pyodbc.Error as e:
            raise DatabaseConnectionException(f"Database error: {e}")

    def GetFinancialRecordsForEmployee(self, employee_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM FinancialRecord WHERE employee_id = ?", employee_id)
            rows = cursor.fetchall()
            if rows:
                for row in rows:
                    print(f"Record id :{row[0]},Employee id:{row[1]},Record date:{row[2]},Description:{row[3]},Amount:{row[4]},Record type:{row[5]}")
                
            else:
                raise FinancialRecordException(f"Employee with ID {employee_id} not found.")
            
        except pyodbc.Error as e:
            raise DatabaseConnectionException(f"Database error: {e}")

    def GetFinancialRecordsForDate(self, Recorddate):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM FinancialRecord WHERE Recorddate = ?", Recorddate)
            rows = cursor.fetchall()
            if rows:
                for row in rows:
                    print(f"Record id :{row[0]},Employee id:{row[1]},Record date:{row[2]},Description:{row[3]},Amount:{row[4]},Record type:{row[5]}")
                
            else:
                raise FinancialRecordException(f"Record with date {Recorddate} not found.")
            
        except pyodbc.Error as e:
            raise DatabaseConnectionException(f"Database error: {e}")
