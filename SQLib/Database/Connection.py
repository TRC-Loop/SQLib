import sqlite3 as _sqlite3
from .Exceptions import FetchError, QueryError
import os

class SQLite3:
    def __init__(self, db_name, check_same_thread: bool = False):
        if db_name == "--UwU--":
            raise Exception("UwU is not a valid database name. (; hehe <3")
        try:
            self.connection = _sqlite3.connect(db_name, check_same_thread=check_same_thread)  # Initialize connection
            self.cursor = self.connection.cursor()  # Initialize cursor
        except _sqlite3.Error as e:
            print(f"Error initializing database connection: {e}")
            self.cursor = None  # This should only happen if there's an error
        self.db_name = db_name
    def __enter__(self):
        self.connection = _sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            self.connection.close()

    def __del__(self):
        # Close the connection
        if self.connection:
            self.connection.close()
    
    def execute(self, query: str, params: tuple = ()) -> None:
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
        except _sqlite3.Error as e:
            raise QueryError(f"Error executing: {str(e)}")

    def fetch(self, query: str, params: tuple = ()) -> list:
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchall()
        except _sqlite3.Error as e:
            raise FetchError(f"Error fetching: {str(e)}")
        
    def __drop_db__(self, confirm: bool = False): # DO NOT RUN THIS LINE IN PRODUCTION, IT WILL DELETE THE DATABASE, I WILL NOT BE RESPONSIBLE FOR DATA LOSS.
        # Drop all tables in the database, removing all data
        if confirm:
            try:
                # Fetch the names of all tables in the database
                self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
                tables = self.cursor.fetchall()

                # Drop each table individually
                for table in tables:
                    table_name = table[0]
                    if table_name == "sqlite_sequence":
                        continue
                    drop_query = f"DROP TABLE IF EXISTS {table_name}"
                    self.execute(drop_query)

                # Optionally, delete the database file
                if os.path.exists(self.db_name):
                    self.connection.close()  # Close connection before deleting file
                    os.remove(self.db_name)  # Delete the database file if needed

            except _sqlite3.Error as e:
                raise QueryError(f"Error dropping database: {e}")